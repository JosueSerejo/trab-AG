# Camel Back 3 (CB3)
# f(x) = 2*x1^2 - 1.05*x1^4 + (1/6)*x1^6 + x1*x2 + x2^2

def obter_config():
    return {"nome": "CB3", 
            "dom": [-5, 5], 
            "ideal": 0.0}

def calcular(c):
    return 2*c[0]**2 - 1.05*c[0]**4 + (1/6)*c[0]**6 + c[0]*c[1] + c[1]**2