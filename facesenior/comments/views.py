from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
# from comments import forms
from comments import models

# Create your views here.
def get_all(request):
    return HttpResponse("andromeda")