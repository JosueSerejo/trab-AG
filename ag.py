import random

def executar(modulo, pop_size=100, geracoes=100, taxa_mut=0.2):
    conf = modulo.obter_config()
    nfe = 0
    pop = []

    # 1. Inicialização (Criação da População Inicial)
    for _ in range(pop_size):
        c = [random.uniform(conf["dom"][0], conf["dom"][1]) for _ in range(2)]
        fit = modulo.calcular(c)
        pop.append([c[0], c[1], fit])
        nfe += 1

    # 2. Ciclo Evolutivo
    for g in range(geracoes):
        # Ordena pelo fitness (índice 2) - Menor valor é o melhor
        pop.sort(key=lambda ind: ind[2])
        
        # Parada antecipada se atingir o objetivo
        if abs(pop[0][2] - conf["ideal"]) <= 0.001: 
            break

        # Elitismo: O melhor da geração atual passa direto para a próxima
        nova_pop = [list(pop[0])] 

        while len(nova_pop) < pop_size:
            # Seleção por Torneio
            p1, p2 = random.sample(pop, 3), random.sample(pop, 3)
            pai1, pai2 = min(p1, key=lambda x: x[2]), min(p2, key=lambda x: x[2])
            
            # Crossover
            filho = [(pai1[0] + pai2[0])/2, (pai1[1] + pai2[1])/2]

            # Mutação e Clipping (Garante que não saia do domínio)
            for i in range(2):
                if random.random() < taxa_mut:
                    filho[i] += random.uniform(-0.1, 0.1)
                filho[i] = max(min(filho[i], conf["dom"][1]), conf["dom"][0])

            # Avaliação do novo filho
            fit_f = modulo.calcular(filho)
            nova_pop.append([filho[0], filho[1], fit_f])
            nfe += 1
        
        # A nova geração substitui a antiga
        pop = nova_pop

    # 3. Resultados Finais
    pop.sort(key=lambda ind: ind[2])
    melhor_fitness = pop[0][2]
    sucesso = 1 if abs(melhor_fitness - conf["ideal"]) <= 0.001 else 0
    
    return nfe, sucesso, melhor_fitness