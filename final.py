from asterisk.ami import (
    AMIClient, 
    SimpleAction, 
    EventListener
    )
import os, time
#--------------------------LAMADAS A AMI------------------------
def llamadarTrabajador(sipuser):
	#print(f'Llamando a {sipuser}')
	action = SimpleAction(
		'Originate',
		Channel=sipuser,
		Exten='105',
		Priority=1,
		Context='redesinteligentes',
		)
	client.send_action(action)

def llamarCliente(sipuser):
	#print(f'Llamando a {sipuser}')
	action = SimpleAction(
		'Originate',
		Channel=sipuser,
		Exten='106',
		Priority=1,
		Context='redesinteligentes',
		)
	client.send_action(action)

def do_bridge(sipuser1,sipuser2):
	#print(f'Uniendo canal de {sipuser1} con {sipuser2}')
	action = SimpleAction(
		'Bridge',
		Channel1=sipuser1,
		Channel2=sipuser2,
	)
	client.send_action(action)

client = AMIClient(address='127.0.0.1',port=5038)
client.login(username='admin',secret='s1234')

#--------------------------AGREGA SIP------------------------
Trabajadores = ["pcuno"]
ListaDeClientes = ["pcdos","pyterm",]
N = len (Trabajadores)
n = len (ListaDeClientes)
ti = .5
ti2= 5

def imprimirListaDeClientes():
    for i in range(1,n+1):
        print(i,")",ListaDeClientes[i-1])

def Trabajador_list():
    os.system('clear')
    print(f'Se tiene(n) {N} Trabajador(es) seleccione la máquina del trabajador:"')
    for i in range(1,N+1):
        print(i,")",Trabajadores[i-1])
    T = int(input("Máquina: \n"))
    return T
    
#--------------------------LLAMADAS ELIGIENDO CLIENTE Y TRBAJADOR------------------------
def LlamanarPorSeleccion():
    a = 0
    while a != 4:
        os.system('clear')
        T = Trabajador_list()
        if T <= N:   
            print (f'Trabajador: {Trabajadores[T-1]}, llamará a:"')
            imprimirListaDeClientes()
            C = int(input("Cliente: "))
            if C <= n:
                os.system('clear')
                print(f'Trabajador {Trabajadores[T-1]} enlazando con: {ListaDeClientes[C-1]}')
                x = f'sip/{Trabajadores[T-1]}'
                llamadarTrabajador(x)
                time.sleep(ti)
                y = f'sip/{ListaDeClientes[C-1]}'
                llamarCliente(y)    
                time.sleep(ti)
                do_bridge(x,y)
                time.sleep(ti2)
            else:
                print ("El cliente", C, "no existe o tecleo mal")
                time.sleep(ti)
                break
        else:
            print ("El trabajador", T, "no existe o tecleo mal")
            time.sleep(ti)
            break
#--------------------------CALL CENTER------------------------
def LlamadasAutomaticas ():
    a =0
    T = Trabajador_list()
    if T <= N:
        x = f'sip/{Trabajadores[T-1]}'
        while a <= n:
            os.system('clear')
            y = f'sip/{ListaDeClientes[a]}'
            print (f'Enlazando a {x} con el cliente {y}')
            time.sleep(ti)
            llamadarTrabajador(x)
            time.sleep(ti)
            llamarCliente(y)    
            time.sleep(ti)
            do_bridge(x,y)
            input('PAUSE')
            a += 1
            if a >= n:
                print("Ha relizado todas sus llamadas vaya por una cheve")
                break
    else:
        print ("El trabajador", T, "no existe o tecleo mal")                
        
"""
os.system('clear')
print("Menu")
print("1) Llamadas multiples trabajadores, multiples clieste")
print("2) Call center")

k = int (input())
if k == 1:
    LlamanarPorSeleccion()
elif k == 2:
    LlamadasAutomaticas()
else:
    print("No existe la opción")
#"""
#"""
x = f'sip/{Trabajadores[0]}'
llamadarTrabajador(x)
time.sleep(.1)
y = f'sip/{ListaDeClientes[1]}'
llamarCliente(y)    
time.sleep(.1)
do_bridge(x,y)
input('enter para continuar')
#""""