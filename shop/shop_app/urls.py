from django.urls import path
from .views import MainPageView,ProductListView

urlpatterns = [
    path("", view = MainPageView.as_view(), name = "main_page"),
    path("products/",view=ProductListView.as_view() )
]