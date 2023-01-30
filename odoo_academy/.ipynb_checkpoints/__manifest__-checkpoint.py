# -*- coding:utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': """Acadent app to manage Training""",
    
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author': 'Odoo',
    
    'website': 'www.prointeccr.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends':  ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
    ],
    
    'demo': [
        'demo/academy_demo.xml',       
    ],
    
}