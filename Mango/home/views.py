from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        'variable':'123'
    }
    return render(request,'index.html',context)
def about(request):
    context={
        'variable1':'458z'
    }
    return render(request,'about.html',context)

def checkout(request):
    return render(request,'checkout.html')

def products(request):
    return render(request,'products.html')

def booterms(request):
    return render(request,'booterms.html')