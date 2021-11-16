
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='indexpage'),
    path('about/',views.about,name='aboutpage'),
    path('contact/',views.contact,name='contactpage'),
    path('client/',views.clients,name='clientpage'),
    path('services/',views.service,name='service'),
    path('banner/',views.banner,name='banner'),
    path('plans/',views.plan,name='plan'),
    path('model/',views.model,name='model'),
    path('logabout/',views.logabout,name='logaboutpage'),

]
