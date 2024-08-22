from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import response
from .serializers import *
from .models import *

# Create your views here.


@api_view(['GET'])
def home(request):
    students_obj = Student.objects.all()
    serializer = StudentSerializer(students_obj, many='True')
    return Response({'status': 200, 'payload': serializer.data})


@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data=request.data)

    if not serializer.is_valid():
        return Response({'status': 403, 'message': 'invalid data'})

    serializer.save()
    return Response({'status': 200, 'payload': serializer.data, 'message': 'successful'})
