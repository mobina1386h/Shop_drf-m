from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from product.views import BrandView,CategoryView,ProductView

router=DefaultRouter()
router.register("brand",BrandView)
router.register("category",CategoryView)
router.register("product",ProductView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]