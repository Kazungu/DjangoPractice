from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	my_content = {
		"my_text": "This is a good thing",
		"my_number": "Better call Saul",
		"my_list": [123,45,6,678,780]
	}
	return render(request,'home.html',my_content)