import socket

#Define qual ip do computador recebera a solicitacao
HOST = ''  

# Define qual porta desse ip recebera a solicitacao
PORT = 5000 

# Cria um object socket que recebe a solicitacao
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

# Associa um processo a um ip e porta
tcp.bind(orig)

#inicia a porta no modo aguardar conexao
tcp.listen(1)

# inicia laco para tratar conexao
while True:
    # Aguarda uma conexao do cliente
    con, cliente = tcp.accept()

    # Quando uma conexao e iniciada, aceita e mostra ip conectado 	
    print 'Concetado por', cliente
    
    #recebe mensagens enviadas pelo cliente
    while True:
        msg = con.recv(1024)
        # Se recebeu uma mensagem vazia encerra o laco de receber mensagens 
        if not msg: break
        print cliente, msg

    # Metodo close encerra a conexao com cliente
    print 'Finalizando conexao do cliente', cliente
    con.close()
