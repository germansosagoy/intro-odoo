from odoo import models, fields


# Creando un modelo (tabla) a partir de una clase
class Libros(models.Model):
    _name = "libreria.libros"  # Nombre de la tabla
    _description = "Esto es una libreria"

    # Nombre del campo(tipo: string)
    name = fields.Char(string='Nombre del libro', required=True)
    genero = fields.Char(string="Genero del libro", required=True)
    autor = fields.Char(string='Autor del libro', required=True)
    foto = fields.Binary('Foto del autor')
   
