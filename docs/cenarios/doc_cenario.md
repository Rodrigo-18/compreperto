# Cenários

**Sistema**: Compre Perto  
**Requisitos funcionais**: Realizar pedido / Aprovar pedido  
**Usuários**: Cliente / Lojista

## Adicionar produtos ao carrinho

1. O sistema apresenta ao cliente a página de busca de produtos
2. O cliente busca por um produto
3. O sistema apresenta uma lista de resultados baseados na pesquisa do cliente
4. O cliente seleciona um produto e clica no botão de adicionar ao carrinho
5. O sistema adiciona o produto ao carrinho
6. O cliente pressiona o botão para ir ao carrinho
7. O sistema apresenta a página do carrinho com os produtos adicionados
8. O cliente pressiona o botão para fechar o pedido

Ponto de extensão "Fazer login"

## Fazer login

1. O sistema apresenta um formulário de login
2. O usuário (seja cliente ou lojista) preenche os campos com seu login e sua senha

Ponto de extensão "Realizar pedido", "Aprovar pedido", "Atualizar estoque"

## Realizar pedido

1. O sistema apresenta a página onde o cliente selecionará a forma de pagamento, o tipo de entrega, e, se a entrega for delivery, o endereço
2. O cliente preenche os dados e pressiona o botão para finalizar e enviar o pedido ao lojista

## Aprovar pedido

1. Após o login, o sistema apresenta ao lojista a página da sua loja
2. O lojista pressiona o botão para acessar a lista de pedidos feitos à sua loja
3. O sistema apresenta uma página com essa lista de pedidos
4. O lojista seleciona um pedido específico e pressiona um botão para visualizar os detalhes do pedido
5. O lojista analisa os detalhes do pedido

Fluxos alternativos:

6. O lojista confirma o pedido  
6.1 Se os detalhes do pedido estiverem conformes, o lojista confirma o pedido  
6.2 O sistema informa ao usuário que o pedido foi confirmado

7. O lojista rejeita o pedido  
7.1 Se os detalhes do pedido não estiverem conformes, o lojista rejeita o pedido  
7.1 O sistema informa ao usuário que o pedido foi rejeitado

## Atualizar o estoque

1. Após o login, o sistema apresenta ao lojista a página da sua loja
2. O lojista pressiona o botão para acessar a lista de produtos cadastrados na sua loja
3. O sistema apresenta uma página com essa lista de produtos
4. O lojista seleciona um produto específico e pressiona um botão para atualizar o número de unidades em estoque
5. O sistema apresenta ao lojista um formulário onde ele pode escolher entre adicionar um número específico de unidades ao estoque ou dois números indicando o número de unidades que vêm dentro de um pacote / caixa e o número desses pacotes / caixas
6. O lojista escolhe a opção de adição
7. O lojista preenche o formulário com o(s) número(s) e pressiona um botão para salvar esses dados no estoque
