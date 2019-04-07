import math

print("""
      =6=4=1=7=9=0=2=5=3==================================
                 =Automatischer Taschenrechner=
      =====================================0=1=1=0=1=0=0=1
Dieser Rechner addiert, subtrahiert, multipliziert, dividert, \n\
errechnet die Potenz der ersten Zahl durch die zweite Zahl (Potenz / x^y), \n\
dividiert die erste Zahl durch die zweite Zahl mit Rest (Modulo / a=b*c+r), \n\
errechnet den größten gemeinsamen Teiler, \n\
den kleinsten gemeinsamen Vielfachen, \n\
die Wurzel aus beiden Zahlen,\n\
ob beide Zahlen Primzahlen sind\n\
auf einmal, mit deinen im folgenden anzugebenen Zahlen
    """)

while True:
    try:
        num1 = int(input("Gib die erste Zahl ein: "))
        break
    except ValueError:
        print("Du brauchst eine Zahl.")

while True:
    try:
        num2 = int(input("Gib die zweite Zahl ein: "))
        break
    except ValueError:
        print("Du brauchst eine Zahl.")

summe1 = num1+num2                           # Addition
summe2 = num1-num2                           # Subtraktion
summe3 = num1*num2                           # Multiplikation
summe4 = num1/num2                           # Division
summe5 = num1**num2                          # Potenz x hoch y
summe6 = num1%num2                           # Division mit Rest (Modulo)
summe7 = math.gcd(num1, num2)                # größter gemeinsamer Teiler von x und y
summe8 = num1*num2/math.gcd(num1, num2)      # kleinestes gemeinsames Vielfaches von x und y
summe9 = math.sqrt(num1)                     # Wurzel aus Zahl1
summe10 = math.sqrt(num2)                    # Wurzel aus Zahl2


print(num1, " + ", num2, "=", summe1, "\n", "___", "\n")
print(num1, " - ", num2, "=", summe2, "\n", "___", "\n")
print(num1, " * ", num2, "=", summe3, "\n", "___", "\n")
print(num1, " / ", num2, "=", summe4, "\n", "___", "\n")
print(num1, " mit Potenz ", num2, "=", summe5, "\n", "___", "\n")
print(num1, " / ", num2, "=", summe4, "+ Rest", summe6, " \n", "___", "\n")
print(num1, " und ", num2, " sind beide durch ", summe7, "teilbar (ggT) \n", "___", "\n")
print(num1, " * ", num2, "=", summe3, "/", summe7, "=", summe8, " (kgV)\n", "___", "\n")
print("Quadratwurzel von", num1, "=", summe9, "\n", "___", "\n")
print("Quadratwurzel von", num2, "=", summe10, "\n", "___", "\n")

# Primzahl#
if num1 >1:
     for x in range(2, num1):
          if (num1 % x) == 0:
            print(num1, "ist keine Primzahl\n", "___", "\n")
            break
     else:
          print (num1, "ist eine Primzahl\n", "___", "\n")
else:
   print(num1,"ist keine Primzahl\n", "___", "\n")

# Collatz
def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(number)
        return result

n1 = num1
while n1 != 1:
    n1 = collatz(int(n1))


# In Fibonacci Count?
def is_fibonacci(n1):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n1
    return n == 0 or abs(round(a) - a) < 1.0 / n1
print(n1)

