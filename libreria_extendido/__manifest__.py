# -*- coding: utf-8 -*-
{
    'name': "libreria_extendido",

    'summary': """
        Agrega ISBN""",
    'description': """
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',
    'depends': ['base','libreria'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/library_menu.xml',
        'views/res_partner.xml',
        'views/templates.xml',
    ],
}
