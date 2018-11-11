from django.shortcuts import render

from .models import Listing

def index(request):
  listings = Listing.objects.all()
  print(listings)
  context = {
    'listings': listings
  }
  return render(request, 'listings/listings.html', context)

def listing(request):
  return render(request, 'listings/listing.html')

def search(request):
  return render(request, 'listings/search.html')