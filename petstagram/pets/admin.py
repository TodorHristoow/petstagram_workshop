from django.contrib import admin
from petstagram.pets.models import Pet


# method 1
# admin.register(Pet)
# class PetAdmin(admin.ModelAdmin):
#   pass
# with str method defined in the forms to show string representation
# shows outside created object and objects inside a form pretty ugly


# 2nd method I think is more beautiful
# shows outside created object very pretty
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")



