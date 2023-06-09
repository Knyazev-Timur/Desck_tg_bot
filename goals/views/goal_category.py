from rest_framework import generics, permissions

from goals.serializers import GoalCategorySerializer


class GoalCategoryCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCategorySerializer