from django.db import models

# tabela de dados funcionarios

class Funcionario(models.Model):

  id = models.AutoField(primary_key=True)

  nome = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )


  idade = models.IntegerField(
    default=0,
    null=False,
    blank=False
  )


  cargo = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )


  

  

  objetos = models.Manager()