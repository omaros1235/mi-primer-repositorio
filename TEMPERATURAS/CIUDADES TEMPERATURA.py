# Definición de las temperaturas para cada ciudad, semana y día
temperaturas = [
    [  # ciudad 1
        [  # semana 1
            {"dia": "Lunes", "temp": 78},
            {"dia": "Martes", "temp": 80},
            {"dia": "Miércoles", "temp": 82},
            {"dia": "Jueves", "temp": 79},
            {"dia": "Viernes", "temp": 85},
            {"dia": "Sábado", "temp": 88},
            {"dia": "Domingo", "temp": 92}
        ],
        [  # semana 2
            {"dia": "Lunes", "temp": 76},
            {"dia": "Martes", "temp": 79},
            {"dia": "Miércoles", "temp": 83},
            {"dia": "Jueves", "temp": 81},
            {"dia": "Viernes", "temp": 87},
            {"dia": "Sábado", "temp": 89},
            {"dia": "Domingo", "temp": 93}
        ],
        [  # semana 3
            {"dia": "Lunes", "temp": 77},
            {"dia": "Martes", "temp": 81},
            {"dia": "Miércoles", "temp": 85},
            {"dia": "Jueves", "temp": 82},
            {"dia": "Viernes", "temp": 88},
            {"dia": "Sábado", "temp": 91},
            {"dia": "Domingo", "temp": 95}
        ],
        [  # semana 4
            {"dia": "Lunes", "temp": 75},
            {"dia": "Martes", "temp": 78},
            {"dia": "Miércoles", "temp": 80},
            {"dia": "Jueves", "temp": 79},
            {"dia": "Viernes", "temp": 84},
            {"dia": "Sábado", "temp": 87},
            {"dia": "Domingo", "temp": 91}
        ]
    ],
    [  # ciudada 2
        [  # semana 1
            {"dia": "Lunes", "temp": 62},
            {"dia": "Martes", "temp": 64},
            {"dia": "Miércoles", "temp": 68},
            {"dia": "Jueves", "temp": 70},
            {"dia": "Viernes", "temp": 73},
            {"dia": "Sábado", "temp": 75},
            {"dia": "Domingo", "temp": 79}
        ],
        [  # semana 2
            {"dia": "Lunes", "temp": 63},
            {"dia": "Martes", "temp": 66},
            {"dia": "Miércoles", "temp": 70},
            {"dia": "Jueves", "temp": 72},
            {"dia": "Viernes", "temp": 75},
            {"dia": "Sábado", "temp": 77},
            {"dia": "Domingo", "temp": 81}
        ],
        [  # semana 3
            {"dia": "Lunes", "temp": 61},
            {"dia": "Martes", "temp": 65},
            {"dia": "Miércoles", "temp": 68},
            {"dia": "Jueves", "temp": 70},
            {"dia": "Viernes", "temp": 72},
            {"dia": "Sábado", "temp": 76},
            {"dia": "Domingo", "temp": 80}
        ],
        [  # semana 4
            {"dia": "Lunes", "temp": 64},
            {"dia": "Martes", "temp": 67},
            {"dia": "Miércoles", "temp": 69},
            {"dia": "Jueves", "temp": 71},
            {"dia": "Viernes", "temp": 74},
            {"dia": "Sábado", "temp": 77},
            {"dia": "Domingo", "temp": 80}
        ]
    ],
    [  # ciudad 3
        [  # semana 1
            {"dia": "Lunes", "temp": 90},
            {"dia": "Martes", "temp": 92},
            {"dia": "Miércoles", "temp": 94},
            {"dia": "Jueves", "temp": 91},
            {"dia": "Viernes", "temp": 88},
            {"dia": "Sábado", "temp": 85},
            {"dia": "Domingo", "temp": 82}
        ],
        [  # semana 2
            {"dia": "Lunes", "temp": 89},
            {"dia": "Martes", "temp": 91},
            {"dia": "Miércoles", "temp": 93},
            {"dia": "Jueves", "temp": 90},
            {"dia": "Viernes", "temp": 87},
            {"dia": "Sábado", "temp": 84},
            {"dia": "Domingo", "temp": 81}
        ],
        [  # semana 3
            {"dia": "Lunes", "temp": 91},
            {"dia": "Martes", "temp": 93},
            {"dia": "Miércoles", "temp": 95},
            {"dia": "Jueves", "temp": 92},
            {"dia": "Viernes", "temp": 89},
            {"dia": "Sábado", "temp": 86},
            {"dia": "Domingo", "temp": 83}
        ],
        [  # semana 4
            {"dia": "Lunes", "temp": 88},
            {"dia": "Martes", "temp": 90},
            {"dia": "Miércoles", "temp": 92},
            {"dia": "Jueves", "temp": 89},
            {"dia": "Viernes", "temp": 86},
            {"dia": "Sábado", "temp": 83},
            {"dia": "Domingo", "temp": 80}
        ]
    ]
]

def calcular_promedio(suma_acumulada, total_acumulado):
  """
  Calcula el promedio de dos valores.

  Parámetros:
    suma_acumulada: La suma acumulada de los valores.
    total_acumulado: El número total de valores.

  Retorno:
    El promedio de los valores.
  """
  return round(suma_acumulada / total_acumulado, 2)

# Calcular el promedio de temperaturas para cada ciudad y semana
no_ciudad = 0
for ciudad in temperaturas:
  no_ciudad += 1
  print(f"CIUDAD No. {no_ciudad}")
  no_semana = 0
  suma_promedio = 0
  for semana in ciudad:
    no_semana += 1
    suma = 0
    for dia in semana:
      # Sumamos la temperatura de cada día
      suma += dia["temp"]
    # Calculamos el promedio de la semana
    promedio = calcular_promedio(suma, len(semana))
    # Acumulamos el promedio de la semana para calcular el promedio mensual
    suma_promedio += promedio
    print(f"El promedio semana No. {no_semana} es: {promedio}")
  # Calculamos el promedio mensual
  promedio_ciudad = calcular_promedio(suma_promedio, len(ciudad))
  print(f"El promedio mensual es: {promedio_ciudad}")