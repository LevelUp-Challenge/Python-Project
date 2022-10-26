#Para o melhor aproveitamento do código, por favor, execute usando a tela inteira.
#RM 95694, 9
#Link do video: https://drive.google.com/file/d/1GbUg6PIjmNr9zuDGfrhtqnodC0bxpMu0/view?usp=sharing

def info():
    choose = "N"
    while choose.upper() != "S":
        nome = str(input("Digite seu nome: "))
        sobrenome = str(input("Digite seu sobrenome: "))
        idade = int(input("Digite aqui sua idade: "))
        #utilização das tuplas
        dic_info = dict([('nm', nome), ('sbnm', sobrenome), ('idd', idade)])
        def funcao(**kwargs):
            print("Confira se as informações abaixo estão corretas sendo a sequencia: nome/sobrenome/idade \n")
            for chave in kwargs:
                print(f"{kwargs.get(chave)}")
        funcao(**dic_info)
        choose = str(input("Estão corretas? S/N \nDigite aqui: "))    

def tabela():
    opcao = ''
    escolha = "S"
    opcao = str(input('Você deseja visualizar a descrição da vaga? (S/N) \nR: '))
    print('*------ MENU LEVEL UP EXPERIENCE ------*')
    if opcao.upper() == 'S':
        while escolha.upper() == 'S':
            menu = str(input("----------\nAbaixo estarão as descrições da vaga.\nQuais delas deseja ter acesso? \n----------\n(1) Sobre a empresa \n(2) O que estamos procurando? \n(3) Outras vagas disponiveis \n(4) Requisitos da vaga \n(5) Beneficios \n(6) Salario \n(7) Responsabilidades \n(8) Iniciar game! \n----------\nDigite aqui o número: "))

            if menu == '1':
                print('----------\nSoftCash! Somos uma empresa de tecnologia focada em otimizar toda a jornada de crédito, compra e venda de imóveis. Nossa plataforma digital está revolucionando o mercado, através de dados e tecnologia. E agora, estamos aumentando o nosso time!')
            elif menu == '2':
                print('----------\nO que procuramos:\n Procuramos estudantes na área de tecnologia, que sejam apaixonados por programar e desenvolver sistemas.')
            elif menu == '3':
                print('----------\nOutras vagas:\n - Desenvolvedora / Desenvolvedor Júnior de Frontend para Bootcamp de Tecnologia \n- Desenvolvedor Full Stack Pleno')
            elif menu == '4':
                print('----------\nRequisitos da vaga:\n - Estar cursando do a partir do 3º semestre em qualquer Graduação na Área de Tecnologia da Informação, no período noturno \n- Interesse em aprendizado de técnicas de desenvolvimento Web e Visão Computacional.')
            elif menu == '5':
                print('----------\nBenefício: Cartão flexível Flash')
            elif menu == '6':
                print('----------\nSalario:\n Bolsa auxílio: 2.250,00')
            elif menu == '7':
                print('----------\nResponsabilidades exigidas pela vaga: \n- Auxiliar nas atividades de análise de sistemas de informação, desenvolvimento, manutenção dos aplicativos, documentação e apoio à usuários de serviços de informática; \n- Fornecer assistência para organização de conteúdos e rotinas dos projetos envolvendo sistemas, e aplicativos, das plataformas e atividades voltadas para a área de educação; \n- Apoiar a capacitação da equipe em ferramentas de TI Monitorar preventivamente servidores com aplicações de banco de dados.')
            elif menu == '8':
                print('----------\nCerto! Agora vamos para o game.')
                break
            else:
                print('----------\nPerdão, não entendi. Escolha um dos números acima!')

            escolha = input('----------\nVocê deseja ver mais alguma outra opção? (S/N)\nR: ')

        print("\nAbaixo será exibido 5 questões, leia com atenção! Boa sorte.")
        print("----------")
    else:
        print('----------\nTudo bem! Então vamos para o game.')
        print("\nAbaixo será exibido 5 questões, leia com atenção! Boa sorte.")
        print("----------")


def primeiroTeste():
    teste1 = [
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
    ]
    ]

    return teste1

def validaRespostaT1(teste1):
    pontosT1 = 0
    i = 0
    while i < len(teste1):
        print(f'{teste1[i][0]}')
        print()
        print("Alternativas: ")

        x = 0
        while x < len(teste1[i][1]):
            print(f'\t{teste1[i][1][x]}')
            x += 1

        print()
        respostaCerta = teste1[i][2]
        resposta = input("Digite aqui sua resposta: ")
        if resposta.upper() == respostaCerta:
            print("Parabéns, alternativa certa")
            pontosT1 +=10
            print(f'Você está com {pontosT1} pontos!')
        else:
            print("Alternativa incorreta")
        print("----------------------------------------------")
        i += 1

    if pontosT1 >= 20:
        print(f'Parabens você foi aprovado com {pontosT1} pontos!')
    else:
        print(f'Você foi reprovado com {pontosT1} pontos, sinto muito por isso! Para ser aprovado precisa abater 70 pontos.')

    return pontosT1

