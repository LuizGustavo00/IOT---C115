import socket

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 65432))
    servidor.listen() #modo escuta do servidor

    print("Aguardando conexão...")
    conexao, endereco = servidor.accept()
    with conexao:
        print(f"Conectado a {endereco}") #endereco conectado

        pontuacao = 0

        conexao.send(b'Bem-vindo ao show do Milhao\n Vamos a primeira pergunta')

        pergunta1 = (
        "Qual a capital da França?\n"
        "a) Berlim\n"
        "b) Madrid\n"
        "c) Paris\n"
        "d) Roma"
        )
        conexao.send(pergunta1.encode())
        resposta = conexao.recv(1024).decode().strip().lower()
        if resposta == 'c':
            pontuacao += 1

        pergunta2 = (
            "Qual o maior planeta do sistema solar?\n"
            "a) Terra\n"
            "b) Júpiter\n"
            "c) Saturno\n"
            "d) Marte"
        )
    
        conexao.send(pergunta2.encode()) #envia pergunta ao cliente
        resposta = conexao.recv(1024).decode().strip().lower() #recebe a resposta
        if resposta == 'b':
            pontuacao += 1

        conexao.send(f'Pontuacao final: {pontuacao}'.encode())

if __name__ == "__main__":
    main()
