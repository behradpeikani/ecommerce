from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product, ProductImage


class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = (ProductImageInline, )
 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)