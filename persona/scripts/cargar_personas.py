import csv
from oficina.models import Oficina
from persona.models import Persona

def run():
    with open('personas.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            oficina = Oficina.objects.filter(nombre_corto=row['oficina_nombre_corto']).first()
            if oficina:
                Persona.objects.get_or_create(
                    nombre=row['nombre'],
                    apellido=row['apellido'],
                    edad=row['edad'],
                    oficina=oficina
                )

