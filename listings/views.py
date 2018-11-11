from django.shortcuts import render

from .models import Listing

def index(request):
  listings = Listing.objects.all()
  context = {
    'listings': listings
  }
  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = Listing.objects.get(pk=listing_id)
  context = {
    'listing': listing
  }
  return render(request, 'listings/listing.html', context)

def search(request):
  return render(request, 'listings/search.html')