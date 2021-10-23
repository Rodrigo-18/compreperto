``` mermaid
sequenceDiagram

    participant C as Cliente
    participant AIV as AdicionarItemView
    participant CR as Carrinho
    participant IC as ItemCarrinho
    participant CV as CarrinhoView
    participant TC as TelaCarrinho
    
    
    C ->> AIV: get(self, request, *args, *kwargs)

    alt carrinho já existe na sessão
        AIV -->> AIV:carrinho = request.session['carrinho'] 
    
    else carrinho ainda não existe
        AIV -->> CR: carrinho = Carrinho.objects.create()
    
    end

    AIV -->> AIV: produto = get_object_or_404(Produto, pk = id_produto)

    alt carrinho já possui 1 produto e tenta-se adicionar um produto de loja difente
        AIV -->> AIV: return HttpResponse('Não é possível adicionar produtos de lojas diferentes')
    
    end
    AIV -->> IC: ItemCarrinho.objects.create(carrinho = carrinho, produto = produto)
    AIV ->> CV: HTTPResponseRedirect(reverse('main:carrinho'))
    CV ->> TC: render(request, 'main/carrinho.html', {'carrinho':carrinho})
    TC -->> C: Exibe Carrinho

    
    
    
    



```