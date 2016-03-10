from django.conf.urls import url
from . import views

urlpatterns=[
    #url(r'^add$',views.nouveau,name="url_nouveau"),
    url(r'^add$',views.UrlCreate.as_view(),name="url_nouveau"), #nouveau url basé sur la classe createview dans les vues génériques
    #url(r'^edition/(?P<pk>\d)$',views.UrlUpdate.as_view(),name="url_update"),#Url pour éditer les raccourcis url
    #faire un url avec code url comme identifiant pour modifier notre object
    url(r'^edition/(?P<code>\w{6})$',views.UrlUpdate.as_view(),name='url_update'),
    url(r'^liste$',views.lire,name="url_liste"),
    url(r'^(?P<code>\w{6})/$',views.redirection,name="url_redirection"),
    #url pour supprimer  une entree avec la class deleteview
    url(r'^supp/(?P<code>\w{6})$',views.UrlDelete.as_view(),name="url_delete")
    
]


