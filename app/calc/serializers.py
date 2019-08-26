from rest_framework import serializers
from rest_framework import mixins
from calc.utility import get_available_options
from calculator.models import Report


class CalculatorSerializers(serializers.Serializer):
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    action = serializers.CharField()

    class Meta:
        model = Report
        exclude = ('id',)

    def create(self, validated_data):
        """ Create a new log and return"""
        return Report.objects.create_report(validated_data['action_name'],
                                            validated_data['action_parameter'],
                                            validated_data['user'])

    def validate(self, data):
        """
            Validate the input
        """
        action = data.get('action')
        action_validate = get_available_options(action)
        if not action_validate:
            raise serializers.ValidationError("No such action")
        try:
            self.first_num = int(data.get('x'))
            self.second_num = int(data.get('y'))
        except Exception as err:
            raise serializers.ValidationError("Cant process, "
                                              "please check the input")
        return data
