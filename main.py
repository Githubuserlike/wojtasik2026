import turtle
import random
import math
import time

def RYSUNEK(rozmiar_swiata,pola,przeciwnicy,miasta,zmiany,Start_x,Start_y):
    turtle.setup(width=rozmiar_swiata,height=rozmiar_swiata)
    turtle.hideturtle()
    turtle.penup()
    turtle.color("green3")
    turtle.shape("circle") 
    turtle.shapesize(0.5, 0.5, 1)
    for mx,my in miasta:
        turtle.setposition(mx,my)
        turtle.pendown()
        turtle.color("yellow")
        turtle.stamp()
        turtle.penup()
    turtle.shapesize(1, 1, 1)
    turtle.color("green3")
    for x1, y1, x2, y2 in pola:
        turtle.teleport(x1,y1)
        turtle.pendown()
        turtle.goto(x1,y2)
        turtle.goto(x2,y2)
        turtle.goto(x2,y1)
        turtle.goto(x1,y1)
        turtle.penup()

    turtle.penup()
    turtle.shape("circle") 
    turtle.shapesize(0.5, 0.5, 1)
    for px,py in przeciwnicy:
        turtle.setposition(px,py)
        turtle.pendown()
        turtle.color("red4")
        turtle.stamp()
        turtle.penup()
    turtle.shape("classic") 
    turtle.shapesize(1, 1, 1)
    turtle.color("black")
    OSIE(rozmiar_swiata)
    turtle.penup()
    turtle.teleport(int(-rozmiar_swiata/2),int(-rozmiar_swiata/2))
    turtle.pensize(1)
    turtle.showturtle()
    turtle.pendown()
    turtle.bgcolor("lightyellow")
    turtle.title("Wyprawa na ratunek świata")
    turtle.penup()
    turtle.teleport(Start_x,Start_y)
    turtle.pendown()
    for cmd in zmiany:
        cmd()
        time.sleep(0.1)

def KON_NAZWA():
    kon=input("Podaj nazwę konia: ")
    return kon
def GRACZ_NAZWA():
    gracz=input("Podaj imię gracza: ")
    return gracz

def OSIE(rozmiar):
    turtle.pensize(3)
    t=turtle
    t.hideturtle()
    t.color("black")
    t.penup()
    t.setpos(-rozmiar/2,-rozmiar/2)
    t.pendown()
    t.goto(-rozmiar/2,rozmiar/2)
    t.goto(rozmiar/2,rozmiar/2)
    t.goto(rozmiar/2,-rozmiar/2)
    t.goto(-rozmiar/2,-rozmiar/2)

def TORNADO(rozmiar_swiata,zmiany):
    pozycja_x=int(-random.randrange(0,int(rozmiar_swiata/4)))
    pozycja_y=int(-random.randrange(0,int(rozmiar_swiata/4)))
    print("Natrafiłeś na tornado które tobą rzuciło")
    
    zmiany.append(lambda:turtle.color("gray"))
    zmiany.append(lambda:turtle.stamp())
    zmiany.append(lambda:turtle.penup())
    zmiany.append(lambda  x=pozycja_x, y=pozycja_y:turtle.teleport(x,y))
    zmiany.append(lambda:turtle.stamp())
    zmiany.append(lambda:turtle.pendown())
    zmiany.append(lambda:turtle.color("black"))
    return pozycja_x,pozycja_y,zmiany


def LAKA(imie_konia,zmiany):
    print(f"Natrafiłeś na łączke i {imie_konia} może się najeść")
    Jedzenie_konia=100
    zmiany.append(lambda:turtle.color("green3"))
    zmiany.append(lambda:turtle.stamp())
    zmiany.append(lambda:turtle.color("black"))
    return Jedzenie_konia,zmiany

def PRZECIWNIK(Rozmiar_Swiata,Poziom_Trudonosci):
    liczba = Poziom_Trudonosci*int(Rozmiar_Swiata/150)
    przeciwnicy = []
    for i in range(liczba):
        lok_x = random.randrange(int(-Rozmiar_Swiata*0.5),int(Rozmiar_Swiata*0.5))
        lok_y = random.randrange(int(-Rozmiar_Swiata*0.5),int(Rozmiar_Swiata*0.5))
        przeciwnicy.append((lok_x,lok_y))
    return przeciwnicy

