from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from django.views import generic
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import BarraPesquisa, NovoUsuarioForm
from .models import ItemCarrinho, Produto, Carrinho, Loja, Endereco, Pedido, Usuario
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

'''
View que gerencia o sistema de busca dá página inicial
'''
class PesquisaView(generic.View):
    # Tratamento da requisição HTTP GET
    def get(self, request):
        # Instancia o formulário de pesquisa e renderiza o mesmo
        form = BarraPesquisa()
        return render(request, 'main/pesquisa.html', {'form':form})

    # Tratamento da requisição HTTP POST
    def post(self, request):
        # Recupera os dados enviados via POST
        form = BarraPesquisa(request.POST)
        campo = None
        if form.is_valid():
            # Recupera o termo digitado pelo usuário
            campo = form.cleaned_data['name']
        produtos = None
        if campo:
            # Busca produtos que tenham o termo no nome ou na marca
            produtos = Produto.objects.filter(
                Q(nome__icontains = campo) | Q(marca__icontains = campo)
            )
        else:
            # Se não tiver um termo, busca todos os produtos
            produtos = Produto.objects.all()
        return render(request, 'main/resultados.html', {'lista': produtos,})

'''
View de detalhes do produto, se encontra em desuso atualmente,
mas, pode ser interessante futuramente
'''
class DetalhesView(generic.View):
    def get(self, request, *args, **kwargs):
        id_produto = kwargs['id_produto']
        # Recupera o produto com o respectivo id
        produto = get_object_or_404(Produto, pk = id_produto)
        # Apresenta os detalhes do produto no template específico
        return render(request, 'main/detalhes.html', {'produto': produto})

'''
View de cadastro
'''      
class RegistroView(generic.View):
    def get(self,request, *args, **kwargs):
        return render(request, 'registration/registro.html', {'registro_form': NovoUsuarioForm()})

    def post(self,request, *args, **kwargs):
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request,usuario.user)
            messages.success(request, 'Cadastrado com sucesso')
            
            if usuario.tipo_user == 'LJ':
                loja = Loja.objects.get(lojista = usuario)
                return redirect ('pedidosLojista')
            return redirect('pesquisa')
        messages.error(request, "Informação inválida")
        return render(request, 'registration/registro.html', {'registro_form': NovoUsuarioForm()})

'''
View de login
'''

class LoginView(generic.View):
    def get(self, request):
        form = AuthenticationForm()

        return render(request, 'registration/login.html', {'login_form': form})
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data.get('username'),
                                password = form.cleaned_data.get('password'))
            
            if user:
                
                login(request, user)
                usuario = Usuario.objects.get(user = user)
                if usuario.tipo_user == "Lojista":
                    loja = Loja.objects.get(lojista = usuario)
                    return redirect('loja/{0}/pedidos'.format(loja.id))

                return redirect(self.request.GET.get('next'))
            else:
                messages.error(request,"Email ou Senha incorretos")
        else: messages.error(request,"Email ou Senha incorretos")

        form = AuthenticationForm()

        return render(request, 'registration/login.html', {'login_form': form})

'''
View de Logout
'''
class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        messages.info(request, "Você saiu com sucesso") 
        return redirect("pesquisa")

'''
View que gerencia a adição de um item ao carrinho
'''
class AdicionarItem(generic.View):
    def get(self, request, *args, **kwargs):
        id_produto = kwargs['id_produto']
        # Recupera o produto com o respectivo id
        produto = get_object_or_404(Produto, pk = id_produto)
        # Apresenta os detalhes do produto no template específico
        # Recuperação do carrinho
        carrinho = None
        if request.session.get('carrinho', False):
            carrinho = Carrinho.objects.get(id=request.session['carrinho'])
            
        else:
            carrinho = Carrinho.objects.create(loja = produto.loja)
            carrinho.save()
            request.session['carrinho'] = carrinho.id

        #recupera todos os itens do carrinho
        itens_carrinho = carrinho.lista_produtos()
        #Checa a origem do produto

        if len(itens_carrinho) > 0 and produto.loja != carrinho.loja:
            return HttpResponse('Não é possível adicionar produtos de lojas diferentes')
        #Caso o item já exista no carrinho, ele apenas aumenta a quantidade
        #desse item lá dentro
        for x in itens_carrinho:
            if produto == x.produto:
                x.quantidade += 1
                x.save()
                return HttpResponseRedirect(reverse('carrinho'))

        #caso o item ainda não exista lá dentro, ele adiciona o novo item e 
        #redireciona para o url do carrinho
        item = ItemCarrinho.objects.create(produto = produto, carrinho = carrinho)
        item.save()
        return HttpResponseRedirect(reverse('carrinho'))


'''
View dos resultados
'''
class ResultadosView(generic.View):
    pass
        
        

