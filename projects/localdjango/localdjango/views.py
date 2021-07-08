from django.http import HttpResponse
import datetime
from django.template import Template, Context


def greeting(request): # first view
    ''' function to say hello '''
    return HttpResponse("Hi Orlando")

def bye(request): # second view
    ''' function to say bye '''
    return HttpResponse("Bye Orlando")

def givetime(request): # third view with time function
    ''' function to give current time '''
    curdate = datetime.datetime.now()
    document = open("/home/calilog/django/projects/localdjango/localdjango/templates/givetime.html")
    plt = Template(document.read())
    document.close()
    ctx = Context()
    doc = plt.render(ctx)        
    return HttpResponse(doc)

def calage(request, age, agno): # fourth view with parameters in urls
    ''' function to calculate age '''
    final_age = agno - datetime.datetime.now().year + age
    document = "<html><body><h2>In %s you will have %s" %(agno, final_age)
    return HttpResponse(document)
