# CDU Pesquisar por produto
## 1. Descrição
O usuário pesquisa por um produto no sistema e são apresentadas produtos com base nesta pesquisa.
## 2. Atores
* Visitante da página.
* Cliente.
## 3. Pré-condições
Não existem pré-condições para este caso de uso.
## 4. Pós-condições
O sistema deve apresentar produtos ao usuário a partir da pesquisa feita.
## 5. Fluxo Principal
1. O usuário acessa o sistema.
1. O usuário preenche os campos de pesquisa com seu endereço e com o produto que deseja comprar, e então pressiona o botão de pesquisar.
1. O sistema apresenta produtos com seus respectivos nomes, valores e localização da loja.
## 6. Fluxos alternativos
4. Caso não haja produtos que se encaixem nos parâmetros pesquisados.  
4.1. O sistema apresenta ao usuário uma mensagem de que não há resultados compatíveis com a pesquisa realizada. 
## 7. Situações de erro
* O sistema informa ao usuário que não foi possível realizar a pesquisa pois não há conexão com a internet.
## 8. Regras de Negócio
* RN 01 
  * Toda pesquisa deve conter um endereço físico e uma sequência de caracteres (String) que diz respeito aos termos que o usuário está buscando.
* RN 02
  * Para que uma loja seja considerada na pesquisa, ela deve ter ao menos um produto.
