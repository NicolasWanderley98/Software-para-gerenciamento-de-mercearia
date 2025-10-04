Software para Gerenciamento de Mercearia

Este repositório contém o código de um software de gerenciamento de mercearia, desenvolvido para facilitar o controle de estoque, vendas e produtos em uma mercearia ou pequeno comércio. O objetivo principal do software é oferecer uma solução simples e eficiente para o gerenciamento do dia a dia do negócio.

Descrição

O Software para Gerenciamento de Mercearia foi desenvolvido com foco em simplicidade e usabilidade, permitindo que o proprietário ou funcionário da mercearia possa facilmente controlar o estoque de produtos, registrar vendas e acompanhar o faturamento.

Funcionalidades principais:

Cadastro de produtos: Permite adicionar, editar e remover produtos do estoque.

Controle de estoque: Monitora a quantidade de produtos disponíveis e avisa quando é necessário reabastecer.

Registro de vendas: Realiza o registro das vendas realizadas, com controle de preço e quantidade.

Relatórios: Geração de relatórios básicos de vendas e estoque.

Interface simples e intuitiva: Facilita a interação com o sistema mesmo para usuários sem experiência em software.

Tecnologias Utilizadas

Linguagem: Python

Frameworks/Bibliotecas: Tkinter (para interface gráfica), SQLite (para banco de dados local)

Sistema Operacional: O software foi desenvolvido para rodar em sistemas operacionais como Windows, Linux e macOS.

Como Usar
Requisitos

Python 3.x instalado em sua máquina.

Dependências do projeto (Tkinter e SQLite) instaladas.

Passos para rodar o software:

Clone o repositório para a sua máquina local:

git clone https://github.com/NicolasWanderley98/Software-para-gerenciamento-de-mercearia.git


Instale as dependências necessárias:

Se você estiver usando um ambiente virtual, ative-o primeiro.

Instale as dependências do projeto:

pip install -r requirements.txt


Caso não tenha o arquivo requirements.txt, as bibliotecas utilizadas (Tkinter e SQLite) já são comuns em instalações padrão do Python. Se necessário, instale o Tkinter manualmente:

sudo apt-get install python3-tk  # Linux
brew install python-tk           # macOS


Execute o software:

Navegue até o diretório do projeto e execute o script principal:

python main.py


Interface gráfica: Ao executar o script, a interface gráfica será aberta. Você poderá adicionar produtos, registrar vendas e visualizar o estoque e relatórios.

Estrutura de Diretórios
Software-para-gerenciamento-de-mercearia/
├── main.py                # Arquivo principal que executa o software
├── database.db            # Banco de dados local SQLite para armazenar dados
├── requirements.txt       # Arquivo com as dependências do projeto (caso necessário)
├── imagens/               # Pasta com imagens (se houver, para o software)
└── README.md              # Este arquivo com as instruções do projeto

Exemplo de Código

Aqui está um exemplo de como a interface do software pode ser inicializada no main.py:

import tkinter as tk
from tkinter import messagebox
import sqlite3

def iniciar():
    # Configurações da interface gráfica (Tkinter)
    janela = tk.Tk()
    janela.title("Gerenciamento de Mercearia")

    # Exemplo de um botão simples
    def cadastrar_produto():
        # Função para cadastrar um produto no banco de dados
        pass

    botao_cadastrar = tk.Button(janela, text="Cadastrar Produto", command=cadastrar_produto)
    botao_cadastrar.pack()

    janela.mainloop()

if __name__ == "__main__":
    iniciar()

Como Contribuir

Se você gostaria de contribuir para o desenvolvimento deste software, siga os passos abaixo:

Fork o repositório.

Clone o repositório para a sua máquina local.

Crie uma nova branch para suas alterações:

git checkout -b minha-alteracao


Faça as alterações desejadas e commit:

git commit -m "Descrição das mudanças"


Envie suas alterações para o seu repositório no GitHub:

git push origin minha-alteracao


Abra um pull request para que possamos revisar e integrar suas mudanças.

Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE
 para mais detalhes.

Agradecimentos

Agradecemos a todos que contribuíram para o desenvolvimento deste software e aos desenvolvedores das tecnologias utilizadas. Este software tem como objetivo melhorar a gestão de pequenos comércios e facilitar o controle de estoque e vendas.
