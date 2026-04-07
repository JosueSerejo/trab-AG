# Aluffi-Pentini (AP)
# f(x) = 0.25*x1^4 - 0.5*x1^2 + 0.1*x1 + 0.5*x2^2

def obter_config():
    return {"nome": "AP", 
            "dom": [-10, 10], 
            "ideal": -0.3523}

def calcular(c):
    return 0.25*c[0]**4 - 0.5*c[0]**2 + 0.1*c[0] + 0.5*c[1]**2