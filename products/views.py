from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, Http404
from .models import Product
from .forms import ProductForm, RawProductForm


def home_view(request,*args,**kwargs):
    context = {

    }
    return render(request,'home.html',context)

def products_createX(request):
    my_form = RawProductForm()

    if request.method == 'POST':
        my_form = RawProductForm(request.POST or None)
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)
        my_form = RawProductForm()
    context = {
        'form': my_form
    }
    return render(request,'product_temp/productForm_viewsX.html',context)


def products_detail(request,*args,**kwargs):
    obj = Product.objects.all()
    """context = {
        'tilte' : obj.title,
        'desc'  : obj.desc,
        'price' : obj.price,
        'status': obj.status
    }"""

    context = {
        'obj' : obj
    }
    return render(request, "product_temp/detail.html", context)

def dynamic_detail(request,*args,**kwargs):
    queryset = Product.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'product_temp/dynamic_detail.html',context)

# def products_createX(request):
#     if request.method == "POST":
#         new_title = request.POST.get('title')
#         #Product.objects.create(title=new_title)
#         print(new_title)
#     context = {}
#     return render(request, 'product_temp/productForm_viewsX.html', context)

def products_create(request):
    # obj = Product.objects.get(id=10)
    # initial_data = {
    #     'title': 'Awesome title'
    # }

    # form = ProductForm(request.POST or None, initial=initial_data, instance=obj)

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'product_temp/productForm_views.html', context)


def dynamic_lookup_view(request, my_id):
    #get_object_or_404 
    #Http404
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    obj = get_object_or_404(Product, id=my_id)
    context = {
        'obj': obj
    }
    return render(request, 'product_temp/lookup.html', context)


def product_delete_view(request,my_id):
    obj = get_object_or_404(Product,id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../../")
    context = {
        'obj': obj
    }
    return render(request,'product_temp/delete_view.html',context)



def product_edit_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)

    initial_data = {
        'title': obj.title,
        'desc' : obj.desc,
        'price': obj.price
    }
    form = ProductForm(request.POST or None,initial=initial_data,instance=obj)

    if form.is_valid():
        form.save()
        return redirect('../../')
    ProductForm()

    context = {
        'form': form
    }
    return render(request, 'product_temp/edit_view.html',context)


