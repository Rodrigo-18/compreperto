# CDU Fechar pedido

## 1. Descrição 
O cliente a partir do produtos presentes no carrinho seleciona a forma de pagamento e envia ao lojista o pedido.

## 2. Atores
* Cliente
## 3. Pré-condições
* Estar logado no sistema.
Possuir um carrinho com produtos de uma loja específica.
## 4. Pós-condições
* O sistema deve apresentar uma página com os pedidos em espera para o cliente, que aguarda a avaliação do lojista.
## 5. Fluxo Principal
1. O Cliente pressiona o botão Finalizar pedido.
1. O sistema apresenta a página com a tela de confirmação para ser selecionado o tipo de pagamento e o tipo de entrega, também é apresentado os produtos, subtotal e o total do pedido. 
1. O cliente seleciona o tipo de pagamento e de entrega(Caso seja necessário), por fim pressiona o botão de confirmação.
1. O Sistema apresenta uma tela com os pedidos realizados pelo cliente.
## 6. Fluxos alternativos
Não possui fluxos alternativos.
## 7. Situações de erro
* O sistema informa ao usuário que não foi possível finalizar o pedido, pois não há conexão com a internet.
## 8. Regras de Negócio
* RN 04
  * Para ser possível finalizar o pedido é necessário estar logado e possuir carrinho com produtos.