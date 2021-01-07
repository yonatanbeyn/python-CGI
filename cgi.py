import cgi# for processing user input specifically forms
import socket
HOST = 'localhost'
PORT = 12345
BUFSIZ = 1024
class WebServer():
    """web server based on a socket. http capsulation """
    def __init__(self,port=8080):#default port for web server
        self.port=port
        self.host=HOST
    def sock_start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Starting server on {host}:{port}".format(host=self.host, port=self.port))#log to the console
            self.socket.bind((self.host, self.port))
            print("Server started on port {port}.".format(port=self.port))

        except Exception as e:
            print("Error: Could not bind to port {port}".format(port=self.port))
            self.shutdown()
            sys.exit(1)
    
