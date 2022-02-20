from email import message
from django.shortcuts import redirect, render
from django.views import View
from .models import * 
from rest_framework.response import Response
import json
from .serializers import VehicleSerializer
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
import ast  
from datetime import datetime
from django.core.checks import messages

# Django Channels
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your views here.
from django.contrib import messages
class home(View):
    def get(self, request):
        get_veh=vehicle.objects.all()
        return  render(request,'home.html',{'dtl':get_veh})

class add_veh(View):
     def get(self, request):
        return  render(request,'addform.html') 

@method_decorator(csrf_exempt,name='dispatch')
class add_vehicle(APIView):
    def post(self,request,formate=None,pk=None):
        data = request.data         
        serializer=VehicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':200,'message':'sucess'})
        return JsonResponse({'status':400,'message':f'{serializer.errors}'})
    
     
        
class showdetails(APIView):
    def get(self,request,pk):
        pid=pk
        get_veh=vehicle.objects.filter(id=pid)
        return render(request,'show_details.html',{'dd':get_veh,'pk':pk})

class notification_test_page(View):
    def get(self,request):
        return render(request, 'notifications_test_page.html')

@method_decorator(csrf_exempt,name='dispatch')
class update_vehicle(View):
    def post(self,request,pk,formate=None):
        id=pk
        get_obj=vehicle.objects.get(id=id)
        name=request.POST.get('f_name')
        if(len(request.FILES)!=0):
            static_map=request.FILES['imgle']
            get_obj.static_map=static_map
        speed=request.POST.get('l_name')
        avg_sped=request.POST.get("u_name")
        temp=request.POST.get('temp')
        level=request.POST.get('level')
        e_state=request.POST.get('ests')
        get_obj.name=name
        get_obj.speed=speed
        get_obj.average_speed=avg_sped
        get_obj.Temprature=temp
        get_obj.Fuel_level=level
        if(e_state=='on'):
            get_obj.Engine_status=True
        else:
            get_obj.Engine_status=False
        get_obj.save()
        pid=pk
        get_veh=vehicle.objects.filter(id=pid)
        return render(request,'show_details.html',{'dd':get_veh,'pk':pk})
        
class show_up(View):
    def get(self, request):
        messages.info(request,'Please Click on name of vehicle to update or delete')
        return redirect('/')

class delete_vehicle(View):
    def get(self,request,pk):
        vehicle.objects.filter(id=pk).delete()
        return redirect('/')