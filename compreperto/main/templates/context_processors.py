from ..models import Carrinho
def cart_itens(request):
    numb_itens = 0
    if 'carrinho' in request.session:
        carrinho = Carrinho.objects.get(id=request.session['carrinho'])
        for x in carrinho.itemcarrinho_set.all():
            numb_itens += 1
    return {
        'cart_number': numb_itens
    }