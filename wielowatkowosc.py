# -*- coding: utf-8 -*-

import thread   # importowanie biblioteki wątków 
import time		# importowanie biblioteki czasu

# definiowanie funkcji dla wątku 
def print_time( threadName, delay): # definiowanie wątku, wypisanie czasu, delay mamy po to, aby wątki nie wykonywały się wszystkie jednocześnie 
    count = 0 # licznik wywołania wątku, 0, ponieważ liczy on w górę 
    while count < 7: # count liczy ilość wywołań wątku 
      time.sleep(delay) # ustawienie uśpienia na delay
      count += 1 # zwiększamy licznik o 1, żeby mógł się skończyć
      print"%s: %s" %( threadName, time.ctime(time.time())) # wypisanie łancuchów znakowych, czyli daty i godziny

def print_text( threadName, delay): # definiowanie wątku, wypisanie tekstu
    count = 0
    while count < 7:
      time.sleep(delay)
      count += 1
      print"%s: %s" %( threadName, "wielowatkowosc")

      
# Stworzenie czterech wątków
try:
    thread.start_new_thread( print_time,("Thread-1",2,)) # stworzenie nowego wątku o pobranej wcześniej nazwie oraz podanym uśpieniu
    thread.start_new_thread( print_text,("Thread-2",4,))
    thread.start_new_thread( print_time,("Thread-3",6,))
    thread.start_new_thread( print_text,("Thread-4",7,))
except:
    print"Błąd: Wątki nie mogą wystartować"
while 1:
    pass

# gdy wątki nie mogą się wykonać pokazuje się tekst
