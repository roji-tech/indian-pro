from django.shortcuts import render


# Create your views here.
def index(request):
  print(request.POST)

  context = {
    "status": "",
  }
  return render(request, "index.html", context)
  # return render(request, "index.html", context, content_type, status, using)
