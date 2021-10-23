# CDU Analisar pedidos em aberto

## 1. Descrição
O lojista acessa a página que contém todos os pedidos que aguardam confirmação.

## 2. Atores
* Lojista.

## 3. Pré-condições
* Estar logado no sistema.
* Ter uma loja cadastrada no sistema.
* Ter produtos cadastrados nesta loja.

## 4. Pós-condições
* O sistema deve apresentar uma página com os pedidos feitos por clientes que estão aguardando confirmação.

## 5. Fluxo Principal
1. O lojista pressiona o botão _Pedidos_ no menu superior da página.
2. O sistema apresenta a página com todos os pedidos em aberto. Cada item desta lista apresenta quais produtos estão no pedido, quantidades de cada produto, valor unitário de cada produto e o valor total do pedido. Assim como dois botões: _Aceitar pedido_ e _Rejeitar pedido_.

## 6. Fluxos alternativos
3. Caso não haja pedidos em aberto.  
3.1 O sistema exibe uma mensagem informando o lojista de que não há pedidos pendentes.

## 7. Situações de erro
* O sistema informa ao usuário que não foi possível acessar a página de pedidos pois não há conexão com a internet.

## 8. Regras de Negócio
* RN 03  
  * Para que uma loja receba pedidos, ela deve ter ao menos um produto.