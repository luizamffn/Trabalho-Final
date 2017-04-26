from django.db import models

# Create your models here.

class Questao(models.Model):
  pergunta = models.CharField(max_length = 255)
  a = models.CharField(max_length = 255)
  b = models.CharField(max_length = 255)
  c = models.CharField(max_length = 255)
  d = models.CharField(max_length = 255)
  correta = models.CharField(max_length = 1)

  def __str__(self):
    return self.pergunta