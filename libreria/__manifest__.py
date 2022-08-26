{
    "name": 'Gestión de biblioteca',
    "summary": 'Administrar el catálogo de la biblioteca y el préstamo de libros.',
    'author': 'Germán Sosa Goy',
    "category": "Services/Library",
    "version": '15.0.1.0.0',
    "website": 'https://germansosagoy.github.io/',
    'description': '',
    'depends': ['base'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/library_menu.xml'
        ],
    'demo': []
}
