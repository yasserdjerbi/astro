# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import werkzeug.utils
import json
import os

class product_label(http.Controller):
    @http.route('/product_label/index/', methods=['POST'], type='json', auth="public", website=True)
    def index(self, **kw):  
        return str ("READY") 