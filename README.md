# Inventario Adaros

Sistema de gestión de inventario físico desarrollado con Django.

## Funcionalidades principales

- Gestión de productos y stock
- Movimientos de entrada y salida
- Importación desde Excel
- Conteo de inventario físico con comparación vs sistema
- Generación de etiquetas y reportes en PDF
- Reporte tipo acta con firma
- Buscador global y filtros dinámicos

## Requisitos

- Python 3.10+
- Django 5.x
- openpyxl
- reportlab

## Cómo instalar

```bash
git clone https://github.com/tu-usuario/inventario-adaros.git
cd inventario-adaros
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
