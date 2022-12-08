# Complete project details at https://RandomNerdTutorials.com
from generateConfig import extract_content
from webPage import web_page

def start_server():
    try:
      import usocket as socket
    except:
      import socket

    import network

    ssid = 'MicroPython-AP'
    password = '123456789'

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password)

    while ap.active() == False:
      pass

    print('Connection successful')
    print(ap.ifconfig())

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
      conn, addr = s.accept()
      print('Got a connection from %s' % str(addr))
      request = conn.recv(1024)
      conn.settimeout(None)
      request = str(request)
      print('Content = %s' % request)
      res = request.find('/onSubmit')
      print('response = %s' % res)
      print(res)
      if res == 6:
          extract_content(request)
      response = web_page()
      conn.send(response)
      conn.close()

