from django.db import models


class Doc(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=255)
    id_contr = models.IntegerField()
    reg_surname = models.CharField(max_length=255)
    reg_name = models.CharField(max_length=255)
    reg_patronymic = models.CharField(max_length=255)
    doc_reg_date = models.DateTimeField(auto_now_add=True)  # при auto_now_add дата и время в поле запишутся один раз и
                                                            # не будут изменяться
    doc_update_date = models.DateTimeField(auto_now=True)  # при auto_now дата и время в поле будут перезаписываться
                                                           # постоянно
    id_executor = models.IntegerField()
    comment = models.TextField(blank=True)


class Contr(models.Model):
    title = models.CharField(max_length=255)
    contr_name = models.CharField(max_length=255)
    contr_surname = models.CharField(max_length=255)
    contr_patronymic = models.CharField(max_length=255)
    telephone = models.IntegerField()
    adress = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255)


class Dep(models.Model):
    title = models.CharField(max_length=255)
    executor_name = models.CharField(max_length=255)
    executor_surname = models.CharField(max_length=255)
    executor_patronymic = models.CharField(max_length=255)
    telephone = models.IntegerField()

