from django.shortcuts import render

# Create your views here.
def muni(request):
    d={'a':10,'b':30,'c':90}
    return render(request,'muni.html',d)
