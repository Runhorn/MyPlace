from django.shortcuts import render
from .models import Estate
# Create your views here.


def estate_list(request):
    estates = Estate.objects.all().order_by('published')
    return render(request, 'Estates/estate_list.html', {'estates': estates})
