'''
Receba o salário de um colaborador e o reajuste seguido o seguinte critério:

    - até 890,00 - 20%
    - entre 891 e 1000 - 15%
    - entre 1000 e 1500 - 10 %
    - acima de 1500 - 5%

informar:

    - salário antes.
    - percentual de aumento aplicado.
    - valor do aumento.
    - novo salário.
'''

salary = float(input('Salário atual: R$ '))
salary_before = salary
percent = 0

if salary <= 890:
    salary *= 1.2
    percent = 20
elif 890 < salary <= 1000:
    salary *= 1.15
    percent = 15
elif 1000 < salary <= 1500:
    salary *= 1.1
    percent = 10
elif salary > 1500:
    salary *= 1.05
    percent = 5

print('-' * 40)
print(f'Salário atual: \t\t\tR${salary_before:.2f}.'
      f'\nPercentual de almento: \t{percent}%.'
      f'\nValor do aumento: \t\tR$ {salary - salary_before:.2f}.'
      f'\nSalário reajustado: \tR$ {salary:.2f}.')
