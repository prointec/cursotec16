# -*- coding:utf-8 -*-

{
    'name': 'Admi Biblioteca',
    
    'summary': """Administracion de biblioteca""",
    
    'description': """
        Adm de biblioteca:
        - Libros
        - Prestamos
        - Otros
    """,
    
    'author': 'Prointec',
    
    'website': 'www.prointeccr.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends':  ['base'],
    
    'data': [
        'security/biblioteca_security.xml',
        'security/ir.model.access.csv',
    ],
    
    'demo': [
        'demo/biblioteca_demo.xml',
        'demo/biblioteca_demo1.xml',
    ],  
}