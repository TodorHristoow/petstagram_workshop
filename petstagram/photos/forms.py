from django import forms
from django.core.exceptions import ValidationError

from petstagram.common.models import PhotoLike, PhotoComment
from petstagram.core.form_mixins import DisabledFormMixin
from petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date',)


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('photo',)


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()  # many to many
            PhotoLike.objects.filter(photo_id=self.instance.id).delete()  # one to many
            PhotoComment.objects.filter(photo_id=self.instance.id).delete()
            self.instance.delete()
        return self.instance
