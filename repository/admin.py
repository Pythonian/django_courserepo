from django.contrib import admin

from .models import Level, Library, Course, Material, ResourceType


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('year',)}


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass


@admin.register(ResourceType)
class ResourceTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'code', 'level']
    list_filter = ['level']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'course']
    list_filter = ['course__level']
    prepopulated_fields = {'slug': ('name',)}
