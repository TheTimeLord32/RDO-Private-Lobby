import os, winreg, requests

def fileReg():
    fileReg = open("RDR2.reg", 'w')
    fileReg.write("Windows Registry Editor Version 5.00\n")
    fileReg.write("[HKEY_LOCAL_MACHINE\SOFTWARE\Rockstar Games]\n")
    fileReg.write("[HKEY_LOCAL_MACHINE\SOFTWARE\Rockstar Games\Red Dead Redemption 2]\n")
    s = "\"Install Dir\"="+"\""+os.getcwd()+"\""+"\n"
    x = s.replace("\\", "\\\\")
    fileReg.write(str(x))

    fileReg.write("\"DisplayName\"=""\"Red Dead Redempion 2\"")
    fileReg.close()
    print("File creato con successo \n")

def readReg():
    access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    key = winreg.OpenKey(access_registry, r"SOFTWARE\Rockstar Games\Red Dead Redemption 2")
    dir, regtype = winreg.QueryValueEx(key, "Install Dir")
    return dir

def installazioneFile():
    value = readReg()
    bootLauncherFlowYMT = value + '\\x64\\' + 'boot_launcher_flow.ymt'
    startupMETA = value + '\\x64\\data\\' + 'startup.meta'

    urlBootLauncherFlowYMT = "https://raw.githubusercontent.com/TheTimeLord32/RDO-Private-Lobby/main/boot_launcher_flow.ymt"
    r1 = requests.get(urlBootLauncherFlowYMT)
    with open(bootLauncherFlowYMT, 'wb') as f:
        f.write(r1.content)
    f.close()

    urlstartupMETA = "https://raw.githubusercontent.com/TheTimeLord32/RDO-Private-Lobby/main/startup.meta"
    r2 = requests.get(urlstartupMETA)
    with open(startupMETA, 'wb') as f:
        f.write(r2.content)
    f.close()

    print("File installati con successo \n")
    return value

def attivaFile():
    directory = readReg()
    boot_disable = directory + "\\x64\\boot_launcher_flow.bak"
    startup_disable = directory + "\\x64\\data\\startup.bak"
    boot_enable = directory + "\\x64\\boot_launcher_flow.ymt"
    startup_enable = directory + "\\x64\\data\\startup.meta"

    os.rename(boot_disable, boot_enable)
    os.rename(startup_disable, startup_enable)
    print("File attivati \n")

def disattivaFile():
    directory = readReg()
    boot_disable = directory + "\\x64\\boot_launcher_flow.bak"
    startup_disable = directory + "\\x64\\data\\startup.bak"
    boot_enable = directory + "\\x64\\boot_launcher_flow.ymt"
    startup_enable = directory + "\\x64\\data\\startup.meta"

    os.rename(boot_enable, boot_disable)
    os.rename(startup_enable, startup_disable)
    print("File disattivati \n")

operazione = input("Scegliere operazione: crea, installa, attiva, disattiva \n")
match operazione:
    case "crea":
        fileReg()
    case "installa":
        installazioneFile()
    case "attiva":
        attivaFile()
    case "disattiva":
        disattivaFile()
    case unknown_command:
        print("Operazione non valida \n")
