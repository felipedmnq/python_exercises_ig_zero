users = open('users.txt', 'r')
report = open('report.txt', 'w')


def extract_bytes(file = ''):
    file_open = open(f'{file}', 'r')
    extract = file_open.readlines()
    extracted = []
    for c in range(6):
        extracted.append(int(extract[c][15:]))
    return extracted


extracted = extract_bytes(file = 'users.txt')
extracted_sum = sum(extracted)

extract = users.readlines()
print()

def report_generator():
    for c in range(6):
        print(f'{c + 1:<4}\t{extract[c][:15]:<15}{(extracted[c]) / (1024 ** 2):>15.2f} MB'
              f'\t\t\t{(extracted[c] * 100) / extracted_sum:>5.2f}%')

print(detail)


def main():
    detail = ('-' * 60)
    print(detail)
    print(f'{"ACME Inc.  - Uso do espaço em disco por usuário.":^60}')
    print(detail)
    print(f'{"No.":<4}\t{"Usuário":<15}\t\t{"Espaço utilizado":^15}\t\t{"% Uso":>}')

    report_generator()


main()