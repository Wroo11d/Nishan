from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from account.controllers import account_controller
from commerce.controllers import commerce_controller

api = NinjaAPI()
api.add_router('auth', account_controller)
api.add_router('', commerce_controller['notifications'])
api.add_router('', commerce_controller['Service'])
api.add_router('', commerce_controller['Center'])
api.add_router('', commerce_controller['Advertising'])
api.add_router('', commerce_controller['News'])
api.add_router('', commerce_controller['Service_opinions'])
api.add_router('', commerce_controller['Center_opinions'])
api.add_router('', commerce_controller['Reservation'])
api.add_router('', commerce_controller['Service_images'])
api.add_router('', commerce_controller['Center_images'])


urlpatterns = [
    path('api/', api.urls),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
