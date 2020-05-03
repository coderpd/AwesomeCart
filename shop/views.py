from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your views here.
def index(request):
	products = Product.objects.all()
	perSlide = 4
	nSlides = ceil(len(products)/perSlide)
	params = {'no_of_slides':nSlides, 'per_slide':perSlide, 'range':range(nSlides), 'product': products}
	return render(request, 'shop/index.html', params)


def about(request):
	return render(request, 'shop/about.html')


def contact(request):
	return HttpResponse('We are at contact')


def tracker(request):
	return HttpResponse('We are at tracker')


def search(request):
	return HttpResponse('We are at search')


def prodView(request):
	return HttpResponse('We are at productView')


def checkout(request):
	return HttpResponse('We are at checkout')
