from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from mini_url.forms import MiniUrlForm
from mini_url.models import MiniUrl
from django.views.generic import CreateView,UpdateView,DeleteView  
from django.core.urlresolvers import reverse_lazy
from django.contrib  import messages
# Create your views here.

#cette fonction peut etre Remplacer par createview 
def nouveau(request):
    if request.method == 'POST':
        form = MiniUrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            pseudo = form.cleaned_data['pseudo']
            form.save()
            return redirect(lire)
    else:
        form=MiniUrlForm()
    return render(request,'mini_url/urlform.html',locals())

def lire(request):
     liste = MiniUrl.objects.order_by('-nbre_acces')
     return render(request,'mini_url/liste.html',locals())


def redirection(request,code):
    mini = get_object_or_404(MiniUrl,code=code)
    mini.nbre_acces +=1
    mini.save()
    
    return redirect(mini.url,permanent=True)

#creer une vue de form avec Createview

class UrlCreate(CreateView):
    model = MiniUrl
    template_name="mini_url/urlform.html"
    form_class = MiniUrlForm
    success_url = reverse_lazy(lire)
    
#Mise à jour des données avec updateview

class UrlUpdate(UpdateView):
    model= MiniUrl
    template_name="mini_url/urlform.html"
    form_class = MiniUrlForm
    success_url = reverse_lazy(lire)

    def get_object(self,queryset=None): #Recuperer les objet avec le code et nons avec la clé primaire en surchageant la methide get_object 
        code = self.kwargs.get('code',None)
        return get_object_or_404(MiniUrl,code=code)

    def form_valid(self,form):
        self.object= form.save()
        #Envoyons un message à l'utilisateur
        messages.success(self.request,"Vos informations ont été mise à jour.")
        
        return HttpResponseRedirect(self.get_success_url())
    
#supprimer un object avec les views 
class UrlDelete(DeleteView):
    model=MiniUrl
    context_object_name="mini_url"
    template_name="mini_url/supprimer.html"
    success_url=reverse_lazy(lire)
    form_class= MiniUrlForm

    def get_object(self,queryset=None):
        code =self.kwargs.get('code',None)
        return get_object_or_404(MiniUrl,code=code)
