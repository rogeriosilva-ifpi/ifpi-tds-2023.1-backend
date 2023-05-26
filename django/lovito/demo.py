def soma(a, b, *args, **kwargs):

    print(type(kwargs))
    print(kwargs)

    arq = kwargs['arquivo']

    s = 0
    for item in args:
        s += item
    return a + b + s


resultado = soma(4, 8, 6, negativo=False, arquivo='r.txt')
print(resultado)
