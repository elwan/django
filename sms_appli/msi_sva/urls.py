from django.conf.urls import patterns ,url
from . import views

urlpatterns =[
    url(r'^test/(?P<msg>"[\w\s]+")/',views.test),#test de capture des chaines de caractéres avec le regex 
    url(r'^sms_save/(?P<id_message>\d{6})/(?P<numero_court>\d{5})/(?P<numero_telephone>\d{12})/(?P<msg>"[\w\s]+")/(?P<mot_cle>\w+)/(?P<date_reception>\d{4}\-\d{2}\-\d{2})/$',views.save_sms),
    #sending message from nexmo
    url(r'^send_sms/(?P<sender>\w+)/(?P<numero>\d{12})/(?P<text>[\w\s]+)/$',views.envoi_sms),
    #url(r'^send_sms/',views.envoi_sms),
]
