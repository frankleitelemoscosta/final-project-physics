import serial
import threading
import sys
import select

arduino = serial.Serial('COM3', 115200, timeout=1)

def ler_dados_serial():
    while True:
        if arduino.in_waiting > 0:  
            dados = arduino.readline().decode('utf-8').strip()
            if dados:
                dados_recebidos.append(dados) 

def capturar_comando_teclado():
    while True:
        comando = input("Digite 'save' para salvar os últimos 10 dados recebidos, 'print' para exibir ou 'exit' para sair: ").strip()
        if comando == 'print':
            if dados_recebidos:
                print("Dados recebidos:")
                for dado in dados_recebidos:
                    print(dado)
                dados_recebidos.clear()
            else:
                print("Nenhum dado recebido.")
        elif comando == 'save':
            if dados_recebidos:
                dados_para_salvar = dados_recebidos[-10:]
                with open('dados_recebidos.txt', 'a') as file:
                    for dado in dados_para_salvar:
                        file.write(dado + '\n')
                print(f"{len(dados_para_salvar)} dados salvos em 'dados_recebidos.txt'.")
                dados_recebidos.clear()
            else:
                print("Nenhum dado para salvar.")
        elif comando == 'exit':
            break
        else:
            print("Comando não reconhecido. Digite 'save', 'print' ou 'exit'.")

dados_recebidos = []

thread_serial = threading.Thread(target=ler_dados_serial, daemon=True)
thread_teclado = threading.Thread(target=capturar_comando_teclado, daemon=True)

thread_serial.start()
thread_teclado.start()

try:
    thread_teclado.join()  
except KeyboardInterrupt:
    print("Programa interrompido.")

arduino.close()
