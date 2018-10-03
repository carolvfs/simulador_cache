from objetos import *

# Chamar este script com redirecionamento da saida para um arquivo texto.
# Ex.: phython simulador_cache.py > saida.txt

# Cria a memoria Principal e define qual o nome do arquivo texto a ser lido como entrada.
mp = MemoriaPrincipal('./blocosMP.txt')

# Cria o controlador da cache.
c = Controlador()

# Os metodos serao chamados para cada politica de substituicao.
# Nao e necessario realizar alteracoes.

print('\n******************************************************************')
print(' >> Executando o Simulador...')
print(' >> Alunas Carolina Veiga e Gyslla Vasconcelos')
print('******************************************************************')

print('\n******************************************************************')
print(' >> Método Direto')
print('******************************************************************')

ch = Cache(16, 'direto')
resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'none')


print('\n******************************************************************')
print(' >> Método Associativo/FIFO')
print('******************************************************************')

ch = Cache(16, 'associativo')
resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'fifo')

print('\n******************************************************************')
print(' >> Método Associativo/LRU')
print('******************************************************************')


ch = Cache(16, 'associativo')
resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'lru')

print('\n******************************************************************')
print(' >>  Método Associativo/LFU')
print('******************************************************************')

ch = Cache(16, 'associativo')
resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'lfu')

print('\n******************************************************************')
print(' >> Método Associativo/RANDOM')
print('******************************************************************')

ch = Cache(16, 'associativo')
resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'random')

print('\n******************************************************************')
print(' >> Método Associativo por Conjunto/FIFO')
print('******************************************************************')

ch = Cache(16, 'associativo por conjunto')
resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'fifo')

print('\n******************************************************************')
print(' >> Método Associativo por Conjunto/LRU')
print('******************************************************************')

ch = Cache(16, 'associativo por conjunto')
resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'lru')

print('\n******************************************************************')
print(' >> Método Associativo por Conjunto/LFU')
print('******************************************************************')

ch = Cache(16, 'associativo por conjunto')
resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'lfu')

print('\n******************************************************************')
print(' >> Método Associativo por Conjunto/RANDOM')
print('******************************************************************')

ch = Cache(16, 'associativo por conjunto')
resultado_da_busca = c.procura_dados(mp.matriz, ch.matriz, ch.metodo, 'random')
