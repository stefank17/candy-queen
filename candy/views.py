from django.shortcuts import render, get_object_or_404, redirect
from candy.forms.candy_form import CandyCreateForm
from candy.models import Candy, CandyImage


# Create your views here.
def index(request):
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
        print(1)
    else:
        form = CandyUpdateForm(instance=instance)
        print(2)
    return render(request, 'candy/update_candy.html', {
        'form': form,
        'id': id
    })