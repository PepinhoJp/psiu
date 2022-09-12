from django.db import models

# Create your models here.
class User(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharFilent(max_length=100)
  email = models.EmailField("Favor escrever um email valido", "Invalido")
  celular = models.CharFilent(max_length=13)  
