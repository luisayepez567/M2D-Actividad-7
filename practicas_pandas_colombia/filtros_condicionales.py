import pandas as pd

data = {
    'Nombre': [
        'Juan Gómez', 'Elena Marín', 'Carlos Ruiz', 'Diana Toro', 'Andrés Felipe', 'Sofía Mesa', 'Mateo Cano', 'Laura Gil', 'Diego León', 'Sara Ortiz',
        'Luis Ángel', 'Marta Lucía', 'Hugo Posada', 'Paula Ríos', 'Simón Vélez', 'Valentina Paz', 'Jorge Eli', 'Camila Luz', 'Samuel Sol', 'Valeria Mar',
        'Ricardo Rey', 'Patricia San', 'Fernando Joy', 'Gloria Esperanza', 'Oscar Darío', 'Clara Inés', 'Iván René', 'Beatriz Pin', 'Mauricio Al', 'Claudia Sol',
        'Gabriel Jaime', 'Adriana María', 'Wilson Fer', 'Sandra Milena', 'Jairo Hernán', 'Natalia Andrea', 'César Augusto', 'Yolanda Estela', 'Héctor Fabio', 'Mónica Liz',
        'Ramiro José', 'Tatiana Marcela', 'Alvaro Javier', 'Lina Fernanda', 'Gonzalo Antonio', 'Angélica María', 'Esteban David', 'Silvia Juliana', 'Roberto Carlos', 'Ximena Paz'
    ],
    'Edad': [25, 34, 45, 28, 31, 23, 40, 29, 37, 26, 52, 41, 33, 27, 30, 24, 48, 32, 29, 35, 39, 44, 27, 50, 31, 36, 42, 28, 33, 46, 29, 38, 43, 31, 47, 25, 34, 41, 55, 30, 37, 26, 44, 28, 51, 32, 24, 33, 49, 27],
    'Ciudad': ['Medellín', 'Bogotá', 'Cali', 'Barranquilla', 'Medellín', 'Envigado', 'Bogotá', 'Sabaneta', 'Pereira', 'Bucaramanga', 'Medellín', 'Cali', 'Bogotá', 'Medellín', 'Itagüí', 'Cali', 'Barranquilla', 'Medellín', 'Bogotá', 'Cali', 'Medellín', 'Bogotá', 'Manizales', 'Pereira', 'Envigado', 'Cali', 'Medellín', 'Bogotá', 'Bucaramanga', 'Itagüí', 'Medellín', 'Bogotá', 'Cali', 'Medellín', 'Sabaneta', 'Cali', 'Barranquilla', 'Medellín', 'Bogotá', 'Cali', 'Medellín', 'Bogotá', 'Manizales', 'Pereira', 'Envigado', 'Cali', 'Medellín', 'Bogotá', 'Bucaramanga', 'Itagüí'],
    'Nivel_Estudio': ['Pregrado', 'Maestría', 'Doctorado', 'Tecnología', 'Especialización', 'Pregrado', 'Maestría', 'Especialización', 'Pregrado', 'Tecnología', 'Doctorado', 'Maestría', 'Pregrado', 'Especialización', 'Tecnología', 'Pregrado', 'Maestría', 'Doctorado', 'Pregrado', 'Especialización', 'Maestría', 'Doctorado', 'Pregrado', 'Maestría', 'Tecnología', 'Especialización', 'Doctorado', 'Pregrado', 'Maestría', 'Especialización', 'Pregrado', 'Doctorado', 'Maestría', 'Tecnología', 'Especialización', 'Pregrado', 'Maestría', 'Doctorado', 'Pregrado', 'Especialización', 'Maestría', 'Pregrado', 'Doctorado', 'Pregrado', 'Maestría', 'Especialización', 'Tecnología', 'Doctorado', 'Pregrado', 'Especialización'],
    'Experiencia_Años': [2, 8, 15, 4, 7, 1, 12, 5, 10, 3, 20, 14, 9, 4, 6, 2, 18, 6, 5, 9, 11, 16, 3, 22, 7, 10, 15, 4, 8, 17, 5, 12, 14, 6, 19, 2, 9, 13, 25, 7, 12, 3, 16, 5, 20, 8, 2, 11, 23, 6],
    'Salario_COP': [3500000, 7500000, 15000000, 2800000, 5200000, 3100000, 9000000, 4800000, 6000000, 2500000, 18000000, 8200000, 5500000, 4500000, 3200000, 3300000, 11000000, 14000000, 4200000, 6500000, 8800000, 16500000, 3800000, 9500000, 3000000, 5800000, 15500000, 4000000, 7800000, 6200000, 4400000, 17000000, 8500000, 3100000, 5900000, 3200000, 8900000, 14500000, 5000000, 6100000, 9200000, 3900000, 16000000, 4300000, 9800000, 6300000, 2900000, 15200000, 4800000, 6000000],
    'Remoto': [True, False, False, True, True, False, True, False, True, False, False, True, False, True, False, True, False, True, False, True, False, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False]
}
df = pd.DataFrame(data)



