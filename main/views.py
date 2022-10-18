from django.shortcuts import render


# Create your views here.
def index(request):
    print(request.POST)
    filter_option = request.POST.get("filter_opt")
    myfile = request.FILES.get("file")

    print(filter_option)
    # print(myfile.name)

    context = {
        "status": "",
    }
    return render(request, "index.html", context)
    # return render(request, "index.html", context, content_type, status, using)
