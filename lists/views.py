from django.http import HttpResponse

# Create your views here.
def home_page(request):
    ''' Home page '''
    return HttpResponse("<html><title>Home Page</title><body><h1>Home Page</h1><body></html>")