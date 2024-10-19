class Empleado:
    def __init__(self, cedula, nombre, direccion, telefono, salario):
        self.cedula = cedula
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.salario = salario

    def obtener_cedula(self):
        return self.cedula

    def obtener_nombre(self):
        return self.nombre

    def actualizar_nombre(self, nombre):
        self.nombre = nombre

    def obtener_direccion(self):
        return self.direccion

    def actualizar_direccion(self, direccion):
        self.direccion = direccion

    def obtener_telefono(self):
        return self.telefono

    def actualizar_telefono(self, telefono):
        self.telefono = telefono

    def obtener_salario(self):
        return self.salario

    def actualizar_salario(self, salario):
        self.salario = salario


class Menu:
    def __init__(self):
        self.empleados = [None] * 10
        self.contador = 0

    def mostrar_menu_principal(self):
        print("\nOpciones del Sistema:")
        print("1. Agregar Empleado")
        print("2. Consultar Empleados")
        print("3. Modificar Empleado")
        print("4. Borrar Empleado")
        print("5. Inicializar Arreglos")
        print("6. Generar Reportes")
        print("7. Salir")

    def agregar_empleado(self):
        if self.contador >= 10:
            print("No se pueden añadir más empleados. El arreglo está lleno.")
            return
        cedula = input("Ingrese cédula: ")
        nombre = input("Ingrese nombre: ")
        direccion = input("Ingrese dirección: ")
        telefono = input("Ingrese teléfono: ")
        salario = float(input("Ingrese salario: "))
        nuevo_empleado = Empleado(cedula, nombre, direccion, telefono, salario)
        self.empleados[self.contador] = nuevo_empleado
        self.contador += 1
        print("Empleado agregado con éxito.")

    def consultar_empleados(self):
        if self.contador == 0:
            print("No hay empleados registrados.")
            return
        for emp in self.empleados[:self.contador]:
            print(f"Cédula: {emp.obtener_cedula()}, Nombre: {emp.obtener_nombre()}, "
                  f"Dirección: {emp.obtener_direccion()}, Teléfono: {emp.obtener_telefono()}, "
                  f"Salario: {emp.obtener_salario()}")

    def modificar_empleado(self):
        cedula = input("Ingrese la cédula del empleado a modificar: ")
        for emp in self.empleados[:self.contador]:
            if emp.obtener_cedula() == cedula:
                emp.actualizar_nombre(input("Nuevo nombre: "))
                emp.actualizar_direccion(input("Nueva dirección: "))
                emp.actualizar_telefono(input("Nuevo teléfono: "))
                emp.actualizar_salario(float(input("Nuevo salario: ")))
                print("Empleado modificado con éxito.")
                return
        print("Empleado no encontrado.")

    def borrar_empleado(self):
        cedula = input("Ingrese la cédula del empleado a borrar: ")
        for i in range(self.contador):
            if self.empleados[i].obtener_cedula() == cedula:
                for j in range(i, self.contador - 1):
                    self.empleados[j] = self.empleados[j + 1]
                self.empleados[self.contador - 1] = None
                self.contador -= 1
                print("Empleado borrado con éxito.")
                return
        print("Empleado no encontrado.")

    def inicializar_arreglos(self):
        self.empleados = [None] * 10
        self.contador = 0
        print("Arreglo de empleados inicializado.")

    def generar_reportes(self):
        while True:
            print("\nOpciones de Reportes:")
            print("1. Listar empleados por nombre")
            print("2. Calcular promedio de salarios")
            print("3. Regresar al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.listar_empleados_por_nombre()
            elif opcion == '2':
                self.calcular_promedio_salarios()
            elif opcion == '3':
                break
            else:
                print("Opción inválida.")

    def listar_empleados_por_nombre(self):
        empleados_ordenados = sorted(self.empleados[:self.contador], key=lambda emp: emp.obtener_nombre())
        for emp in empleados_ordenados:
            print(f"{emp.obtener_nombre()} - Cédula: {emp.obtener_cedula()}")

    def calcular_promedio_salarios(self):
        if self.contador == 0:
            print("No hay empleados para calcular el promedio.")
            return
        total_salarios = sum(emp.obtener_salario() for emp in self.empleados[:self.contador])
        promedio = total_salarios / self.contador
        print(f"El promedio de salarios es: {promedio:.2f}")


def main():
    menu = Menu()
    while True:
        menu.mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            menu.agregar_empleado()
        elif opcion == '2':
            menu.consultar_empleados()
        elif opcion == '3':
            menu.modificar_empleado()
        elif opcion == '4':
            menu.borrar_empleado()
        elif opcion == '5':
            menu.inicializar_arreglos()
        elif opcion == '6':
            menu.generar_reportes()
        elif opcion == '7':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
