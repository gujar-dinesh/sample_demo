from django import forms
from .models import PostData
from .models import Postuser
 
class userForm(forms.ModelForm):
	Usera=forms.CharField()
	class Meta():
		model=PostData
		fields=('text',)
