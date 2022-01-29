"""
Ohjelmointi 1: tehtävä 2.7: Fibonaccin lukusarja
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def main():
    lukujen_maara = int(input("How many Fibonacci numbers do you want? "))
    fibonacci = 1
    print(f"1. {fibonacci} \n2. {fibonacci}")

    edellinen_fib = 1
    sita_edellinen_fib = 1

    rivinumero = 3

    for _ in range(lukujen_maara-2):
        fibonacci = edellinen_fib + sita_edellinen_fib
        print(f"{rivinumero}. {fibonacci}")
        sita_edellinen_fib = edellinen_fib
        edellinen_fib = fibonacci
        rivinumero += 1

if __name__ == "__main__":
    main()