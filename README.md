# Algoritmos Genéticos

Este repositório contém a implementação de dois Algoritmos Genéticos (AG) desenvolvidos em **Python** para encontrar o mínimo global de funções matemáticas complexas. O projeto foca na comparação de desempenho entre as funções **Camel Back 3 (CB3)** e **Aluffi-Pentini (AP)**.

**Disciplina:** Fundamentos de Inteligência Artificial  
**Docente:** Dario Brito Calçada  
**Discente:** Willamy Josué Santos Serejo

## Estrutura do Projeto

O projeto adota uma arquitetura modular, separando a lógica do motor evolutivo das definições matemáticas de cada problema:

* `ag.py`: Contém a função `executar`, responsável pelo ciclo evolutivo (Seleção, Crossover, Mutação e Elitismo).
* `fun_cb3.py`: Módulo de configuração para a função Camel Back 3.
* `fun_ap.py`: Módulo de configuração para a função Aluffi-Pentini.
* `main.py`: Script principal que gerencia as 100 execuções de teste e consolida as métricas de desempenho.

## Especificações Técnicas

Os algoritmos utilizam as seguintes estratégias de computação evolutiva:

1.  **Seleção por Torneio:** Escolha dos pais baseada na disputa entre indivíduos aleatórios (Tamanho 3 para CB3 e 5 para AP).
2.  **Crossover Aritmético:** Geração de descendentes através da média aritmética exata dos genes dos pais.
3.  **Mutação e Clipping:** Aplicação de ruído aleatório ($\pm 0.1$) com trava de segurança para garantir que os indivíduos permaneçam dentro do domínio definido.
4.  **Elitismo:** Preservação obrigatória do melhor indivíduo de cada geração para a seguinte.
5.  **Critério de Parada:** Baseado na distância absoluta ($abs$) entre o fitness alcançado e o valor ideal esperado, com tolerância de $0.001$.

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/JosueSerejo/trab-AG.git]
2.  **Navegue até a pasta:**
    ```bash
    cd seu-repositorio
    ```
3.  **Inicie os testes:**
    ```bash
    python main.py
    ```

---