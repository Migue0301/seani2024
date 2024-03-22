from django.contrib import admin
from django.urls import include, path
from exam import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('exam/', include('exam.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]