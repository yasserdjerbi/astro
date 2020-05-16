from odoo import api, fields, models, _
from odoo.exceptions import Warning, ValidationError, UserError
from functools import partial
import psycopg2
from odoo.tools import float_is_zero
import logging
from odoo import api, fields, models, tools, _
_logger = logging.getLogger(__name__)

class pos_order(models.Model):
    _inherit = 'pos.order'
    #@api.model
    #def _order_fields(self, ui_order):
    #    process_line = partial(self.env['pos.order.line']._order_line_fields, session_id=ui_order['pos_session_id'])
    #    pos_reference = self.get_sequence()
    #    return {
    #                'name':         pos_reference,
    #                'user_id':      ui_order['user_id'] or False,
    #                'session_id':   ui_order['pos_session_id'],
    #                'lines':        [process_line(l) for l in ui_order['lines']] if ui_order['lines'] else False,
    #                'pos_reference': pos_reference,
    #                'partner_id':   ui_order['partner_id'] or False,
    #                'date_order':   ui_order['creation_date'],
    #                'fiscal_position_id': ui_order['fiscal_position_id'],
    #                'pricelist_id': ui_order['pricelist_id'],
    #                'amount_paid':  ui_order['amount_paid'],
    #                'amount_total':  ui_order['amount_total'],
    #                'amount_tax':  ui_order['amount_tax'],
    #                'amount_return':  ui_order['amount_return'],
    #                'pos_reference1': pos_reference,
    #            }
#
   
    
    @api.multi
    def get_sequence(self):
        sequence = self.env['ir.sequence'].search([('code','=','DPOS')], limit=1)
        sequence_number = str("")
        if(sequence):
            sequence = self.env['ir.sequence'].next_by_code('DPOS')
            sequence_number = sequence
        else:
            error_msg = _('Please define sequence with "DPOS" as code')
            raise ValidationError(error_msg)
        return sequence_number