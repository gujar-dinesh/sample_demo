from django.shortcuts import render,get_object_or_404
from .forms import userForm
from .models import Postuser, PostData
from django.http import HttpResponse
# Create your views here.
def post(request):
	a=userForm()
	if request.method =="POST":
		a=userForm(data=request.POST)
		print("request Received")
		if a.is_valid():
			new_post= a.save(commit=False)
			userd=Postuser.objects.all()
			print("Data Validated")
			name=get_object_or_404(Postuser,username__startswith=a.cleaned_data['Usera'])
			if(name):
				print("match Found")
				new_post.username=name
				new_post.save()
				print("post saved")
				return HttpResponse("SUCCESS")
			else:
				return HttpResponse("INVALID USERNAME")
	return render(request,"form_pg.html",{'a':a})
