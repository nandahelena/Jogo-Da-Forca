import random, os

with open("palavras.txt", "w") as arquivo:
    arquivo.write("ESCOLA\nCASA\nCOMPUTADOR\nPYTHON\nBICICLETA")

def randomizar_palavra():
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    palavras = [palavra.strip() for palavra in palavras]
    palavra_aleatoria = random.choice(palavras)
    return palavra_aleatoria

def iniciar_jogo():
    palavra_aleatoria = randomizar_palavra()
    palavra_sliced = [letra for letra in palavra_aleatoria]
    palavra_forca = ["_" for letra in palavra_aleatoria]

    tentativas = 6
    letras_tried = []

    print("Bem-vindo ao Jogo da Forca!\n")
    while palavra_sliced != palavra_forca:
        
        print(f"Palavra:", " ".join(palavra_forca))
        print(f"\nTentativas restantes: {tentativas}")
        print(f"Letras tentadas:", " ".join(letras_tried) if len(letras_tried) > 1 else "Nenhuma")

        while True:
            letra = input("Digite uma letra: ").upper()

            if len(letra) != 1:
                print("Por favor, insira somente 1 letra.")
            elif not letra.isalpha():
                print("Por favor, insira um caractere de A-Z.")
            else:
                break

        letras_tried.append(letra)

        if letra in palavra_sliced:
            print(f"\nBoa! A letra '{letra}' está na palavra.")
            for j in range(len(palavra_sliced)):
                if palavra_sliced[j] == letra:
                    palavra_forca[j] = letra
        else:
            print(f"\nA letra '{letra}' não está na palavra.")
            tentativas -= 1
            if tentativas == 0: break
    
    if palavra_sliced == palavra_forca:
        print(f"\nParabéns! Você acertou a palavra: {palavra_aleatoria}")
    else:
        print(f"\nFim de jogo! A palavra era: {palavra_aleatoria}")


if not os.path.exists("palavras.txt"):
    print("O arquivo que contém as perguntas não foi encontrado, por favor, tente novamente.")
elif os.path.getsize("palavras.txt") == 0:
    print("O arquivo que contém as perguntas está vazio, por favor, tente novamente antes de prosseguir.")
else:
    iniciar_jogo()
