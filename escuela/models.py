from typing_extensions import Required
from odoo import models, fields


class ProfesoresRecord(models.Model):
    _name = "profesor.profesor"
    nombre = fields.Char(string="Nombre", Required=True)
    primer_apellido = fields.Char(string="Primer apellido", Required=True)
    foto = fields.Binary(string="Foto de perfil")
    edad = fields.Integer(string="Edad")
    fecha_nac = fields.Date(string="Fecha de nacimiento")
    genero = fields.Selection(
        [('m', 'Masculino'), ('f', 'Femenino',), ('o', 'Otro')], string="Género")


class AsignaturasRecord(models.Model):
    _name = "asignatura.asignatura"
    nombre = fields.Char(string="Nombre", Required=True)
    temas = fields.Integer(string='Temas')
    tipo = fields.Selection([('m', 'Matematicas', ('g', 'Geografía'),
                            ('l', 'Literatura'), ('a', 'Artes'), 'm', 'Música')])
    profesor = fields.Many2one('profesor.profesor', string="Profesor")
