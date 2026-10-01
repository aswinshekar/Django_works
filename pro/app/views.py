from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

# function based

# def Home(request):
#     if request.method == "GET":
#         return HttpResponse("Welcome To Django")
#
# #define INDEX VIEW -- return "index page"
# def index(request):
#     if request.method=="GET":
#         return HttpResponse("WELCOME TO INDEX PAGE")

from django.views import View
class Home(View):
    def get (self,request):
        return HttpResponse("WELCOME HOME")
class Index(View):
    def get (self,request):
        return HttpResponse("WELCOME INDEX")
