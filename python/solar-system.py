#! /usr/bin/python

words = open( 'english-words.txt','r' ).readlines()
planets = open( 'planets.txt','r' ).readlines()

for planet in planets:
    word_count = 0
    planet = planet.strip()
    for word in words:
        word = word.strip()
        if word in planet and word_count > 0:
            print( "\033[92m\033[1m" + planet + "\033[0m" )
        elif word in planet:
            print( planet )
            word_count += 1

