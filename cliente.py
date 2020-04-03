import socket

# Endereco IP do Servidor, 127.0.0.1 indica que e o ip local do computador
HOST = '127.0.0.1'     

# Porta que o Servidor esta ouvindo
PORT = 5000            

#cria um objeto para controlar conexao TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = (HOST, PORT)

#Inicia uma conexao com o servidor
tcp.connect(dest)

print 'Para sair use CTRL+X\n'

#Recebe uma entrada do teclado
msg = raw_input()

#Fica no loop enquanto nao receber ctrl+x 
while msg <> '\x18':
    # envia mensagem escrita pelo usuario	
    tcp.send (msg)
    #espera uma nova mensagem do usuario	
    msg = raw_input()

#fecha conexao com servidor
tcp.close()
