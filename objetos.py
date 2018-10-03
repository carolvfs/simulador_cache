
from random import randint

########################################################################
#Funcao auxiliar

def mat_cria(num_linhas, num_colunas, valor):

    matriz = []
    for i in range(num_linhas):
        # cria a linha i
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        # adiciona linha à matriz
        matriz.append(linha)

    return matriz
#########################################################################

class Cache(object):

    def __init__(self, tamanho_cache, metodo_mapeamento):
        self.tamanho_cache = tamanho_cache
        self.metodo = metodo_mapeamento  # padronizar com letras minusculas
        self.construirCache()

    def construirCache(self):
        if self.metodo == 'direto' or self.metodo == 'associativo':
            self.matriz = self.tamanho_cache * [0]

        elif self.metodo == 'associativo por conjunto':
            self.matriz = mat_cria(int(self.tamanho_cache / 2), 2, int(0))
        else:
            print('metodo invalido')


class MemoriaPrincipal(object):

    def __init__(self, nome_arquivo):
        self.matriz = self.importa_dados(nome_arquivo)

    def importa_dados(self, nome_arquivo):
        mp = []
        with open(nome_arquivo) as arq:
            for linha in arq:
                if linha.strip() != ' ':
                    linha_spl = linha.split(';')
                    mp.append(linha_spl[0].strip())

        for i in range(len(mp)):
            mp[i] = int(mp[i])

        return mp


class Controlador(object):

    def procura_dados(self, mp, ch, metodo, politica):

        if metodo == 'direto':
            self.procura_dados_metodo_direto(mp, ch)

        elif metodo == 'associativo':
            self.procura_dados_metodo_associativo(mp, ch, politica)

        elif metodo == 'associativo por conjunto':
            self.procura_dados_metodo_associativo_por_conjunto(mp, ch, politica)


    def procura_dados_metodo_direto(self, mp, ch):

        hit = miss = 0

        for i in range(len(mp)):
            tag = int(mp[i] % len(ch))

            if ch[tag] == mp[i]:
                hit += 1
                print(f'\nBloco procurado: {mp[i]}.\nResultado da busca: HIT.')
            else:
                miss += 1
                ch[tag] = mp[i]
                print(f'\nBloco procurado: {mp[i]} \nResultado da busca: MISS. \nPosicao na cache: {tag}')
                print(ch)


        print('\nMiss: %0.2f %%' % (miss * 100 / (miss + hit)))
        print('Hit: %0.2f %%' % (hit * 100 / (miss + hit)))


    def procura_dados_metodo_associativo(self, mp, ch, politica):

        k = 0
        hit = miss = 0

        if politica == 'fifo' or politica == 'lru':
            aux = [None] * int(len(ch))
        elif politica == 'lfu':
            aux = [0] * int(len(ch))

        for i in range(len(mp)):
            var = False

            for j in range(len(ch)):

                if mp[i] == ch[j]:
                    var = True
                    hit += 1
                    print(f'\nBloco procurado: {mp[i]}.\nResultado da busca: HIT.')
                    if politica == 'lru':
                        aux[j] = i
                    elif politica == 'lfu':
                        aux[j] = aux[j] + 1

            if var == False:
                miss += 1

                while k < len(ch) and ch[k] != 0:  # procura lugar vazio na cache

                    k += 1

                if k < len(ch):  # se tiver lugar na linha(tag) da cache...
                    ch[k] = mp[i]
                    if politica == 'fifo':
                        aux[k] = i
                    elif politica == 'lru':
                        aux[k] = i
                    elif politica == 'lfu':
                        aux[k] += 1
                    print(
                        f'\nBloco procurado: {mp[i]} \nResultado da busca: MISS. \nPosicao na cache: {k}.')
                    print(k)
                else:

                    if politica == 'random':
                        indice = randint(0, len(ch) - 1)
                        # print(indice)
                        ch[indice] = mp[i]
                        print(
                            f'\nBloco procurado: {mp[i]} \nResultado da busca: MISS. \nPosicao na cache: {indice}.')
                    else:
                        menor_indice = aux.index(min(aux))
                        if politica == 'fifo':
                            ch[menor_indice] = mp[i]
                            aux[menor_indice] = i
                        elif politica == 'lru':
                            ch[menor_indice] = mp[i]
                            aux[menor_indice] = i
                        elif politica == 'lfu':
                            ch[menor_indice] = mp[i]

                        print(
                            f'\nBloco procurado: {mp[i]} \nResultado da busca: MISS. \nPosicao na cache: {menor_indice}.')

            print(ch)
            if politica != 'random':
                print(aux)

        print('Miss: %0.2f %%' % (miss * 100 / (miss + hit)))
        print('Hit: %0.2f %%' % (hit * 100 / (miss + hit)))

    def procura_dados_metodo_associativo_por_conjunto(self, mp, ch, politica):

        hit = miss = 0

        if politica == 'lru' or politica == 'fifo':
            aux = mat_cria(int(len(ch)), 2, None)
        elif politica == 'lfu':
            aux = mat_cria(int(len(ch)), 2, int(0))

        for i in range(len(mp)):

            kk = 0
            var = False

            tag = int(mp[i] % len(ch))
            # print(tag)

            for jj in range(len(ch[0])):
                if mp[i] == ch[tag][jj]:
                    var = True
                    hit += 1

                    print(f'\nBloco procurado: {mp[i]}.\nResultado da busca: HIT.')
                    if politica == 'lru':
                        aux[tag][jj] = i

                    elif politica == 'lfu':
                        aux[tag][jj] = aux[tag][jj] + 1



            if var == False:  # nao foi encontrada na cache
                miss += 1

                while kk < len(ch[0]) and ch[tag][kk] != 0:  # procura lugar vazio na cache
                    kk += 1

                if kk < len(ch[0]):  # se tiver lugar na linha(tag) da cache...

                    ch[tag][kk] = mp[i]
                    if politica == 'fifo':
                        aux[tag][kk] = i
                    elif politica == 'lru':
                        aux[tag][kk] = i
                    elif politica == 'lfu':
                        aux[tag][kk] += 1
                    print(
                        f'\nBloco procurado: {mp[i]} \nResultado da busca: MISS. \nPosicao na cache: tag = {tag}, coluna = {kk}.')

                else:

                    if politica == 'random':
                        indice = randint(0, len(ch[0]) - 1)
                        # print(indice)
                        ch[tag][indice] = mp[i]
                        print(
                            f'\nBloco procurado: {mp[ii]} \nResultado da busca: MISS. \nPosicao na cache: tag = {tag}, coluna = {indice}.')
                    else:
                        menor_indice = (aux[tag]).index(min(aux[tag]))
                        if politica == 'fifo':
                            ch[tag][menor_indice] = mp[i]
                            aux[tag][menor_indice] = i
                        elif politica == 'lru':
                            ch[tag][menor_indice] = mp[i]
                            aux[tag][menor_indice] = i
                        elif politica == 'lfu':
                            ch[tag][menor_indice] = mp[i]
                        print(
                            f'\nBloco procurado: {mp[i]} \nResultado da busca: MISS. \nPosicao na cache: tag = {tag}, coluna = {menor_indice}.')

            print(ch)
            if politica != 'random':
                print(aux)

        print('\nMiss: %0.2f %%' % (miss * 100 / (miss + hit)))
        print('Hit: %0.2f %%' % (hit * 100 / (miss + hit)))










