import socket

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 65432))

    while True:
        mensagem = cliente.recv(1024).decode()
        print(mensagem)
        
        if "?" in mensagem:#confirma se é uma pergunta
            resposta = input("Digite sua resposta: ")
            cliente.send(resposta.strip().encode())#envia a resposta ao servido
        elif "Pontuacao final" in mensagem:
            break

    cliente.close()

if __name__ == "__main__":
    main()