class VendedorDM():
  
  def to_string(self):
    return {
     "id": self.idvendedor,
     "nome": self.nome,
     "nivel": self.nivel 
    }

  def __init__(self, idvendedor, nome, nivel) -> None:
      self.idvendedor = idvendedor
      self.nome = nome
      self.nivel = nivel
      