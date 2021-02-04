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
           print(outputdata)
           connectionSocket.send(b"200 OK")

           for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())

           connectionSocket.send("\r\n".encode())
           connectionSocket.close()
           exit()
       except IOError:
      
           connectionSocket.send(b"404 Not Found")
           connectionSocket.close()
           exit()

   serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(13331)