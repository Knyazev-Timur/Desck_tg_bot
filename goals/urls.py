from django.urls import path

# from .views import goal_category
from .views.goal_category import GoalCategoryListView, GoalCategoryCreateView, GoalCategoryDetailView
from goals.views.goals import GoalListView, GoalCreateView, GoaDetailView


urlpatterns = [
    path('goal_category/create', GoalCategoryCreateView.as_view(), name='create_category'),
    path('goal_category/list', GoalCategoryListView.as_view(), name='category_list'),
    path('goal_category/<int:pk>', GoalCategoryDetailView.as_view(), name='category_detail'),

    path('goal/create', GoalCreateView.as_view(), name='create_goal'),
    path('goal/list', GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>', GoaDetailView.as_view(), name='goal_detail'),
]