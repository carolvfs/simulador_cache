from objetos import *


ch = Cache(16, 'direto')
#ch = Cache(16, 'associativo')
#ch = Cache(16, 'associativo por conjunto')

mp = MemoriaPrincipal('./blocosMP.txt')
c = Controlador()

#resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'fifo')
#resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'lru')
resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'lfu')
#resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'random')
