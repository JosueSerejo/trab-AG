import random

def executar(modulo, tamanho_pop=80, geracoes=100, taxa_mut=0.3):
    conf = modulo.obter_config()
    limites = conf["dom"]
    alvo_real = conf["ideal"]

    nfe = 0
    populacao = []

    def criar_individuo(genes, fitness):
        x, y = genes
        return [x, y, fitness]

    def gerar_genes():
        return [random.uniform(limites[0], limites[1]) for _ in range(2)]

    def selecionar_torneio(pop):
        grupo1 = random.sample(pop, 5)
        grupo2 = random.sample(pop, 5)
        pai1 = min(grupo1, key=lambda x: x[2])
        pai2 = min(grupo2, key=lambda x: x[2])
        return pai1, pai2

    def crossover(pai1, pai2):
        x = (pai1[0] + pai2[0]) / 2
        y = (pai1[1] + pai2[1]) / 2
        return [x, y]

    def mutacao_clipping(filho, taxa_mut, limites):
        for i in range(len(filho)):
            if random.random() < taxa_mut:
                filho[i] += random.uniform(-0.1, 0.1)
            filho[i] = max(min(filho[i], limites[1]), limites[0])
        return filho

    for _ in range(tamanho_pop):
        genes = gerar_genes()
        fit = modulo.calcular(genes)
        populacao.append(criar_individuo(genes, fit))
        nfe += 1

    for _ in range(geracoes):
        populacao.sort(key=lambda ind: ind[2])

        if abs(populacao[0][2] - alvo_real) <= 0.001:
            break

        nova_pop = [list(populacao[0])]

        while len(nova_pop) < tamanho_pop:
            pai1, pai2 = selecionar_torneio(populacao)
            filho = crossover(pai1, pai2)
            filho = mutacao_clipping(filho, taxa_mut, limites)

            fit_f = modulo.calcular(filho)
            nova_pop.append(criar_individuo(filho, fit_f))
            nfe += 1

        populacao = nova_pop

    populacao.sort(key=lambda ind: ind[2])
    
    distancia_final = abs(populacao[0][2] - alvo_real)
    sucesso = 1 if distancia_final <= 0.001 else 0

    return nfe, sucesso, populacao[0][2]