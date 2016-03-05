from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^add$',views.nouveau,name="url_nouveau"),
    url(r'^liste$',views.lire,name="url_liste"),
    url(r'^(?P<code>\w{6})/$',views.redirection,name="url_redirection"),
    
]

