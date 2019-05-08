from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from candy.forms.candy_form import CandyCreateForm, CandyUpdateForm
from candy.models import Candy, CandyImage


# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        candies = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.candyimage_set.first().image
        } for x in  Candy.objects.filter(name__icontains=search_filter)]
        # candies = list(Candy.objects.filter(name__icontains=search_filter).values())
        return JsonResponse({'data': candies})
    context = {'candies': Candy.objects.all().order_by('name')}
    return render(request, 'candy/index.html', context)

def get_candy_by_id(request, id):
    return render(request, 'candy/candy_details.html', {
        'candy': get_object_or_404(Candy, pk=id)
    })

def create_candy(request):
    if request.method == 'POST':
        form = CandyCreateForm(data=request.POST)
        if form.is_valid():
            candy = form.save()
            candy_image = CandyImage(image=request.POST['image'], candy=candy)
            candy_image.save()
            return redirect('candy-index')

    else:
        form = CandyCreateForm()
    return render(request, 'candy/create_candy.html', {
        'form': form
    })

def delete_candy(request, id):
    candy = get_object_or_404(Candy, pk=id)
    candy.delete()
    return redirect('candy-index')


def update_candy(request, id):
    instance = get_object_or_404(Candy, pk=id)
    if request.method == 'POST':
        form = CandyUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('candy_details', id=id)
    else:
        form = CandyUpdateForm(instance=instance)
    return render(request, 'candy/update_candy.html', {
        'form': form,
        'id': id
    })