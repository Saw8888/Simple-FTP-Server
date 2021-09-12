import socket,os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

ip = socket.gethostbyname(socket.gethostname())
PATH = ''
os.chdir(PATH)

addr = (ip,21)
authorizer = DummyAuthorizer()
authorizer.add_user('admin','adminpass','.',perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(addr,handler)
server.serve_forever()