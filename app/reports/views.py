from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reports import serializers
from rest_framework.authentication import TokenAuthentication
import xlwt
from calculator.models import Report
from django.http import HttpResponse
from calc.utility import get_current_date, get_current_month, get_current_year


class ReportGenerateMixin(object):

    def write_excel(self, columns, file_name):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = \
            'attachment; filename={0}'.format(file_name)

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Report')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        #columns = ['action_name', 'Parameters', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        rows = self.get_queryset()
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response


class DailyReportView(ReportGenerateMixin,
                      generics.GenericAPIView):
    """
        Generate Daily Report.

    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ReportManageSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Report.objects.filter(
                created_at__date=get_current_date()).\
                values_list('action_name', 'action_parameter')
        return Report.objects.filter(user=self.request.user,
                                     created_at=get_current_date()
                                     ).values_list('action_name',
                                                   'action_parameter')

    def get(self, request):
        return self.write_excel(['action_name', 'Parameters', ],
                                 "daily.xls")


class MonthlyReportView(ReportGenerateMixin,
                        generics.GenericAPIView):
    """
        Generate Monthly Report.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ReportManageSerializer

    def get_queryset(self):
        month = self.request.query_params.get('month', get_current_month())
        year = self.request.query_params.get('year', get_current_year())
        if self.request.user.is_superuser:
            return Report.objects.filter(created_at__month=int(month),
                                         created_at__year=int(year)). \
                values_list('action_name', 'action_parameter')
        return Report.objects.filter(user=self.request.user,
                                     created_at__month=int(month),
                                     created_at__year=int(year)
                                     ).\
            values_list('action_name', 'action_parameter')

    def get(self, request, month, year):
        return self.write_excel(['action_name', 'Parameters', ],
                                 "monthly.xls")


class YearlyReportView(ReportGenerateMixin,
                       generics.GenericAPIView):
    """
        Yearly  Report.
        ____

    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = serializers.ReportManageSerializer

    def get_serializer(self, queryset, many=True):
        return self.serializer_class(
            queryset,
            many=many,
        )

    def get_queryset(self):
        year = self.request.query_params.get('year', get_current_year())
        if self.request.user.is_superuser:
            return Report.objects.filter(created_at__year=int(year),).\
                values_list('action_name', 'action_parameter')
        return Report.objects.filter(user=self.request.user,
                                     created_at__year=int(year)
                                     ).values_list('action_name',
                                                   'action_parameter')

    def get(self, request, year):

        return self.write_excel(['action_name', 'Parameters', ],
                                 "yearly.xls")
