from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.status import status
from . models import employees
from . serializers import employeesSerializer
from django.views.generic import TemplateView
from django.http import JsonResponse
import pdb
import urllib.request
import json
# import services
# Create your views here.

class employeeList(APIView):

    def get(self, request):
        employee1=employees.objects.all()
        serializerr=employeesSerializer(employee1, many=True)
        jsonR= {'data': serializerr.data}
        # print(jsonR)
        # pdb.set_trace()
        return JsonResponse(jsonR)

    def post(self):
        pass

class firstPage(TemplateView):
      template_name = "index.html"
      def get(self,request):
        quary = request.GET.get('quary')
        url = 'http://localhost:8000/employees/'
        json_obj = urllib.request.urlopen(url)
        decode = json.load(json_obj)
        return render(request, self.template_name, {'objects':decode['objects']})
    # def viewEmployee(request):
    #     if request.method == 'GET':
    #         Employee_list = employees.objects.all()
    #         Emloyeess=[]
    #         for emp in Employee_list:
    #             Emloyeess.append({"firstname": emp.firstname, "lastname": emp.lastname, "emp_id": emp.emp_id})
    #         return JsonResponse(Emloyeess, safe=False)

      