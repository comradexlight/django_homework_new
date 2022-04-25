from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
from .permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsAdminUser, ]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly(), IsAdminUser()]
        return []

    def get_queryset(self):
        """ Переопределяем queryset, чтобы показывать черновики только создателям"""
        not_draft_ads = []
        user = self.request.user
        advertisements = self.queryset
        for ads in advertisements:
            if ads.status in ('OPEN', 'CLOSED') or (ads.status == 'DRAFT' and ads.creator == user):
                not_draft_ads.append(ads.pk)
        return Advertisement.objects.filter(id__in=not_draft_ads)

    @action(detail=False, methods=['PATCH'], name='add_bookmark', url_path='add-bookmark',
            url_name='add-bookmark')
    def add_bookmark(self, request):
        user = request.user
        if user != Advertisement.objects.get(id=request.data['id']).creator:
            user.favourites.add(Advertisement.objects.get(id=request.data['id']))
            return Response("OK", status=status.HTTP_200_OK)
        else:
            raise ValueError('Вы не можете добавить своё объявление в избранное')

    @action(detail=False, methods=['GET'], name='bookmarks_list', url_path='bookmarks-list',
            url_name='bookmarks-list')
    def bookmarks_list(self, request):
        if request.user is int:
            queryset = Advertisement.objects.filter(favourites=request.user)
        else:
            raise ValueError('Вам нужно авторизоваться, чтобы посмотреть список избранных объявлений')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
