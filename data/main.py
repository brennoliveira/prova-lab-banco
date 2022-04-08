from ETL.extract import ExtractClientes,ExtractVendedores,ExtractProdutos,ExtractItensVenda,ExtractVendas
from ETL.transform import TransformaClientes,TransformaProduto, TransformaTempo, TransformaVendedor,TransformaGestao,TransformaItensVenda,TransformaVenda
from ETL.load import LoadDmCliente,LoadDmGestaoFT,LoadDmItensVenda,LoadDmProduto,LoadDmTempo,LoadDmVenda,LoadDmVendedor
from connect.connect import connect_db


engine = connect_db()

# ExtractClientes(engine)
# ExtractVendedores(engine)
# ExtractProdutos(engine)
# ExtractItensVenda(engine)
# ExtractVendas(engine)

# TransformaProduto(engine)
# TransformaClientes(engine)
# TransformaTempo(engine)
# TransformaVendedor(engine)
# TransformaVenda(engine)
# TransformaItensVenda(engine)
# TransformaGestao(engine)
LoadDmVendedor(engine)
LoadDmGestaoFT(engine)
LoadDmItensVenda(engine)
LoadDmProduto(engine)
LoadDmCliente(engine)
LoadDmTempo(engine)
LoadDmVenda(engine)