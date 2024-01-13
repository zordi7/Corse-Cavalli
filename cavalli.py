import random
import Dati

########################################################################################################

def carte():
    semi = ['denari','coppe','spade','bastoni']
    seme_avanzamento = random.choice(semi)
    return seme_avanzamento

########################################################################################################

def calcolo_vincitore():
    
    denari=[]
    coppe=[]
    spade=[]
    bastoni=[]
    
    
    
    for i in range(1,10):
        s = carte()
        print(s)
        if s == 'denari':
            denari.append(1)
        elif s == 'coppe':
            coppe.append(1)
        elif s == 'spade':
            spade.append(1)
        else:
            bastoni.append(1)
    
    lc = len(coppe)
    ld = len(denari)
    ls = len(spade)
    lb = len(bastoni)
    
    vincitore = max(lc,ld,ls,lb)
    
    if vincitore == lc:
        cavallo_vincitore = 'coppe'
    elif vincitore == ld:
        cavallo_vincitore = 'denari'
    elif vincitore == lb:
        cavallo_vincitore = 'bastoni'
    else:
        cavallo_vincitore = 'spade'

    return cavallo_vincitore

########################################################################################################

def fine_partita(Budget, Budget_iniziale):
    
    print("La partita è finita")

    while True:
    
        if Budget > Budget_iniziale:
            
            vincita = Budget - Budget_iniziale
            print(f"Il tuo budget è di: {Budget}, hai guadagnato {vincita} ")
            break
        
        elif Budget == Budget_iniziale:
            
            Budget = Budget_iniziale
            print(f"Il tuo budget è di: {Budget}, sei in pari")
            break
        
        else:
            perdita = Budget_iniziale - Budget
            print(f"Il tuo budget è di: {Budget}, hai perso {perdita} ")
            break

########################################################################################################

def gioco(Budget, Budget_iniziale):
    
    puntata = int(input("Inserisci puntata: "))

    while puntata > Budget:
        print("Puntata non valida")
        puntata = int(input("Inserisci puntata: "))


    print("Digita 'spade' per puntare sul cavallo di spade, 'denari' per quello di denari, 'coppe' per quello di coppe, 'bastoni' per quello di bastoni")
    cavallo_puntato = str(input())
    
    Dati.spazi(1)

    Budget -= puntata
    
    ##################################

    cavallo_vincitore = calcolo_vincitore()
    
    Dati.spazi(1)
    
    print("Ha vinto il cavallo di ", cavallo_vincitore)
    
    Dati.spazi(1)
    ###############################
    if cavallo_puntato == cavallo_vincitore:
        
        print("Hai vinto")
        Budget += puntata * 2
        Dati.spazi(1)
        print("Budget = ", Budget)
        
        if Budget == 0:
            fine_partita(Budget, Budget_iniziale)

        ###############

        nuova_partita = str(input("Vuoi giocare ancora? [s/n]: "))
        if nuova_partita == 's':
            gioco(Budget, Budget_iniziale)
        else:
            fine_partita(Budget, Budget_iniziale)
    
    else:
        print("Hai perso")
        Dati.spazi(1)
        print("Budget", Budget)
        

        if Budget == 0:
            fine_partita(Budget, Budget_iniziale)
        
        ##################

        nuova_partita = str(input("Vuoi giocare ancora? [s/n]: "))
        if nuova_partita == 's':
            gioco(Budget, Budget_iniziale)
        else:
            fine_partita(Budget, Budget_iniziale)


##################################################################################       
def main():
    
    Budget=int(input("Inserisci Budget: "))
    Budget_iniziale = Budget
    
    gioco(Budget, Budget_iniziale)

main()