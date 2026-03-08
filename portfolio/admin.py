from django.contrib import admin

from .models import Author, CaseStudy, Category, Item, Message, Service, Skill, Testimony, Work


class ItemInline(admin.TabularInline):
    model = Item


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "display_order")
    list_filter = ("category", "is_featured")
    search_fields = ("title", "summary", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "featured", "updated_at")
    list_filter = ("featured",)
    search_fields = ("title", "problem", "solution")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("rusname", "engname")
    search_fields = ("rusname", "engname")


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ("name", "lastname")
    search_fields = ("name", "lastname", "text")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ("name", "description")
    search_fields = ("name", "description")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "lastname", "title", "location")
    search_fields = ("name", "lastname", "title", "location")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "service")
    search_fields = ("name",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject")
    search_fields = ("name", "email", "subject")