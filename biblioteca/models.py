from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField
    email = models.EmailField(unique=True)
    estado = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Bibliotecario(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField
    email = models.EmailField(unique=True)
    estado = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    ano_publicacao = models.CharField(max_length=4)
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo
    
class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.livro.titulo} emprestado para {self.usuario.nome}'
    
class Reserva(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_reserva = models.DateField(auto_now_add=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return f'Reserva de {self.livro.titulo} para {self.usuario.nome}'











    





