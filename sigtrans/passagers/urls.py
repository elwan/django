from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$',views.ListePassager.as_view(),name="liste_passager"),
]
