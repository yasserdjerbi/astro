# -*- coding: utf-8 -*-
{
    'name': 'Product label',
    'description': "",
    'author': "",
    'website': "",
    'summary': "",
    'version': '0.1',
    "license": "OPL-1",
    'support': '',
    'category': 'Stock',
        # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
             'views/templates.xml',             
             'views/views.xml',
             'views/report_label.xml',
            ],
    'installable': True,
}
