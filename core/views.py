from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'index.html', context)           # Se puede llamar al archivo index.html directamente ya que en settings.py en TEMPLATES -> DIRS se establece la ubicacion de la carpeta en donde esta  index.html