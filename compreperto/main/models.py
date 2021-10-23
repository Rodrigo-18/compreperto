from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

class Usuario(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  TIPO_USUARIO_CHOICES = (
    ('Lojista', 'LJ'),
    ('Cliente', 'CL')
  )

  tipo_user = models.CharField(max_length=7, choices=TIPO_USUARIO_CHOICES, default='Cliente')
  

class Loja(models.Model):
  nome = models.CharField(max_length = 30)
  lojista = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  avaliacao = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
  TIPOS_STATUS = (
    ('Aberto', 'A'),
    ('Fechado', 'F'),
  )

  status = models.CharField(max_length=7, choices=TIPOS_STATUS, default='Aberto')

  def __str__(self):
    return self.nome

class Produto(models.Model):
  TIPOS_MEDIDA = (
    ('KG', 'kg'),
    ('G', 'g'),
    ('MG', 'mg'),
    ('L', 'L'),
    ('ML', 'ml'),
  )

  nome = models.CharField(max_length=30)
  marca = models.CharField(max_length=30)
  quantidade_unitaria = models.IntegerField()
  medida = models.FloatField(default=0.0)
  tipo_medida = models.CharField(max_length=2, choices=TIPOS_MEDIDA)
  valor = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
  quantidade = models.IntegerField(default=0)
  loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
  disponivel = models.BooleanField(default=True)
 
  def __str__(self):
    return self.nome + " " + self.marca + " " + str(self.medida) + self.tipo_medida

class Carrinho(models.Model):

  data = models.DateField(("data_criação"), auto_now=True, auto_now_add=False)
  
  loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
  
  def lista_produtos(self):
    return self.itemcarrinho_set.all()
  
  def quantidade_produtos(self):
    quantidade = 0
    for produto in self.lista_produtos():
      quantidade += produto.quantidade
    return quantidade

  def total(self) -> float:
    lista = self.lista_produtos()

    total = 0
    for item in lista:
      total += item.subtotal()
    
    return total


class ItemCarrinho(models.Model):
  carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  quantidade = models.IntegerField(default=1)

  def subtotal(self) -> float:
    return self.produto.valor * self.quantidade

  def __str__(self):
    return "Item: " + self.produto.nome

class Endereco(models.Model):
  latitude = models.FloatField(default=32.2)
  longitude = models.FloatField(default=32.3)
  nome_rua = models.CharField(max_length=60)
  numero_residencia = models.IntegerField()
  complemento = models.CharField(max_length=60)

  def __str__(self):
    return self.nome_rua 

class Pedido(models.Model):
  TIPOS_ENTREGA = (
    ('T', 'Take-away'),
    ('D', 'Delivery'),
  )

  TIPOS_PAGAMENTO = (
    ('D', 'Dinheiro'),
    ('C', 'Cartão'),
    ('P', 'Pix'),
  )

  STATUS = (
    ('E', 'Em aguardo'),
    ('A', 'Aceito'),
    ('C', 'Cancelado'),
  )

  carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
  data = models.DateField(default=timezone.now)
  tipo_entrega = models.CharField(max_length=1, choices=TIPOS_ENTREGA)
  tipo_pagamento = models.CharField(max_length=1, choices=TIPOS_PAGAMENTO)
  status = models.CharField(max_length=1, choices=STATUS, default='E')
  loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
  cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
  