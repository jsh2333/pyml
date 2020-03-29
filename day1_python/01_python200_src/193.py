import socket

HOST = ''
PORT = 9009

def runServer():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:	
      sock.bind((HOST, PORT))		
      sock.listen(1)
      print('클라이언트 연결을 기다리는 중..')
      conn, addr = sock.accept()
      
      with conn:
         print('[%s]와 연결됨' %addr[0])
         while True:	
            data = conn.recv(1024)
            if not data:
               break
            print('메시지 수신 [%s]' %data.decode())
            conn.sendall(data)

runServer()
