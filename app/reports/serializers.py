from rest_framework import serializers
from calculator.models import Report


class ReportManageSerializer(serializers.Serializer):
    x = serializers.IntegerField()

    class Meta:

        model = Report
        fields = ('action_name', 'action_parameter',)


class MonthlyReportManageSerializer(serializers.Serializer):

    class Meta:

        model = Report
        fields = ('action_name', 'action_parameter',)


class YearlyReportManageSerializer(serializers.Serializer):

    class Meta:

        model = Report
        fields = ('action_name', 'action_parameter',)
