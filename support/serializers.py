from rest_framework import serializers

from support.models import Tiket, TiketMessage, Answer


#Отправка первого тикета пользователем
class TiketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tiket
        fields = '__all__'

#Отправка второго подтикета пользователем
class TiketMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = TiketMessage
        fields = '__all__'



#Вывод основного тикета
class TiketListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tiket
        fields = '__all__'



#Вывод подтикета
class TiketListMessangeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TiketMessage
        fields = '__all__'


class AnswerTiketSerializers(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    class Meta:
        model = Answer
        fields = '__all__'

