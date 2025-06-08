
# from django.contrib import admin
# from django.urls import path , include
# from django.views.generic import RedirectView
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('app.urls')),
# ]
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='counter', permanent=False)),  
    path('', include('app.urls')), 

    
]