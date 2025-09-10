from suma import sumar
from resta import restar
from multiplicacion import multiplicar
from division import dividir

def obtener_numeros():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        return a, b
    except ValueError:
        print("Error: Entrada inválida. Intente de nuevo.")
        return None, None

def menu():
    while True:
        print("\n--- CALCULADORA ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "5":
            print("Saliendo de la calculadora.")
            break

        a, b = obtener_numeros()
        if a is None or b is None:
            continue

        if opcion == "1":
            resultado = sumar(a, b)
        elif opcion == "2":
            resultado = restar(a, b)
        elif opcion == "3":
            resultado = multiplicar(a, b)
        elif opcion == "4":
            resultado = dividir(a, b)
        else:
            print("Opción inválida. Intente de nuevo.")
            continue

        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    menu()

