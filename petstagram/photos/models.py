from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from petstagram.core.model_mixin import StrFromFieldsMixin
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_less_than_5mb

UserModel = get_user_model()


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'location')
    MIN_DESCRIPTION_LEN = 10
    MAX_DESCRIPTION_LEN = 300

    MAX_LOCATION_LEN = 30

    photo = models.ImageField(
        upload_to='pet_photos',
        null=False,
        blank=True,
        validators=(
            validate_file_less_than_5mb,
        ),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LEN,
        validators=(
            validators.MinLengthValidator(MIN_DESCRIPTION_LEN),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LEN,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        # Automatically sets date on save (create or update)
        auto_now=True,
        null=False,
        blank=True,
    )

    # One-to-one relations
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    # Many-to-many relationship
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
