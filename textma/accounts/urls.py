from django.conf.urls import patterns, url,include 
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
   # url(r'^login/$','django.contrib.auth.views.login',name='login',
   #             kwargs={'template_name': 'comptes/login.html'}),
    #url(r'^logout/$','django.contrib.auth.views.logout',name='logout',
    #                kwargs={'next_page': '/'}),
    #url('^',include('django.contrib.auth.urls')),
    #url(r'^login/',auth_views.login,{'template_name':'accounts/login.html'},name='login'),
    url(r'^$',views.home,name='home'),
    #url(r'^home/',views.home),
    
]
