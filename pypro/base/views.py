from django.http import HttpResponse


# Create your views here.
def home(reuqests):
    return HttpResponse('Óla Django')
