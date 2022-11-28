A = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'] # lista primaria para
B = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7'] # visualizar as opções
C = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'] #

print('A  B  C') # inicio do menu
print('       ')

for i in range(7): # Loop de 7 vesez para mostrar as opções na tela
    print(A[i] + ' ' + B[i] + ' ' + C[i]) # print 7x na tela
print('       ')
print('--------------------------------')
nun1 = input(' Digite a coluna 1° pergunta: ')  # 1° pergunta
print('--------------------------------')
print('       ')

if nun1 == 'A':     # If para escolha selecionar a opção desejada
    LI = B + A + C  # se optar pela coluna A LI recebe novos dados
                    # com a coluna B em Primeiro A em segundo C por ultimo
if nun1 == 'B':
    LI = A + B + C

if nun1 == 'C':
    LI = A + C + B

A = [] # Limpa a variável A
B = [] # Limpa a variável B
C = [] # Limpa a variável C

print('A  B  C')
print('       ')

for i in range(1):
    A.append(LI[0])
    B.append(LI[1])
    C.append(LI[2])
    A.append(LI[3])
    B.append(LI[4])
    C.append(LI[5])
    A.append(LI[6])
    B.append(LI[7])
    C.append(LI[8])
    A.append(LI[9])
    B.append(LI[10])
    C.append(LI[11])
    A.append(LI[12])
    B.append(LI[13])
    C.append(LI[14])
    A.append(LI[15])
    B.append(LI[16])
    C.append(LI[17])
    A.append(LI[18])
    B.append(LI[19])
    C.append(LI[20])

# print(A)
# print(B)
# print(C)

for i in range(7):
    print(A[i] + ' ' + B[i] + ' ' + C[i])
print('       ')
print('--------------------------------')
nun1 = input('Digite a coluna 1° pergunta: ')  # 1° pergunta
print('--------------------------------')
if nun1 == 'A':
    LI = B + A + C

if nun1 == 'B':
    LI = A + B + C

if nun1 == 'C':
    LI = A + C + B

A = []
B = []
C = []

print('A  B  C')
print('       ')

for i in range(1):
    A.append(LI[0])
    B.append(LI[1])
    C.append(LI[2])
    A.append(LI[3])
    B.append(LI[4])
    C.append(LI[5])
    A.append(LI[6])
    B.append(LI[7])
    C.append(LI[8])
    A.append(LI[9])
    B.append(LI[10])
    C.append(LI[11])
    A.append(LI[12])
    B.append(LI[13])
    C.append(LI[14])
    A.append(LI[15])
    B.append(LI[16])
    C.append(LI[17])
    A.append(LI[18])
    B.append(LI[19])
    C.append(LI[20])

# print(A)
# print(B)
# print(C)

for i in range(7):
    print(A[i] + ' ' + B[i] + ' ' + C[i])
print('       ')
print('--------------------------------')
nun1 = input('Digite a coluna 1° pergunta: ')  # 1° pergunta
print('--------------------------------')
if nun1 == 'A':
    LI = B + A + C

if nun1 == 'B':
    LI = A + B + C

if nun1 == 'C':
    LI = A + C + B

A = []
B = []
C = []

for i in range(1):
    A.append(LI[0])
    B.append(LI[1])
    C.append(LI[2])
    A.append(LI[3])
    B.append(LI[4])
    C.append(LI[5])
    A.append(LI[6])
    B.append(LI[7])
    C.append(LI[8])
    A.append(LI[9])
    B.append(LI[10])
    C.append(LI[11])
    A.append(LI[12])
    B.append(LI[13])
    C.append(LI[14])
    A.append(LI[15])
    B.append(LI[16])
    C.append(LI[17])
    A.append(LI[18])
    B.append(LI[19])
    C.append(LI[20])

# print(A)
# print(B)
# print(C)
# print('       ') se deixar da errado na b6 e c6 incrival perguntar para Willian
print('A escolha foi : ',LI[10])
# print('       ') se deixar da errado na b6 e c6 incrival perguntar para Willian