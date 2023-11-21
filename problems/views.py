from django.http import HttpResponse
from django.template import loader

# Create your views here.
def problems(request):
    template = loader.get_template('problems.html')
    return HttpResponse(template.render())