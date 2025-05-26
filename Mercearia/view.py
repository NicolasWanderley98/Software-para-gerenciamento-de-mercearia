import Controller
import os.path

def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write("")

criarArquivos("categoria.txt", "clientes.txt",
              "estoque.txt", "fornecedores.txt",
              "funcionarios.txt", "vendas.txt")

if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar ( Categorias )\n"
                           "Digite 2 para acessar ( Estoque )\n"
                           "Digite 3 para acessar ( Fornecedor )\n"
                           "Digite 4 para acessar ( Cliente )\n"
                           "Digite 5 para acessar ( Funcionario )\n"
                           "Digite 6 para acessar ( Vendas )\n"
                           "Digite 7 para ver os produtos mais vendidos\n"
                           "Digite 8 para sair\n"))

        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma categoria\n"
                                     "Digite 2 para remover uma categoria\n"
                                     "Digite 3 para alterar uma categoria\n"
                                     "Digite 4 para mostrar uma categoria\n"
                                     "Digite 5 para sair\n"))

                if decidir == 1:
                    categoria = input('Digite a categoria que deseja cadastrar\n')
                    cat.cadastrarCategoria(categoria)
                elif decidir == 2:
                    categoria = input('Digite a categoria que deseja remover\n')
                    cat.cadastrarCategoria(categoria)
                elif decidir == 3:
                    categoria = input('Digite a categoria que deseja alterar\n')
                    novaCategoria = input('Digite a categoria para qual deseja alterar\n')
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break
        elif local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma produto\n"
                                     "Digite 2 para remover uma produto\n"
                                     "Digite 3 para alterar uma produto\n"
                                     "Digite 4 para mostrar uma produto\n"
                                     "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input('Digite o nome do produto: \n')
                    preco = input('Digite o preco do produto: \n')
                    categoria = input('Digite a categoria do produto \n')
                    quantidade = input('Digite a quantidade do produto: \n')

                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    categoria = input('Digite o produto que deseja remover\n')
                    cat.removerProduto(produto)
                elif decidir == 3:
                    categoria = input('Digite o produto que deseja alterar\n')
                    nomeAlterar = input('Digite o nome do produto que deseja alterar\n')
                    nome = input('Digite o novo nome do produto: \n')
                    preco = input('Digite o novo preco do produto: \n')
                    categoria = input('Digite a nova categoria do produto \n')
                    quantidade = input('Digite a nova quantidade do produto: \n')
                    cat.alterarProduto(nomeAlterar, nome,preco , categoria, quantidade)
                elif decidir == 4:
                    cat.mostrarEstoque()
                else:
                    break
