#### Fonction secondaire
"""
author: marie-emilienne.gnamien@edu.esiee.fr

"""

def ispalindrome(p):
    """
    Détermine si la chaine de caracteres entrée est un palindrome.

    Args:
    
    p: chaine de caracteres

    Returns: Une valeur booléenne

    """

    p = p.lower()
    intab = 'éèêîôùàçë'
    outab = 'eeeiouace'
    trantab = str.maketrans(intab,outab)
    chsp = "?,.;:!'-"
    p = p.translate(trantab)
    pspace = '' #chaine de caractères p sans espaces
    chainefinale = '' #chaine de caractères p à l'envers

    if not ' ' in p: #cas où on a une chaîne sans espaces
        s = p[::-1]
        if s == p:
            return True

    elif ' ' in p: #cas où on a une chaine de caractères avec espaces
        for c in p:
            if c == ' ' or c in chsp:
                continue
            pspace += c
        for c in p[::-1]:
            if c == ' ' or c in chsp:
                continue
            chainefinale += c

        if chainefinale == pspace:
            return True

    return False


#### Fonction principale
def main():
    """
    S'occupe des appels à la fonction secondaire

    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
