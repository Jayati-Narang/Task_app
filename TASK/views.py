from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Data

def top_5_rated(request):
    out = Data.get_top_5_rated(Data)
    return HttpResponse(out)

def total_payment_wise(request):
    out = Data.get_total_payment_wise(Data)
    return HttpResponse(out)

def avg_rating_product_branch_wise(request):
    out = Data.get_avg_rating_product_branch_wise(Data)
    return HttpResponse(out) 