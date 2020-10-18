from django.shortcuts import render
from .models import Estate
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def estate_list(request):
    estates = Estate.objects.all().order_by('published')
    return render(request, 'estates/estate_list.html', {'estates': estates})


def estate_detail(request):
    pass


@login_required(login_url='/owner/login')
def estate_create(request):
    form = forms.CreateEstateOffer()
    return render(request, 'estates/estate_add.html', {'form': form})


