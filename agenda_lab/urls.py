from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path ('eventos/<str:titulo_evento>/', views.local_evento, name='local_evento'),
    path('agenda/', views.lista_eventos, name='lista_eventos'),
    path('', RedirectView.as_view(url='/agenda/')),
]
