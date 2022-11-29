from django.urls import path

from . import views

urlpatterns=[
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('client_dashboard',views.client_dashboard, name='client_dashboard'),
    path('admin_dashboard',views.admin_dashboard, name='admin_dashboard'),
    path('get_register_page',views.get_register_page, name='get_register_page'),
    path('register_user',views.register_user, name='register_user'),
    path('login_details/', views.login_details, name="login_details"),
    path('dashboard/add_mobile/', views.add_mobile, name="add_mobile"),
    path('dashboard/edit_mobile_information/<int:mobile_id>/', views.edit_mobile_information, name="edit_mobile_information"),
    path('dashboard/edit_server_information/<int:server_id>/', views.edit_server_information, name="edit_server_information"),
    path('dashboard/add_mobile/save_mobile_information/', views.save_mobile_information, name="save_mobile_information"),
    path('dashboard/add_server/', views.add_server, name="add_server"),
    path('dashboard/add_server/save_server_information/', views.save_server_information, name="save_server_information"),
    path('dashboard/add_equipments/',views.add_equipments, name='add_equipments'),
    path('client_request_mobile/',views.client_request_mobile, name='client_request_mobile'),
    path('client_request_server/',views.client_request_server, name='client_request_server'),
    path('dashboard/procurement_request/',views.procurement_request, name='procurement_request'),
    path('dashboard/procurement_request/allotment_device/',views.allotment_device, name='allotment_device')
    
]
