import climage 
import random
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
# converts the image to print in terminal 
#form of ANSI Escape codes 
print(colored(255,0,0,R'           //─────────────\            '))
print(colored(255,0,0,R'         ///               \\\\        '))
print(colored(255,0,0,R'      ////        ┌─┐         \\       '))
print(colored(255,0,0,R'     //           │┼│          \\      '))
print(colored(255,0,0,R'    //            │┼│            \\    '))
print(colored(255,0,0,R'   //             │┼│              \\  '))
print(colored(255,0,0,R' ///              │┼│                \\'))
print(colored(255,0,0,R" /               ─┴┼┴─               \\"))
print(colored(255,0,0,R'│        ;##     xx│xx     ##;        │'))
print(colored(255,0,0,R'│        ;####xxxx   xxxx####;        │'))
print(colored(255,0,0,R'│          ###x         x###          │'))
print(colored(255,0,0,R'│             │         │             │'))
print(colored(255,0,0,R'│             │ │     │ │             │'))
print(colored(255,0,0,R'│             │ └─   ─┘ │             │'))
print(colored(255,0,0,R'\\           ##┼       ┼##           / '))
print(colored(255,0,0,R' \\         ####│ ┌─┐ │####         // '))
print(colored(255,0,0,R'   \\      ##   │ │┼│ │   ##      ///  '))
print(colored(255,0,0,R'    \\    ##    └─┴┴┴─┘    ##    //    '))
print(colored(255,0,0,R'     \\\           ▼            //     '))
print(colored(255,0,0,R'       \\                     ///      '))
print(colored(255,0,0,R'        \\\                 ///        '))
print(colored(255,0,0,R'          \\\───────────── //          '))

#prints output on console. 
print("Bem-Vindo ao simulador Tropa De Elite")
tropas = 10
fundos = 0
veiculos_terrestres = 0
veiculos_aereos = 0
odiopopular = 0
complexos_restantes = 7
suspeitos_em_custodia = 0
poder_das_frentes = [0, 3, 3, 3]
informações = 0
treinamento = 1
progresso = 0
defesa = 1
ataque = 1
tatica = 20
print("Seu Objetivo é Achar e Destruir a Operação do Baiano")
print("Para alcançar o Baiano é necessário executar operações nas três frentes de entrada")
print("Quanto mais operações forem feitas nas frentes, mais ódio popular será gerado e")
print("mais pessoas se unirão ao tráfico")
print("Progresso concede infantaria, os alicerces de uma operação bem sucedida")
print("Progresso também concede veiculos aéreos e terrestres, quando empregados esses podem")
print("proporcionar grande auxílio à infantaria")
print("Tropas com conhecimento tático podem capturar suspeitos mais facilmente ao invés de meramente assasiná-los")
print("Informações são obtidas através de interrogatórios executados em suspeitos obtidos em operações")
print("informações podem ser gastas para conhecer melhor as forças em frentes específicas")
print("Treinamento multiplica o dano das suas tropas, concede conhecimento tático, e aumenta sua resistência")
print("Porém consome dois terços dos soldados à disposição")
while True:
    print("Digite 'progresso' para Verificar o progresso da operação")
    print("Digite 'avaliartropas' para entender suas tropas e equipamentos")
    print("Digite 'conduziroperação' para subir o morro")
    print("Digite 'treinar' para treinar suas tropas")
    print("Digite 'recrutamento' para conseguir tropas e equipamento")
    print("Digite 'interrogar' para interrogar suspeitos")
    if complexos_restantes == 0:
        print(colored(255, 0, 0, "Digite 'baiano' para invadir e executar o Baiano e garantir o sono do papa"))
    inp = input("")
    match inp:
        case "progresso":
            print(f"faltam ainda {complexos_restantes} subidas no morro para alcançar o baiano")
            print(f"{odiopopular} ódio ao BOPE na população")
            print(f"conduza uma operação para conseguir um destacamento de equipamento")
        case "avaliartropas":
            print(f"Treinamento Do Bope: {treinamento}")
            print(f"Tropas: {tropas}")
            print(f"Cada soldado tem {ataque} pontos de ataque")
            print(f"Cada soldado tem {defesa} pontos de defesa")
            print(f"Cada soldado tem %{tatica} de tática (chance de capturar inimigo vivo)")
            print(f"Veículos Aéreos: {veiculos_aereos}")
            print(f"Veículos Terrestres: {veiculos_terrestres}")
        case "conduziroperação":
            print("TODO")
        case "treinar":
            tatica += 5
            tropas -= tropas // 1.5
            treinamento += 1
        case "recrutamento":
            for i in range(progresso):
                da = random.randint(1,4)
                if da == 1:
                    tropas += 5
                    print(f'5 novatos se juntaram ao batalhão')
                if da == 2:
                    veiculos_terrestres += 1
                    print(f'o batalhão ganhou um blindado novo')
                if da == 2:
                    veiculos_aereos += 1
                    print(f'o batalhão ganhou um helicóptero novo')
            progresso = 0
        case "interrogar":
            print("TODO")


