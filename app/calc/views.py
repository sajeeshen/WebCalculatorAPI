from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import ugettext_lazy as _
from calc import serializers
from rest_framework.authentication import TokenAuthentication
from calc.utility import get_available_options
from calc.utility import do_calculation
from calc.permissions import IsSuperUser
from calculator.models import Report

ACCESS_ERROR = _("You dont have permission for this operation")


class Calculator(generics.GenericAPIView):
    """
    This is the Generic API for calculator
    ---
    x : First Number
    y : Second Number
    action : Can be Add/Sub/Mul

    """
    serializer_class = serializers.CalculatorSerializers
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):
        action = self.request.data.get('action')
        if action:
            valid_options = get_available_options(action)
            if valid_options and valid_options[0]['admin_required']:
                # if the admin required is true
                # then assign the user permission
                self.permission_classes = (IsSuperUser, )
            else:
                self.permission_classes = (IsAuthenticated, )
        else:
            self.permission_classes = (IsAuthenticated,)
        return super(self.__class__, self).get_permissions()

    def post(self, request):
        serializer = serializers.CalculatorSerializers(data=request.data)
        if serializer.is_valid():
            x = self.request.data.get('x', '')
            y = self.request.data.get('y', '')
            action = self.request.data.get('action', '')
            action_parameter = {'x': x, 'y': y}
            serializer.save(user=request.user,
                            action_name=action,
                            action_parameter=action_parameter
                            )

            return Response({'result': 'success',
                             'value': do_calculation(action, x, y)},
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
