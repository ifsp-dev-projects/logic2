class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

PRODUTOS = [
    Produto(1, 'Notebook Gamer X', 5200.00),
    Produto(2, 'Mouse Sem Fio', 150.00),
    Produto(3, 'Teclado Mecânico RGB', 350.00),
    Produto(4, 'Monitor 27" Full HD', 1800.00),
    Produto(5, 'Headset Gamer 7.1', 420.00),
    Produto(6, 'Webcam Full HD', 280.00),
    Produto(7, 'Mousepad RGB', 120.00),
    Produto(8, 'SSD 1TB NVMe', 450.00),
    Produto(9, 'Memória RAM 16GB', 320.00),
    Produto(10, 'Placa de Vídeo RTX 4060', 2800.00),
    Produto(11, 'Gabinete Gamer', 380.00),
    Produto(12, 'Fonte 750W 80 Plus', 520.00),
    Produto(13, 'Cadeira Gamer Ergonômica', 1200.00),
    Produto(14, 'Mesa para Computador', 650.00),
    Produto(15, 'Hub USB 3.0', 90.00),
    Produto(16, 'Cooler para Processador', 180.00),
    Produto(17, 'Impressora Laser', 890.00),
    Produto(18, 'Tablet 10" Full HD', 1500.00),
    Produto(19, 'Smartphone Flagship', 3500.00),
    Produto(20, 'Smartwatch Esportivo', 680.00)
]

def buscar_produto_por_id(produto_id):
    for produto in PRODUTOS:
        if produto.id == produto_id:
            return produto
    return None

def buscar_produtos_por_nome(nome):
    nome = nome.lower()
    return [p for p in PRODUTOS if nome in p.nome.lower()]
