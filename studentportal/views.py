from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request):
    context = {}
    if request.method == "GET":
        return render(request, 'studentportal/index.html', context)
