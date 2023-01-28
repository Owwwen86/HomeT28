from django.urls import path

from ads.views.cat import CategoryUpdateView, CategoryDeleteView, CategoryListView, CategoryDetailView, \
    CategoryCreateView

urlpatterns = [
    path('', CategoryListView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    path('<int:pk>/', CategoryDetailView.as_view()),
    path('<int:pk>/update/', CategoryUpdateView.as_view()),
    path('<int:pk>/delete/', CategoryDeleteView.as_view()),
]
