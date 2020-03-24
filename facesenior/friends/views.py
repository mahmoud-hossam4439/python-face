from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect

from users import models as usersmodel
from friends import models as friendmodel

from friends import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def addfriend(request):
 if request.method=='POST':
      form = forms.AddfriendForm(request.POST)
      if form.is_valid():
            # Add New Book to database
           user = request.user
           n = request.POST['friend']
           g = User.objects.get(username=n )
           friendmodel.friends.objects.create(frind_id=g, user_id = user )

           return HttpResponseRedirect("/posts/getpost")
 else:
    form = forms.AddfriendForm()
    return render(request,'addfriend.html',{"form":form})

@login_required
def get_myfriends(request):

     user = request.user

     mm = friendmodel.friends.objects.filter(user_id=user).values('frind_id__username')

     return render(request, 'get_myfriends.html', {'data': mm})




