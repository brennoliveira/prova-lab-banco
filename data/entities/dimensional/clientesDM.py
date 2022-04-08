class ClientesDM():
  def to_string(self):
    return {
      "idcliente": self.idcliente,
      "nome": self.cliente,
      "estado": self.estado,
      "sexo": self.sexo,
      "status": self.status
    }
  def __init__(self, idcliente, cliente, estado, sexo, status) -> None:
      self.idcliente = idcliente
      self.cliente = cliente
      self.estado = estado
      self.sexo = sexo
      self.status = status
