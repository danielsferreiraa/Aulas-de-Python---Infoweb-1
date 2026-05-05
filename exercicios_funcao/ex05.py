def letras_na_palavra(p, l):
    if len(l) == 1:
       return p.count(l)
    else:
        return "ERRO"

rep = 0

while rep != 3:
    palavra = input("Digite uma palavra: ")
    letra = input("Digite uma letra: ")
    print(letras_na_palavra(palavra, letra))
    rep += 1
