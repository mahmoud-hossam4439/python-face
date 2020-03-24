from django import forms
class AddfriendForm(forms.Form):
   friend = forms.CharField(label='enter username here', max_length=1000)