def segundoTeste():
    teste2 = [
        [         
            'Pergunta 1:\nEntre os operadores abaixo, qual deles tem a maior ordem de precedência?',
            [             
                'Alternativa A - "*"',             
                'Alternativa B - "/"',             
                'Alternativa C - "+"',             
                'Alternativa D - "-"',             
                'Alternativa E - "x"'         
            ],         
            'A'     
        ],     
        [         
            'Pergunta 2:\nO que é o HTML?',         
            [             
                'Alternativa A - Uma linguagem de programação',             
                'Alternativa B - Um framework',             
                'Alternativa C - Um banco de dados',             
                'Alternativa D - Uma linguagem de formatação',             
                'Alternativa E - Nenhuma das alternativas',                   
                ],         
            'D'     
        ],
        [
            'Pergunta 3:\nQual os valores de um dado Booleano?',
            [
                'Alternativa A - P E N',
                'Alternativa B - Numeros inteiros',
                'Alternativa C - Numeros reais',
                'Alternativa D - Qualquer tipo de texto',
                'Alternativa E - True e False'
            ],
            'E'
        ]
        ]

    return teste2

def validaRespostaT2(teste2):
    pontosT2 = 0
    i = 0
    while i < len(teste2):
        print(f'{teste2[i][0]}')
        print()
        print("Alternativas: ")

        x = 0
        while x < len(teste2[i][1]):
            print(f'\t{teste2[i][1][x]}')
            x += 1

        print()
        respostaCerta = teste2[i][2]
        resposta = input("Digite aqui sua resposta: ")
        if resposta.upper() == respostaCerta:
            print("Parabéns, alternativa certa")
            pontosT2 +=10
            print(f'Você está com {pontosT2} pontos!')
        else:
            print("Alternativa incorreta")
        print("----------------------------------------------")
        i += 1

    if pontosT2 >= 20:
        print(f'Parabens você foi aprovado com {pontosT2} pontos!')
    else:
        print(f'Você foi reprovado com {pontosT2} pontos, sinto muito por isso! Para ser aprovado precisa abater 70 pontos.')

    return pontosT2

def terceiroTeste():
    teste3 = [
        [         
            'Pergunta 1:\nOnde as variáveis ficam armazenadas?',
            [             
                'Alternativa A - "No programa/software"',             
                'Alternativa B - "No banco de dados"',             
                'Alternativa C - "Na memoria RAM do computador"',             
                'Alternativa D - "Elas não ficam armazenadas"',             
                'Alternativa E - "No software, banco de dados e na memoria RAM"'         
            ],         
            'C'     
        ],     
        [         
            'Pergunta 2:\nO que é a sigla MVC em Java?',         
            [             
                'Alternativa A - Model, View e Controller',             
                'Alternativa B - Mark, Void e Command',             
                'Alternativa C - Mandatory, Value e Center',             
                'Alternativa D - Model, View e Command',             
                'Alternativa E - Todas estão incorretas!',                   
                ],         
            'A'     
        ],
        [
            'Pergunta 3:\nComo se chama o comando para inserir dados dentro de um SQL?',
            [
                'Alternativa A - Create table',
                'Alternativa B - Insert into',
                'Alternativa C - Commit',
                'Alternativa D - Insert Value',
                'Alternativa E - Nenhuma das alternativas'
            ],
            'B'
        ]
        ]

    return teste3

def validaRespostaT3(teste3):
    pontosT3 = 0
    i = 0
    while i < len(teste3):
        print(f'{teste3[i][0]}')
        print()
        print("Alternativas: ")

        x = 0
        while x < len(teste3[i][1]):
            print(f'\t{teste3[i][1][x]}')
            x += 1

        print()
        respostaCerta = teste3[i][2]
        resposta = input("Digite aqui sua resposta: ")
        if resposta.upper() == respostaCerta:
            print("Parabéns, alternativa certa")
            pontosT3 +=10
            print(f'Você está com {pontosT3} pontos!')
        else:
            print("Alternativa incorreta")
        print("\n----------------------------------------------\n")
        i += 1

    if pontosT3 >= 20:
        print(f'Parabens você foi aprovado com {pontosT3} pontos!')
        print("\n----------------------------------------------\n")

    else:
        print(f'Você foi reprovado com {pontosT3} pontos, sinto muito por isso! Para ser aprovado precisa abater 20 pontos.')
        print("\n----------------------------------------------\n")
        
    return pontosT3

def armazena_pontos(pontosT1, pontosT2, pontosT3):
    totalPontos = {"Pontos no 1º Teste" : pontosT1, "Pontos no 2º Teste" : pontosT2, "Pontos no 3º Teste" : pontosT3}

    return totalPontos

def mostraPontos(totalPontos):
    for k, v in totalPontos.items():
        print(f"O total de {k} foi {v} \n")  

def principal():
    info()
    tabela()
    teste1 = primeiroTeste()
    pontosT1 =validaRespostaT1(teste1)
    teste2 = segundoTeste()
    pontosT2 = validaRespostaT2(teste2)
    teste3 = terceiroTeste()
    pontosT3 = validaRespostaT3(teste3)
    totalPontos = armazena_pontos(pontosT1, pontosT2, pontosT3)
    mostraPontos(totalPontos)

principal()