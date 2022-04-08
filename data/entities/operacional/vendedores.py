class Vendedores():

  def to_string(self):
    return {
     "id": self.idvendedor,
     "nome": self.nome 
    }

  def __init__(self, idvendedor, nome) -> None:
      self.idvendedor = idvendedor
      self.nome = nome
      