from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields= ['id ', 'name' ,'age','address'] #one way to specify field
        # exclude= ['id'] #exclude only mentioned
        fields = '__all__'  # include all
