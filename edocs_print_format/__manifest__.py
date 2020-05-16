# -*- coding: utf-8 -*-
{
    'name': 'POS Reporte / Informe Z & Formato Ticket de venta',
    'description': "Informe Z & Formato Ticket de venta",
    'author': "ROCKSCRIPTS",
    'website': "https://instagram.com/rockscripts",
    'summary': "Formato para documentos contables",
    'version': '0.1',
    "license": "OPL-1",
    'price':'30',
    'currency':'USD',
    'support': 'rockscripts@gmail.com',
    'category': 'Point of Sale',
    "images": ["images/banner.png"],
        # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'point_of_sale'],

    # always loaded
    'data': [
             'views/templates.xml',             
             'views/report_base.xml',
             'views/report_z_tmpl.xml',
             'views/report_z_tmpl_dian.xml',
             'views/pos_config.xml',
             'data/mail_attachment.xml',
            ],
    'qweb': [
                'static/src/xml/pos.xml'
            ],
    'security/z_pos.csv'
    #"external_dependencies": {"python" : ["pytesseract"]},
    'installable': True,
}