# 1. Altos Ingresos: Seleccionar profesionales con salario superior a 10.000.000.
altos_ingresos = df[df['Salario_COP'] > 10000000]
print("\n--- 1. Altos Ingresos: Salario > 10M ---")
print(altos_ingresos)

# 2. Sede Principal: Filtrar a todos los empleados cuya ciudad sea 'Medellín'.
sede_principal = df[df['Ciudad'] == 'Medellín']
print("\n--- 2. Sede Principal: Medellín ---")
print(sede_principal)

# 3. Experiencia Sénior: Obtener registros de personas con más de 15 años de experiencia.
experiencia_senior = df[df['Experiencia_Años'] > 15]
print("\n--- 3. Experiencia Sénior: > 15 años ---")
print(experiencia_senior)

# 4. Investigación Remota: Listar doctores que trabajen de forma remota.
investigacion_remota = df[(df['Nivel_Estudio'] == 'Doctorado') & (df['Remoto'] == True)]
print("\n--- 4. Investigación Remota: Doctores en remoto ---")
print(investigacion_remota)

# 5. Segmento Joven: Filtrar personas con edades entre 25 y 30 años inclusive.
segmento_joven = df[df['Edad'].between(25, 30)]
print("\n--- 5. Segmento Joven: Edades entre 25 y 30 ---")
print(segmento_joven)

# 6. Optimización en Bogotá: Buscar quienes ganen menos de 4.000.000 y vivan en 'Bogotá'.
optimizacion_bogota = df[(df['Salario_COP'] < 4000000) & (df['Ciudad'] == 'Bogotá')]
print("\n--- 6. Optimización en Bogotá: < 4M en Bogotá ---")
print(optimizacion_bogota)

# 7. Especialistas Valle: Filtrar profesionales de 'Cali' con nivel 'Especialización'.
especialistas_valle = df[(df['Ciudad'] == 'Cali') & (df['Nivel_Estudio'] == 'Especialización')]
print("\n--- 7. Especialistas Valle: Especialización en Cali ---")
print(especialistas_valle)

# 8. Altos Salarios Junior: Seleccionar registros con experiencia < 5 años y salario > 4.000.000.
altos_salarios_junior = df[(df['Experiencia_Años'] < 5) & (df['Salario_COP'] > 4000000)]
print("\n--- 8. Altos Salarios Junior: < 5 años y > 4M ---")
print(altos_salarios_junior)

# 9. Nivel Técnico: Filtrar registros con nivel de estudio 'Tecnología' o 'Pregrado'.
nivel_tecnico = df[df['Nivel_Estudio'].isin(['Tecnología', 'Pregrado'])]
print("\n--- 9. Nivel Técnico: Tecnología o Pregrado ---")
print(nivel_tecnico)

# 10. Presencialidad Santander: Obtener empleados de 'Bucaramanga' con modalidad presencial.
presencialidad_santander = df[(df['Ciudad'] == 'Bucaramanga') & (df['Remoto'] == False)]
print("\n--- 10. Presencialidad Santander: Bucaramanga presencial ---")
print(presencialidad_santander)


