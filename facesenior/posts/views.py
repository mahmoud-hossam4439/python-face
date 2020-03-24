from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from posts import models as postsmodel
from users import models as usersmodel
from friends import models as friendmodel
from posts import forms
from django.contrib.auth.decorators import login_required

##############################################


@login_required
def addpost(request):
 if request.method=='POST':
      form = forms.AddpostForm(request.POST)
      if form.is_valid():
            # Add New Book to database
           user = request.user
           n = request.POST['posts']
           postsmodel.posts.objects.create(post_desc=n , user_id = user )

           return HttpResponseRedirect("getpost")
 else:
    form = forms.AddpostForm()
    return render(request,'addposts.html',{"form":form})



@login_required
def get_all(request):

    user = request.user
    fuser = friendmodel.friends.objects.filter(user_id=user).values('frind_id')
    fuser =list(fuser)
    fuserlist = []
    for u in fuser:
        fuserlist.append(u['frind_id'])
    fuserlist.append(user.id)

    mm = postsmodel.posts.objects.filter(user_id__in = fuserlist   ).values('post_desc' , 'user_id__username' , 'post_id')
    print(mm)
    return render(request, 'get_posts.html', {'data': mm})

@login_required
def get_mypost(request):

    user = request.user

    mm = postsmodel.posts.objects.filter(user_id = user ).values('post_desc' , 'user_id__username')

    return render(request, 'get_mypost.html', {'data': mm})



@login_required
def get_delete(request , post_id):

    postsmodel.posts.objects.filter(post_id=post_id , user_id = request.user ).delete()

    return HttpResponseRedirect("/posts/getpost")



@login_required
def get_edit(request , post_id):
    if request.method == 'POST':
        form = forms.AddpostForm(request.POST)
        if form.is_valid():
            # Add New Book to database
            user = request.user
            n = request.POST['posts']

            t = postsmodel.posts.objects.get(post_id = post_id)
            t.post_desc = n  # change field
            t.save()  # this will update only

            return HttpResponseRedirect("/posts/getpost")
    else:
        vpost =  postsmodel.posts.objects.filter(post_id = post_id  ).values('post_desc' )
        form = forms.AddpostForm(initial = {'posts':vpost[0]['post_desc']})
        return render(request, 'editpost.html', {"form": form ,'pp':post_id})