def MIASTECZKO(Rozmiar_Swiata,Poziom_Trudnosci):
    liczba = int(30/Poziom_Trudnosci)
    miasta = []
    for i in range(liczba):
        lokalizacja_x = random.randrange(int(-Rozmiar_Swiata*0.5),int(Rozmiar_Swiata*0.5))
        lokalizacja_y = random.randrange(int(-Rozmiar_Swiata*0.5),int(Rozmiar_Swiata*0.5))
        miasta.append((lokalizacja_x,lokalizacja_y))
    return miasta

def NAJBLIZSZE(pozycja_x,pozycja_y,miasta,rozmiar_swiata):
    najblizej=None
    min_dystants=float("inf")

    for mx,my in miasta:
        dystans=math.sqrt((pozycja_x-mx)**2+(pozycja_y-my)**2)
        if dystans<min_dystants:
            min_dystants=dystans
            najblizej=(f"Najbliższe miasto znajduje się w: ({mx+int(rozmiar_swiata/2)},{my+int(rozmiar_swiata/2)})")
    return najblizej
#Teorytycznie 
def POLE(Rozmiar_Swiata,Poziom_Trudnosci):
    liczba = math.ceil(Poziom_Trudnosci*1.5)
    pola=[]
    for i in range(liczba):
        lokalizacja_x = random.randrange(int(-Rozmiar_Swiata*0.5),int(Rozmiar_Swiata*0.5))
        lokalizacja_xk = lokalizacja_x+int(Rozmiar_Swiata/5)
        lokalizacja_y = random.randrange(int(-Rozmiar_Swiata*0.5),int(Rozmiar_Swiata*0.5))
        lokalizacja_yk= lokalizacja_y+int(Rozmiar_Swiata/5)
        pola.append((lokalizacja_x,lokalizacja_y,lokalizacja_xk,lokalizacja_yk))
    
    return pola 

def KIERUNEK(zmiany):
    try:
        Kierunek = float(input("Podaj kat w ktorym idziesz (0-360): "))
        if Kierunek >360 or Kierunek<0:
            print("Podano błędne dane. Spróbuj ponownie")
            return KIERUNEK(zmiany)
        zmiany.append(lambda k=Kierunek: turtle.setheading(k+90))
        return Kierunek
    except:
        return KIERUNEK(zmiany)

def KAKTUS(pola,pozycja_x,pozycja_y,max_predkosc,jedzenie_k,jedzenie_g,zmiany,czas):
    for x1, y1, x2, y2 in pola:
        if x1 <= pozycja_x <= x2 and y1 <= pozycja_y <= y2:
            print("Gracz jest w polu kaktusów")
            jedzenie_k=int(jedzenie_k/2)
            jedzenie_g=int(jedzenie_g/2)
            czas+=1
            zmiany.append(lambda: turtle.color('green'))
            
            if pozycja_x - x1 <= max_predkosc:
                print("Zbliżasz się do wyjścia z pola")

           
            elif x2 - pozycja_x <= max_predkosc:
                print("Zbliżasz się do wyjścia z pola")

            
            elif pozycja_y - y1 <= max_predkosc:
                print("Zbliżasz się do wyjścia z pola")

            
            elif y2 - pozycja_y <= max_predkosc:
                print("Zbliżasz się do wyjścia z pola")
        elif x1 - max_predkosc <= pozycja_x < x1 and y1 <= pozycja_y <= y2:
            print("Zbliżasz się do pola kaktusów. Wejście w pole usuwa połowę jedzenia")
            
        elif x2 < pozycja_x <= x2 + max_predkosc and y1 <= pozycja_y <= y2:
            print("Zbliżasz się do pola kaktusów. Wejście w pole usuwa połowę jedzenia")
            
        elif y1 - max_predkosc <= pozycja_y < y1 and x1 <= pozycja_x <= x2:
            print("Zbliżasz się do pola kaktusów. Wejście w pole usuwa połowę jedzenia")
            
        elif y2 < pozycja_y <= y2 + max_predkosc and x1 <= pozycja_x <= x2:
            print("Zbliżasz się do pola kaktusów. Wejście w pole usuwa połowę jedzenia")
    return jedzenie_k,jedzenie_g,zmiany,czas       
        
