#coding=utf-8
import socket

def handle_client(client_socket):
    recv_data = client_socket.recf(1024).decode('utf-8')
    requese_header_lines = recv_data.splitlines()
    for line in request_header_lines:
        print(line)

    response_headers = "HTTP/1.1 200 OK\r\n"
    response_headers += "\r\n"

    response_body = "hello world"
    reponse = response_headers + response_body
    client_socket.send(response.encode("utf-8"))
    client_socket.close()

def main():
    server_socket = socket.socket()
