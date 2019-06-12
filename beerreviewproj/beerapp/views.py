from django.shortcuts import render, get_object_or_404
from .models import BeerType, Beer, Review
from .forms import BeerForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'beerapp/index.html')

def gettypes(request):
    type_list=BeerType.objects.all()
    return render(request, 'beerapp/types.html' ,{'type_list' : type_list})

def getbeers(request):
    beers_list=Beer.objects.all()
    return render(request, 'beerapp/beers.html', {'beers_list': beers_list})

def beerdetails(request, id):
    prod=get_object_or_404(Beer, pk=id)
    discount=prod.memberdiscount
    reviews=Review.objects.filter(beer=id).count()
    context={
        'prod' : prod,
        'discount' : discount, 
        'reviews' : reviews,
    }
    return render(request, 'beerapp/beerdetails.html', context=context)

@login_required
def newBeer(request):
     form=BeerForm
     if request.method=='POST':
          form=BeerForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=BeerForm()
     else:
          form=BeerForm()
     return render(request, 'beerapp/newbeer.html', {'form': form})

@login_required
def newReview(request):
    form=ReviewForm
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'beerapp/newreview.html', {'form' : form})


def loginmessage(request):
    return render(request, 'beerapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'beerapp/logoutmessage.html')