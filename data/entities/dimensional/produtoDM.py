class ProdutoDM():
  
  def to_string(self):
    return {
      "id": self.idproduto,
      "produto": self.produto,
      "classe": self.classe
    }

  def __init__(self, idproduto, produto, classe) -> None:
      self.idproduto = idproduto
      self.produto = produto
      self.classe = classe
      