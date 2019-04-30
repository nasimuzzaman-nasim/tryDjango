from django.shortcuts import render
from products.models import Product

# Create your views here.


def love(request,*args,**kwargs):
	item = {
	"a":"good",
	"b": "better",
	"c": "best",
	"lis": [1,2,1,3],
	"title" : "<h3>this is funny, huh?</h3>"
	}
	return render(request,"love.html",item)

def new(request,*args,**kwargs):
	return render(request,'redirect.html',{})
