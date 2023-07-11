from django.shortcuts import render, redirect

from petstagram.common.utils import get_user_liked_photo
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.forms import PhotoCreateForm
from petstagram.photos.models import Photo


def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST)
        if form.is_valid():
            photo = form.save()
            return redirect('details photo', pk=photo.pk)
    context = {
        'form': form,
    }
    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    photo = Photo.objects.filter(pk=pk).get
    context = {
        'photo': photo,
        'has_user_liked_photo': get_user_liked_photo(pk),
        'photos': photos,
    }
    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    return render(request, 'photos/photo-edit-page.html')


def delete_photo(request, pk):
    pass
