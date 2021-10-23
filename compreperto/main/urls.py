from django.urls import path
from main import views

urlpatterns = [
    path('',views.PesquisaView.as_view(), name='pesquisa'),
    path('produto/<int:id_produto>/detalhes/', views.DetalhesView.as_view(), name='detalhes'),
    path('loja/<int:id_loja>', views.DetalhesLoja.as_view(), name='detalhesLoja'),
    path('carrinho/', views.CarrinhoView.as_view(), name= 'carrinho'),
    path('resultados/', views.ResultadosView.as_view(), name = 'resultados'),
    path('carrinho/<int:id_produto>/add', views.AdicionarItem.as_view(), name = 'adicionar'),

    path('pedidos/confirmar', views.ConfirmarPedido.as_view(), name = 'confirmar'),
    path('pedidos/', views.ListarPedidos.as_view(), name = 'pedidos'),
    path('loja/pedidos', views.ListarPedidosLojista.as_view(), name='pedidosLojista'),
    path('loja/pedidos/<int:id_pedido>', views.DetalhesPedidoLojista.as_view(), name='detalhesPedidoLojista'),
    path('loja/pedidos/confirmar/<int:id_pedido>', views.ConfirmarPedidoLojista.as_view(), name='confirmarPedidoLojista'),
    path('loja/pedidos/rejeitar/<int:id_pedido>', views.RejeitarPedidoLojista.as_view(), name='rejeitarPedidoLojista'),
    # AUTENTICAÇÃO
    path('registro', views.RegistroView.as_view(), name='registro'),
    path('login',views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(),name='logout'),
    path('produtos/', views.GerenciarEstoque.as_view(), name = 'produtos'),
    path('produtos/indisponiveis/', views.DeletarProdutos.as_view(), name = 'deletar'),

]
