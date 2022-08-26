from odoo import models, fields
from ..api import api

import logging
_logger = logging.getLogger(__name__)


# Creando un modelo (tabla) a partir de una clase
class Blockbuster(models.Model):
    _name = "blockbuster.database"  # Nombre de la tabla
    _description = "Esto es la base de blockbuster"

    # Nombre del campo(tipo: string)
    name = fields.Char(string="Nombre de la pelicula", required=True)

    def action_get_trending(self):
        tmdb = api('511f7d4c0cad0f61cb9e7037eae11ff2')
        response = tmdb.get('/trending/{}/{}'.format('all','week'))

        _logger.info('----------- response: ')
        _logger.info(response)
        {pelis:[{
            name: 'Rapido y furioso',
        }]}
        for peli in response['pelis']:
            self.env['blockbuster.peliculas'].create({
                'name': peli['name'], #rapido y furioso
                'director': '',
                'genero':'',
                'presupuesto':'',
                'fecha_estreno':'',
            })

        