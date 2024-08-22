def main():
    perros = []
    
    while True:
        nombre = input("Ingrese el nombre del perro (máximo 8 caracteres): ")
        if len(nombre) > 8:
            print("El nombre no debe tener más de 8 caracteres. Intente de nuevo.")
            continue
        
        try:
            peso = float(input("Ingrese el peso del perro en kg: "))
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico válido para el peso.")
            continue
        
        perros = perros(nombre, peso)
        print(perros.registrar())
    
        perros.append(perros)
        
        continuar = input("¿Desea registrar otro perro? (s/n): ")
        if continuar.lower() != 's':
            break
    
    # Mostrar la información de todos los perros registrados
    print("\n--- Información de los Perros Registrados ---")
    for p in perros:
        print(f"Nombre: {p.nombre}, Peso: {p.peso}kg, Clasificación: {p.clasificacion}, Estado: {p.estado}")

if __name__ == "__main__":
    main()