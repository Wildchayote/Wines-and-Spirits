from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    #readonly_fields = ['name', 'category']
    #raw_id_fields = ['user']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    #readonly_fields = ['category']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)


# username = Tanushree, email = tanushree7252@gmail.com, password = 1234
