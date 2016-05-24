from django.conf.urls import patterns, url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns= [
    url(r'^ajouter/',views.MesssageCreate.as_view(),name="nouveau_message"),
    url(r'^liste/',views.ListeMessage.as_view(),name="lister_message"),
    url(r'^editer/(?P<code>\w{6})$',views.MessageUpdate.as_view(),name="update_message"),
    url(r'^delete/(?P<code>\w{6})$',views.MessageDelete.as_view(),name="delete_message"),
    url(r'^envoi/(?P<code>\w{6})$',views.envoi_message,name="envoyer_message"),
    
]


