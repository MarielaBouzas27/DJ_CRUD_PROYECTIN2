import csv
from oficina.models import Oficina

def run():
    with open('oficinas.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Oficina.objects.get_or_create(
                nombre=row['nombre'],
                nombre_corto=row['nombre_corto']
            )
