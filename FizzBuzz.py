i = 0

while i < 100:  # indico que el ciclo se termine en cuanto i>100
    i = i+1  # le sumo 1 en cada ciclo sino seria infinito
    if i % 3 == 0 and i % 5 == 0:  # declaro todo lo que quiero que pase cuando x condicion paseS
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)
