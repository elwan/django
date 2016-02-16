from django.conf.urls import patterns,url
#from . import views

urlpatterns =patterns('blog.views',
                      url(r'^accueil$','home'),
                      url(r'^article/(?P<id_article>\d+)$','vue_article'),
                      url(r'^add/(?P<nbr1>\d+)/(?P<nbr2>\d+)$','calcul'),
)



