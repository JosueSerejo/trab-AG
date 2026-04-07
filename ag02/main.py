import fun_ap as AP
import ag

def realizar_testes(modulo):
    conf = modulo.obter_config()
    total_nfe, total_sucesso = 0, 0
    execucoes = 100
    
    print(f"Executando AG para: {conf['nome']}")
    
    for _ in range(execucoes):
        nfe, suc, fit = ag.executar(modulo)
        total_nfe += nfe
        total_sucesso += suc
        ultimo_fit = fit
        
    print(f"Média NFE: {total_nfe / execucoes:.0f}")
    print(f"Taxa de Sucesso: {total_sucesso}%")
    print(f"Último Fitness: {ultimo_fit:.6f}")

realizar_testes(AP)