from django.urls import path

from .views import goal_category

urlpatterns = [
    path('goal_category/create', goal_category.GoalCategoryCreateView.as_view(), name='create_category'),
]