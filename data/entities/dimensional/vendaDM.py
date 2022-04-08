class VendaDM():
  
  def to_string(self):
    return {
      "id_venda": self.idvenda,
      "total": self.total
    }

  def __init__(self, idvenda, total) -> None:
      self.idvenda = idvenda
      self.total = total
      