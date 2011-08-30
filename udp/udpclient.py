#!/usr/bin/env python

"""
An echo client that allows the user to send multiple lines to the server.
Entering a blank line will exit the client.
"""

import socket
import sys
import select
from logger import Logger

class UDP_Client:

    def __init__(self, ip, port):
        self.host = ip
        self.port = port 
        self.size = 1024
        self.socket = None
        self.username = ''
        clientLogger = Logger('udpclient.log')
        clientLogger.logger.info('Starting UDP client.');

    def open_socket(self):
        try:
          self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket.SOCK_DGRAM for datagrams
          #self.socket.connect((self.host, self.port))
          #clientLogger.logger.info('Connection to server made')
        except socket.error:
          clientLogger.logger.error('Server refused connection.')
          print "Error, server refused connection"

    def close_socket(self):
        self.socket.close()
        clientLogger.logger.info('Connection closed.')

    def send(self, message):
        try:
          self.socket.sendto(message, (self.host, self.port))
        except socket.error:
          clientLogger.logger.error('Send request failed')
          print "Error, send request failed"
          self.close_socket()
          sys.exit(0)
         
    def spam(self):
      buff = 2048 * '\0'
      clientLogger.logger.info('Spamming the server now')
      print "Spamming the server now"
      while 1:
        self.send(buff)

if __name__ == '__main__':

    clientLogger = Logger('udpclient.log')
    clientLogger.logger.info('Starting UDP client')
    print "Starting UDP client"

    try:
      c = UDP_Client(sys.argv[1], int(sys.argv[2]))
      c.open_socket()
      c.spam()
    except IndexError:
      print 'Enter name and port' 
