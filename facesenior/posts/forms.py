from django import forms
class AddpostForm(forms.Form):
   posts = forms.CharField(label='enter your statues', max_length=1000)




