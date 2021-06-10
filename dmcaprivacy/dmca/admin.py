from django.contrib import admin
from .models import Clients, GoogleReports, Nicks, NicksHasPages, Pages, TubeHasPages, TubePages, TubeReports

# Register your models here.

admin.site.register(GoogleReports)
admin.site.register(Nicks)
admin.site.register(NicksHasPages)
admin.site.register(Pages)
admin.site.register(TubeHasPages)
admin.site.register(TubePages)
admin.site.register(TubeReports)
admin.site.register(Clients)
