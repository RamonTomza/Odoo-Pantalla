# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api


class Modelo(models.Model):
    _name = 'modulo.modulo'
    _description = 'Modelo'

    name = fields.Char(string='Descripcion')
    customer=fields.Many2one(string='Cliente', comodel_name='res.partner')
    date=fields.Datetime(string='Fecha')
    type=fields.Selection([('P', 'Presencial'), ('W', 'Whatsapp'), ('T', 'Telefono')], string='Tipo', required=True)
    done=fields.Boolean(string='Realizada', readonly=True)
    image=fields.Binary(string='Imagen')

    def toggle_state(self):
        self.done=not self.done

    def f_create(self):
        modelo={
            'name': 'ORM test',
            'customer': 1,
            'date':str(datetime.date(2023, 2, 7)),
            'type': 'P',
            'done': False
        }
        print(modelo)
        self.env['modulo.modulo'].create(modelo)

    def f_search_update(self):
        modelo=self.env['modulo.modulo'].search([('name', '=', 'ORM test')])
        print('search()', modelo, modelo.name)