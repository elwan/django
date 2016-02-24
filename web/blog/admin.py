from django.contrib import admin
from blog.models import Categorie,Article,Membre
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre','auteur','date','apercu_contenu')
    list_filter  = ('auteur','categorie')
    #date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre','contenu')
    

    def apercu_contenu(self,article):
        text = article.contenu[0:40]
        if len(article.contenu) > 40 :
            return "{}...".format(text)
        else:
            return text
        
admin.site.register(Categorie)
admin.site.register(Membre)
admin.site.register(Article,ArticleAdmin)
