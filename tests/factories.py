import factory
from product.models import Brand,Category,Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Category
    name=factory.sequence(lambda x:f"category_{x}")

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Brand
    name=factory.sequence(lambda x:f"brand_{x}")

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Product
    name=factory.sequence(lambda x:f"procduct_{x}")
    description=factory.sequence(lambda x:f"description_{x}")
    is_digital=False
    brand=factory.SubFactory(BrandFactory)
    category=factory.SubFactory(CategoryFactory)