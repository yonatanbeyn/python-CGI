import socket
import signal # Allow socket destruction on Ctrl+C
import sys
import time
import threading
import logging

class WebServer():
    """
    Class for describing simple HTTP server objects
    """

    def __init__(self, port=8080):
        self.host = socket.gethostname().split('.')[0] # Default to any avialable network interface
        self._logger = logging.getLogger(__name__)#__name__,  means  every instance of this socket can log  to a file .
                                             # and the logger name will be the name of the logger instance.
        self.port = port
        self.content_dir = 'web' # Directory where webpage files are stored

    def start(self):
        """
        Attempts to create and bind a socket to launch the server
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            print("Starting server on {host}:{port}".format(host=self.host, port=self.port))
            self.socket.bind((self.host, self.port))
            print("Server started on port {port}.".format(port=self.port))

        except Exception as e:
            print("Error: Could not bind to port {port}".format(port=self.port))
            self.shutdown()
            sys.exit(1)

        self._listen() # Start listening for connections# listen called here
    def _generate_headers(self, response_code):
        """
        Generate HTTP response headers.
        Parameters:
            - response_code: HTTP response code to add to the header. 200 and 404 supported
        Returns:
            A formatted HTTP header for the given response_code
        """
        header = ''
        if response_code == 200:
            header += 'HTTP/1.1 200 OK\n'
        elif response_code == 404:
            header += 'HTTP/1.1 404 Not Found\n'

        time_now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        header += 'Date: {now}\n'.format(now=time_now)
        header += 'Server: Simple-Python-Server\n'
        header += 'Connection: close\n\n' # Signal that connection will be closed after completing the request
        return header        
        
#WebServer().start()        
    def _listen(self):
        
        """
        Listens on self.port for any incoming connections
        """
        self.socket.listen(5)
        while True:
            (client, address) = self.socket.accept()
            #client.settimeout(60)
            #print("Recieved connection from {addr}".format(addr=address))
            threading.Thread(target=self._handle_client, args=(client, address)).start()
    def _handle_client(self,client,adress):
        packet_size=1024
        while True:
            #print('client : ',client)
            data=client.recv(packet_size).decode()
            #print(data)
            if not data :
                break
            request_method=data.split(' ')[0] #the first but return as string
            print(request_method)#get,post ,put ,
            
            print(data[3:])
            print(type(data))
            #print(len(data)) for debug
            print(type(request_method))
            if request_method=='GET' or request_method == 'HEAD':
                print('hello')
                file_requested=data.split(' ')[1].  # after get
                print(file_requested)
                if file_requested=='/':
                    file_requested='index.html'
                filepath_to_serve =   file_requested
                print("Serving web page [{fp}]".format(fp=filepath_to_serve))
                try:
                    f = open(file_requested, 'rb')
                    if request_method == "GET": # Read only for GET
                        response_data = f.read()
                        #print(response_data)
                   # f.close()
                    response_header = self._generate_headers(200)
                    response = response_header.encode()
                    response += response_data
                    client.send(response)
                    client.close()
                    break
                    
                    
          

                except Exception as e:
                    print("File not found. Serving 404 page.")
                    response_header = self._generate_headers(404)
                    
                    
                    
                    response = response_header.encode()
                    #if request_method == "GET":
                    #    response += response_data

                    client.send(response)
                    client.close()
                    break
                else:
                    print("Unknown HTTP request method: {method}".format(method=request_method)) 
x=WebServer(8012).start()
#print(x._logger)
