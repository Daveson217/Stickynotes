from django.contrib import admin
from .models import Note
from django.contrib.auth.models import Group


# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'background_color', 'is_done', 'date_added')
    list_display_links = ('title', 'id')


admin.site.register(Note, NoteAdmin)
admin.site.unregister(Group)