def WALKA(liczba_krokow,Jedzenie_gracza,przeciwnicy,polozenie_x,polozenie_y,poziom,zmiany,max_p,napo):
    for px,py in przeciwnicy: 
        if abs(polozenie_x - px) <= max_p and abs(polozenie_y - py) <= max_p:
            print("Napotkałeś przeciwnika")
            walka_w=input("Co robisz? Atakujesz-ryzyko utraty jedzenia (A) Ganiasz się z nim aż uda ci się uciec-utrata kilku tur (U): ").upper()
            if walka_w=="A":
                utrata=random.randrange(0,poziom+2)
                if utrata>1:
                    print("Udało ci się pokonać przeciwnika niestety utraciłeś część jedzenia")
                    Jedzenie_gracza-=poziom*7
                    zmiany.append(lambda: turtle.color("red"))
                    przeciwnicy.remove((px, py))
                    napo+=1
                else:
                    print("Udało ci się pokonać przeciwnika bez uszczerbku na zapasach")
                    przeciwnicy.remove((px, py))
                    napo+=1
                zmiany.append(lambda: turtle.color("pink"))
            elif walka_w=="U":
                liczba_krokow-=poziom*5
                print(f"Uciekłeś przeciwnikowi ale zajęło ci to {poziom*5} kroków")
                zmiany.append(lambda: turtle.color("orange"))
                przeciwnicy.remove((px, py))
                napo+=1
            else:
                print("Niepoprawny wybor, spróbuj ponownie")
                return WALKA(liczba_krokow,Jedzenie_gracza,przeciwnicy,polozenie_x,polozenie_y,poziom,zmiany,max_p,napo)
            zmiany.append(lambda: turtle.stamp())
            zmiany.append(lambda: turtle.color("black"))
    return liczba_krokow,Jedzenie_gracza,przeciwnicy,zmiany,napo    




def WYBOR(aktualna_predkosc,Kat,polozenie_x,polozenie_y,miasta,rozmiar_swiata,Jedzenie_gracza,Jedzenie_konia,max_predkosc,zmiany,Dom_x,Dom_y):
    Wybor = input("Chcesz kontynuować w tym kierunku(K), czy może wolisz zmienić (Z), czy sprawdzić położenie najbliższego miasta oraz celu (S) : ").upper()
    if Wybor=="K":
        if aktualna_predkosc<0:
            aktualna_predkosc=3
        aktualna_predkosc=int(((aktualna_predkosc*10)**1.15)/10)
        if aktualna_predkosc>max_predkosc:
            aktualna_predkosc=max_predkosc
    elif Wybor=="Z":
        aktualna_predkosc=3
        Kat=KIERUNEK(zmiany)
    elif Wybor=="S":
        najblizej = NAJBLIZSZE(polozenie_x,polozenie_y,miasta,rozmiar_swiata)
        aktualna_predkosc=0
        Jedzenie_gracza+=1
        Jedzenie_konia+=1
        print(f"Najblizsze miasto znajduje sie {najblizej}")
        print(f"Cel znajduje sie ({Dom_x},{Dom_y})")
    else:
        print("Niepoprawny wybor, spróbuj ponownie")
        return WYBOR(aktualna_predkosc,Kat,polozenie_x,polozenie_y,miasta,rozmiar_swiata,Jedzenie_gracza,Jedzenie_konia,max_predkosc,zmiany,Dom_x,Dom_y)
    return aktualna_predkosc,Kat,Jedzenie_gracza,Jedzenie_konia
def POZIOM():
    try:
        poziom = int(input("Podaj poziom trudności (1-Łatwy,2-Średni,3-Trudny): "))
        if poziom>3 or poziom<1:
                print("Podano złe dane")
                return POZIOM()
        else:
            return poziom
    except:
        print("Podano błędne wymiary")
        return POZIOM()
def ROZMIAR_SWIATA():
    try:
        rozmiar_swiata = int(input("Podaj rozmiar świata (100-900): "))
        if rozmiar_swiata>900 or rozmiar_swiata<100:
                print("Podano złe dane")
                return ROZMIAR_SWIATA()
        else:
            return rozmiar_swiata
    except:
        print("Podano błędne wymiary")
        return ROZMIAR_SWIATA()
        
        

