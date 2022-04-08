class TempoDM():
  
  def to_string(self):
    return {
      "id_tempo": self.idtempo,
      "dia": self.dia,
      "mes": self.mes,
      "ano": self.ano,
      "trimestre": self.trimestre
    }

  def __init__(self, idtempo, dia, mes, ano, trimestre) -> None:
      self.idtempo = idtempo
      self.dia = dia
      self.mes = mes
      self.ano = ano
      self.trimestre = trimestre
      