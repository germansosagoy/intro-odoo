from odoo import models, fields
from ..api import api


# Creando un modelo (tabla) a partir de una clase
class Blockbuster(models.Model):
    _name = "blockbuster.peliculas"  # Nombre de la tabla
    _description = "Esto es un blockbuster de peliculas"

    # Nombre del campo(tipo: string)
    name = fields.Char(string="Nombre de la pelicula", required=True)
    director = fields.Char(string='Director', required=True)
    genero = fields.Char(string="Genero")
    presupuesto = fields.Char(string='Presupuesto')
    fecha_estreno = fields.Date('')
    disponibilidad = fields.Boolean('¿Está disponible?')

    api_json = fields.Text()

    def action_hit_the_api(self):
        for record in self:
            # llamar a la api pasandole algunos parametros
            # con la respuesta escribir el campo api_json