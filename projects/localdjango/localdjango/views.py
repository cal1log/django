from django.http import HttpResponse
import datetime

def greeting(request): # first view
    ''' function to say hello '''
    return HttpResponse("Hi Orlando")

def bye(request): # second view
    ''' function to say bye '''
    return HttpResponse("Bye Orlando")

def givetime(request): # third view with time function
    ''' function to give current time '''
    curdate = datetime.datetime.now()
    document = """
    <html>
    <body>
    <h1>
    Current time %s
    </h1>
    </body>
    </html> """ % curdate
    return HttpResponse(document)

def calage(request, age, agno): # fourth view with parameters in urls
    ''' function to calculate age '''
    final_age = agno - datetime.datetime.now().year + age
    document = "<html><body><h2>In %s you will have %s" %(agno, final_age)
    return HttpResponse(document)
