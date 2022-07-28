from django.shortcuts import HttpResponse 
   
def index(request):
    any = request.GET['number']
    any = int(any)**2
    print(any)

    return HttpResponse(f'{any}')