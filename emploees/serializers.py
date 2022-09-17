from rest_framework import serializers

from .models import Emploees


class EmploeesSerializer(serializers.ModelSerializer):
    """Вывод списка всех сотрудников"""
    id = serializers.IntegerField()
    person = serializers.CharField(max_length=30)
    function = serializers.CharField(max_length=30)

    def create(self, validated_data):
        """
        Создание нового пользователя

        :param validated_data: данные пришедшие с POST запроса
        :return: новый созданный объект
        """
        return Emploees.objects.create(**validated_data)

    def update(self, validated_data, instance=None):
        """
        Изменение существующего пользователя
        
        :param validated_data: данные пришедшие с PUT запроса
        :param instance: обект класса Emploees
        :return: измененный обект класса Emploees
        """""
        instance.id = validated_data.get('id', instance.id)
        instance.person = validated_data.get('person', instance.person)
        instance.function = validated_data.get('function', instance.function)
        instance.save()
        return instance

