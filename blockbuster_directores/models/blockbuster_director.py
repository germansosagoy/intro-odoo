# -*- coding: utf-8 -*-
from odoo import models, fields, api


class BlockbusterDirectores(models.Model):
    _inherit = 'blockbuster.peliculas'

    codigo = fields.Char(required=True)
    cod_pelicula = fields.Char(compute='_compute_cod_interno', store=True)

    @api.depends('name', 'director', 'codigo', 'cod_pelicula')
    def _compute_cod_interno(self):
        for pelicula in self:
            lista = []
            if pelicula.name:
                lista.append(pelicula.name)
            if pelicula.director:
                lista.append(pelicula.director)
            if pelicula.codigo:
                lista.append(pelicula.codigo)
            if lista:
                pelicula.cod_pelicula = ' - '.join(lista)
            else:
                pelicula.cod_pelicula = 1
