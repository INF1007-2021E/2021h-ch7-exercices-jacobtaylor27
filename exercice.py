#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import turtle

# TODO: Définissez vos fonction ici
def trouverMasseVolume(a = 3, b = 2, c = 5, mv = 16):
    volume = (4/3) * math.pi * a*b*c
    mass = mv * volume
    return mass, volume 

def freq(sentence):
    count = {}
    for l in sentence:
        if l in count:
            count[l] += 1
        else:
            count[l] = 1
    count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}
    for i in count.items():
        if i[1] >= 5:
            count[i[0]] = i[1]
    return count

x = lambda dic : "La lettre la plus férquente est " + list(dic.keys())[0]

def tree(len, t):
    if len > 5:
        t.forward(len)
        t.right(25)
        tree(len - 15, t)
        t.left(50)
        tree(len - 15, t)
        t.right(25)
        t.backward(len)

def drawTree():
    t = turtle.Turtle()
    écran = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.width(3)
    tree(90,t)
    écran.exitonclick()

def valide(str):
    for c in str:
        if str or c == "g" or c == "t" or c == "a" or c == "c":
            return True
        else:
            return False

def saisie():
    val = ""
    while not valide(val):
        val = input("entrez des caractères: ")
    return val

def proportion(chaine, seq):
    return (chaine.count(seq) / len(chaine)) * 100 

def adn():
    chaine = saisie()
    séquence = saisie()
    print(f"""chaîne : {chaine}\nséquence : {séquence}\nIl y a {round(proportion(chaine, séquence),2)} % de "{séquence}" """)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(trouverMasseVolume(2,4,5,5))
    print(x(freq("salut les amis")))
    drawTree()
    adn()