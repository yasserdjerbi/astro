from odoo import api, fields, models, _
from odoo.exceptions import Warning
from odoo.osv import osv
from odoo.addons import decimal_precision as dp
from odoo.http import request
import json, base64, qrcode
from io import BytesIO
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.lib.units import mm
import barcode
from barcode.writer import ImageWriter
from barcode import generate

class product_temnplate(models.Model):
    _inherit = 'product.template'
    
    @api.multi
    def print_product_template(self):
        REPORT_ID = 'product_label.report_product_label_tmpl'        
        data = {
                   'product_name':self.name,
                   'product_bar_code':self.barcode,
                   'product_list_price':self.list_price,
                   'qr_code':self.generate_QR(self.barcode),
                   'bar_code':self.generate_BARCODE(self.barcode),
                   'currency_symbol':self.currency_id.symbol
                }
        return self.env.ref(REPORT_ID).report_action(self,data=data)
    
    def generate_QR(self, data):
        qr = qrcode.QRCode (
                                version=1,
                                error_correction=qrcode.constants.ERROR_CORRECT_L,
                                box_size=20,
                                border=4,
                            )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_code = base64.b64encode(temp.getvalue())
        return str('data:image/png;base64,') + str(qr_code.decode())
    
    def generate_BARCODE(self, data):
        options = {'width': 100 * mm, 'height': 50 * mm}
        ret_val = createBarcodeDrawing('Code128', value=data, **options)  
        barcode = base64.encodestring(ret_val.asString('png')).decode()
        #raise Warning(str('data:image/png;base64,') + str(barcode))
        return str('data:image/png;base64,') + str(barcode)
        return barcode
    
