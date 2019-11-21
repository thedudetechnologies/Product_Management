from django.contrib import admin
from .models import User
from man_prod.models import Category, Product

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
