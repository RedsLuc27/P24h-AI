import socket
import time

#def des choses importantes
IP = '127.0.0.1'
PORT = 1234
BUFFER_SIZE = 4096
x = 1
nbD = 0
nbA = 0
nbS = 0


#CONNECTION
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

#DEF DE SEND
def snd(s, msg):
    s.sendall((msg + '\n').encode())
    print("SND: ", msg)

if __name__ == "__main__":
    while True:
        #RECEIVE 
        data = s.recv(BUFFER_SIZE).decode().strip()
        print("RECU: " + data)

        #send le nom d'équipe
        NAME = "RedsLuc27\n"
        if data == "NOM_EQUIPE":
            snd(s, "RedsLuc27")

        #si debut tour
        if "DEBUT_TOUR" in data:
            TRUC = data
            Trucsplit = TRUC.split("|")
            print(Trucsplit)
            print(Trucsplit[2])
            print("Nb de carte piocher")
            print(nbD)
            print(nbA)
            print(nbS)
            nuit = 0

            #Je vérif si j'ai pas piocher déja plus de 8 cartes.
            if int(Trucsplit[2]) == 3 or int(Trucsplit[2]) == 7 or int(Trucsplit[2]) == 11:
                if nbD > 8:
                    snd(s, "UTILISER|DEFENSE")
                    nbD = nbD - nbD
                if nbA > 8:
                    snd(s, "UTILISER|ATTAQUE")
                    nbA = nbA - nbA
                if nbS > 8:
                    snd(s, "UTILISER|SAVOIR")
                    nbS = nbS - nbS
                print("nuit")
                nbS = nbS + 1
                snd(s,"PIOCHER|2")
                nuit = nuit + 1

            #Je vérif le meilleur truc de la pioche.
            if nuit == 0:
                snd(s, "PIOCHES")
                data = s.recv(BUFFER_SIZE).decode().strip()
                data.startswith("DEFENSE")
                PIOCHES = data
                Pisplit = PIOCHES.split("|")

                #Split l'array pour savoir def att sav
                print(Pisplit[0], Pisplit[1])
                print(Pisplit[2], Pisplit[3])
                print(Pisplit[4], Pisplit[5])
                print(Pisplit[6], Pisplit[7])
                print(Pisplit[8], Pisplit[9])
                print(Pisplit[10], Pisplit[11])
                DEF = int(Pisplit[1])
                ATT = int(Pisplit[3])
                SAV = int(Pisplit[5])
                DEF1 = Pisplit[6] + Pisplit[7]
                ATT1 = Pisplit[8] + Pisplit[9]
                SAV1 = Pisplit[10] + Pisplit[11]

                #Détermine quelle carte piocher par rapport a mon score
                snd(s, "MOI")
                data = s.recv(BUFFER_SIZE).decode().strip()
                MOI = data
                print(MOI)
                Moisplit = MOI.split("|")
                DEFM = int(Moisplit[1])
                ATTM = int(Moisplit[2])
                SAVM = int(Moisplit[3])
                print(Moisplit[1])
                print(Moisplit[2])
                print(Moisplit[3])
                #print("DEF" + DEFM, DEF)
                #print("ATT" + ATTM, ATT)
                #print("SAV" + SAVM, SAV)
                if DEFM == 0 and DEF > 0:
                    print("JE PIOCHE DEF")
                    snd(s, "PIOCHER|0")
                    nbD = nbD + 1
                else:
                    print("JE PIOCHE PAS DE DEF")
                    if ATTM == 10019783647958738478756 and ATT > 10:
                        print("JE PIOCHE ATT")
                        snd(s, "PIOCHER|1")
                        nbA = nbA + 1
                    else:
                        print("JE PIOCHE PAS D'ATT")
                        if SAVM == 0 and SAV > 2:
                            print("JE PIOCHE SAV")
                            snd(s, "PIOCHER|2")
                            nbS = nbS + 1
                        else:
                            nbS = nbS + 1
                            snd(s,"PIOCHER|2")
                            print("JE PIOCHE PAS DE SAV")