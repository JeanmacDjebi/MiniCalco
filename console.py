""" Module gerant l'affichage console """
import os

def clear_console(): # Nettoyage de la console
	os.system("cls")
	
def pause_message(mss): # Mise en pause de la console
	clear_console()
	return input(mss)
	
def space(n = 1): # Création d'espace
	i = 0
	while i < n :
		print("\n")
		i += 1

def del_space(str): # Supprime les espaces
	return  str.replace(' ','')
	
def bar(width): # Imprime une bar
	i = 0
	line = ""
	while i < width:
		line += "-"
		i += 1	
	print(line)

def breakpoint(v=""): # Bloquer l'execution d'un programme pour deboggage
	print(v)
	os.system("pause")
