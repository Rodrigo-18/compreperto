## Projeto Compre Perto

### Mapa do Site
Versão 1.0, de 13 de julho de 2021.

```mermaid
graph TD;
  Página_inicial-->Resultado_de_buscas;
  Página_inicial-->Login_de_usuário;
  Página_inicial-->Carrinho_de_compras;
  Resultado_de_buscas-->Detalhes_de_produto;
  Resultado_de_buscas-->Carrinho_de_compras;
  Detalhes_de_produto-->Carrinho_de_compras;
  Carrinho_de_compras-->Login_de_usuário;
  Login_de_usuário-->Fechamento_de_pedido;
```