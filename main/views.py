from urllib.request import Request
from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
# Create your views here.


def index(request):
    if request.method == "POST":
        myfile = request.FILES.get("file")
        filter_option = request.POST.get("filter_opt")
        if myfile:
            print(myfile.name)
        print("THIS IS A POST")
        print(filter_option)

        print("GOT HERE")

        context = {
            "status": "this",
            "filter_option": filter_option,
            "file": myfile
        }
        return render(request, "index.html", context)

    return render(request, "index.html")
    # return render(request, "index.html", context, content_type, status, using)
