from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Data
from .forms import DataCreate

def index(request):
    data = Data.objects.all()
    return render(request, 'read.html', {'data': data})

def create(request):
    create = DataCreate()
    if request.method == 'POST':
        create = DataCreate(request.POST)
        if create.is_valid():
            create.save()
            return redirect('index')
        else:
            return HttpResponse("""Please fill the form correctly""")
    else: 
        return render(request, 'create.html', {'create': create})
    
def update_data(request, invoice_id):
    try:
        obj = Data.objects.get(invoice_id = invoice_id)
    except Data.DoesNotExist:
        return redirect('index')
    
    form = DataCreate(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'create.html', {'create': form})

def delete_data(request, invoice_id):
    try: 
        obj = Data.objects.get(invoice_id = invoice_id)
    except Data.DoesNotExist:
        return redirect('index')
    
    obj.delete()
    return redirect('index')

def top_5_rated(request):
    out = Data.get_top_5_rated(Data)
    # return HttpResponse(out)
    return render(request, 'top_5.html', {'data': out})

def total_payment_wise(request):
    out = Data.get_total_payment_wise(Data)
    return render(request, 'total_payment_wise.html', {'data': out})
    
    # return HttpResponse(out)

def avg_rating_product_branch_wise(request):
    out = Data.get_avg_rating_product_branch_wise(Data)
    return render(request, 'avg_rating.html', {'data': out})
    
    # return HttpResponse(out) 