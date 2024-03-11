
import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo", "openai"]
    return random.choice(palavras)

def jogar_forca(palavra):
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 6  # Número máximo de tentativas

    while tentativas > 0 and "_" in palavra_oculta:
        letra = input("Digite uma letra: ").lower()

        if letra.isalpha() and len(letra) == 1:
            if letra in palavra:
                print("Letra correta!")
                for i in range(len(palavra)):
                    if letra == palavra[i]:
                        palavra_oculta[i] = letra
            else:
                tentativas -= 1
                print(f"Letra errada! Tentativas restantes: {tentativas}")
        else:
            print("Por favor, digite uma única letra válida.")

        print("Palavra: ", " ".join(palavra_oculta))

    if "_" not in palavra_oculta:
        print("Parabéns! Você venceu. A palavra era:", palavra)
    else:
        print("Game over. A palavra era:", palavra)

if __name__ == "__main__":
    palavra_escolhida = escolher_palavra()
    print("Bem-vindo ao jogo da forca!")
    jogar_forca(palavra_escolhida)
