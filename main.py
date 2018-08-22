#Programme python d'une calculatrice

from console import *
	
""" Variables globale """
calcul = ""
operators = ['/','*','+','-']
w = 55

""" Fonctions de gestion de la calculatrice """
def indicator(pos): # Imprime une bar
	i = 0
	line = ""
	size = len(calcul)
	while i < size:
		if i == pos :
			line += '^'
		else : 
			line += ' '
		i += 1	
	print(calcul)
	print(line)

def check_calcul_validate():
	'''
	Fonction vérifiant la validée du calcul
	'''
	no_err = True
	limit = len(calcul) -1
	
	for i, v in enumerate(calcul) :
	
		j = i+1		
		
		if v in operators and i != limit:
			if calcul[j] in operators :
				print("Erreur de syntaxe : Deux operateurs se suivent")
				indicator(j)
				no_err = False	
		elif not v in operators and v != " ":
			try :
				int(v)
			except ValueError:
				print("Erreur de syntaxe : Il y'a un caractère dans le calcul")
				indicator(i)
				no_err = False
				break
		elif(v in operators and i == limit):
			print("Erreur de syntaxe : Il y'a un opérateur en trop")
			indicator(limit)
			no_err = False	
					
	return no_err

def get_calcul_data():
	'''
	Fonction qui extrait les composants du calcul
	'''
	
	cal = calcul
	
	start = current_pos_operator = 0
	tab = []
	
	first_operator = True
	
	cal = del_space(cal)
			
	for i, operator  in enumerate(cal) :
	
		if operator in operators:
		
			if first_operator:
				first_operator = False
				start = 0
			else:
				start = current_pos_operator + 1
			
			current_pos_operator = i
						
			tab.append(cal[start:i])
			tab.append(cal[i])
				
	tab.append(cal[(current_pos_operator + 1):len(cal)])
	
	return tab
	
def operation(p,x,y):
	'''
	Fonction gérant les calculs elementaires en tenant compte de le priorite
	'''
	x = float(x)
	y = float(y)
	
	if p == 0:
		return x / y
	elif p == 1:
		return x * y
	elif p == 2:
		return x + y
	else:
		return x - y
	
def start_calcul():
	'''
	Fonction effectuant le calcul
	'''
	
	i = 0
	j = 0
	step = 1
	prioroty_level = 0
		
	tab = get_calcul_data()
		
	while(prioroty_level != 4): 
			
		if(tab[i] == operators[j]):

			try:
				tab[i - 1] = operation(prioroty_level,tab[i - 1],tab[i + 1])
			except ZeroDivisionError:
				return "math_error"
				
			del tab[i + 1]
			del tab[i]
			
			i -= 1
							
		if not operators[j] in tab:
			i = 0
			j += 1
			prioroty_level += 1
		else:
			i += step
			
	return tab[0] 
	
	
""" Main """	

os.system("mode con cols=55 lines=30")	
os.system("title MiniCalco v1") 										
clear_console()
go = True

print("\n\t\tBienvenue sur MiniCalco")
bar(w)

while go :
	calcul = str(input("-> "))
	
	if calcul == "None": 
		go = False
	else : 
		clear_console()

		print("\n\t\t\tMiniCalco"); bar(w)

		if check_calcul_validate() : # On verifie la validité du calcul
			
			result = start_calcul() # Lancement du calcul
			
			if(result == "math_error"):
				display = "    Math Error"
			else :
				display = "-> " + str(result)
				
			print("  ",calcul)
			bar(w)
			print(display)
			bar(w)

		else :
			bar(w)		
