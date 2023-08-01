from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__', include('debug_toolbar.urls')),
]
