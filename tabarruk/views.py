from django.shortcuts import render,redirect
from .forms import ContactForm
from .bot import get_contact
from .models import Product,Product_uz

def index(request):
        form=ContactForm()
        if request.method=="POST":
            form=ContactForm(request.POST)
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            middlename = request.POST.get('middlename')
            phone = request.POST.get('phone')
            x=str("name : "+ name +"\n"
                  'surname : '+ surname + "\n"
                  'middlename : '+ middlename + "\n"
                  'phone : '+ phone + "\n")
            get_contact(x)
            if form.is_valid():
                form.save()
                return redirect("index")
        products_uz = Product_uz.objects.all()
        context={'form':form,'products_uz': products_uz}
        return render(request,"index.html",context)


def ru(request):
        form = ContactForm()
        if request.method == "POST":
            form = ContactForm(request.POST)
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            middlename = request.POST.get('middlename')
            phone = request.POST.get('phone')
            x = str("name : " + name + "\n"
            'surname : ' + surname + "\n"
            'middlename : ' + middlename + "\n"
            'phone : ' + phone + "\n")
            get_contact(x)
            if form.is_valid():
                form.save()
                return redirect("ru")
        products = Product.objects.all()
        context = {'form': form,'products': products}

        return render(request, "ru.html", context)
