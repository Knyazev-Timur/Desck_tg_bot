from django.urls import path

# from .views import goal_category
from .views.goal_category import GoalCategoryListView, GoalCategoryCreateView

urlpatterns = [
    path('goal_category/create', GoalCategoryCreateView.as_view(), name='create_category'),
    path('goal_category/list', GoalCategoryListView.as_view(), name='category_list'),
]