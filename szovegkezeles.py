def szepnapvan():
    szoveg: str = "Szép nap van"

    '''Írd ki  a szöveget első karakterét'''

    print(szoveg[0])
    '''Írd ki  a szöveget 2. karakterét!'''
    print(szoveg[1])
    '''Írd ki  a szöveget hosszát'''
    print("A hossz: ",len([szoveg]))
    ''''Írd ki a szöveg utolsó karakterét'''
    print("utolsó",szoveg[len(szoveg)-1])

    """ írd ki a aszöveg karaktereit egymás alá betűnként """
    i:int = 0
    while i < len(szoveg):
        print(szoveg[i])

        i += 1

def szovegkezeles():
    szoveg:str = "Ez egy teszt szoveg."
    print(szoveg)
    print(szoveg.upper)
    """ Van e a szövegben 'teszt' szöveg"""
    """SZÖVEG VÁLTOZÓBAN hol szerepel a s betű? """
    '''Alakítsd át minden szó kezdőbetűjét nagybetűssé!'''
    """Cseréld ki a a teszt szót próbá-ra!"""

    
    x:int = szoveg.find("teszt")
    if x >= 0:
        print("igaz")
    else:
        print("hamis") 

    print(szoveg.index("s")), " helyen szerepele s betű"
    print(szoveg.title())
    print(szoveg.replace)("teszt", "próba")


    def aszoveg_visszafele(szoveg:str):
        '''A paramtéterben kapott szöveg visszafelé kiírva egymás mellé a betű'''
    # print(szoveg[::-1])
    i:int= len(szoveg)
    while i!=0:
        print(szoveg[i-1],end "")
        i -=1
    '''Hány "a" betű van a szövegben?'''
    def a_betuk_szama(szoveg:str):
        # print(szoveg.count("a"))
        i:int =0
        a_szam:int =0
        while i<len(szoveg):
            if szoveg[i] == 'a':
                a_szam += 1
            i += 1
        print("Abetűk száma: ", a_szam)    
    
    
