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
	params = {'allprods': allprods}
	return render(request, 'shop/index.html', params)


def about(request):
	return render(request, 'shop/about.html')


def contact(request):
	return render(request, 'shop/contact.html')


def tracker(request):
	return render(request, 'shop/tracker.html')


def search(request):
	return render(request, 'shop/search.html')


def prodView(request, id):
	# Fetch the product using the id
	params = {'Product': Product.objects.filter(id=id)[0]}
	return render(request, 'shop/prodview.html', params)


def checkout(request):
	return render(request, 'shop/checkout.html')
