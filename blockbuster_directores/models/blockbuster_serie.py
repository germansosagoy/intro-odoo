# -*- coding: utf-8 -*-
from odoo import models, fields, api

class BlockbusterDirectores(models.Model):
    _inherit = "blockbuster.peliculas"

    codigo = fields.Char(required=True)
    cod_serie = fields.Char(compute='_compute_cod_serie')

    # @api.depends('name', 'genero')
    # def _compute_cod_serie(self):
    #      for serie in self:
    #           lista = []
    #            if serie.name:
    #                 lista.append(serie.name)
    #             if serie.genero:
    #                 lista.append(serie.genero)
    #             if serie.codigo:
    #                 lista.append(serie.codigo)
    #             if serie.cod_serie = '-'.join(lista)
