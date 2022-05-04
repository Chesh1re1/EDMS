from django.db import models
from django.urls import reverse


class Doc(models.Model):
    number = models.IntegerField(verbose_name='Номер')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    id_contr = models.ForeignKey('Contr', on_delete=models.PROTECT, verbose_name='Контрагент', default=1)
    reg_surname = models.CharField(max_length=255, verbose_name='Фамилия регистратора')
    reg_name = models.CharField(max_length=255, verbose_name='Имя регистратора')
    reg_patronymic = models.CharField(max_length=255, verbose_name='Отчество регистратора')
    doc_reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    # при auto_now_add дата и время в поле запишутся один раз и не будут изменяться
    doc_update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    # при auto_now дата и время в поле будут перезаписываться постоянно
    id_executor = models.ForeignKey('Dep', on_delete=models.PROTECT, verbose_name='Исполнитель', default=1)
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    def get_absolute_url(self):
        return reverse('doc', kwargs={'doc_id': self.pk})

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Contr(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    contr_name = models.CharField(max_length=255, verbose_name='Имя контрагента')
    contr_surname = models.CharField(max_length=255, verbose_name='Фамилия контрагента')
    contr_patronymic = models.CharField(max_length=255, verbose_name='Отчество контрагента')
    telephone = models.BigIntegerField(verbose_name='Телефон')
    adress = models.CharField(max_length=255, verbose_name='Адресс')
    apartment = models.CharField(max_length=255, verbose_name='Офис')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class Dep(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    executor_name = models.CharField(max_length=255, verbose_name='Имя исполнителя')
    executor_surname = models.CharField(max_length=255, verbose_name='Фамилия исполнителя')
    executor_patronymic = models.CharField(max_length=255, verbose_name='Отчество исполнителя')
    telephone = models.BigIntegerField(verbose_name='Телефон')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

