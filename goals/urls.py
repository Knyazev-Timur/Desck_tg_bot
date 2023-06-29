from django.urls import path

# from .views import goal_category
from .views.goal_category import GoalCategoryListView, GoalCategoryCreateView, GoalCategoryDetailView
from goals.views.goals import GoalListView, GoalCreateView, GoaDetailView
from goals.views.goal_comment import GoalCommentListView, GoalCommentCreateView, GoalCommentDetailView
from goals.views.board import BoardDetailView, BoardListView, BoardCreateViews



urlpatterns = [
    path('board/create', BoardCreateViews.as_view(), name='create_board'),
    path('board/list', BoardListView.as_view(), name='board_list'),
    path('board/<int:pk>', BoardDetailView.as_view(), name='board_detail'),


    path('goal_category/create', GoalCategoryCreateView.as_view(), name='create_category'),
    path('goal_category/list', GoalCategoryListView.as_view(), name='category_list'),
    path('goal_category/<int:pk>', GoalCategoryDetailView.as_view(), name='category_detail'),

    path('goal/create', GoalCreateView.as_view(), name='create_goal'),
    path('goal/list', GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>', GoaDetailView.as_view(), name='goal_detail'),

    path('goal_comment/create', GoalCommentCreateView.as_view(), name='create_comment'),
    path('goal_comment/list', GoalCommentListView.as_view(), name='comment_list'),
    path('goal_comment/<int:pk>', GoalCommentDetailView.as_view(), name='comment_detail'),
]
