class GestaoFT():
  
  def to_string(self):
    return {
      "id_p": self.idproduto,
      "id_v": self.idvenda,
      "id_tempo": self.idtempo,
      "id_vendedor": self.idvendedor,
      "id_c": self.idcliente,
      "qtd_vendas": self.qtd_vendas
    }

  def __init__(self, idproduto, idvenda, idtempo, idvendedor, idcliente, qtd_vendas) -> None:
      self.idproduto = idproduto
      self.idvenda = idvenda
      self.idtempo = idtempo
      self.idvendedor = idvendedor
      self.idcliente = idcliente
      self.qtd_vendas = qtd_vendas
      