from django.urls import path
from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # landing page
    path('',views.landing, name='landing'),

    # category views
    path('catalogo', views.categories_list, name='categories_list'),
    path('catalogo/<int:pk>', views.category_detail, name='categories_detail'),

    # product views
    path('products/<int:pk>', views.product_detail, name='product_detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)