from django.shortcuts import render, redirect
from .models import Category, Product
from datetime import datetime
from .forms import CategoryForm


# Create your views here.
def add_category(request):
    user = request.user
    content = {}
    cat_form = CategoryForm
    content['cat_form'] = cat_form
    content['btn_name'] = 'Add'
    if request.method == 'POST':
        cat_name = request.POST['cat_name']
        form = CategoryForm(request.POST)
        if form.is_valid():
            check = Category.objects.filter(user=user, cat_name=cat_name)
            dtnow = datetime.now()
            dtformat = datetime.strftime(dtnow, '%Y-%m-%d')
            if check:
                print("Category Already Exist")
            else:
                Category.objects.create(user=user, cat_name=cat_name, created=dtformat, updated=dtformat)

    user_categories = Category.objects.filter(user=user)
    if len(user_categories) > 0:
        content['category'] = user_categories

    return render(request, 'category.html', content)


def edit_cat(request, id):
    user = request.user
    # import pdb; pdb.set_trace()
    check = Category.objects.filter(user=user, id=id)
    content = {}
    cat_form = CategoryForm(initial={'cat_name': check[0].cat_name })
    content['btn_name'] = 'Update'

    if request.method == 'POST':
        cat_name = request.POST['cat_name']
        form = CategoryForm(request.POST)
        if form.is_valid():

            dtnow = datetime.now()
            dtformat = datetime.strftime(dtnow, '%Y-%m-%d')
            check2 = Category.objects.filter(user=user, cat_name=cat_name)
            if check and not check2:
                check.update(user=user, cat_name=cat_name, updated=dtformat)
                return redirect('categories')
            else:
                msg = 'Category Already Available'

    user_categories = Category.objects.filter(user=user)
    content['cat_form'] = cat_form
    if len(user_categories) > 0:
        content['category'] = user_categories

    return render(request, 'category.html', content)


def destroy_cat(request, id):
    user = request.user
    cat_to_del = Category.objects.filter(id=id,user=user)
    cat_to_del.delete()

    return redirect('categories')


def show_product(request):
    user = request.user
    content = {}
    product = Product.objects.filter(user=user)
    content['product'] = product

    return render(request,'view_product.html',content)


def add_product(request):
    user = request.user
    cat_data = Category.objects.filter(user=user)
    content = {}
    msg = ''
    content['cat_data'] =cat_data
    if request.method == 'POST':
        category = Category.objects.get(id=request.POST['category'])
        product_name = request.POST['product_name']
        image = request.FILES['file_name']
        category = category
        descriptions = request.POST['product_details']
        check = Product.objects.filter(user=user,product_name=product_name)
        if check:
            msg = 'Product Already Added'
        else:
            Product.objects.create(user=user, product_name=product_name, image=image, category=category, description=descriptions)
            msg = 'Product Added Successfully'
        content['msg'] = msg

    return render(request,'add_update.html', content)


def edit_product(request, id):
    pass


def destroy_product(request, id):
    prod_to_del = Product.objects.get(id=id)
    prod_to_del.delete()

    return redirect('crud_product')


