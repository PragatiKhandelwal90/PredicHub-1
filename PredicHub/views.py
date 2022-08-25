from django.shortcuts import render

# Views
def index(request):
    return render(request, "index.html")