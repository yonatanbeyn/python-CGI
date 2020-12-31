import cgi
import socket
from time import ctime
HOST = 'localhost'
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST, PORT)
if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)
    server_socket.setsockopt( socket.SOL_SOCKET,
    socket.SO_REUSEADDR, 1 )
    while True:
        print('Server waiting for connection...')
        client_sock, addr = server_socket.accept()
        print('Client connected from: ', addr)
        while True:
            data = client_sock.recv(BUFSIZ)
            #print the received data to check the request type and it's header file
            print("Received from client: %s" % data.decode('utf-8'))
            #print(data)
           # if not data or data.decode('utf-8') == 'END':
               # break
       
            #data to be sended
            data1="""Content-type:text/html\r\n\r\n"""
            data2="""<html>"""
            data3="""<body>"""
        
            data4="""<p> it works</p>"""
            data5="""</body>"""
            data6="""</html>"""
            try:
                client_sock.send(bytes(data1, 'utf-8'))
                client_sock.send(bytes(data2, 'utf-8'))
                client_sock.send(bytes(data3, 'utf-8'))
                client_sock.send(bytes(data4, 'utf-8'))
                client_sock.send(bytes(data5, 'utf-8'))
                client_sock.send(bytes(data6, 'utf-8')) 
            
            except KeyboardInterrupt:
                print("program exiting")
        client_sock.close()
    server_socket.close()
