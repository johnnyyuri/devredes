from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)#define o tipo de registro
    data_cricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Registro(models.Model):

    ip = models.CharField(max_length=15)#ip
    
    dominio2 = models.CharField(max_length=30)#dominio

    prioridade = models.CharField(max_length=1) 

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       
        a = "| "
        a= a + self.dominio2
        a = a + " |"
        a= a +  str(self.categoria) 
        a=a+" |"
        a= a + self.ip
        a=a+" |"
        return a