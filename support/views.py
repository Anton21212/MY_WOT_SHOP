from drf_multiple_model.views import FlatMultipleModelAPIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from support.models import Tiket, TiketMessage
from support.serializers import TiketSerializers, TiketMessageSerializers, \
    TiketListSerializers, TiketListMessangeSerializers, AnswerTiketSerializers

from rest_framework.permissions import IsAuthenticated


class TiketCreateView(generics.CreateAPIView):
    """
    Отправка первого тикета пользователем
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = TiketSerializers


class TiketMessageView(generics.CreateAPIView):
    """
    Отправка второго подтикета пользователем
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = TiketMessageSerializers


class TikitsAllListView(FlatMultipleModelAPIView):
    """
    Отображение всех тикетов , всех пользователей(для саппорта)
    """
    permission_classes = (IsAdminUser,)
    querylist = [
        {'queryset': Tiket.objects.all(), 'serializer_class': TiketListSerializers},
        {'queryset': TiketMessage.objects.all(), 'serializer_class': TiketListMessangeSerializers}
    ]


class AnswerTiket(generics.CreateAPIView):
    """
    Ответ саппорта
    """
    permission_classes = (IsAdminUser,)
    serializer_class = AnswerTiketSerializers
