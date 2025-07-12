from django.contrib import admin
from .models import Collage, ImageItem


class ImageItemInline(admin.TabularInline):
    model = ImageItem
    extra = 1
    fields = ('image', 'caption', 'order', 'x_position', 'y_position', 'width', 'height')
    readonly_fields = ('image',)


@admin.register(Collage)
class CollageAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'template_id', 'frame_style', 'image_count', 'created_at')
    list_filter = ('template_id', 'frame_style', 'created_at', 'user')
    search_fields = ('title', 'user__username')
    readonly_fields = ('created_at',)
    inlines = [ImageItemInline]
    
    def save_model(self, request, obj, form, change):
        if not change:  
            obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(ImageItem)
class ImageItemAdmin(admin.ModelAdmin):
    list_display = ('collage', 'order', 'caption', 'x_position', 'y_position')
    list_filter = ('collage__user', 'collage__template_id')
    search_fields = ('collage__title', 'caption')
    list_editable = ('order', 'x_position', 'y_position')
