class Produtos():

  def to_string(self):
    return {
      "id": self.idproduto,
      "produto": self.produto,
      "preco": self.preco
    }

  def __init__(self, idproduto, produto, preco) -> None:
      self.idproduto = idproduto
      self.produto = produto
      self.preco = preco
      