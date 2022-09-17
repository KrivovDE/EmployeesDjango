from rest_framework import generics
from rest_framework.response import Response

from .models import Emploees
from .serializers import EmploeesSerializer


class EmploeesAPIView(generics.ListAPIView):
    """
    Базовый класс для представлений
    отвечает за CRUD операции
    """

    def get(self, request):
        """
        Возвращает объекты Emploees
        """
        lst = Emploees.objects.all()
        return Response({'post': EmploeesSerializer(lst, many=True).data})

    def post(self, request):
        """
        Валидирует полученные данные, проверяет наличие аналогичных записей в БД

        :return: Вновь созданный объект Emploees
        """
        serializer = EmploeesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # тут нужно проверить есть ли такой пользователь в базе
        lst = Emploees.objects.all()
        if serializer not in EmploeesSerializer(lst, many=True).data:
            serializer.save()
            return Response({'post': serializer.data})
        else:
            return Response({'error': 'Такой пользователь уже существует'})

    def put(self, request, *args, **kwargs):
        """
        При наличии соответствующего pk, изменяет запись в БД

        :return: Измененный объект Emploees
        """
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Невозможно изменить пользователя'})
        try:
            instance = Emploees.objects.get(pk=pk)
        except:
            return Response({'error': 'Пользователь не найден'})

        serializer = EmploeesSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        """
        При наличии соответствующего pk, удаляет запись в БД

        :return: Response - об удалении записи из БД
        """
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'Метод не определен'})
        else:
            instance = Emploees.objects.get(pk=pk)
            instance.delete()
            return Response({'post': 'Пользователь удален' + str(pk)})
