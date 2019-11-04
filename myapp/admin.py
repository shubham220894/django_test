from django.contrib import admin
from django.utils.safestring import mark_safe

from myapp.models import TestModel


# Register your models here.
@admin.register(TestModel)
class TestModel(admin.ModelAdmin):
    fields = ("name", "image",)
    list_display = ("id", "name", "image",)
    readonly_fields = ("id",)
    
    def image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
        )
        )
