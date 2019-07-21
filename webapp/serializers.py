from rest_framework import serializers
from . models import employees

class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        # fileds=['fistname']
        fields='__all__'