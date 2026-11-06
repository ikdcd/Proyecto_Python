from datetime import datetime

class Logger:
    # Metodos
    def newLog(titulo, mensaje):
        with open("log/logs.txt", "a", encoding="utf-8") as f:
            fechaActual = datetime.now().strftime("%Y-%m-%d")
            horaActual = datetime.now().strftime("%H:%M:%S")
            f.write(f"[{fechaActual} {horaActual}] {titulo}: {mensaje}\n\n")

    def newLogHeader(titulo):
        fechaActual = datetime.now().strftime("%Y-%m-%d")
        horaActual = datetime.now().strftime("%H:%M:%S")
        with open("log/logs.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{"="*20}[ {fechaActual} {horaActual} | {titulo} ]{"="*20}\n\n")
