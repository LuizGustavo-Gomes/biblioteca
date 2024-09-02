from django.contrib import admin
from .models import Usuario, Bibliotecario, Livro, Emprestimo, Reserva

admin.site.register(Usuario)
admin.site.register(Bibliotecario)
admin.site.register(Livro)
admin.site.register(Emprestimo)
admin.site.register(Reserva)