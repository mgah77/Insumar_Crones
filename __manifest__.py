{
    'name': 'Insumar Crones',
    'version': '1.0',
    'category': 'Base',
    'summary': 'Crones varios',
    'author': 'M.Gah',
    'depends': ['account','l10n_cl_fe'],
    'data': [
        'data/cron_reparos.xml',
        'views/account.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'static/src/css/menu_reparo.css',
        ],
    },
    'installable': True,
    'application': True,
}