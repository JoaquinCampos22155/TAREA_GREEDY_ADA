#INSTANCIA
estudiantes = [
    {"nombre": "A",  "carrera": "IQ",    "promedio": 85},
    {"nombre": "B",  "carrera": "IQ",    "promedio": 90},
    {"nombre": "C",  "carrera": "II",    "promedio": 88},
    {"nombre": "D",  "carrera": "II",    "promedio": 79},
    {"nombre": "E",  "carrera": "ICCTI", "promedio": 91},
    {"nombre": "F",  "carrera": "ICCTI", "promedio": 84},
    {"nombre": "G",  "carrera": "IA",    "promedio": 87},
    {"nombre": "H",  "carrera": "IA",    "promedio": 83},
    {"nombre": "I",  "carrera": "N",     "promedio": 92},
    {"nombre": "J",  "carrera": "N",     "promedio": 89},
    {"nombre": "K",  "carrera": "A",     "promedio": 78},
    {"nombre": "L",  "carrera": "A",     "promedio": 81},
    {"nombre": "M",  "carrera": "ICA",   "promedio": 94},
    {"nombre": "N",  "carrera": "ICA",   "promedio": 76},
    {"nombre": "O",  "carrera": "M",     "promedio": 82},
    {"nombre": "P",  "carrera": "M",     "promedio": 88},
    {"nombre": "Q",  "carrera": "F",     "promedio": 77},
    {"nombre": "R",  "carrera": "F",     "promedio": 79},
    {"nombre": "S",  "carrera": "Q",     "promedio": 86},
    {"nombre": "T",  "carrera": "P",     "promedio": 93},
]

estudiantes_ordenados = sorted(estudiantes, key=lambda x: x["promedio"], reverse=True)

equipo_final = []
carreras_seleccionadas = set()

for estudiante in estudiantes_ordenados:
    if estudiante["carrera"] not in carreras_seleccionadas:
        equipo_final.append(estudiante)
        carreras_seleccionadas.add(estudiante["carrera"])

print("Equipo seleccionado:")
for e in equipo_final:
    print(f"- {e['nombre']} ({e['carrera']}): promedio {e['promedio']}")

suma_total = sum(e["promedio"] for e in equipo_final)
print(f"\nSuma total de promedios: {suma_total}")
