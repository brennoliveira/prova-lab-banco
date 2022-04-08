def defineClass(item):
  classe = ''
  if item.preco <= 499.99:
    classe = 'P'
  elif item.preco > 500 or item.preco <= 2999.99:
    classe = 'M'
  elif item.preco >= 3000:
    classe = 'A'
  return classe

def defineNivel(lista_vendedor, lista_venda):
  total_valor, nivel = 0, 1
  for i in lista_venda:
    for j in lista_vendedor:
      if i.idvendedor == j.idvendedor:
        total_valor += i.total

  if total_valor <= 199000:
    nivel = 1
  elif total_valor >= 200000 or total_valor <= 299000:
    nivel = 2
  elif total_valor >= 300000:
    nivel = 3
  return nivel


def defineTrimestre(item):
  trimestre = 0
  if int(item.data.strftime('%m')) <= 3:
    trimestre = 1
  elif int(item.data.strftime('%m')) >= 4 or int(item.data.strftime('%m')) <= 6:
    trimestre = 2
  elif int(item.data.strftime('%m')) >= 7 or int(item.data.strftime('%m')) <= 9:
    trimestre = 3
  elif int(item.data.strftime('%m')) >= 10:
    trimestre = 4
  return trimestre

def defineStatus(item):
  s = ''
  if item.status == 'Silver':
    s = 'S'
  elif item.status == 'Gold': 
    s = 'G'
  elif item.status == 'Platinum':
    s = 'P'
  return s