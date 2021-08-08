from django.views.generic import TemplateView
from django.views.generic import CreateView 

# Create your views here.

#def home(request):
#    return render(request, 'index.html')

class HomeView(TemplateView):
    template_name = 'index.html'