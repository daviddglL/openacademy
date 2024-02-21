# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Academia de cursos de programación para aprender de todo""",

    'description': """
        Academia de programación
    """,

    'author': "Daniel López ",
    'website': "https://www.openacademy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Formación',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/openacademy.xml',
        'demo/demo.xml'
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'application':True,
    'sequence':1
}
