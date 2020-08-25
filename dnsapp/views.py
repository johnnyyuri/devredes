from django.shortcuts import render,redirect
from .models import Registro, Categoria
from django.http import HttpResponse
from .form import RegisterForm
import datetime


# Create your views here.

def listagem(request):

    data={}
    #data2={}

    data['registro']= Registro.objects.all() 
#    data2['categoria']= Registro.objects.all() 

    return render (request, 'listagem.html', data)


def addreg(request):
#https://www.youtube.com/watch?v=3XOS_UpJirU
    data = {}
    form = RegisterForm(request.POST or None)

    # Verificar se o form é valido
    if form.is_valid() :
      #  dominio= None
        dom = form.cleaned_data['dominio2'] #pega o domino, pq a RN- regra de negocio diz que pode ter apenas um dominio para um ip

        try:  
            dominio= Registro.objects.get(dominio2=dom)
        
        except Registro.DoesNotExist :
            form.save() #Salva
            return redirect('url_listagem') #E redireciona para a listagem

        else:
            dominio= Registro.objects.get(dominio2=dom)

            if dominio.dominio2 == dom :
                form = RegisterForm(None)

            else :
                form.save() #Salva
                return redirect('url_listagem') #E redireciona para a listagem

    data['form'] = form
    return render(request, 'form.html',data)

def delete(request,pk):
    data={}
    registro= Registro.objects.get(pk=pk) 
    registro.delete()      
    return redirect('url_listagem') # E redireciona para a listagem

def update(request, pk):

    data = {}
    registro = Registro.objects.get(pk=pk)

    form = RegisterForm(request.POST or None, instance=registro) #Passar o formulario preenchido
    
    if request.method == "POST" :

        dom= registro.dominio2
        print(pk)   
       # print(dom)
  
        try:  
            dominio= Registro.objects.get(dominio2=dom)
        
        except Registro.DoesNotExist :
          
            form.save() #Salva
            return redirect('url_listagem') #E redireciona para a listagem

        else:
            dominio= Registro.objects.get(dominio2=dom)

            if dominio.dominio2 == dom :
                
                form.save() #Salva
                return redirect('url_listagem') #E redireciona para a listagem

            else :
                return redirect('url_listagem') #E redireciona para a listagem



    data['form'] = form
    data['registro'] = registro

    return render(request, 'form.html', data)

