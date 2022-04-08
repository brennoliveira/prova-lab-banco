class ItensVendaDM():
  
  def to_string(self):
    return {
      "id_p": self.idproduto,
      "id_v": self.idvenda,
      "valor_u": self.valorunitario,
      "desc": self.desconto
    }

  def __init__(self, idproduto, idvenda, valorunitario, desconto) -> None:
      self.idproduto = idproduto
      self.idvenda = idvenda
      self.valorunitario = valorunitario
      self.desconto = desconto
      