from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields= ['id ', 'name' ,'age','address'] #one way to specify field
        # exclude= ['id'] #exclude only mentioned
        fields = '__all__'  # include all

    def validate(self, data):
        age = data.get('age')
        name = data.get('name')
        # Validate age
        if age is not None and age < 18:
            raise serializers.ValidationError(
                {'error': 'age must not be less than 18'}
            )
         # Validate name
        name = data.get('name')
        if name:
            # Remove spaces for validation
            cleaned_name = name.replace(" ", "")
            if not cleaned_name.isalpha():
                raise serializers.ValidationError(
                    {'name': 'Name must contain only alphabetic characters'}
                )

        return data
