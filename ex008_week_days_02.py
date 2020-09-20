day = int(input('Dia da semana: '))
if day == 1:
    print('Domingo.')
elif day == 2:          # o ELIF é interligado ao IF, dessa forma, o programa passa por todos os ELIFS antes de chegar
    print('Segunda.')   # no ELSE. ao fazer as verificações e encontar uma condição "True" ele pula as demais verigficações.
elif day == 3:
    print('Terça.')
elif day == 4:
    print('Quarta.')
elif day == 5:
    print('Quinta.')
elif day == 6:
    print('Sexta.')
elif day == 7:
    print('Sábado')
else:
    print('Valor inválido!')