from django.shortcuts import render
from .models import Davlat, Region
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Count


def index(request):
    regions = Region.objects.values('country_id').annotate(c=Count("*"))

    regions = {r["country_id"]: r["c"] for r in regions}

    # for r in regions:
    #     print(r)

    return render(request, 'main/index.html', {
        "list": Davlat.objects.all(),
        "regions": regions
    })


def create(request):
    if request.method == 'POST':
        d = Davlat(name=request.POST['name'], poytaxt=request.POST['poytaxt'])
        d.save()
        messages.success(request, "Ushbu davlat muvaffaqiyatli yaratildi!")
        return redirect('main_index')

    return render(request, 'main/edit.html')


def log(request):
    context = {
        "list": Davlat.objects.all()
    }
    return render(request, 'main/log.html')


def update(request, id):
    try:
        d = Davlat.objects.get(id=id)
    except Davlat.DoesNotExist:
        return redirect('main_index')

    if request.method == 'POST':
        d.name = request.POST['name']
        d.poytaxt = request.POST['poytaxt']
        d.save()
        messages.success(request, "Ushbu davlat muvaffaqiyatli tahrirlandi!")
        return redirect('main_index')

    return render(request, 'main/edit.html', {
        'd': d
    })


def delete(request, id):
    try:
        Davlat.objects.filter(id=id).delete()
        messages.success(request, "Ushbu davlat muvaffaqiyatli o'chirildi!")
    except:
        messages.warning(request, "Ushbu davlatni o'chirib bo'lmaydi")
    return redirect('main_index')


def region_create(request, id):
    try:
        country = Davlat.objects.get(id=id)
    except Davlat.DoesNotExist:
        return redirect('main_index')

    if request.method == 'POST':
        region = Region(name=request.POST.get('name'), country=country)
        # region.country_id = country.id
        region.save()
        messages.success(request, "Ushbu viloyat muvaffaqiyatli yaratildi!")
        return redirect('main_region_index', id=country.id)

    return render(request, 'main/region_edit.html', {
        'country': country
    })


def region_update(request, id):
    try:
        region = Region.objects.get(id=id)
    except Region.DoesNotExist:
        return redirect('main_index')

    if request.method == 'POST':
        region.name = request.POST['name']

        region.save()
        messages.success(request, "Ushbu viloyat muvaffaqiyatli tahrirlandi!")
        return redirect('main_region_index', id=region.country_id)
    return render(request, 'main/region_edit.html', {
        'country': region.country,
        'region': region
    })


def region_index(request, id):
    try:
        country = Davlat.objects.get(id=id)
    except Davlat.DoesNotExist:
        return redirect('main_index')

    regions = Region.objects.filter(country=country).all()

    return render(request, 'main/region_index.html', {
        'country': country,
        'regions': regions
    })


def region_delete(request, id, cid):
    Region.objects.filter(id=id).delete()
    messages.success(request, "Ushbu viloyat muvaffaqiyatli o'chirildi!")
    return redirect('main_region_index', id=cid)