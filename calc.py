# Calculadora para proyecto Docker + GitHub CI/CD
def calcular():
    print("=== Calculadora en Docker ===")
    operacion = input("Ingresa una operación (ej: 5+3): ")

    try:
        resultado = eval(operacion)
        print("Resultado:", resultado)
    except:
        print("Error: operación inválida")

if __name__ == "__main__":
    calcular()