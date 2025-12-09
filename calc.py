# Calculadora para proyecto Docker + GitHub CI/CD
def calcular():
    print("Bienvenido a mi proyecto de Docker!")

    print("=== Calculadora en Docker ===")
    operacion = input("Ingresa una operación (ej: 5+3): ")
    if operacion.strip() == "":
        print("No ingresaste nada")
        return

    try:
        resultado = eval(operacion)
        print("\033[92mResultado:", resultado, "\033[0m")
    except:
        print("Error: operación inválida")

if __name__ == "__main__":
    calcular()