import os #importando bibloteca do python

restaurantes = [ "Bolo na Mesa", "Docinho delicia"]

def exibir_nome_do_programa():
    print(""""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)
#para pegar essas fontes eu fui no navegador em https://fsymbols.com/letters/ 

def exibir_opcoes():

    print("""
        1. 𝒞𝒶𝒹𝒶𝓈𝓉𝓇𝒶𝓇 ℛℯ𝓈𝓉𝒶𝓊𝓇𝒶𝓃𝓉ℯ
        2. ℒ𝒾𝓈𝓉𝒶𝓇 ℛℯ𝓈𝓉𝒶𝓊𝓇𝒶𝓃𝓉ℯ
        3. 𝒜𝓉𝒾𝓋𝒶𝓇 𝓇ℯ𝓈𝓉𝒶𝓊𝓇𝒶𝓃𝓉ℯ
        4.𝒮𝒶𝒾𝓇
        """)


def cadastrar_novo_restaurante():
    os.system('cls')
    print("Cadastro de novos restaurantes ")
    nome_restaurantes = input("Digite o nome do restaurante que você deseja cadastrar: ")
    restaurantes.append(nome_restaurantes)
    print(f"O restaurante {nome_restaurantes} foi cadastrado com sucesso!\n")
    input("Digite qualquer tecla para voltar ao menu principal")
    main()#quando eu tirei o main daqui todos os prints apareceram, por que? 

def listar_restaurantes():
    os.system('cls')
    print("Lista de restaurantes cadastradaos: ")
    for restaurante in restaurantes:
        print(f".{restaurante}")
    input("Digite qualquer tecla para voltar ao menu principal")
    main()

    
def finalizar_app():#para usar função em python uso def e não function
    os.system('cls')#esse os é uma biblioteca do python para para lipara o terminal quando essa função for executada
    print("Encerramdo o programa\n")

def opcao_invalida():
    print("Opção invalida")
    input("Digite uma tecla para voltar ao menú principal")
    main()

def escolher_opcao(): 
    try:#quando eu digitava uma letra era retornado um erro em que era esperado um tipo int e não um str. aqui estou dizendo pro código tentar fazer essa conversão e caso e caso ele não consiga execute o bloco do exept. Assim o codigo não vai quebrar
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()#substituí o print por uma função
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main(): #definindo a função main
    os.system('cls')#lipar o terminal
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':#quando o arquivo executar isso e verificar que este arquivo é  main vai executar a sequencia de comando que estiver dentro do bloco de código dele  
    main() #chamando a função main e executa o que tem dentro dela
#Quando pedimos para que um programa Python seja executado, o interpretador cria uma 
#variável chamada __name__. Se o __name__ for __main__ (principal, em inglês), significa 
#que esse código não será importado por outros scripts de código Python, e ele será o programa 
#principal.

