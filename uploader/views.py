from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import ImageForm
from .models import Image


def image_upload_view(request):
    """Process images uploaded by users"""
    images = Image.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            form = ImageForm()
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj, 'images': images})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form, 'images': images})

def delete_view(request, id):
    image = Image.objects.get(pk=id)
    # storage = image.image.storage
    # image_path = image.image.path
    image.delete()
    # storage.delete(image_path)
    return HttpResponseRedirect(reverse('home'))
