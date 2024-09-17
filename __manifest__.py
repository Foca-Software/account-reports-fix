# -*- coding: utf-8 -*-
# (C) 2020 Smile (<http://www.smile.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "Account Reports Fix",
    "version": "13.0.2.0.0",
    "sequence": 100,
    "category": "Nybble",
    "author": "Nybble",
    "license": 'LGPL-3',
    "description": """
        Corrección para el error del informe de impuestos""",
    "depends": [ 'account','account_reports','account_withholding','l10n_ar_reports'
    ],
    "data": [
        "views/account_ar_vat_line_view.xml"
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
