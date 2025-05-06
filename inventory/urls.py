from django.urls import path
from inventory.views import ProductCreateAndListView, ProductView, ProductAttributeCreateAndListView, ProductAttributeView, UnitListCreateView, BrandListAndCreateView

urlpatterns = [
    path('products/', ProductCreateAndListView.as_view()),
    path('products/<int:pk>/', ProductView.as_view()),
    path('attributes/', ProductAttributeCreateAndListView.as_view()),
    path('attributes/<int:pk>/', ProductAttributeView.as_view()),
    path('brands/', BrandListAndCreateView.as_view()),
    path('units/', UnitListCreateView.as_view()),
]