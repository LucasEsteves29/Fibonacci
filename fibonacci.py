# fibonacci
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# numero negativo: exception
# 0: nao imprimir
# Somar -1 e -2 da lista

def fibonacci(num):

    if num == 0:
        return []
    
    if num < 0:
        raise ValueError('Numbers below zero are not allowed.')
    
    prev = 0
    curr = 1
    res = []

    for i in range(num):
        curr, prev = curr + prev, curr
        res.append(curr) 

    return res

try:
    
    v = fibonacci(-2)
    print(v)

except ValueError as e:
    print(f'Erro: {e}')
        
        
    





    

    
