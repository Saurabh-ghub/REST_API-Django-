from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.
def marksheets(request):
    stu = Student.objects.all()
    res=[]
    for st in stu:
        serializer = StudentSerializer(st)
        json_data = JSONRenderer().render(serializer.data) 
        res.append(json_data)
    return HttpResponse(res)
def studentmark(request,pk):
    stu = Student.objects.get(id=pk)
    
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data) 
       
    return HttpResponse(json_data)