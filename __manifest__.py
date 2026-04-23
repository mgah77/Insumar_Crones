{
    'name': 'Ajuste Automático de Stock',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Ajusta stock a una cifra fija semanalmente en bodegas seleccionadas',
    'author': 'M.Gah',
    'depends': ['account', 'parches_insumar'],
    'data': [
        'data/cron_reparos.xml',
    ],
    'installable': True,
    'application': True,
}