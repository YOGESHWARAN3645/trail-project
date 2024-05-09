from django.urls import path
from sign_up import views

urlpatterns = [
    path('',views.login_page,name= 'login_page'),
    path('register/',views.registration_page, name= 'register'),
    path('registered/',views.registration_success,name='registration_successful'),
    path('home/',views.home_page,name='home_page'),
    path('home/ai',views.ai_page,name='ai_page'),
    path('home/cloud',views.cloud_page,name='cloud_page'),
    path('lmw/',views.lmw_page,name='lmw_page'),
    path('contact/',views.contact_page,name='contact_page'),


]

