from django.contrib import admin
from django.utils.safestring import mark_safe

from agency.models import *


@admin.register(InCityObjectType)
class InCityObjectTypeAdmin(admin.ModelAdmin):
    list_display = ('id','gethtmlPhoto', 'title','slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.icon:
            return mark_safe(f"<img src='{picture.icon.url}' width=50>")

    gethtmlPhoto.short_description = 'миниатюра'


# class InCityRegionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     prepopulated_fields = {'slug': ('title',)}
#     save_on_top = True


# class MetroStationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     prepopulated_fields = {'slug': ('title',)}
#     save_on_top = True

@admin.register(RoomAmount)
class RoomAmountAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_amount', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True


# class BathroomTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# class ElevatorTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# class FlatStateAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# class ObjectConstructionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True

# @admin.register(Balcony)
# class BalconyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
class GalleryAdmin(admin.TabularInline):
    model = Gallery
    fields = ('gallery_image', 'gethtmlPhoto', 'note', 'is_published')
    readonly_fields = ('gethtmlPhoto',)

    def gethtmlPhoto(self, picture):
        if picture.gallery_image:
            return mark_safe(f"<img src='{picture.gallery_image.url}' width=75>")

    gethtmlPhoto.short_description = 'миниатюра'


class InCityObjectAdmin(admin.ModelAdmin):
    inlines = [GalleryAdmin]
    list_display = ('sale_or_rent', 'title', 'rooms', 'gethtmlPhoto', 'city_region', 'price', 'object_type', 'is_published')
    list_display_links = ('sale_or_rent', 'title')
    search_fields = ('title', 'rooms', 'city_region',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=50>")

    gethtmlPhoto.short_description = 'миниатюра'


class GalleryAdmin2(admin.TabularInline):
    model = Gallery2
    fields = ('gallery_image2', 'gethtmlPhoto', 'note2', 'is_published')
    readonly_fields = ('gethtmlPhoto',)

    def gethtmlPhoto(self, picture):
        if picture.gallery_image2:
            return mark_safe(f"<img src='{picture.gallery_image2.url}' width=75>")

    gethtmlPhoto.short_description = 'миниатюра'


class OutCityObjectAdmin(admin.ModelAdmin):
    inlines = [GalleryAdmin2]
    list_display = (
        'id', 'title', 'gethtmlPhoto', 'object_adress', 'land_square', 'price', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'land_square',)
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_published', 'time_create')
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=50>")

    gethtmlPhoto.short_description = 'миниатюра'


@admin.register(OutCityObjectType)
class OutCityObjectTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'gethtmlPhoto', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.icon:
            return mark_safe(f"<img src='{picture.icon.url}' width=50>")

    gethtmlPhoto.short_description = 'миниатюра'


#

# @admin.register(TypeOfOwnership)
# class TypeOfOwnershipAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(Electricity)
# class ElectricityAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(Water)
# class WaterAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(Gas)
# class GasAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(Bath)
# class BathAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(Landings)
# class LandingsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(Garage)
# class GarageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(Greenhouse)
# class GreenhouseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(Security)
# class SecurityAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(GoodRoad)
# class GoodRoadAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(WinterAccess)
# class WinterAccessAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(ShopNearly)
# class ShopNearlyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(WaterNearly)
# class WaterNearlyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# @admin.register(ForestNearly)
# class ForestNearlyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


@admin.register(Graphics)
class GraphicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'gethtmlPhoto', 'description', 'note', 'is_published')
    list_display_links = ('id', 'description')
    search_fields = ('description', 'note')
    list_editable = ('is_published',)
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=50>")

    gethtmlPhoto.short_description = 'миниатюра'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    save_on_top = True


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'gethtmlPhoto', 'description', 'extra_description', 'is_published')
    list_display_links = ('id', 'description')
    search_fields = ('description',)
    list_editable = ('is_published',)
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=50>")

    gethtmlPhoto.short_description = 'миниатюра'


admin.site.register(InCityObject, InCityObjectAdmin)
admin.site.register(OutCityObject, OutCityObjectAdmin)
# admin.site.register(MetroStation, MetroStationAdmin)
# admin.site.register(RoomAmount, RoomAmountAdmin)
# admin.site.register(BathroomType, BathroomTypeAdmin)
# admin.site.register(ElevatorType, ElevatorTypeAdmin)
# admin.site.register(FlatState, FlatStateAdmin)
# admin.site.register(ObjectConstruction, ObjectConstructionAdmin)


admin.site.site_header = 'ЕЦН'
