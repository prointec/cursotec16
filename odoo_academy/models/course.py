# -*- coding:utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='Level', 
                             selection = [('beginner','Beginner'),
                                          ('intermediate','Intermediate'),
                                          ('advanced','Advanced')],
                             copy = False)
    
    active = fields.Boolean(string='Active', default='True')
    
    base_price = fields.Float(string='Base Price', default=0.00)
    addtional_fee = fields.Float(string='Additional Fee', default=0.00)
    total_price = fields.Float(string='Total Price', read_only=True)
    
    session_ids = fields.One2many(comodel_name='academy.session',
                                   inverse_name='course_id',
                                   string='Sessions')
    
    
    @api.onchange('base_price','addtional_fee')
    def _onchange_total_price(self):
        if self.base_price < 0.00:
            raise UserError('Base Price cannot be set as Negative')
        self.total_price = self.base_price + self.addtional_fee
        
    @api.constrains('addtional_fee')
    def _check_addtional_fee(self):
        for record in self:
            if record.addtional_fee < 10.00:
                raise ValidationError('Addtional fee cannot be less than 10.00 %s' % record.addtional_fee)
        