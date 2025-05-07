from django.urls import path
from inventory.views import ProductCreateAndListView, ProductView, ProductAttributeCreateAndListView, ProductAttributeView, UnitListCreateView, BrandListAndCreateView, AttributeListAndCreateView, AttributeValueListAndCreateView, CategoryListAndCreateView, BrandView, UnitView, CategoryView, AttributeView, AttributeValueView

urlpatterns = [
    path('products/', ProductCreateAndListView.as_view()),
    path('products/<int:pk>/', ProductView.as_view()),
    path('product-attributes/', ProductAttributeCreateAndListView.as_view()),
    path('product-attributes/<int:pk>/', ProductAttributeView.as_view()),
    path('brands/', BrandListAndCreateView.as_view()),
    path('brands/<int:pk>/', BrandView.as_view()),
    path('units/', UnitListCreateView.as_view()),
    path('units/<int:pk>/', UnitView.as_view()),
    path('attributes/', AttributeListAndCreateView.as_view()),
    path('attributes/<int:pk>/', AttributeView.as_view()),
    path('attribute-values/', AttributeValueListAndCreateView.as_view()),
    path('attribute-values/<int:pk>/', AttributeValueView.as_view()),
    path('categories/', CategoryListAndCreateView.as_view()),
    path('categories/<int:pk>/', CategoryView),
]