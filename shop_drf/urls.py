from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from product.views import BrandView,CategoryView,ProductView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router=DefaultRouter()
router.register("brand",BrandView)
router.register("category",CategoryView)
router.register("product",ProductView,basename="product")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/doc/', SpectacularSwaggerView.as_view(url_name='schema')),
]