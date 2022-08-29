# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibreriaLibros(models.Model):
    _inherit = "libreria.libros"

    isbn = fields.Char(required=True)
    codigo_interno = fields.Char(compute='_compute_codigo_interno')

    @api.depends('name', 'autor', 'isbn')
    def _compute_codigo_interno(self):
        for libro in self:
            lista = []
            if libro.name:
                lista.append(libro.name)
            if libro.autor:
                lista.append(libro.autor)
            if libro.isbn:
                lista.append(libro.isbn)
            if lista:
                libro.codigo_interno = '-'.join(lista)