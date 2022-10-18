from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "status": "",
    }
    return render(request, "index.html", context)
    # return render(request, "index.html", context, content_type, status, using)


# Create your views here.
def filter(request):
    print(request.POST)
    print("GOT HERE")
    filter_option = request.POST.get("filter_opt")
    myfile = request.FILES.get("file")

    print(filter_option)
    # print(myfile.name)

    context = {
        "status": "",
    }
    return render(request, "index.html", context)
    # return render(request, "index.html", context, content_type, status, using)
