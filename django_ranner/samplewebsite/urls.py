
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Admin Alfeed"
admin.site.site_title = "Alfeed Admin Portal"
admin.site.index_title = "Welcome to Alfeed Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)