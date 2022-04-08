import timeit
import sqlalchemy as sa
import pandas as pd
from entities.operacional import clientes,itens_venda,produtos,vendas,vendedores

def ExtractClientes(engine):
  lista = []
  items = 0
  print("extracting Clientes")
  start = timeit.default_timer()
  
  sql = 'SELECT * FROM relacional.clientes'
  df = pd.read_sql(sql, engine)
  
  
  for index, item in df.iterrows():
    lista.append(clientes.Clientes(**item))
    items += 1
    
  print(lista[2].to_string())
  end = timeit.default_timer()
  exec_time = end - start
  print(f"itens: {items} \ntempo: {exec_time:.2f}s")
  
  return lista
  
  
def ExtractVendedores(engine):
  lista = []
  items = 0
  print("extracting Vendedores")
  start = timeit.default_timer()
  
  sql = 'SELECT * FROM relacional.vendedores'
  df = pd.read_sql(sql, engine)
  
  
  for index, item in df.iterrows():
    lista.append(vendedores.Vendedores(**item))
    items += 1
    
  print(lista[2].to_string())
  end = timeit.default_timer()
  exec_time = end - start
  print(f"itens: {items} \ntempo: {exec_time:.2f}s")
  
  return lista
  
    
def ExtractProdutos(engine):
  lista = []
  items = 0
  print("extracting Produtos")
  start = timeit.default_timer()
  
  sql = 'SELECT * FROM relacional.produtos'
  df = pd.read_sql(sql, engine)
  
  
  for index, item in df.iterrows():
    lista.append(produtos.Produtos(**item))
    items += 1
    
  print(lista[9].to_string())
  end = timeit.default_timer()
  exec_time = end - start
  print(f"itens: {items} \ntempo: {exec_time:.2f}s")
  
  return lista
  
    
def ExtractItensVenda(engine):
  lista = []
  items = 0
  print("extracting ItensVenda")
  start = timeit.default_timer()
  
  sql = 'SELECT * FROM relacional.itensvenda'
  df = pd.read_sql(sql, engine)
  
  
  for index, item in df.iterrows():
    lista.append(itens_venda.ItensVenda(**item))
    items += 1
    
  print(lista[2].to_string())
  end = timeit.default_timer()
  exec_time = end - start
  print(f"itens: {items} \ntempo: {exec_time:.2f}s")
  
  return lista
    
def ExtractVendas(engine):
  lista = []
  items = 0
  print("extracting Vendas")
  start = timeit.default_timer()
  
  sql = 'SELECT * FROM relacional.vendas'
  df = pd.read_sql(sql, engine)
  
  
  for index, item in df.iterrows():
    lista.append(vendas.Vendas(**item))
    items += 1
    
  print(lista[300].to_string())
  end = timeit.default_timer()
  exec_time = end - start
  print(f"itens: {items} \ntempo: {exec_time:.2f}s")
  
  return lista
