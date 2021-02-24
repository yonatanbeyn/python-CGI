import cgi# for processing user input specifically forms
import logging #logging webserver activity
import socket
HOST = 'localhost'
port = 12345
buffersize = 1024



class WebServer():
    """web server based on a socket. http capsulation """
    def __init__(self,port=8080):#default port for web server
        self._logger = logging.getLogger(__name__)#__name__,  means  every instance of this socket can log  to a file .
                                                # and the logger name will be the name of the logger instance.
        self.c_handler = logging.StreamHandler()
        self.f_handler = logging.FileHandler('file.log')
        self.c_handler.setLevel(logging.WARNING)
        self.f_handler.setLevel(logging.ERROR)
        self.port=port
        self.host=HOST
    def sock_start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# stream tcp type socket
        try:
            print("Starting server on {host}:{port}".format(host=self.host, port=self.port))#print to cosole for debugging purpose
            self.socket.bind((self.host, self.port))# socket start at port 12345, and localhost,
            print("Server started on port {port}.".format(port=self.port))
        #exception handling 
        #possible port in use by other applications
        except Exception as e:
            print("Error: Could not bind to port {port}".format(port=self.port))
             logging.error("Error occurred", exc_info=True)
            self.shutdown()#kill socket
            sys.exit(1)
                self._listen() # Start listening for connections# listen called here
    
