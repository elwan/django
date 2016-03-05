from django.shortcuts import render,redirect,get_object_or_404
from mini_url.forms import MiniUrlForm
from mini_url.models import MiniUrl 
# Create your views here.

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
