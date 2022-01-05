email = input('digite seu e-mail para que eu retorne seu servidor: ')

#descobrindo o servidor do email
tam = len(email)
i=0
for i in range (0,tam):
    if email[i] == '@':
        cont = i;

print('o servidor do email é: {}'.format(email[cont:]))
 

