#!/usr/bin/python
# -*- coding: utf-8 -*-

#pingsweep version 0.1, anteriormente llamado pinger.

import subprocess
import sys
import getopt

def main(argv):
    octe_foo = 0
    red = ''
    op_cont = ''

    try:
        opts, args = getopt.getopt(argv,"hr:i:f:",["red","ipinicio=","ipfin="])
    except getopt.GetoptError:
        print "\nError, debes de utilizar el comando de la siguiente forma:"
        print "(Todo tiene una razón de ser)"
        print "pinger.py -r <red> -i <primera_ip> -f <ultima_ip>"
        print "o"
        print "pinger.py --red <red> --ipinicio <primera_ip --ipfin <ultima_ip>\n"
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print "Espere, la ayuda ya viene en camino."
            print "..."
            print "..."
            print "¡Listo!, una disculpa por la demora."
            print "Este es un pequeño script en Python que utiliza el comando PING nativo del sistema operativo para identificar equipos o dispositivos activos en una red local."
            print "Definir argumento:"
            print "\t -i o --ipinicio: Es la primera dirección IP, del ultimo octeto de una dirección IP, donde se empezara a hacer ping."
            print "\t -o o --ipfin: Es la ultima dirección IP, del ultimo octeto de una dirección IP, donde se empezara a hacer ping."
            print "\t -r o --red: Aqui se define la red, del tipo C, donde se realizaran los ping."
            print "Si no sabes a que octeto de una dirección IP me refiero, o que es un octeto entonces sí no puedo ayudarte."
            sys.exit()
        elif opt in ("-r", "--red"):
            red = arg
        elif opt in ("-i", "--ipinicio"):
            octeinicio = int(arg)
        elif opt in ("-f", "--ipfinal"):
            octefin = int(arg)
    if (octeinicio > octefin):
        print "\n\n\nLa IP de inicio es posterior a la IP de fin, muy probablemente te equivocaste pero no te preocupes, yo lo arreglo."
        octe_foo = octeinicio
        octeinicio = octefin
        octefin = octe_foo
    print "La red es: " + red
    print "La ip de inicio es: " + str(octeinicio)
    print "La ip de fin es: " + str(octefin)
    print "¿HASTA aqui todo bien?"
    print "Una vez que el programa empiece no hay forma de pararlo."
    op_cont = raw_input('¿Quieres continuar? (S)í/(N)o: ')
    if op_cont in ["s", "S"]:
        pinger(red, octeinicio, octefin)
    else:
        print "Sabia decisión\n"
        sys.exit()


def pinger(ired,ipi,ipf):
    ips = []
    for ultimo_oct in range (ipi, ipf+1):
        command_ping = "ping -c 8 " + ired + "." + str(ultimo_oct)
        print "Ejecutando: " + command_ping
        ping_exe = subprocess.Popen (command_ping, stdout = subprocess.PIPE, shell = True)
        ping_status = ping_exe.wait()
        #print "Status/Code exit: " + str(ping_status)
        if ping_status != 0:
            print "La IP " + ired + "." + str(ultimo_oct) + " no está activa."
        else:
            print "La IP " + ired + "." + str(ultimo_oct) + " está activa."
            ips.append(ired + "." + str(ultimo_oct))
    print "\nListado de IPs activas:"
    for ip in ips:
        print ip




if __name__ == "__main__":
   main(sys.argv[1:])