def KOORDY_X(rozmiar_swiata):
    if rozmiar_swiata>400:
        try:  
            Start_x = int(input("Podaj położenie na osi x (0-100): "))
            if Start_x>100 or Start_x<0:
                print("Podano złe dane")
                return KOORDY_X(rozmiar_swiata)
            else:
                Start_x-=int(rozmiar_swiata/2)
                return Start_x
        except:
            print("Podano błędne wymiary")
            return KOORDY_X(rozmiar_swiata)
    else:
        try:  
            Start_x = int(input("Podaj położenie na osi x (0-25): "))
            if Start_x>25 or Start_x<0:
                print("Podano złe dane")
                return KOORDY_X(rozmiar_swiata)
            else:
                Start_x-=int(rozmiar_swiata/2)
                return Start_x
        except:
            print("Podano błędne wymiary")
            return KOORDY_X(rozmiar_swiata)
def KOORDY_Y(rozmiar_swiata):
    if rozmiar_swiata>400:
        try:  
            Start_y = int(input("Podaj położenie na osi y (0-100): "))
            if Start_y>100 or Start_y<0:
                print("Podano złe dane")
                return KOORDY_Y(rozmiar_swiata)
            else:
                Start_y-=int(rozmiar_swiata/2)
                return Start_y
        except:
            print("Podano błędne wymiary")
            return KOORDY_Y(rozmiar_swiata)
    else:
        try:  
            Start_y = int(input("Podaj położenie na osi y (0-25): "))
            if Start_y>25 or Start_y<0:
                print("Podano złe dane")
                return KOORDY_Y(rozmiar_swiata)
            else:
                Start_y-=int(rozmiar_swiata/2)
                return Start_y
        except:
            print("Podano błędne wymiary")
            return KOORDY_Y(rozmiar_swiata)
def MAX_SPEED():
    try:  
        max_predkosc = int(input("Podaj maksymalną prędkość konia (5-25): "))
        if max_predkosc>25 or max_predkosc<5:
            print("Podano nieprawidłową prędkość")
            return MAX_SPEED()
        else:
            return max_predkosc
    except:
        print("Podano błędne wymiary")
        return MAX_SPEED()
def START_PLAYER():
    try:  
        start_player = int(input("Podaj startową ilość jedzenia gracza w %(10-100) : "))
        if start_player>100 or start_player<10:
            print("Podano nieprawidłową liczbę")
            return START_PLAYER()
        else:
            return start_player
    except:
        print("Podano błędne wymiary")
        return START_PLAYER()
def START_HORSE():
    try:  
        start_horse = int(input("Podaj startową ilość jedzenia konia w %(10-100) : "))
        if start_horse>100 or start_horse<10:
            print("Podano nieprawidłową liczbę")
            return START_HORSE()
        else:
            return start_horse
    except:
        print("Podano błędne wymiary")
        return START_HORSE()


