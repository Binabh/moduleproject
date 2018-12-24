from django.shortcuts import render

def showIndex(request):
    return render(request,'moduleproject/homepage.html', context = None)