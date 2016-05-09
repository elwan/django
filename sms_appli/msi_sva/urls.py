from django.conf.urls import patterns ,url
from . import views

urlpatterns =[
    url(r'^test/(?P<msg>[\w\s]+)/',views.test),
    url(r'^sms_save/(?P<id_message>\d{6})/(?P<numero_court>\d{5})/(?P<numero_telephone>\d{12})/(?P<msg>[\w\s]+)/(?P<mot_cle>\w+)/(?P<date_reception>\d{2}\-\d{2}\-\d{4})/$',views.save_sms),
]
