texto = 'victor'
email = "victor@gmail.com"

print(texto[0]) #= v
print('tamanho do texto: {}'.format(len(texto)))
print('tamanho do email: {}'.format(len(email)))
print('ultima letra do email: {}'.format(email[-1]))
print('ultima letra do email: {}'.format(email[-2]))
print('ultima letra do email: {}'.format(email[-3]))
print('ultima letra do email: {}'.format(email[-4]))
print('ultima letra do email: {}'.format(email[-5]))

#descobrindo o servidor do email
tam = len(email)
i=0
for i in range (0,tam):
    if email[i] == '@':
        cont = i;

print('o servidor do email é: {}'.format(email[cont:]))
 
