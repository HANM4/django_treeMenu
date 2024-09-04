from django.contrib import admin
from .models import TreeMenu, BranchMenu


class MenuBranchInline(admin.TabularInline):
    model = BranchMenu
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuBranchInline,]


admin.site.register(TreeMenu, MenuAdmin)
admin.site.register(BranchMenu)
