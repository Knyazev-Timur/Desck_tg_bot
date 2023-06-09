from rest_framework import generics, permissions, filters

from goals.models import GoalCategory
from goals.serializers import GoalCategorySerializer


class GoalCategoryCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCategorySerializer


class GoalCategoryListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCategorySerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title', 'created'] # поля сортировки
    ordering = ['title']
    search_fields = ['title']

    def get_queryset(self):
        return GoalCategory.objects.select_related('user').filter(user=self.request.user).exclude(is_deleted=True)


