import fun_ap
import fun_cb3
import ag

def realizar_testes(modulo):
    conf = modulo.obter_config()
    total_nfe, total_sucesso = 0, 0
    ultimo_fit = 0
    execucoes = 100
    
    print(f"Rodando {execucoes} vezes para: {conf['nome']}...")
    
    for _ in range(execucoes):
        nfe, suc, fit = ag.executar(modulo)
        total_nfe += nfe
        total_sucesso += suc
        ultimo_fit = fit
        
    print(f"Média de NFE: {total_nfe / execucoes:.0f}")
    print(f"Taxa de Sucesso (SR): {total_sucesso}%")
    print(f"Melhor fitness da última rodada: {ultimo_fit:.6f}\n")

realizar_testes(fun_ap)
realizar_testes(fun_cb3)