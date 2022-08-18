perguntas = [
    [
        'pergunta 1',
        [
            'alterantiva A',
            'alterantiva B',
            'alterantiva C',
            'alternativa D',
            'alternativa E'
        ],
        'B'
    ],
    [
        'pergunta 2',
        [
            'alterantiva A',
            'alterantiva B',
            'alterantiva C',
            'alternativa D',
            'alternativa E'
        ],
        'C'
    ],
    [
        'pergunta 3',
        [
            'alterantiva A',
            'alterantiva B',
            'alterantiva C',
            'alternativa D',
            'alternativa E'
        ],
        'E'
    ],
]

i = 0
while i < len(perguntas):
    print(f'Pergunta: {perguntas[i][0]}')
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
        print("Parabéns, aleternativa certa")
    else:
        print("Alternativa incorreta")
    print("----------------------------------------------")
    i += 1