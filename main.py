class Carta(object):
    def valor_real(self):
        return self.ordem.index(self.numero)

    def valor_do_naipe(self):
        return ['o', 'e', 'c', 'p'].index(self.naipe)

    def __init__(self, numero, naipe, carta_virada):
        self.numero = numero
        self.naipe = naipe
        self.carta_virada = carta_virada
        self.ordem = self.define_ordem()

    def __cmp__(self, outra_carta):
        if self.carta_virada != outra_carta.carta_virada:
            raise CartaViradaDiferente()

        if self.eh_manilha() and outra_carta.eh_manilha():
            return self.valor_do_naipe() - outra_carta.valor_do_naipe()

        return self.valor_real() - outra_carta.valor_real()

    def eh_manilha(self):
        return self.valor_real() == (len(self.ordem) - 1)

    def define_ordem(self):
        ordem = ['q','j','k','a','2','3']
        posicao_da_manilha = (ordem.index(self.carta_virada.numero) + 1) % len(ordem)
        manilha = ordem.pop(posicao_da_manilha)
        ordem.append(manilha)
        return ordem

class CartaVirada(object):
    def __init__(self, numero):
        self.numero = numero

    def __cmp__(self, outra_carta):
        if self.numero == outra_carta.numero:
            return 0
        return 1

class CartaViradaDiferente(Exception):
    pass
