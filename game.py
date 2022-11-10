from Models.calcular import Calcular

def main() -> None:
     pontos:int = 0
     jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input("Informe o nivel de dificuldade desejado\n[1, 2, 3 ou 4]:\n"))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação:\n')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if(calc.checar_resultado(resultado)):
        pontos+=1
        print(f'Você tem {pontos} pontos(s)!')

    continuar: int = int(input('Deseja continuar no jogo? [1 -sim, 0 - não]\n'))

    if continuar:
        jogar(pontos)

    else:
        print(f'Você finalizou com {pontos} ponto(s)')
        print('Obrigado!')



if __name__ == '__main__':
    main()