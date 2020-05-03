from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your views here.
def index(request):
	perSlide = 4
	cats = {item['category'] for item in Product.objects.values('category')}
	allprods = []
	for cat in cats:
		prod = Product.objects.filter(category=cat)
		nSlides = ceil(len(prod) / perSlide)
		allprods.append([prod, range(nSlides), perSlide, nSlides])
	params = {'allprods':allprods}
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