def GRA():
    napotkane_miasta=0
    napotkani_przeciwnicy=0
    laki=0
    tornada=0
    tury_w_kaktusach=0
    Wygrana=False
    zmiany =[]
    odleglosc=0
    print("Kąty w tym programie są jak kąty na Kompasie, a nie jak w układzie współrzędnych w matematyce (0°-Północ, 90°-Wschód, 180°-Południe, 270°-Zachód)")
    poziom_trudnosci=POZIOM()
    rozmiar_swiata=ROZMIAR_SWIATA()
    Start_x=KOORDY_X(rozmiar_swiata)
    Start_y=KOORDY_Y(rozmiar_swiata)
    max_predkosc=MAX_SPEED()
    Jedzenie_gracza=START_PLAYER()
    Gracz0=Jedzenie_gracza
    Jedzenie_konia =START_HORSE()
    Kon_0=Jedzenie_konia
    miasta=MIASTECZKO(rozmiar_swiata,poziom_trudnosci)
    przeciwnicy=PRZECIWNIK(rozmiar_swiata,poziom_trudnosci)
    przeciwnicy_start = list(przeciwnicy)
    pozycja_x=Start_x
    pozycja_y = Start_y
    aktualna_predkosc=3
    liczba_krokow=150/poziom_trudnosci
    imie_konia = KON_NAZWA()
    imie_gracza = GRACZ_NAZWA()
    Pole=POLE(rozmiar_swiata,poziom_trudnosci)

    zjedzone_kon=0
    zjedzone_gracz=0


    Dom_x = (int((rozmiar_swiata-Start_x)/2)+random.randrange(0,50))
    if Dom_x>rozmiar_swiata*0.5:
        Dom_x=random.randrange(0,int(rozmiar_swiata*0.5))

    Dom_y=(int((rozmiar_swiata-Start_y)/2)+random.randrange(0,50))
    if Dom_y>rozmiar_swiata*0.5:
        Dom_y=random.randrange(0,int(rozmiar_swiata*0.5))

    print("Podróżujesz przez dziki zachód i nagle natrafiasz na zniszczone UFO a w nim plany na inwazję na świat")
    print("Musisz ich powstrzymać")
    print("Twoim celem jest dostanie się do białego domu aby móc się przygotować zanim kosmici zaatakują")
    print(f"Położenie celu {Dom_x+int(rozmiar_swiata*0.5)},{Dom_y+int(rozmiar_swiata*0.5)}")
    print(f"Twoje położenie {Start_x+int(rozmiar_swiata*0.5)},{Start_y+int(rozmiar_swiata*0.5)}")
    kat=KIERUNEK(zmiany)
    kat0=kat
    numer=0



    Przegrana = ""
    print("PARAMETRY WYPRAWY ")
    print(f"Gracz: {imie_gracza}, Koń: {imie_konia}")
    print(f"Poziom trudności: {poziom_trudnosci}")
    print(f"Rozmiar świata: {rozmiar_swiata}x{rozmiar_swiata}")
    print(f"Granice świata: 0 do {rozmiar_swiata}")
    print(f"Pozycja startowa: ({Start_x+int(rozmiar_swiata/2)}, {Start_y+int(rozmiar_swiata/2)})")
    print(f"Kąt startowy: {kat}°")
    print(f"Maksymalna prędkość: {max_predkosc}")
    print(f"Jedzenie gracza: {Jedzenie_gracza}%")
    print(f"Jedzenie konia: {Jedzenie_konia}%")
    print(f"Cel wyprawy: ({Dom_x+int(rozmiar_swiata*0.5)}, {Dom_y+int(rozmiar_swiata*0.5)})")
    print(f"Limit tur: {int(liczba_krokow)}")
    print(f"Warunek wygranej: dotrzeć do celu w limicie tur")
    print(f"Warunki przegranej: brak jedzenia gracza/konia, wyjście poza mapę, koniec tur")
    while True:
        numer+=1
        print(f"Tura {numer}")
        if Wygrana:
            break
        if liczba_krokow<=0:
            Przegrana="Czas"
            break
        if pozycja_x*2>rozmiar_swiata or pozycja_y*2>rozmiar_swiata or pozycja_x<int(-rozmiar_swiata/2 + 1) or pozycja_y<int(-rozmiar_swiata/2 + 1):
            Przegrana="Daleko"
            break
        zmiany.append(lambda: turtle.color('black'))
        print(f"Zostało {int(liczba_krokow)} tur")
        print(f"Jedzenie przed krokiem {imie_gracza}: {Jedzenie_gracza}%, {imie_konia}: {Jedzenie_konia}%")
        print(f"Pozycja przed ruchem: ({pozycja_x+int(rozmiar_swiata/2)}, {pozycja_y+int(rozmiar_swiata/2)})")
        aktualna_predkosc,kat,Jedzenie_gracza,Jedzenie_konia=WYBOR(aktualna_predkosc,kat,pozycja_x,pozycja_y,miasta,rozmiar_swiata,Jedzenie_gracza,Jedzenie_konia,max_predkosc,zmiany,Dom_x,Dom_y)
        pozycja_x += round(math.sin(math.radians(kat))*aktualna_predkosc)
        pozycja_y += round(math.cos(math.radians(kat))*aktualna_predkosc)
        zmiany.append(lambda x=pozycja_x,y=pozycja_y: turtle.goto(x,y))
        if random.randint(0,100)<=1*poziom_trudnosci:
            pozycja_x,pozycja_y,zmiany=TORNADO(rozmiar_swiata,zmiany)
            tornada+=1
        Jedzenie_konia,Jedzenie_gracza,zmiany,tury_w_kaktusach=KAKTUS(Pole,pozycja_x,pozycja_y,max_predkosc,Jedzenie_konia,Jedzenie_gracza,zmiany,tury_w_kaktusach)
        print(f"Koordynaty po ruchu({pozycja_x+int(rozmiar_swiata*0.5)},{pozycja_y+int(rozmiar_swiata*0.5)})")
            

        odleglosc+=aktualna_predkosc
        liczba_krokow-=1
        Jedzenie_gracza-=1*poziom_trudnosci
        zjedzone_gracz+=poziom_trudnosci
        Jedzenie_konia-=int(aktualna_predkosc*poziom_trudnosci*0.1) + 2*poziom_trudnosci
        zjedzone_kon+=int(aktualna_predkosc*poziom_trudnosci*0.1) + 2*poziom_trudnosci
        if random.randint(0,100)*poziom_trudnosci<=6:
            Jedzenie_konia,zmiany=LAKA(imie_konia,zmiany)
            laki+=1
        for mx,my in miasta:
            if abs(pozycja_x - mx) <= max_predkosc and abs(pozycja_y - my) <= max_predkosc:
                Jedzenie_gracza=100
                Jedzenie_konia=100
                print("Jesteś w mieście")
                napotkane_miasta+=1
                zmiany.append(lambda: turtle.color("yellow"))
                zmiany.append(lambda: turtle.stamp())
                zmiany.append(lambda: turtle.color("black"))
        liczba_krokow,Jedzenie_gracza,przeciwnicy,zmiany,napotkani_przeciwnicy=WALKA(liczba_krokow,Jedzenie_gracza,przeciwnicy,pozycja_x,pozycja_y,poziom_trudnosci,zmiany,max_predkosc,napotkani_przeciwnicy)
        print(f"{imie_gracza} ma {Jedzenie_gracza}% Jedzenia,{imie_konia} ma {Jedzenie_konia}% Jedzenia")
        if Jedzenie_konia<=0:
            Przegrana="Koń"
            break
        if Jedzenie_gracza<=0:
            Przegrana="Gracz"
            break
        if abs(pozycja_x - Dom_x) <= 15 and abs(pozycja_y - Dom_y)<= 15:
            Wygrana=True
            break
    if Wygrana:
        print("WYGRAŁEŚ, OCALIŁEŚ ŚWIAT PRZED KOSMITAMI")
        if poziom_trudnosci==1:
            print("Grałeś na łatwym trybie trudności")
        if poziom_trudnosci==2:
            print("Grałeś na średnim trybie trudności")
        if poziom_trudnosci==3:
            print("Grałeś na trudnym trybie trudności")
        print(f"Zacząłeś z {Gracz0}% punktów jedzenia gracza i {Kon_0}% punktów jedzenia konia")
        print(f"Pokonałeś {odleglosc} jednostek odleglosci")
        print(f"Napotkałeś {napotkane_miasta} miast/miasta,{napotkani_przeciwnicy} przeciwnika/przeciwników,{tornada} tornad, {laki} łąk i spędziłeś {tury_w_kaktusach} w polu kaktusów")
        print(f"Zacząłeś w {Start_x,Start_y}, a skończyłeś {pozycja_x,pozycja_y}")
        print(f"Twój kąt początkowy to był {kat0}")
        print(f"Zajęło ci to {150/poziom_trudnosci-liczba_krokow}")
        print(f"Koń o imieniu {imie_konia} zjadł {zjedzone_kon} jedzenia")
        print(f"Gracz {imie_gracza} zjadł {zjedzone_gracz} jedzenia")
        print(f"Twoje przemieszczenie wynosi około {round(math.sqrt((Start_x-pozycja_x)**2+(Start_y-pozycja_y)**2))}")
        RYSUNEK(rozmiar_swiata,Pole,przeciwnicy_start,miasta,zmiany,Start_x,Start_y)
        turtle.color("blue")
        turtle.shape("square")
        turtle.stamp()
        turtle.mainloop()
        time.sleep(1)

    elif Przegrana=="Koń":
        print("Koń padł z głodu - Przegrałeś")
        if poziom_trudnosci==1:
            print("Grałeś na łatwym trybie trudności")
        if poziom_trudnosci==2:
            print("Grałeś na średnim trybie trudności")
        if poziom_trudnosci==3:
            print("Grałeś na trudnym trybie trudności")
        print(f"Zacząłeś z {Gracz0}% punktów jedzenia gracza i {Kon_0}% punktów jedzenia konia")
        print(f"Napotkałeś {napotkane_miasta} miast/miasta,{napotkani_przeciwnicy} przeciwnika/przeciwników,{tornada} tornad, {laki} łąk i spędziłeś {tury_w_kaktusach} w polu kaktusów")
        print(f"Zacząłeś w {Start_x,Start_y}, a skończyłeś {pozycja_x,pozycja_y}")
        print(f"Twój kąt początkowy to był {kat0}")
        print(f"Pokonałeś {odleglosc} jednostek odleglosci")
        print(f"Przeżyłeś {int(150/poziom_trudnosci-liczba_krokow)} tur" )
        print(f"Koń o imieniu {imie_konia} zjadł {zjedzone_kon} jedzenia")
        print(f"Gracz {imie_gracza} zjadł {zjedzone_gracz} jedzenia")
        print(f"Twoje przemieszczenie wynosi około{round(math.sqrt((Start_x-pozycja_x)**2+(Start_y-pozycja_y)**2))}")
        RYSUNEK(rozmiar_swiata,Pole,przeciwnicy_start,miasta,zmiany,Start_x,Start_y)
        turtle.color("red2")
        turtle.shape("square")
        turtle.stamp()
        turtle.mainloop()
        time.sleep(1)
    elif Przegrana=="Gracz":
        print("Gracz padł z głodu- przegrana")
        if poziom_trudnosci==1:
            print("Grałeś na łatwym trybie trudności")
        if poziom_trudnosci==2:
            print("Grałeś na średnim trybie trudności")
        if poziom_trudnosci==3:
            print("Grałeś na trudnym trybie trudności")
        print(f"Zacząłeś z {Gracz0}% punktów jedzenia gracza i {Kon_0}% punktów jedzenia konia")
        print(f"Napotkałeś {napotkane_miasta} miast/miasta,{napotkani_przeciwnicy} przeciwnika/przeciwników,{tornada} tornad, {laki} łąk i spędziłeś {tury_w_kaktusach} w polu kaktusów")
        print(f"Zacząłeś w {Start_x,Start_y}, a skończyłeś {pozycja_x,pozycja_y}")
        print(f"Twój kąt początkowy to był {kat0}")
        print(f"Pokonałeś {odleglosc} jednostek odleglosci")
        print(f"Przeżyłeś {int(150/poziom_trudnosci-liczba_krokow)} tur" )
        print(f"Koń o imieniu {imie_konia} zjadł {zjedzone_kon} jedzenia")
        print(f"Gracz {imie_gracza} zjadł {zjedzone_gracz} jedzenia")
        print(f"Twoje przemieszczenie wynosi około{round(math.sqrt((Start_x-pozycja_x)**2+(Start_y-pozycja_y)**2))}")
        RYSUNEK(rozmiar_swiata,Pole,przeciwnicy_start,miasta,zmiany,Start_x,Start_y)
        turtle.color("red2")
        turtle.shape("square")
        turtle.stamp()
        turtle.mainloop()
        time.sleep(1)
    elif Przegrana=="Daleko":
        print("Wyszedłeś poza mapę- Przegrałeś")
        if poziom_trudnosci==1:
            print("Grałeś na łatwym trybie trudności")
        if poziom_trudnosci==2:
            print("Grałeś na średnim trybie trudności")
        if poziom_trudnosci==3:
            print("Grałeś na trudnym trybie trudności")
        print(f"Zacząłeś z {Gracz0}% punktów jedzenia gracza i {Kon_0}% punktów jedzenia konia")
        print(f"Napotkałeś {napotkane_miasta} miast/miasta,{napotkani_przeciwnicy} przeciwnika/przeciwników,{tornada} tornad, {laki} łąk i spędziłeś {tury_w_kaktusach} w polu kaktusów")
        print(f"Zacząłeś w {Start_x,Start_y}, a skończyłeś {pozycja_x,pozycja_y}")
        print(f"Twój kąt początkowy to był {kat0}")
        print(f"Pokonałeś {odleglosc} jednostek odleglosci")
        print(f"Przeżyłeś {int(150/poziom_trudnosci-liczba_krokow)} tur" )
        print(f"Koń o imieniu {imie_konia} zjadł {zjedzone_kon} jedzenia")
        print(f"Gracz {imie_gracza} zjadł {zjedzone_gracz} jedzenia")
        print(f"Twoje przemieszczenie wynosi około{round(math.sqrt((Start_x-pozycja_x)**2+(Start_y-pozycja_y)**2))}")
        RYSUNEK(rozmiar_swiata,Pole,przeciwnicy_start,miasta,zmiany,Start_x,Start_y)
        turtle.color("red2")
        turtle.shape("square")
        turtle.stamp()
        turtle.mainloop()
        time.sleep(1)
    elif Przegrana=="Czas":
        print("Skończył ci się czas - Przegrana")
        if poziom_trudnosci==1:
            print("Grałeś na łatwym trybie trudności")
        if poziom_trudnosci==2:
            print("Grałeś na średnim trybie trudności")
        if poziom_trudnosci==3:
            print("Grałeś na trudnym trybie trudności")
        print(f"Zacząłeś z {Gracz0}% punktów jedzenia gracza i {Kon_0}% punktów jedzenia konia")
        print(f"Napotkałeś {napotkane_miasta} miast/miasta,{napotkani_przeciwnicy} przeciwnika/przeciwników,{tornada} tornad, {laki} łąk i spędziłeś {tury_w_kaktusach} w polu kaktusów")
        print(f"Zacząłeś w {Start_x,Start_y}, a skończyłeś {pozycja_x,pozycja_y}")
        print(f"Twój kąt początkowy to był {kat0}")
        print(f"Pokonałeś {odleglosc} jednostek odleglosci")
        print(f"Przeżyłeś {150/poziom_trudnosci-liczba_krokow} tur" )
        print(f"Koń o imieniu {imie_konia} zjadł {zjedzone_kon} jedzenia")
        print(f"Gracz {imie_gracza} zjadł {zjedzone_gracz} jedzenia")
        print(f"Twoje przemieszczenie wynosi około{round(math.sqrt((Start_x-pozycja_x)**2+(Start_y-pozycja_y)**2))}")
        RYSUNEK(rozmiar_swiata,Pole,przeciwnicy_start,miasta,zmiany,Start_x,Start_y)
        turtle.color("red2")
        turtle.shape("square")
        turtle.stamp()
        turtle.mainloop()
        time.sleep(1)
    else:
        print("Przegrałeś z nieznanego powodu")
        if poziom_trudnosci==1:
            print("Grałeś na łatwym trybie trudności")
        if poziom_trudnosci==2:
            print("Grałeś na średnim trybie trudności")
        if poziom_trudnosci==3:
            print("Grałeś na trudnym trybie trudności")
        print(f"Zacząłeś z {Gracz0}% punktów jedzenia gracza i {Kon_0}% punktów jedzenia konia")
        print(f"Napotkałeś {napotkane_miasta} miast/miasta,{napotkani_przeciwnicy} przeciwnika/przeciwników,{tornada} tornad, {laki} łąk i spędziłeś {tury_w_kaktusach} w polu kaktusów")
        print(f"Zacząłeś w {Start_x,Start_y}, a skończyłeś {pozycja_x,pozycja_y}")
        print(f"Twój kąt początkowy to był {kat0}")
        print(f"Pokonałeś {odleglosc} jednostek odleglosci")
        print(f"Przeżyłeś {150/poziom_trudnosci-liczba_krokow} tur" )
        print(f"Koń o imieniu {imie_konia} zjadł {zjedzone_kon} jedzenia")
        print(f"Gracz {imie_gracza} zjadł {zjedzone_gracz} jedzenia")
        print(f"Twoje przemieszczenie wynosi około{round(math.sqrt((Start_x-pozycja_x)**2+(Start_y-pozycja_y)**2))}")
        RYSUNEK(rozmiar_swiata,Pole,przeciwnicy_start,miasta,zmiany,Start_x,Start_y)
        turtle.color("red2")
        turtle.shape("square")
        turtle.stamp()
        turtle.mainloop()
        time.sleep(1)
    while True:
        ponownie = input("Czy chcesz zagrać ponownie? (T/N): ").upper()
        if ponownie == "T":
            GRA()
            break
        elif ponownie == "N":
            print("Dziękuję za rozgrywkę!")
            return(False)
        else:
            print("Podano złą odpowiedź")
    
grac_dalej=GRA()

