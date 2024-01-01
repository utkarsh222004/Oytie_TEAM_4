"""
URL configuration for assignment_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from assignment_management import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('login/',views.login),
    path('loginmap/',views.loginmap,name="loginmap"),
    path('teacherpage/',views.loginmap,name="teacherpage"),
    path('studentpage/',views.loginmap,name="studentpage"),
    path('studentregister/',views.studentregister,name="studentregister"),
    path('teacherregister/',views.teacherregister,name="teacherregister"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name='logout'),
    path('assignment_response/<int:id>',views.assignment_response,name="assignment_response"),
    path('edit_assign/<int:id>',views.edit_assign,name="edit_assign"),
    path('check/<int:assign>/<int:id>',views.check,name="check"),
    path('submit_solution/',views.submit_solution,name="submit_solution"),
    path('assign_marks/',views.assign_marks,name='assign_marks'),
    path('assignment_creation/',views.assignment_creation,name="assignment_creation"),
    path('add_assignment/',views.add_assignment,name="add_assignment")
]


 