# -*- coding: utf-8 -*-
{
    'name': "blockbuster_directores",

    'summary': """
        Agrega directores de cine""",
    'description': """
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','blockbuster'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/blockbuster_menu.xml',
        'views/res_partner.xml',
        'views/templates.xml',
    ],
    'installable': True,
}
