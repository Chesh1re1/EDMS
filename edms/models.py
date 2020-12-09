from django.db import models


class Doc(models.Model):
    number = models.IntegerField(verbose_name='Номер')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    id_contr = models.IntegerField(verbose_name='Контрагент')
    reg_surname = models.CharField(max_length=255, verbose_name='Фамилия регистроторав')
    reg_name = models.CharField(max_length=255, verbose_name='Имя регистратора')
    reg_patronymic = models.CharField(max_length=255, verbose_name='Отчество регистратора')
    doc_reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    # при auto_now_add дата и время в поле запишутся один раз и не будут изменяться
    doc_update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    # при auto_now дата и время в поле будут перезаписываться постоянно
    id_executor = models.IntegerField(verbose_name='Исполнитель')
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Contr(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    contr_name = models.CharField(max_length=255, verbose_name='Имя контрагента')
    contr_surname = models.CharField(max_length=255, verbose_name='Фамилия контрагента')
    contr_patronymic = models.CharField(max_length=255, verbose_name='Отчество контрагента')
    telephone = models.IntegerField(verbose_name='Телефон')
    adress = models.CharField(max_length=255, verbose_name='Адресс')
    apartment = models.CharField(max_length=255, verbose_name='Офис')

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class Dep(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    executor_name = models.CharField(max_length=255, verbose_name='Имя исполнителя')
    executor_surname = models.CharField(max_length=255, verbose_name='Фамилия исполнителя')
    executor_patronymic = models.CharField(max_length=255, verbose_name='Отчество исполнителя')
    telephone = models.IntegerField(verbose_name='Телефон')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

