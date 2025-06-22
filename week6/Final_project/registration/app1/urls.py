from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('adminpanel/',views.admin_panel,name='admin'),
    path('add/',views.add_user,name='add'),
    path('update/<str:id>',views.update_user,name='update'),
    path('delete/<str:id>',views.delete_user,name='delete')
]