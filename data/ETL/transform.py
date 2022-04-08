import pandas as pd
import sqlalchemy as sa
import timeit
from ETL.extract import ExtractClientes,ExtractItensVenda,ExtractProdutos,ExtractVendas,ExtractVendedores
from entities.dimensional import clientesDM,gestaoFT,itens_vendaDM,produtoDM,tempoDM,vendaDM,vendedorDM
from utils.utils import defineClass,defineNivel,defineTrimestre

def TransformaClientes(engineDM):
    listaDW = []
    print("transformação de Clientes")
    start = timeit.default_timer()
    
    lista_op =  ExtractClientes(engineDM)
        
    for i in lista_op:
       listaDW.append(clientesDM.ClientesDM(i.idcliente, i.cliente, i.estado, i.sexo, i.status))

    print(listaDW[2].to_string())        
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")
    
    return listaDW
  

def TransformaProduto(engineDM):
    listaDW = []
    print("transformação de Produto")
    start = timeit.default_timer()
    
    lista_op =  ExtractProdutos(engineDM)
        
    for i in lista_op:
       listaDW.append(produtoDM.ProdutoDM(i.idproduto, i.produto, defineClass(i)))

    print(listaDW[9].to_string())    
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")
    
    return listaDW

def TransformaVendedor(engineDM):
    listaDW = []
    print("transformação de Vendedor")
    start = timeit.default_timer()
    
    lista_op =  ExtractVendedores(engineDM)
    lista_op_vendas = ExtractVendas(engineDM)
        
    for i in lista_op:
       listaDW.append(vendedorDM.VendedorDM(i.idvendedor, i.nome, defineNivel(lista_op, lista_op_vendas)))


    print(listaDW[7].to_string())    
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")
    
    return listaDW


def TransformaItensVenda(engineDM):
    listaDW = []
    print("transformação de ItensVenda")
    start = timeit.default_timer()
    
    lista_op =  ExtractItensVenda(engineDM)
        
    for i in lista_op:
       listaDW.append(itens_vendaDM.ItensVendaDM(i.iditensvenda, i.idproduto, i.idvenda,  
                                                  i.valorunitario, i.desconto))

    print(listaDW[2].to_string())    
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")
    
    return listaDW


def TransformaTempo(engineDM):
    listaDW = []
    id_tempo = 0
    print("transformação de Tempo")
    start = timeit.default_timer()
    
    lista_op =  ExtractVendas(engineDM)
        
    for i in lista_op:
      id_tempo += 1
      listaDW.append(tempoDM.TempoDM(id_tempo, i.data.strftime('%d'), i.data.strftime('%m'), 
                                    i.data.strftime('%Y'), defineTrimestre(i)))

    print(listaDW[2].to_string())    
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")
    
    return listaDW


def TransformaVenda(engineDM):
    listaDW = []
    print("transformação de Venda")
    start = timeit.default_timer()
    
    lista_op =  ExtractVendas(engineDM)
        
    for i in lista_op:
       listaDW.append(vendaDM.VendaDM(i.idvenda, i.total))

    print(listaDW[2].to_string())    
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")
    
    return listaDW


def TransformaGestao(engineDM):
    listaDW = []
    print("transformação de Gestao")
    start = timeit.default_timer()
    
    tempo_id = 0
    venda = ExtractVendas(engineDM)
    itens_venda = ExtractItensVenda(engineDM)

        
    for i in venda:
        tempo_id += 1
        for j in itens_venda:
            listaDW.append(gestaoFT.GestaoFT(tempo_id, i.idvenda, 
                                        j.iditensvenda, i.idvenda,
                                        j.idproduto, sum(j.valortotal)))

    print(listaDW[2].to_string())    
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")
    
    return listaDW