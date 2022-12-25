from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Owner
from .models import Pet
from .models import Shelter
from .models import PetInShelter
from .forms import OwnerFormAdmin
from .forms import PetFormAdmin


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city']
    list_display_links = ['first_name', 'last_name']
    list_filter = ['city']
    search_fields = ['first_name', 'last_name', 'city']
    list_per_page = 5
    ordering = ['last_name']
    form = OwnerFormAdmin


class PetAdmin(admin.ModelAdmin):
    list_display = ['breed', 'nickname', 'age', 'sex', 'owner', 'get_photo']
    list_display_links = ['breed', 'nickname']
    list_editable = ['owner']
    list_filter = ['owner']
    search_fields = ['breed', 'nickname', 'sex']
    list_per_page = 5
    ordering = ['breed', 'nickname']
    form = PetFormAdmin

    @staticmethod
    def get_photo(obj):
        if obj.photo:
            return mark_safe(
                f'<img class="img-circle" src="{obj.photo.url}" '
                f' width="50" height="50">'
            )


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Shelter)
admin.site.register(PetInShelter)

