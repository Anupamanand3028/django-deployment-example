from django.urls import path
from AppTwo import views

# TEMPLATE TAGGING
app_name = 'AppTwo'

urlpatterns = [
    path('help/', views.help, name="help"),
    path('relative/',views.relative,name="relative"),
    path('users/',views.users, name="users"),
    path('register/',views.register, name="register"),
    path('forms/',views.form_name_view,name="form_name"),
    path('login/',views.user_login, name="user_login")
]
