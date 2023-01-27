# -*- coding:utf-8 -*-

from odoo import models, fields, api

class Libro(models.Model):
    
    _name = 'biblioteca.libro'
    _description = 'Informacion del libro'
    
    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Description')
      
    autores = fields.Char(string='Autor')
    editores = fields.Char(string='Editores')
    genero = fields.Char(string='Genero')
    ano_edicion = fields.Integer(string='Año Edición', copy=False)
        
    isbn = fields.Char(string='ISBN', copy=False)

    active = fields.Boolean(string='Active', default='True')