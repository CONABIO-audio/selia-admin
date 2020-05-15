from django.contrib import admin


class TermAdmin(admin.ModelAdmin):
    search_fields = ['term_type__name', 'value']
    autocomplete_fields = ['term_type']


class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
