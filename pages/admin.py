from django.contrib import admin
from .models import *

admin.site.register(SeoOptimization)
admin.site.register(TopBar)
admin.site.register(MainBanner)
admin.site.register(SectionBanner)
admin.site.register(ComponentDump)
admin.site.register(Testimonial)
admin.site.register(GetStarted)

@admin.register(NavLink)
class NavLinkAdmin(admin.ModelAdmin):
    '''Admin View for NavLink'''

    list_display = ['links']

    @admin.display(description='Link Name')
    def links(self, obj):
        return (f'{obj.title}').upper()

    
@admin.register(NavLinkItem)
class NavLinkItemAdmin(admin.ModelAdmin):
    '''Admin View for NavLinkItem'''

    list_display = ['links','title','url_link']
    list_editable = ['url_link']

    @admin.display(description='Link Name')
    def links(self, obj):
        return (f'{obj.navlink.title}').upper()
    
