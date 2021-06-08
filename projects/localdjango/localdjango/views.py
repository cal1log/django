from django.http import HttpResponse

def greeting(request): # first view
    ''' function to say hello '''
    return HttpResponse("Hi Orlando")

def bye(request): # second view
    ''' function to say bye '''
    return HttpResponse("Bye Orlando")