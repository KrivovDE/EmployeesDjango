from django.db import models


class Person(models.Model):
    """
    Person создаст таблицу базы данных следующим образом:

    CREATE TABLE 'Работники' (
    "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
     );

    Поле id добавляется автоматически и по сути своей является суррогатным ключем,
    но это поведение можно переопределить.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.surname} - {self.first_name}'

    class Meta:
        db_table = 'Работники'
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Function(models.Model):
    """
    Создаст таблицу 'Должности'
    """
    function = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.function}'

    class Meta:
        db_table = 'Должности'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Emploees(models.Model):
    """
     Создаст таблицу 'Сотрудники', через отношение 'многие к одному' с таблицами 'Работники' и 'Должности'
     Переопределено стандартное поведение моделей django,
     добавлено поле id - primary_key.
    """
    id = models.IntegerField(primary_key=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    # Отношение OneToOneField рекомендовано к использованию для уникальных полей,
    # вместо сочетания ForeignKey - unique=True

    function = models.ForeignKey(Function, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.person} - {self.function}'

    class Meta:
        db_table = 'Сотрудники'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'





