from django.urls import path
from rest_framework import routers

from support.views import *

app_name = 'support'

urlpatterns = [
    path('support/create/', TiketCreateView.as_view(), name='create'),
    path('supportmessange/create/', TiketMessageView.as_view(), name='additional_ticket'),
    path('all_tiket/', TikitsAllListView.as_view(), name="all_ticket"),
    path('answer/', AnswerTiket.as_view(), name='answer'),
]
