totmaior = 0
totmenor = 0
for peso in range(1,6):
    pessoas = float(input('Qual o peso da {} pessoa?...').format('peso'))
    if peso == 1:
        totmaior = pessoas
        totmenor = pessoas
    else:
        if pessoas > totmaior:
            totmaior = pessoas
        if peso < totmenor:
            totmenor = pessoas
print('O maior peso lido foi de {}kg'.format(totmaior))
print('O menor peso lido foi de {}kg'.format(totmenor))
