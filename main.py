from membresia import Gratis  # o como se llame tu archivo principal de clases  

def mostrar_menu():
    print("\n--- Bienvenido a la plataforma de streaming ---")
    print("1. Cambiar a Membresía Básica")
    print("2. Cambiar a Membresía Familiar")
    print("3. Cambiar a Membresía Sin Conexión")
    print("4. Cambiar a Membresía Pro")
    print("5. Salir")

def mostrar_detalles(membresia):
    print("\n--- Detalles de tu membresía actual ---")
    print(f"Tipo de membresía: {membresia.__class__.__name__}")
    print(f"Correo: {membresia.correo_suscriptor}")
    print(f"Número de tarjeta: {membresia.numero_tarjeta}")
    print(f"Dispositivos permitidos: {membresia.dispositivos}")
    print(f"Costo mensual: ${membresia.costo}")

    # Verificar si tiene días de regalo
    if hasattr(membresia, 'dias_regalo'):
        print(f"Días de regalo: {membresia.dias_regalo}")

if __name__ == "__main__":
    correo = input("Ingresa tu correo electrónico: ")
    tarjeta = input("Ingresa el número de tu tarjeta: ")

    # Se crea la membresía inicial: Gratis
    suscripcion = Gratis(correo, tarjeta)
    mostrar_detalles(suscripcion)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion in ['1', '2', '3', '4']:
            suscripcion = suscripcion.cambiar_suscripcion(int(opcion))
            mostrar_detalles(suscripcion)
        elif opcion == '5':
            print("Gracias por usar la plataforma. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")