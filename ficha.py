#Ars magica Interface
from características import *
from habilidades import *

class explicação:
    "Olá, sou Aziel Melo. Criei esta aplicação com o objetivo de ter uma Interface gráfica \n para facilitar jogar ars magica com meus amigos. Espero que você se divirta utilizando-a! \n"
pass

#No futuro, com a adição do acesso a banco de dados, essa  sessão da aplicação será transformada em umobjeto DTO

class ficha(características, habilidades):
    "Essa é o formato geral de fichas para ars magica \n"
    def __init__(self):
        super().caracConstrutor()
        super().habConstrutor()
    def mudaFOR(força):
        self.FOR = força
pass

MagoIgnácio = ficha()

print(explicação.__doc__)
