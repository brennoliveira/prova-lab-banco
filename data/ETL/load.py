from connect.connect import connect_db,connect_dm
import timeit
from ETL.transform import TransformaClientes,TransformaGestao,TransformaItensVenda,TransformaProduto,TransformaTempo,TransformaVenda,TransformaVendedor
from entities.dimensional import clientesDM,gestaoFT,itens_vendaDM,produtoDM,tempoDM,vendaDM,vendedorDM
import sqlalchemy as sa

# engine_OP = connect_db()
engine_DP = connect_dm()

metadata = sa.MetaData(bind=None)

dm_tempo = sa.Table('TEMPODM', metadata, autoload=True, autoload_with=engine_DP)
dm_itensvenda = sa.Table('ITENS_VENDADM', metadata, autoload=True, autoload_with=engine_DP)
dm_vendas = sa.Table('VENDADM', metadata, autoload=True, autoload_with=engine_DP)
dm_cliente = sa.Table('CLIENTESDM', metadata, autoload=True, autoload_with=engine_DP)
dm_produto = sa.Table('PRODUTODM', metadata, autoload=True, autoload_with=engine_DP)
ft_vendas = sa.Table('VENDADM', metadata, autoload=True, autoload_with=engine_DP)
dm_vendedor = sa.Table('VENDEDORDM', metadata, autoload=True, autoload_with=engine_DP)


def LoadDmCliente(engine_OP):
    print("Iniciando processo de Carregamento dos Clientes")
    start = timeit.default_timer()
    lista = TransformaClientes(engine_OP)
        
    for item in lista :
        ins = dm_cliente.insert().values(id_cliente = item.idcliente, cliente = item.cliente,estado = item.estado,sexo = item.sexo, status= item.status  )
        result = engine_DP.execute(ins)
                
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")


def LoadDmItensVenda(engine_OP):
    print("Iniciando processo de Carregamento dos LoadDmItensVenda")
    start = timeit.default_timer()
    lista = TransformaItensVenda(engine_OP)
        
    count = 0
    for item in lista :
        count += 1
        ins = dm_itensvenda.insert().values(id_itensvenda = count, id_produto = item.idproduto,valorunitario = item.valorunitario,desconto = item.desconto)
        result = engine_DP.execute(ins)
                
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")

def LoadDmProduto(engine_OP):
    print("Iniciando processo de Carregamento dos Produto")
    start = timeit.default_timer()
    lista = TransformaProduto(engine_OP)
        
    for item in lista :
        ins = dm_produto.insert().values(id_produto = item.idproduto, produto = item.produto,classe = item.classe)
        result = engine_DP.execute(ins)
                
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")

def LoadDmVenda(engine_OP):
    print("Iniciando processo de Carregamento dos venda")
    start = timeit.default_timer()
    lista = TransformaVenda(engine_OP)
        
    for item in lista :
        ins = dm_vendas.insert().values(id_venda = item.venda, valor_total = item.total)
        result = engine_DP.execute(ins)
                
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")

def LoadDmVendedor(engine_OP):
    print("Iniciando processo de Carregamento dos venda")
    start = timeit.default_timer()
    lista = TransformaVendedor(engine_OP)
        
    for item in lista :
        ins = dm_vendedor.insert().values(id_vendedor = item.idvendedor, nome = item.nome, nivel = item.nivel)
        result = engine_DP.execute(ins)
                
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")

def LoadDmGestaoFT(engine_OP):
    print("Iniciando processo de Carregamento dos gestaoft")
    start = timeit.default_timer()
    lista = TransformaGestao(engine_OP)
    countr = 0
    for item in lista :
        countr += 1
        ins = ft_vendas.insert().values(id_tempo = item.idtempo, id_venda = item.idvenda, id_itensvenda = countr, id_vendedor=item.idvendedor, id_produto = item.idproduto, qtd_vendas = item.qtd_vendas)
        result = engine_DP.execute(ins)
                
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")

def LoadDmTempo(engine_OP):
    print("Iniciando processo de Carregamento dos tempo")
    start = timeit.default_timer()
    lista = TransformaTempo(engine_OP)
        
    for item in lista :
        ins = dm_tempo.insert().values(id_tempo = item.idtempo, dia = item.dia, mes = item.mes, ano=item.ano, trimestre = item.trimestre)
        result = engine_DP.execute(ins)
                
    end = timeit.default_timer()
    exec_time = end - start
    print(f"empo: {exec_time:.2f}s")
