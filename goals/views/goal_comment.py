from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions

from goals.models import GoalComment
from goals.permissions import GoalCommentPermission
from goals.serializers import GoalCommentSerializer, GoalCommentWithUser


class GoalCommentCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCommentSerializer


class GoalCommentListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCommentWithUser
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['goal']
    ordering = ['-created']

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)

class GoalCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [GoalCommentPermission]
    serializer_class = GoalCommentWithUser

    def get_queryset(self):
        return GoalComment.objects.select_related('user').filter(
            goal__category__board__participants__user=self.request.user
        )
