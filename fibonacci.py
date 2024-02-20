
def fibonacci(num):

    if num == 0:
        return []
    
    if num < 0:
        raise ValueError('Numbers below zero are not allowed.')
    
    prev = 0    # PREVIOUS
    curr = 1    # CURRENT
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
