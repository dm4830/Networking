from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
   serverSocket = socket(AF_INET, SOCK_STREAM)
   serverSocket.bind(('',port))
   serverSocket.listen()

   while True:
       print('Ready to serve...')
       connectionSocket, addr = serverSocket.accept()     #Fill in end
       try:
           message =  connectionSocket.recv(1024)
           filename = message.split()[1]
           f = open(filename[1:])
           outputdata = f.read()
           f.close()
           connectionSocket.send("200 OK\r\n".encode())
           connectionSocket.close()

           for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())

           connectionSocket.send("\r\n".encode())
           connectionSocket.close()
       except IOError:
      
           connectionSocket.send("404 Not Found\r\n".encode())
           connectionSocket.close()

   serverSocket.close()
   sys.exit() 

if __name__ == "__main__":
   webServer(13331)