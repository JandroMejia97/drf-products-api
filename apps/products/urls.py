from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'variations', VariationViewSet)