# -*- coding:utf-8 -*-

from odoo import models, fields, api

class Libro(models.Model):
    
    _name = 'biblioteca.libro'
    _description = 'Informacion del libro'
    
    nombre = fields.Char(string='Nombre', required=True)
    descricion = fields.Text(string='Description')
      
    autor = fields.Char('Autor', copy=False)

    active = fields.Boolean(string='Active', default='True')