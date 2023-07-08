from petstagram.common.models import PhotoLike
import pyperclip


def get_user_liked_photo(photo_id):
    # TODO: fix when auth
    return PhotoLike.objects.filter(photo_id=photo_id)


def get_photo_url(request, photo_id):
    # http://127.0.0.1:8000/#photo-1
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
