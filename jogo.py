pontos = 0
perguntas = [
    [
        'Pergunta 1:\nSelecione a alternativa correta que corresponde a uma função de entrada de dados no python:',
        [
            'alterantiva A - While()',
            'alterantiva B - Input()',
            'alterantiva C - Print()',
            'alternativa D - If()',
            'alternativa E - Case()'
        ],
        'B'
    ],
    [
        'Pergunta 2:\nSelecione a alternativa incorreta:',
        [
            'alterantiva A - "For()" é uma estrutura de repetição',
            'alterantiva B - "Input()" é uma função de entrada de dados',
            'alterantiva C - "If/Else" é uma estrutura de repetição',
            'alternativa D - "x += 5" é igual a: x = x + 5',
            'alternativa E - "Case()" é uma estrutura condicional'
        ],
        'C'
    ],
    [
        'Pergunta 3:\nUma lista, por padrão, começa pelo Array de numero:',
        [
            'alterantiva A - Todas alternativas estão incorretas!',
            'alterantiva B - "-1"',
            'alterantiva C - "10"',
            'alternativa D - "5"',
            'alternativa E - "0"'
        ],
        'E'
    ],
]

i = 0
while i < len(perguntas):
    print(f'{perguntas[i][0]}')
    print()
    print("Alternativas: ")

    x = 0
    while x < len(perguntas[i][1]):
        print(f'\t{perguntas[i][1][x]}')
        x += 1

    print()
    respostaCerta = perguntas[i][2]
    resposta = input("Digite a alternativa correta: ")
    if resposta.upper() == respostaCerta:
        pontos += 35
        print(f"Parabéns, alternativa certa! Você está com {pontos} pontos.")
        
    else:
        print("Alternativa incorreta")
    print("----------------------------------------------")
    i += 1

if pontos > 70:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado.")