from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links =('id','title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','address','description','city','state','zipcode','price')
    list_per_page = 20

admin.site.register(Listing, ListingAdmin)



