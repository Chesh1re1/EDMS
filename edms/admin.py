from django.contrib import admin

from .models import Doc, Dep, Contr


class DocAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'doc_reg_date', 'id_contr', 'id_executor')
    search_fields = ('id', 'title', 'doc_reg_date', 'id_contr', 'id_executor')
    list_filter = ('id_contr', 'id_executor')


class DepAdmin(admin.ModelAdmin):
    list_display = ('title', 'executor_surname', 'executor_name', 'executor_patronymic', 'telephone')
    search_fields = ('id', 'title')


class ContrAdmin(admin.ModelAdmin):
    list_display = ('title', 'contr_surname', 'contr_name', 'contr_patronymic', 'telephone', 'adress')
    search_fields = ('id', 'title')


admin.site.register(Doc, DocAdmin)
admin.site.register(Dep, DepAdmin)
admin.site.register(Contr, ContrAdmin)
