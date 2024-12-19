from django.contrib import admin
from .models import Brand,Category,Product,ProductLine

class ProductLineInLines(admin.TabularInline):
    model=ProductLine
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductLineInLines]
    
admin.site.register(Brand)
admin.site.register(Category)
#admin.site.register(Product)
admin.site.register(ProductLine)