'''
View padrão do carrinho
'''
class CarrinhoView(generic.View):
    def get(self,request, *args, **kwargs):

        #tenta recuperar o carrinho da sessão e retorna se conseguir
        if 'carrinho' in request.session:
            carrinho = Carrinho.objects.get(id=request.session['carrinho'])
            return render(request, 'main/carrinho.html', {'carrinho': carrinho})
        
        #se não conseguir recuperar, cria e retorna o carrinho zerado
        carrinho = {}
        return render(request, 'main/carrinho.html', {'carrinho':carrinho})

class DetalhesLoja(generic.View):
    def get(self, request, *args, **kwargs):
        id_loja = kwargs['id_loja']
        
        loja = get_object_or_404(Loja, pk=id_loja)

        produtos = Produto.objects.filter(loja=loja)

        return render(request, 'main/loja.html', {'loja': loja, 'produtos': produtos})


class ConfirmarPedido(LoginRequiredMixin,generic.View):
    
    def get(self, request):
        if 'carrinho' in request.session:
         carrinho = Carrinho.objects.get(id=request.session['carrinho'])
         return render(request, 'main/confirmar_pedido.html', {'carrinho': carrinho})
        return redirect('/')
    def post(self, request):
          rua = request.POST["nome_rua"]
          numero = request.POST["numero_residencia"]
          complemento= request.POST["complemento"]
          tipo_pag= request.POST["tipo_pagamento"]
          tipo_entrega= request.POST["tipo_entrega"]
          endereco = Endereco.objects.create(nome_rua=rua, complemento = complemento, numero_residencia = numero)
          endereco.save()
          carrinho = Carrinho.objects.get(id=request.session['carrinho'])
          loja = carrinho.loja
          usuario = get_object_or_404(Usuario, user = request.user)
          pedido = Pedido.objects.create(endereco = endereco, tipo_entrega = tipo_entrega, tipo_pagamento = tipo_pag, loja = loja, carrinho = carrinho, cliente = usuario)
          pedido.save()
          del request.session['carrinho']
          return redirect('/pedidos')

class ListarPedidos(LoginRequiredMixin,generic.View):
    def get(self, request):
        user = get_object_or_404(Usuario, user = request.user)
        pedidos = Pedido.objects.filter(cliente = user).order_by('data')
        if pedidos:
           return render(request, 'main/pedido.html', {'pedidos': pedidos})
        else:
           return render(request, 'main/pedido.html', {'message_erro': "Não possui pedidos! "})

class ListarPedidosLojista(LoginRequiredMixin,generic.View):
    def get(self, request, *args, **kwargs):
        loja = Loja.objects.filter(lojista = request.user.usuario)
        pedidos = Pedido.objects.filter(loja=loja[0])

        if pedidos:
            return render(request, 'main/pedidos-lojista.html', {'pedidos': pedidos})
        else:
            return render(request, 'main/pedidos-lojista.html', {'mensagem': 'Não há pedidos'})


class DetalhesPedidoLojista(LoginRequiredMixin,generic.View):
    def get(self, request, *args, **kwargs):
        id_pedido = kwargs['id_pedido']
        pedido = get_object_or_404(Pedido, id=id_pedido)

        if pedido:
            return render(request, 'main/detalhe-pedido-lojista.html', {'pedido' : pedido})

class ConfirmarPedidoLojista(LoginRequiredMixin,generic.View):
    def get(self, request, *args, **kwargs):
        id_pedido = kwargs['id_pedido']
        pedido = get_object_or_404(Pedido, id=id_pedido)

        setattr(pedido, 'status', 'A')

        pedido.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class RejeitarPedidoLojista(LoginRequiredMixin,generic.View):
    def get(self, request, *args, **kwargs):
        id_pedido = kwargs['id_pedido']
        pedido = get_object_or_404(Pedido, id=id_pedido)

        setattr(pedido, 'status', 'C')

        pedido.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class GerenciarEstoque(LoginRequiredMixin,generic.View):
    def get(self, request):
        loja = get_object_or_404(Loja, pk=1)
        produtos = Produto.objects.filter(loja=loja, disponivel=True)
        return render(request, 'main/estoque.html', {'produtos': produtos, 'loja':loja})
        
    def post(self, request):
        loja = get_object_or_404(Loja, pk=1)
        produtos = Produto.objects.filter(loja=loja, disponivel=True)
        for qua in produtos:
            id = qua.id
            check = "check"+str(id)
            Produto.objects.filter(id = id).update(quantidade = request.POST[str(id)], disponivel = request.POST[check])
        return redirect('/produtos')
class DeletarProdutos(LoginRequiredMixin,generic.View):
    def get(self, request):
        loja = get_object_or_404(Loja, pk=1)
        produtos = Produto.objects.filter(loja=loja, disponivel=False)
        return render(request, 'main/excluir_produto.html', {'produtos': produtos, 'loja':loja})
        
    def post(self, request):
        loja = get_object_or_404(Loja, pk=1)
        produtos = Produto.objects.filter(loja=loja, disponivel=False)
        for qua in produtos:
            id = str(qua.id)
            if request.POST[id] == 'True':
                Produto.objects.filter(id = id).delete()
        return redirect('/produtos/indisponiveis')

