from django.shortcuts import render , redirect
import json
# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
from .models import Register,Mobile_Information,Hosting_Information,Server_Information,Server_Information,Mapping_Server_Mobile,Device_Status,Procurement_Request,Allotment
from django.shortcuts import render,get_object_or_404
from django import forms
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from datetime import datetime, timedelta
#from django.views.decorators.csrf import csrf_exempt


@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
@api_view(['GET', 'POST'])        
def admin_dashboard(request):
    # if request.method == 'GET':
        # print("here in dashboard")
     if "user_id" in request.session:
        return render(request,'admin_dashboard.html')
     else:
        return redirect('login')         

 
@api_view(['GET', 'POST'])             
def login_details(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        if "logout" in request.session:
            del request.session["logout"]
            print('deleted logout')
            return redirect('login')
            
    elif request.method == 'POST':
        login_data = request.data
        client_count = Register.objects.filter(username=login_data['name'],password=login_data['pwd']).count()
        if client_count == 0:
            print('Not a valid user')
            messages.error(request, 'Not valid user')
            print(messages.error(request, 'Not valid user'))
            return redirect('login') 
        else:    
            client_data = Register.objects.get(username = login_data['name']) 
            mobile_details = Mobile_Information.objects.all()
            mobile_lst = list(mobile_details)
            print(mobile_details,type(mobile_details))
            server_details = Server_Information.objects.all()
            server_lst = list(server_details)
            print(server_details,type(server_details))
            if login_data['name'] == "ssumukh" and login_data['pwd'] == "developer123":
                print("success")
                if len(mobile_lst)==0  and len(server_lst)==0:
                    request.session["user_id"] = client_data.id
                    return Response(status=status.HTTP_200_OK, data={'status':'success','user_type':'developer','db_data':'empty_data'})
                # elif len(mobile_lst)>0  or len(server_lst)>0:    
                    # request.session["user_id"] = client_data.id
                    # return Response(status=status.HTTP_200_OK, data={'status':'success','user_type':'developer','db_data':'empty_data'})
                else:    
                    request.session["user_id"] = client_data.id
                    return Response(status=status.HTTP_200_OK, data={'status':'success','user_type':'developer','db_data':'non_empty_data'})
            if login_data['name'] == "ssaily" and login_data['pwd'] == "admin123":
                print("success")
                request.session["user_id"] = "ssaily"
                return Response(status=status.HTTP_200_OK, data={'status':'success','user_type':'admin','db_data':'empty_data'})         
            if client_count == 1:
                request.session["user_id"] = client_data.id
                return Response(status=status.HTTP_200_OK, data={'status':'success','user_type':'client','db_data':'empty_data'})           
        
@api_view(['GET', 'POST'])       
def register_user(request):
    if request.method == 'POST':
        register_data = request.data
        print(register_data)
        client_register = Register()
        client_register.name = register_data['name']
        client_register.email = register_data['email']
        client_register.location = register_data['loc']
        client_register.username = register_data['username']
        client_register.password = register_data['password']
  
        if Register.objects.filter(email = client_register.email):
            messages.error(request, 'Email already exist')
            return redirect('get_register_page')

        if Register.objects.filter(username = client_register.username):
            messages.error(request, 'Username already exist')            
            return redirect('get_register_page')
            
        client_register.save()    
            
        print('done')
        return redirect("login")
                
def get_register_page(request):    
    return render(request,'pages-register_client.html')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
def login(request):
    return render(request,'pages-login.html')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
def logout(request):
    # if "user_id" in request.session:
        # del request.session["user_id"]
    request.session.flush()
    print('deleted all')
    request.session["logout"] = True
    return redirect('login')
   
@cache_control(no_cache=True, must_revalidate=True, no_store=True)   
def dashboard(request):    
    mobile_list = []
    server_list = []
    if "user_id" in request.session:
        mobile_details = Mobile_Information.objects.all()
        server_details = Server_Information.objects.all()
        for items in mobile_details:
            status_details = Device_Status.objects.get(device_information_id = items.id,category='mobile')
            mobile_list.append({'Id':items.id,'Type':items.types,'Model':items.model,'OS':items.os,'Device Id':items.device_id,'Server Id':items.server_device_id,
                               'Hosted At':items.location_of_hosting,'Status':status_details.status})
        for items in server_details:
            status_details = Device_Status.objects.get(device_information_id = items.id,category='server')
            server_list.append({'Id':items.id,'Type':items.types,'Model':items.model,'Server Capacity':items.server_capacity,'Device Id':items.device_id,
                               'Hosted At':items.location_of_hosting,'Status':status_details.status})                       
        print('mobile_list',mobile_list) 
        print('server_list',server_list) 
        return render(request,'dashboard.html',{'mobile_list':mobile_list,'server_list':server_list,'col_mobile':mobile_list[0],'col_server':server_list[0]})
    else:
        return redirect('login')    
        
def add_mobile(request):  
    if "user_id" in request.session:
        server_details = Server_Information.objects.all()
        print('details',server_details)
        return render(request,'add-mobile.html',{'server_details':server_details}) 
    else:
        return redirect('login')          

def add_server(request):  
    if "user_id" in request.session:
        return render(request,'add-server.html')
    else:
        return redirect('login')          
    
def add_equipments(request):    
    return render(request,'add-equipments.html')  
    
@api_view(['GET', 'POST'])    
def edit_mobile_information(request,mobile_id): 
    print('*****',mobile_id)
    query_dict = {}
    query = Mobile_Information.objects.get(id = mobile_id)
    server_detail = Server_Information.objects.all()
    if request.method == 'GET':
        query_dict = {'id':query.id,'types':query.types,'model':query.model,'manufacturer':query.manufacturer,'make':query.make,'os':query.os,
                      'device_id':query.device_id,'serial_number':query.serial_number,'ip_address':query.ip_address,
                      'location_of_hosting':query.location_of_hosting,'date_of_purchase':query.date_of_purchase,
                      'server_device_id':query.server_device_id,'phone_number':query.phone_number}
        print(query_dict)     
        return render(request,'edit-mobile.html',{'query_dict':query_dict,'server_detail':server_detail})
    elif request.method == 'POST':
        edit_data = request.data
        print('#######',mobile_id)
        print('edit_data',edit_data) 
        query.types = edit_data['device_type']
        query.model = edit_data['mobile_model']
        query.manufacturer = edit_data['manufacturer']
        query.make = edit_data['make']
        query.os = edit_data['os_type']
        query.device_id = edit_data['device_id']
        query.serial_number = edit_data['serial_number'] 
        query.ip_address = edit_data['ip_address']
        query.location_of_hosting = edit_data['loc']
        query.date_of_purchase = edit_data['pur_date']
        query.server_device_id = edit_data['server_name']
        query.phone_number = edit_data['phn_num']
        query.updated_date = datetime.now()
        query.save()    
        return Response(status=status.HTTP_200_OK, data={'status':'success'})
        
@api_view(['GET', 'POST'])    
def edit_server_information(request,server_id): 
    print('*****',server_id)
    query_dict = {}
    query = Server_Information.objects.get(id = server_id)
    if request.method == 'GET':
        query_dict = {'id':query.id,'types':query.types,'model':query.model,'manufacturer':query.manufacturer,'make':query.make,'capacity':query.server_capacity,
                      'device_id':query.device_id,'serial_number':query.serial_number,'ip_address':query.ip_address,
                      'location_of_hosting':query.location_of_hosting,'date_of_purchase':query.date_of_purchase}
        print(query_dict)     
        return render(request,'edit-server.html',{'query_dict':query_dict})
    elif request.method == 'POST':
        edit_data = request.data
        print('edit_data',edit_data) 
        query.types = edit_data['device_type']
        query.model = edit_data['mobile_model']
        query.manufacturer = edit_data['manufacturer']
        query.make = edit_data['make']
        query.server_capacity = edit_data['capacity']
        query.device_id = edit_data['device_id']
        query.serial_number = edit_data['serial_number'] 
        query.ip_address = edit_data['ip_address']
        query.location_of_hosting = edit_data['loc']
        query.date_of_purchase = edit_data['pur_date']
        query.updated_date = datetime.now()
        query.save()    
        return Response(status=status.HTTP_200_OK, data={'status':'success'})        
        

@api_view(['POST'])
def save_mobile_information(request):
    if request.method == 'POST':
        if "user_id" in request.session:
            print("here in mobile infor")
            mobile_data = request.data
            mobile_data = mobile_data.dict()
            print(mobile_data)
            add_mobile = Mobile_Information()
            device_status_obj = Device_Status()
            add_mobile.types = mobile_data['device_type']
            add_mobile.model = mobile_data['mobile_model']
            add_mobile.manufacturer = mobile_data['manufacturer']
            add_mobile.make = mobile_data['make']
            add_mobile.os = mobile_data['os_type']
            add_mobile.device_id = mobile_data['device_id']
            add_mobile.serial_number = mobile_data['serial_number'] 
            add_mobile.ip_address = mobile_data['ip_address']
            add_mobile.location_of_hosting = mobile_data['loc']
            add_mobile.date_of_purchase = mobile_data['pur_date']
            add_mobile.server_device_id = mobile_data['server_name']
            add_mobile.phone_number = mobile_data['phn_num']
            add_mobile.updated_date = datetime.now()
            add_mobile.save()
            device_status_obj.device_information_id = add_mobile.id
            device_status_obj.category = "mobile"
            device_status_obj.user_id = 0
            device_status_obj.status = "inactive"
            device_status_obj.save()
            if "server_name" in mobile_data and mobile_data['server_name']  != None:
                server_data = Server_Information.objects.get(device_id = mobile_data['server_name']) 
                mapping_server_obj = Mapping_Server_Mobile()
                mapping_server_obj.server_information_id = server_data.id
                mapping_server_obj.mobile_information_id = add_mobile.id
                mapping_server_obj.save()
            if "loc" in mobile_data and "device_id" in mobile_data:
                hosting_obj = Hosting_Information()
                hosting_obj.location = mobile_data["loc"]
                hosting_obj.category = "mobile"
                hosting_obj.device_id = mobile_data["device_id"] 
                hosting_obj.save()
            return Response(status=status.HTTP_200_OK, data={'status':'success','data':mobile_data})
        else:
            return redirect('login')
    
@api_view(['POST'])
def save_server_information(request):
    if request.method == 'POST':
        if "user_id" in request.session:
            print("here in server infor")
            server_data = request.data
            server_data = server_data.dict()
            print(server_data)
            server_status_obj = Device_Status()
            add_server = Server_Information()
            add_server.types = server_data['server_type']
            add_server.model = server_data['model_type']
            add_server.manufacturer = server_data['manufacturer']
            add_server.make = server_data['make']
            add_server.device_id = server_data['device_id']
            add_server.serial_number = server_data['serial_number']
            add_server.server_capacity = server_data['server_capacity']
            add_server.ip_address = server_data['ip_address']
            add_server.location_of_hosting = server_data['loc']
            add_server.date_of_purchase = server_data['pur_date']
            add_server.updated_date = datetime.now()
            add_server.save()
            server_status_obj.device_information_id = add_server.id
            server_status_obj.category = "server"
            server_status_obj.user_id = 0
            server_status_obj.status = "active"
            server_status_obj.save()
            if "loc" in server_data and "device_id" in server_data:
                hosting_obj = Hosting_Information()
                hosting_obj.location = server_data["loc"]
                hosting_obj.category = "server"
                hosting_obj.device_id = server_data["device_id"] 
                hosting_obj.save()
            # server_data = server_data.dict()
            return Response(status=status.HTTP_200_OK, data={'status':'success','data':server_data})
        else:
            return redirect('login')  
                                
# @api_view(['POST','GET'])            
# def request_mobile(request):
    # d_type = ''
    # if request.method == 'GET':
        # if "user_id" in request.session:
            # req = request.data
            # req = req.dict()
            # d_type = req['device_type']
            # return Response(status=status.HTTP_200_OK, data={'status':'success'})
    # if request.method == 'POST':
        # u_id = request.session['user_id'] 
        # user_query = Register.objects.get(id = u_id)
        # if d_type == 'mobile':
            # mobile_d = []
            # device_status = Device_Status.objects.filter(category='mobile',status='inactive').values()
            # for item in device_status:
                # mobile_details = Mobile_Information.objects.filter(id=item['device_information_id'], location_of_hosting__exact = user_query.location).values() 
                # print(type(mobile_details))
                # mobile_lst = list(mobile_details)
                # if len(mobile_lst) > 0:
                    # mobile_d.append(mobile_lst[0])
            # return render(request,'request_mobile.html',{'mobile_data':mobile_d})
            
  
def client_dashboard(request):    
    mobile_d = []
    server_d = []
    if "user_id" in request.session:
        u_id = request.session['user_id'] 
        user_query = Register.objects.get(id = u_id)
        device_status_mobile = Device_Status.objects.filter(category='mobile',status='inactive').values()
        for item in device_status_mobile:
                mobile_details = Mobile_Information.objects.filter(id=item['device_information_id'], location_of_hosting__exact = user_query.location).values() 
                print(type(mobile_details))
                mobile_lst = list(mobile_details)
                if len(mobile_lst) > 0:
                    mobile_d.append({'type':mobile_lst[0]['types'],'model':mobile_lst[0]['model'],'os':mobile_lst[0]['os'],'device_mobile_id':mobile_lst[0]['device_id']})
        mbl_d = list({v['type']:v for v in mobile_d}.values())                    
        print(mbl_d)
        device_status_server = Device_Status.objects.filter(category='server',status='active').values()
        for item in device_status_server:
                server_details = Server_Information.objects.filter(id=item['device_information_id'], location_of_hosting__exact = user_query.location).values() 
                print(type(server_details))
                server_lst = list(server_details)
                if len(server_lst) > 0:
                     server_d.append({'type':server_lst[0]['types'],'model':server_lst[0]['model'],'device_server_id':server_lst[0]['device_id']})
        svr_d = list({v['model']:v for v in server_d}.values())                     
        print(svr_d)         
        return render(request,'client_dashboard.html',{'mobile_list':mbl_d,'server_list':svr_d,'col_mobile':mbl_d[0],'col_server':svr_d[0]})
    else:
        return redirect('login') 

@api_view(['POST'])
def client_request_mobile(request):
    if request.method == 'POST':
        req_data = request.data
        u_id = request.session['user_id'] 
        device_type = 'mobile'
        types = req_data['device_type']
        model = req_data['mobile_model']
        os = req_data['os']
        device_id = req_data['device_id']
        number_days = req_data["days"]
        request_date = datetime.now()
        request_status = ''
        pro_obj = Procurement_Request()
        pro_obj.user_id = u_id
        pro_obj.device_type = device_type
        pro_obj.types = types
        pro_obj.model = model
        pro_obj.os = os
        pro_obj.device_id = device_id
        pro_obj.number_days = number_days
        pro_obj.request_date = request_date
        pro_obj.request_status = request_status
        pro_obj.save()
        print('data',req_data)
        
        return Response(status=status.HTTP_200_OK, data={'status':'success'})    
        
@api_view(['POST'])
def client_request_server(request):
    if request.method == 'POST':
        data = request.data
        print('data',data)
        req_data = request.data
        u_id = request.session['user_id'] 
        device_type = 'server'
        types = req_data['device_type']
        model = req_data['mobile_model']
        device_id = req_data['device_id']
        number_days = req_data["days"]
        request_date = datetime.now()
        request_status = ''
        pro_obj = Procurement_Request()
        pro_obj.user_id = u_id
        pro_obj.device_type = device_type
        pro_obj.types = types
        pro_obj.model = model
        pro_obj.device_id = device_id
        pro_obj.number_days = number_days
        pro_obj.request_date = request_date
        pro_obj.request_status = request_status
        pro_obj.save()
        print('data',req_data)
        return Response(status=status.HTTP_200_OK, data={'status':'success'})  

def procurement_request(request):    
    procurement_list = []
    if "user_id" in request.session:
        procurement_details = Procurement_Request.objects.all()
        procurement_d = list(procurement_details)
        print(procurement_d) 
        for items in procurement_d:
            procurement_list.append({'user_id':items.user_id,'device_type':items.device_type,'types':items.types,
                                     'model':items.model,'os':items.os,'device_id':items.device_id,'number_days':items.number_days})
            print(procurement_list)
        return render(request,'procured_request.html',{'procurement_list':procurement_list,'col_list':procurement_list[0]})  


@api_view(['POST'])
def allotment_device(request): 
    mobile_lst = []
    if request.method == 'POST':
        data = request.data
        u_id = data['user_id'] 
        device_type = data['device_type']
        types = data['types']
        model = data['model']
        device_id = data['device_id']
        number_days = data["number_days"]
        current_date = datetime.now()
        mobile_d = Mobile_Information.objects.filter(device_id=device_id).values()
        procurement_d = Procurement_Request.objects.filter(device_id=device_id,user_id=u_id)
        allot_obj = Allotment()
        for mobile_id in mobile_d:
            # mobile_id.append({'id':mobile_id[0]["id"]})  
            allot_obj.user_id = u_id
            allot_obj.device_type = device_type
            allot_obj.device_information_id = mobile_id['id']
            allot_obj.allot_date = current_date
            # allot_obj.expired_date = current_date + timedelta.days(number_days) 
            allot_obj.expired_date = current_date
            allot_obj.save()
            print('done')
            device_status = Device_Status.objects.filter(device_information_id=mobile_id['id'],category=device_type)
            print(device_status)
            for s in device_status:
                s.status = 'active'
                s.user_id = u_id
                s.save()
            for p in procurement_d: 
                p.request_status = 'alloted'
                p.save()
            print('here in allotment',data)
            
        return Response(status=status.HTTP_200_OK, data={'status':'success'})  

            
        