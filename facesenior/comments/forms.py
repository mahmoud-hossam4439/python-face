from django import forms
class AddcommentForm(forms.Form):
   posts = forms.CharField(label='enter your statues', max_length=1000)




