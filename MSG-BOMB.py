#
## Created by: JerryFS-bit
#

import pyautogui
import time
from colorama import Fore
from pyfiglet import figlet_format
from os import system, path, name

def info_author():
    print("Creado por: JerryFS-Bit")
    print("_____________________________________________________")
    print(Fore.LIGHTRED_EX + "Github    : https://github.com/JerryFS-bit" + Fore.RESET)
    print("_____________________________________________________")

def Cscreen():
    if name == "posix":
        system("clear")
    else:
        system("cls")

def function():
    mensaje = input(" [" + Fore.LIGHTGREEN_EX + "*" + Fore.RESET + "] Escribe el contenido del mensaje: ") 
    num_msj = int(input(" [" + Fore.LIGHTGREEN_EX + "*" + Fore.RESET + "] Numero de mensajes a enviar: " + Fore.RESET))
    timestart = int(input(" [" + Fore.LIGHTGREEN_EX + "*" + Fore.RESET + "] Indique en seg, el retardo de inicio : "))
    timesms = int(input(" [" + Fore.LIGHTGREEN_EX + "*" + Fore.RESET + "] Indique en seg, el tiempo de envio entre mensajes : " + Fore.RESET)) 
    print(" [" + Fore.YELLOW + "OK" + Fore.RESET + "]" + Fore.LIGHTCYAN_EX +" El spam va a empezar en ",timestart," segundos")
    return mensaje, num_msj, timestart, timesms


def Spam():
    value = 0
    banner = figlet_format("MSG-BOMB", font = "slant")
    print(Fore.LIGHTCYAN_EX + banner + Fore.RESET)
    info_author()

    print(Fore.YELLOW + "\n\nNOTA: PARA LA OPCION DEL SPAM CON UN ARCHIVO, DEBE CREARSE EN EL MISMO DIRECTORIO !!" + Fore.RESET)
    sel = input("\n [" + Fore.LIGHTGREEN_EX + "*" + Fore.RESET + "] Presione 'M' para escribir un mensaje personalizado, de lo contrario presione 'F' para usar un archivo como mensaje: ").upper()
    if sel == 'M':
        mensaje, num_msj, timestart, timesms = function()

    elif sel == 'F':
        name = str(input(" [" + Fore.YELLOW + "!" + Fore.RESET + "] INGRESE EL NOMBRE DEL ARCHIVO (La extension debe ser .txt): "))
        if path.exists(name):
            file = open(name,"r+", encoding="utf-8", errors="ignore")
            mensaje = file.read(100000)
            num_msj = int(input(" [" + Fore.LIGHTGREEN_EX + "*" + Fore.RESET + "] Numero de mensajes a enviar: "))
            timestart = int(input(" [" + Fore.LIGHTGREEN_EX + "*" + Fore.RESET + "] Indique en seg, el retardo de inicio : " + Fore.RESET))
            timesms = int(input(" [" + Fore.LIGHTGREEN_EX + "*" + Fore.RESET + "] Indique en seg, el tiempo de envio entre mensajes : ")) 
            print(" [" + Fore.YELLOW + "OK" + Fore.RESET + "]" + Fore.LIGHTCYAN_EX +" El spam va a empezar en ",timestart," segundos")

        else:
            print(" [" + Fore.RED + "!" + Fore.RESET + "] EL ARCHIVO NO EXISTE !!")
            exit()    


    time.sleep(timestart)
    Cscreen()
    print(" [!] No cierre la terminal: Ataque en proceso !!")

    while True: 
        value += 1
        pyautogui.write(mensaje)
        time.sleep(timesms)
        pyautogui.press("Enter")
        
        print(" [" + Fore.GREEN + "OK" + Fore.RESET + "]" + " -> ",value," Mensajes enviados de ", num_msj)
        if (value == num_msj):
            print(Fore.GREEN + "\nATAQUE CORRECTAMENTE FINALIZADO !!" + Fore.RESET)
            break

try:
    Cscreen()
    Spam()

except(KeyboardInterrupt):
    print(Fore.LIGHTRED_EX + "\nEl programa se a finalizado por el usuario !!" + Fore.RESET)
