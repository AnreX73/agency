from django.contrib import admin
from django.utils.safestring import mark_safe

from agency.models import *


# class InCityObjectTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     prepopulated_fields = {'slug': ('title',)}
#     save_on_top = True
#
#
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

# @admin.register(RoomAmount)
# class RoomAmountAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# class BathroomTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True

#
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

@admin.register(InCityObject)
class InCityObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rooms', 'gethtmlPhoto', 'city_region', 'price', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'rooms', 'city_region',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=50>")

    gethtmlPhoto.short_description = 'миниатюра'


@admin.register(OutCityObject)
class OutCityObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'object_type', 'object_adress', 'land_square', 'price', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'land_square',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    save_on_top = True


# @admin.register(OutCityObjectType)
# class OutCityObjectTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     prepopulated_fields = {'slug': ('title',)}
#     save_on_top = True
#
#
# @admin.register(TypeOfOwnership)
# class TypeOfOwnershipAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(Electricity)
# class ElectricityAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(Water)
# class WaterAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(Gas)
# class GasAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(Bath)
# class BathAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(Landings)
# class LandingsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(Garage)
# class GarageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(Greenhouse)
# class GreenhouseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(Security)
# class SecurityAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(GoodRoad)
# class GoodRoadAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(WinterAccess)
# class WinterAccessAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(ShopNearly)
# class ShopNearlyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(WaterNearly)
# class WaterNearlyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True
#
#
# @admin.register(ForestNearly)
# class ForestNearlyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     save_on_top = True


# admin.site.register(InCityObjectType, InCityObjectTypeAdmin)
# admin.site.register(InCityRegion, InCityRegionAdmin)
# admin.site.register(MetroStation, MetroStationAdmin)
# admin.site.register(RoomAmount, RoomAmountAdmin)
# admin.site.register(BathroomType, BathroomTypeAdmin)
# admin.site.register(ElevatorType, ElevatorTypeAdmin)
# admin.site.register(FlatState, FlatStateAdmin)
# admin.site.register(ObjectConstruction, ObjectConstructionAdmin)


admin.site.site_header = 'GRANT GARANT'
