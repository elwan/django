from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^accueil$',views.home),
    #url(r'^article/(?P<id_article>\d+)$',views.vue_article),
    url(r'^add/(?P<nbr1>\d+)/(?P<nbr2>\d+)$',views.calcul),
    url(r'^redirection$',views.view_redirection),
    url(r'^date$',views.heure_actuelle),
    url(r'^div/(?P<nbr1>\d+)/(?P<nbr2>\d+)$',views.division),
   # url(r'^$',views.accueil),
    url(r'^$',views.ListeArticles.as_view(),name="blog_liste"),
    url(r'^article/(?P<id>\d+)$',views.lire),
    url(r'^contact/$',views.contact),
    url(r'articleform/$',views.articleform),
    url(r'membre/$',views.nouveau_membre),
    url(r'^faq',views.FaqView.as_view(),name="faq"),
]



