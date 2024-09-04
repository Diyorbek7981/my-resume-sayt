from django.contrib import admin
from .models import About, Education, Professional, Service, Advantage, Friend, Contact_me, Contact, Links

# Register your models here.


admin.site.register(About)
admin.site.register(Education)
admin.site.register(Professional)
admin.site.register(Service)
admin.site.register(Advantage)
admin.site.register(Friend)
admin.site.register(Contact_me)
admin.site.register(Links)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', "is_published")
    list_filter = ('created_at',)
    search_fields = ('name', 'phone')
