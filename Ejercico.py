def main():
    nombres_alumnos = []
    for i in range(10):
        nombre_alumno = input("Ingrese el nombre del alumno {}: ".format(i + 1))
        nombres_alumnos.append(nombre_alumno)

    nombres_materias = []
    for i in range(5):
        nombre_materia = input("Ingrese el nombre de la materia {}: ".format(i + 1))
        nombres_materias.append(nombre_materia)

    calificaciones = []
    for alumno in range(10):
        print("Ingrese las calificaciones para el alumno", nombres_alumnos[alumno])
        calificaciones_alumno = []
        for materia in range(5):
            calificacion = float(input("Calificación en {} : ".format(nombres_materias[materia])))
            calificaciones_alumno.append(calificacion)
        calificaciones.append(calificaciones_alumno)
    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Ver una fila")
        print("2. Ver una columna")
        print("3. Ver la matriz de calificaciones completa")
        print("4. Ver una calificación específica")
        print("5. Salir")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            fila = int(input("Ingresa el número de fila que quieres ver (1-10): "))
            print("Calificaciones de", nombres_alumnos[fila - 1] + ":", calificaciones[fila - 1])
        elif opcion == 2:
            columna = int(input("Ingresa el número de columna que quieres ver (1-5): "))
            print("Calificaciones de la columna", nombres_materias[columna - 1], ":")
            for fila in calificaciones:
                print(fila[columna - 1])
        elif opcion == 3:
            print("Matriz de calificaciones:")
            for i, fila in enumerate(calificaciones):
                print(nombres_alumnos[i], ":", fila)
        elif opcion == 4:
            alumno = int(input("Ingresa el número de alumno (1-10): "))
            materia = int(input("Ingresa el número de materia (1-5): "))
            print("La calificación de", nombres_alumnos[alumno - 1], "en la materia", nombres_materias[materia - 1], "es:", calificaciones[alumno - 1][materia - 1])
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
