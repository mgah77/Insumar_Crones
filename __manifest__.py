{
    'name': 'Ajuste Automático de Stock',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Ajusta stock a una cifra fija semanalmente en bodegas seleccionadas',
    'author': 'M.Gah',
    'depends': ['stock', 'product'],
    'data': [
        'views/warehouse_views.xml',
        'views/product_views.xml',
        'security/cron_data.xml',
    ],
    'installable': True,
    'application': True,
}