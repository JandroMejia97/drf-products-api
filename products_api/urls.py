"""products_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from rest_framework_simplejwt.views import (
    token_verify,
    token_refresh,
    token_obtain_pair,
)

from apps.users.views import me_account
from apps.users.urls import router as user_router
from apps.products.urls import router as product_router

router = routers.DefaultRouter()
router.registry.extend(product_router.registry)
router.registry.extend(user_router.registry)

urlpatterns = [
    path(
        'api/',
        include((
                'rest_framework.urls',
                'drf'
            ),
            namespace='drf'
        )
    ),
    path(
        'api/',
        include((
                router.urls,
                'products_api'
            ),
            namespace='products_api'
        )
    ),
    path('api/me/', me_account, name='me'),
    path('api/token/', token_obtain_pair, name='token_obtain_pair'),
    path('api/token/verify/', token_verify, name='token_verify'),
    path('api/token/refresh/', token_refresh, name='token_refresh'),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)
