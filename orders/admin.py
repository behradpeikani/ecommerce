from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemAdmin(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ('product',)

class OrderAdmin(admin.ModelAdmin):
	list_filter = ('paid',)
	inlines = (OrderItemAdmin,)

admin.site.register(Order, OrderAdmin)