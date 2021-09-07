from django.contrib import admin
from .models import Clients, GoogleReports, Nicks, Pages, TubeHasPages, TubePages, TubeReports, Plans, NicksPages

# Register your models here.


class NickPageInline(admin.TabularInline):
    model = NicksPages
    extra = 1


class NickPage(admin.ModelAdmin):
    inlines = [NickPageInline, ]
    list_display = (
        'clients_id_clie', 'nick', 'prio',
    )
    search_fields = ('clients_id_clie',)
    filter_horizontal = ['pages', ]


admin.site.register(GoogleReports)
admin.site.register(Nicks, NickPage)
admin.site.register(Pages)
admin.site.register(TubeHasPages)
admin.site.register(TubePages)
admin.site.register(TubeReports)
admin.site.register(Clients)
admin.site.register(Plans)
