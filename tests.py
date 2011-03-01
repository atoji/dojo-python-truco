from main import Carta, CartaVirada, CartaViradaDiferente

def test_compara_duas_cartas():
    assert Carta('2', 'e', CartaVirada('q')) < Carta('3', 'e', CartaVirada('q'))

def test_compara_duas_cartas_com_letra():
    assert Carta('j', 'e', CartaVirada('q')) > Carta('q', 'e', CartaVirada('q'))

def test_compara_duas_cartas_sendo_uma_a_manilha():
    assert Carta('2', 'e', CartaVirada('a')) > Carta('3', 'e', CartaVirada('a'))

def test_compara_duas_manilhas():
    assert Carta('a', 'e', CartaVirada('k')) < Carta('a', 'p', CartaVirada('k'))

def test_compara_duas_cartas_de_mesmo_numero_nao_manilhas():
    assert Carta('3', 'e', CartaVirada('k')) == Carta('3', 'o', CartaVirada('k'))

def test_carta_eh_manilha():
    assert Carta('a', 'e', CartaVirada('k')).eh_manilha()

def test_cartas_com_carta_virada_diferentes_da_erro_na_comparacao():
    try:
        Carta('3', 'e', CartaVirada('k')) == Carta('3', 'o', CartaVirada('a'))
        assert False
    except CartaViradaDiferente:
        assert True
