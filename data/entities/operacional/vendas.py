class Vendas():

  def to_string(self):
    return {
      "id_venda": self.idvenda,
      "id_vendedor": self.idvendedor,
      "id_c": self.idcliente,
      "data": self.data,
      "total": self.total
    }

  def __init__(self, idvenda, idvendedor, idcliente, data, total) -> None:
      self.idvenda = idvenda
      self.idvendedor = idvendedor
      self.idcliente = idcliente
      self.data = data
      self.total = total
      