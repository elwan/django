from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$',views.ListePassager.as_view(),name="liste_passager"),
    url(r'^add$',views.PassagerCreate.as_view(),name="create_passager"),
    url(r'^update/(?P<pk>\d)$',views.PassagerUpdate.as_view(),name="update_passager"),
    url(r'^delete/(?P<pk>\d)$',views.PassagerDelete.as_view(),name="delete_passager"),
    
    
]

