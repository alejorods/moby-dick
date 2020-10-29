# Guía 3 - Ejercicio 6 (INGLÉS).
print("Guía 3 - Ejercicio 6 (INGLÉS).")

import numpy as np

file_en = open('Moby_Dick_EN.txt', 'r')

md_en = file_en.read()

total = len(md_en)
print()
print("Moby Dick en inglés tiene", total, "caracteres.")

print()
print("Ítem (b)")
#Ítem (b).

dict_1 = {}

for i in md_en:                                #Lista cuántas veces aparece cada caracter en Moby Dick en inglés.
    if i in dict_1:
        dict_1[i] = dict_1[i] + 1
    else:
        dict_1[i] = 1

print()
print("La distribución de caracteres es:")
print(dict_1)                           

probs_1 = {}

for i in dict_1:                               #Lista la probabilidad por caracter en Moby Dick en inglés.
    probs_1[i] = dict_1[i]/total

print()
print("La probabilidad por caracter es:")
print(probs_1)                          
values_1 = probs_1.values()
total_probs_1 = sum(values_1)                    #Verifica que la suma de las probabilidades es igual uno.
print()
print("La suma de las probabilidades es:")
print(total_probs_1)

s_1 = 0
for i in dict_1:                               #Calcula la entropía por caracter usando la aproximación de orden uno.
    entropy_1 = -probs_1[i]*np.log2(probs_1[i])
    s_1 = s_1 + entropy_1

print()
print("La entropía por caracter de Moby Dick en inglés, medida en bits es:")
print(s_1)

print()
print("Ítem (c)")
#Ítem (c)

dict_2 = {}

for i in range(0,len(md_en)):                  #Lista cuántas veces aparece cada bigrama en Moby Dick en inglés.
    bigram = md_en[i:i+2]
    if bigram in dict_2:
        dict_2[bigram] = dict_2[bigram] + 1
    else:
        dict_2[bigram] = 1

print()
print("La distribución de bigramas es:")
print(dict_2)

probs_2 = {}

for i in dict_2:                               #Lista la probabilidad por bigrama en Moby Dick en inglés.
    probs_2[i] = dict_2[i]/total

print()
print("La probabilidad por bigrama es:")
print(probs_2)                          
values_2 = probs_2.values()
total_probs_2 = sum(values_2)                    #Verifica que la suma de las probabilidades es igual uno.
print()
print("La suma de las probabilidades es:")
print(total_probs_2)

s_2 = 0
for i in dict_2:                               
    entropy_2 = -probs_2[i]*np.log2(probs_2[i])
    s_2 = s_2 + entropy_2
s_2 = s_2 - s_1                                #Calcula la entropía por bigrama.

print()
print("La entropía por caracter de Moby Dick en inglés para bigramas, medida en bits es:")
print(s_2)

print()
print("Ítem (d)")
#Ítem (d)

dict_3 = {}

for i in range(0,len(md_en)):                  #Lista cuántas veces aparece cada trigrama en Moby Dick en inglés.
    trigram = md_en[i:i+3]
    if trigram in dict_3:
        dict_3[trigram] = dict_3[trigram] + 1
    else:
        dict_3[trigram] = 1

print()
print("La distribución de trigramas es:")
print(dict_3)

probs_3 = {}

for i in dict_3:                               #Lista la probabilidad por trigrama en Moby Dick en inglés.
    probs_3[i] = dict_3[i]/total

print()
print("La probabilidad por trigrama es:")
print(probs_3)                          
values_3 = probs_3.values()
total_probs_3 = sum(values_3)                    #Verifica que la suma de las probabilidades es igual uno.
print()
print("La suma de las probabilidades es:")
print(total_probs_3)

s_3 = 0
for i in dict_3:                               
    entropy_3 = -probs_3[i]*np.log2(probs_3[i])
    s_3 = s_3 + entropy_3
s_3 = s_3 - s_2 - s_1                                #Calcula la entropía por trigrama.

print()                            
print("La entropía por caracter de Moby Dick en inglés para trigramas, medida en bits es:")
print(s_3)

print()
print("Ítem (e)")
#Ítem (e)

import random

letters = 'abcdefghijklmnopqrstuvwxyz '
text = ''.join((random.choice(letters) for i in range(total))) 
#Genera un texto aleatorio con distribución uniforme con la cantidad de caracteres totales de Moby Dick.

dict_E1 = {}

for i in text:                                
    if i in dict_E1:
        dict_E1[i] = dict_E1[i] + 1
    else:
        dict_E1[i] = 1

probs_E1 = {}

for i in dict_E1:                               
    probs_E1[i] = dict_E1[i]/total

# values_E1 = probs_E1.values()
# total_probs_E1 = sum(values_E1)                    
# print("La suma de las probabilidades es:")
# print(total_probs_E1)

s_E1 = 0
for i in dict_E1:                               
    entropy_E1 = -probs_E1[i]*np.log2(probs_E1[i])
    s_E1 = s_E1 + entropy_E1

print()
print("La entropía por caracter del texto aleatorio, medida en bits es:")
print(s_E1)

dict_E2 = {}

for i in range(0,total):                  
    bigram_E2 = text[i:i+2]
    if bigram_E2 in dict_E2:
        dict_E2[bigram_E2] = dict_E2[bigram_E2] + 1
    else:
        dict_E2[bigram_E2] = 1

probs_E2 = {}

for i in dict_E2:                           
    probs_E2[i] = dict_E2[i]/total

# values_E2 = probs_E2.values()
# total_probs_E2 = sum(values_E2)                 
# print("La suma de las probabilidades es:")
# print(total_probs_E2)

s_E2 = 0
for i in dict_E2:                               
    entropy_E2 = -probs_E2[i]*np.log2(probs_E2[i])
    s_E2 = s_E2 + entropy_E2
s_E2 = s_E2 - s_E1

print()
print("La entropía por caracter del texto aleatorio para bigramas, medida en bits es:")
print(s_E2)

dict_E3 = {}

for i in range(0,total):                
    trigram_E3 = text[i:i+3]
    if trigram_E3 in dict_E3:
        dict_E3[trigram_E3] = dict_E3[trigram_E3] + 1
    else:
        dict_E3[trigram_E3] = 1

probs_E3 = {}

for i in dict_E3:                               
    probs_E3[i] = dict_E3[i]/total

# values_E3 = probs_E3.values()
# total_probs_E3 = sum(values_E3)                    
# print("La suma de las probabilidades es:")
# print(total_probs_E3)

s_E3 = 0
for i in dict_E3:                               
    entropy_E3 = -probs_E3[i]*np.log2(probs_E3[i])
    s_E3 = s_E3 + entropy_E3
s_E3 = s_E3 - s_E2 - s_E1                                

print()
print("La entropía por caracter del texto aleatorio para trigramas, medida en bits es:")
print(s_E3)
