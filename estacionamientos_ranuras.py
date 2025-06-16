import datetime
import os
import platform

from rich import print as print
from rich.console import Console
from rich.table import Table

"""
Objetivo:  Gestionar el ingreso y salida en un estacionamiento
           privado de vehículos.

            1.- La empresa cuenta con un lugar físico par 20
                estacionamientos.
            2.- El horario de atención es de 6:30 a 21:00 horas.
            3.- Cobra 10 pesos por minuto.
            4.- Se ingresa solo la patente del auto para registrar
                el ingreso y se emite un vale que indica: N°de serie (es
                un número correlativo de 6 dígitos), fecha actual,
                hora actual, n° estacionamiento (se debe buscar si
                existe estacionamiento disponible y asignar uno) y patente.
            5.- Al retirar el vehículo debe presentar el vale y se ingresa
                el número de serie, se calculan los minutos estacionados y
                se presenta el valor a pagar, una vez pagado se libera el
                estacionamiento ocupado.
            6.- Se requiere una vista de todos los estacionamientos indicando su
                número y estado (ocupado/disponible)
            7.- Se requiere un reporte de los vehículos estacionados y el monto
                en dinero recaudado para una fecha específica (se debe ingresar una fecha
                por teclado)
            8.- Se requiere un reporte de los vehículos estacionados y el monto
                en dinero recaudado para u
                n rango de fechas (se deben ingresar por teclado)
"""

# VARIABLES DE MIERDA
inicio_horario_atencion = datetime.time(0, 4)  # 6:00
fin_horario_atencion = datetime.time(21, 0)  # 21:00
espacios_disponibles = 20
espacios_usados = 0
contador_alltime_espacios_usados = espacios_usados
ranuras= [None] * 20
autos_alltime = []
cobro_por_minuto = 10


# funciones de mierda
def the_world():
    if platform.system() == "Windows":
        os.system("pause")
    elif platform.system() in ["Linux", "Darwin"]:
        print("[grey50]Presione Enter para continuar...[/grey50]")
        input()


def cleanup():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() in ["Linux", "Darwin"]:
        os.system("clear")


