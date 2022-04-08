class ItensVenda():

  def to_string(self):
    return {
      "id_i_v": self.iditensvenda,
      "id_p": self.idproduto,
      "id_v": self.idvenda,
      "qtd": self.quantidade,
      "valor_u": self.valorunitario,
      "valor_t": self.valortotal,
      "desc": self.desconto
    }

  def __init__(self, iditensvenda, idproduto, idvenda, quantidade, valorunitario, valortotal, desconto) -> None:
      self.iditensvenda = iditensvenda
      self.idproduto = idproduto
      self.idvenda = idvenda
      self.quantidade = quantidade
      self.valorunitario = valorunitario
      self.valortotal = valortotal
      self.desconto = desconto
      