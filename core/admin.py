from django.contrib import admin
from .models import *

# Register your models here.

class QuestaoAdmin(admin.ModelAdmin):
  list_display = ('pergunta', 'correta')

admin.site.register(Questao, QuestaoAdmin)