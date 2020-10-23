'''
file = open('helloNewFile.txt', 'w')

file.write('Felipe esta escrevendo seu primeiro arquivo em python')
file.write('\nFunciona mesmo\n')
file.writelines(['Ola', 'aquivo', 'do', 'Felipe'])
'''

'''
file = open('helloNewFile.txt', 'r')
#print(file.read())

#print(file.readline())

print(file.readlines())
'''

file = open('helloNewFile.txt', 'a')
file.write('\nNova Linha')
file.close()