# empieza el loop
cleanup()
while True:
    cleanup()
    print("[bright_yellow][MENÚ][/bright_yellow]")
    print("[bright_yellow]----[/bright_yellow]" * 15)
    print("1. Registrar vehículo")
    print("2. Retirar vehículo")
    print("3. Listar estacionamientos")
    print("4. Historial de vehículos retirados")
    print("5. Reporte de vehículos estacionados")
    print("6. Salir")
    print("[bright_yellow]----[bright_yellow]" * 15, "\n")
    print("[bright_yellow][DATOS][/bright_yellow]")
    print(f"Horario de atención: {inicio_horario_atencion} - {fin_horario_atencion}")
    print(f"Espacios de estacionamientos restantes: {espacios_disponibles}")

    while True:
        try:
            seleccion = int(input("\nSeleccione una opción (1-6):"))
        except ValueError:
            print("Por favor, ingrese un número válido.")
        else:
            if seleccion in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print("Opción no válida. Por favor, seleccione un número dentro de la lista")

    match seleccion:
        case 1:
            cleanup()
            print("[bright_yellow][INGRESO VEHÍCULO][/bright_yellow]")
            print("[bright_yellow]----[/bright_yellow]" * 15)
            if datetime.datetime.now().time() < inicio_horario_atencion or datetime.datetime.now().time() > fin_horario_atencion:
                print("El estacionamiento está cerrado. Horario de atención: 6:30 - 21:00")

            else:
                if espacios_disponibles > 0:
                    print("Ingrese la patente del vehículo:")
                    while True:
                        patente = input("\n").strip().upper().replace("-", "").replace(" ", "")
                        if len(patente) > 6 or len(patente) < 5:
                            print("Número patente invalido, porfavor ingrese número de patente valido.")
                        else:
                            break
                    patente_ya_existe = False
                    for reg in ranuras:
                        if reg is not None and reg["patente"] == patente:
                            patente_ya_existe = True
                            break

                    if patente_ya_existe:
                        print(f"[red]Error: El vehículo con patente {patente} ya está estacionado.[/red]")
                        print("No se puede ingresar el mismo vehículo dos veces.")
                    else:
                        n_serie = f"{contador_alltime_espacios_usados:06d}"
                        horario_entrada = datetime.datetime.now()
                        n_estacionamiento = espacios_usados

                        index_ranura = None
                        for i in range(20):
                            if ranuras[i] is None:
                                index_ranura = i
                                break
                        if index_ranura is not None:
                            n_estacionamiento = index_ranura + 1
                            registro = {
                                "n_serie": n_serie,
                                "horario_entrada": horario_entrada.isoformat(),
                                "n_estacionamiento": n_estacionamiento,
                                "patente": patente,
                            }
                            ranuras[index_ranura] = registro #type: ignore [ NO ESTA ROTO, VEA LINEA 42 ]
                            cleanup()
                            print(f"Vehículo con patente {patente} ingresado correctamente.")
                            print("[bright_yellow][BOLETA][/bright_yellow]")
                            print("[bright_yellow]----[bright_yellow]" * 15)
                            print(registro)
                            espacios_disponibles -= 1
                            espacios_usados += 1
                            contador_alltime_espacios_usados += 1
                else:
                    print("No hay espacios disponibles en el estacionamiento.")

        case 2:
            cleanup()
            print("[bright_yellow][RETIRAR VEHÍCULO][/bright_yellow]")
            print("[bright_yellow]----[/bright_yellow]" * 15)
            if espacios_usados == 0:
                print("No hay vehículos estacionados.")
            # ayo ock can you turn my lobster into a- *MEOWWW*
            # YOOOO
            #
            # *MEOWWW*
            else:
                """
                print("¿Desea buscar por:")
                print("1. Número de serie")
                print("2. Patente")
                print("3. Cancelar búsqueda")
                while True:
                    opcion_busqueda = int(input("Seleccione una opción (1, 2 o 3): "))
                    if opcion_busqueda in [1, 2, 3]:
                        break
                    else:
                        print("Opción inválida. Intente de nuevo.")

                if opcion_busqueda == 1:"""
                clave = "n_serie"
                valor = input("Ingrese el número de serie del vehículo: ").strip()

                # elif opcion_busqueda == 2:
                # clave = "patente"
                # valor = input("Ingrese la patente del vehículo: ").strip().upper()

                # else:
                # continue

                encontrado = None
                for i, reg in enumerate(ranuras):
                    if reg and reg[clave] == valor:
                        encontrado = i
                        break

                if encontrado is not None:
                    tabla_encontrada = ranuras[encontrado]
                    horario_entrada = datetime.datetime.fromisoformat(ranuras[encontrado]["horario_entrada"]) # type: ignore [DALE, ANDÁ A LABURAR]
                    horario_salida = datetime.datetime.now()
                    diferencia_horario = horario_salida - horario_entrada
                    minutos_estacionados = int(diferencia_horario.total_seconds() // 60)
                    monto_a_pagar = minutos_estacionados * cobro_por_minuto

                    cleanup()
                    print("[bright_yellow][BOLETA DE RETIRO][/bright_yellow]")
                    print("[bright_yellow]----[/bright_yellow]" * 15)
                    table = Table(show_lines=True)
                    table.add_column("N° Serie")
                    table.add_column("N° Estacionamiento")
                    table.add_column("Horario Entrada")
                    table.add_column("Horario Salida")
                    table.add_column("Monto a Pagar")
                    table.add_row(
                        tabla_encontrada["n_serie"], # type: ignore [NO ESTA ROTO, VEA LINEA 42]
                        str(tabla_encontrada["n_estacionamiento"]), # type: ignore [NO ESTA ROTO, VEA LINEA 42]
                        horario_entrada.strftime("%H:%M:%S") , # type: ignore [NO ESTA ROTO, VEA LINEA 42]
                        horario_salida.strftime("%H:%M:%S"),
                        f"${monto_a_pagar}"
                    )
                    console = Console()
                    console.print(table)


                    while True:
                        confirmar = input("Quiere borrar este vehículo? (s/n):\n").strip().lower()
                        if confirmar == "s":
                            registro = ranuras[encontrado]
                            registro["horario_salida"] = datetime.datetime.now().isoformat() # type: ignore [NO ESTA ROTO, VEA LINEA 42]
                            registro["monto_pagado"] = monto_a_pagar # type: ignore [abuela, mira el tung tung tung tung tung sahur abuela - ANDÁ A LABURAR]
                            autos_alltime.append(registro)
                            ranuras[encontrado] = None
                            espacios_disponibles += 1
                            espacios_usados -= 1
                            print("Vehículo correctamente eliminado.")

                            break
                        elif confirmar == "n":
                            print("Entendido. Vehículo no eliminado.")
                            break
                        else:
                            print("Opción invalida, seleccione S o N.")
                else:
                    print("No se encontró el vehículo.")

        # case 3:
        #     cleanup()
        #     print("[ESTACIONAMIENTOS]")
        #     print("----" * 15)
        #     if espacios_usados == 0:
        #         print("No hay vehículos estacionados.")
        #     else:
        #         for i, reg in enumerate(ranuras):
        #             if reg is None:
        #                 print(f"Estacionamiento {i + 1}: Disponible")
        #             else:
        #                 print(
        #                     f"Estacionamiento {i + 1}: Ocupado - Número de serie: {reg['n_serie']} - Patente: {reg['patente']}"
        #                 )
        #         print("")
        case 3:
            cleanup()
            table = Table(title="Estacionamientos", show_lines=True)
            table.add_column("N° Ranura")
            table.add_column("Estado")
            table.add_column("N° Serie")
            table.add_column("Patente")
            table.add_column("Total a Pagar")

            for i, reg in enumerate(ranuras):
                if reg is None:
                    table.add_row(str(i + 1), "[green]Disponible[/green]", "-", "-", "-")
                else:
                    horario_entrada = datetime.datetime.fromisoformat(reg["horario_entrada"])
                    ahora = datetime.datetime.now()
                    minutos_estacionados = int((ahora - horario_entrada).total_seconds() // 60)
                    precio = minutos_estacionados * cobro_por_minuto

                    table.add_row(
                        str(i + 1),
                        "[red]Ocupado[/red]",
                        reg["n_serie"],
                        reg["patente"],
                        f"${precio}",
                )
            console = Console()
            cleanup()
            console.print(table)

        case 4:
            cleanup()
            print("[bright_yellow][HISTORIAL DE VEHÍCULOS RETIRADOS][/bright_yellow]")
            print("[bright_yellow]----[/bright_yellow]" * 15)
            if not autos_alltime:
                print("Aún no hay vehículos registrados como retirados.")
            else:
                table = Table(show_lines=True)
                table.add_column("N° Serie")
                table.add_column("N° Estacionamiento")
                table.add_column("Patente")
                table.add_column("Horario Entrada")
                table.add_column("Horario Salida")
                table.add_column("Monto Pagado")

                for auto in autos_alltime:
                    entrada = auto.get("horario_entrada", "-")
                    salida = auto.get("horario_salida", "-")
                    if entrada != "-":
                        entrada = datetime.datetime.fromisoformat(entrada).strftime("%H:%M:%S")
                    if salida != "-":
                        salida = datetime.datetime.fromisoformat(salida).strftime("%H:%M:%S")

                    table.add_row(
                        auto["n_serie"],
                        str(auto["n_estacionamiento"]),
                        auto["patente"],
                        entrada,
                        salida,
                        f"${auto.get('monto_pagado', 0)}"
                    )
                console = Console()
                console.print(table)
        case 5:
            # may the horrors begin, gott hilf mir
            cleanup()
            print("[bright_yellow][REPORTE DE VEHÍCULOS ESTACIONADOS][/bright_yellow]")
            print("[bright_yellow]----[/bright_yellow]" * 15)
            while True:
                    fecha_input = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
                    try:
                        fecha_consulta = datetime.datetime.strptime(fecha_input, "%Y-%m-%d").date()

                        # Reset variables for this report
                        vehiculos_en_fecha = []
                        total_recaudado = 0

                        # Find vehicles that were checked out on the requested date
                        for auto in autos_alltime:
                            if "horario_salida" in auto:
                                salida_date = datetime.datetime.fromisoformat(auto["horario_salida"]).date()
                                if salida_date == fecha_consulta:
                                    vehiculos_en_fecha.append(auto)
                                    # Add this vehicle's payment to the total
                                    total_recaudado += auto.get("monto_pagado", 0)

                        if not vehiculos_en_fecha:
                            print(f"No hay vehículos retirados en la fecha {fecha_input}.")
                        else:
                            # Create one table for all vehicles
                            table = Table(title=f"Vehículos retirados el {fecha_input}", show_lines=True)
                            table.add_column("N° Serie")
                            table.add_column("Patente")
                            table.add_column("Horario Entrada")
                            table.add_column("Horario Salida")
                            table.add_column("Monto Pagado")

                            for auto in vehiculos_en_fecha:
                                entrada = datetime.datetime.fromisoformat(auto["horario_entrada"]).strftime("%Y-%m-%d %H:%M:%S")
                                salida = datetime.datetime.fromisoformat(auto["horario_salida"]).strftime("%Y-%m-%d %H:%M:%S")

                                table.add_row(
                                    auto["n_serie"],
                                    auto["patente"],
                                    entrada,
                                    salida,
                                    f"${auto.get('monto_pagado', 0)}"
                                )

                            console = Console()
                            console.print(table)
                            print(f"\n[bright_green]Total recaudado: ${total_recaudado}[/bright_green]")

                        # Exit the while loop after successfully showing the report
                        break
                    except ValueError:
                        print("Fecha inválida. Por favor, ingrese una fecha en formato YYYY-MM-DD.")


        case 6:
            cleanup()
            break
    the_world()
print("\n[red]Adios, mi gente![/red]")
