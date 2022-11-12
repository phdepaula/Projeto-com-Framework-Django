from django.contrib import admin

from .models import Produto, Cliente


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class CLienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, CLienteAdmin)
