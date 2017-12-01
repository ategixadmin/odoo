# -*- coding: utf-8 -*-

{
    'name': 'Azul Payment Acquirer',
    'category': 'Accounting',
    'summary': 'Payment Acquirer: Azul Implementation',
    'version': '1.0',
    'description': """Azul Payment Acquirer""",
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_authorize_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'installable': True,
}
