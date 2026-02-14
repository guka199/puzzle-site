from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.GET.get("key") != "abc123":
        return HttpResponse("Not allowed")
    return render(request, "puzzle/index.html")

