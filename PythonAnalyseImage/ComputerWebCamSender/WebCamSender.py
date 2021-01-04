# Dette program sender en webcam stream.
# For at teste prograamet så skal programmet WebCamReciever
# være sat til at køre.

import struct, sys, pickle, cv2, socket, numpy as np

port = 6789
cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1',port))

while True:
    ret,frame=cap.read()
    # Serialize frame
    data = pickle.dumps(frame)

    # Send message length first
    message_size = struct.pack("L", len(data))

    # Then data
    clientsocket.sendall(message_size + data)


