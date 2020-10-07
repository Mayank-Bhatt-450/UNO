"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
urlpatterns = [#path('',views.hello.as_view())

path('login', views.log_in,name='log_in'),
path('update_status', views.update_status),
#path('login',views.login_view, name = 'login ')
path("<username>,<password>_login", views.login,name='login '),
path('register', views.register,name='register'),
path('<responce>_myturn', views.myturn),
path("<username>_is_joined",views.is_joined),
path("<username>_create_room",views.create_room),
path("<username>,<host>_join_room",views.join_room),
path("<host>_wating_room",views.wating_room),
path("<username>,<host>_leave_waiting",views.leave_waiting),
path("<username>,<host>_leave_game",views.leave_game),
path("<host>_start_game",views.start_game),
path("<username>_game_state_view",views.game_state_view)

]
