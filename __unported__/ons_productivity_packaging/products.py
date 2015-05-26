# -*- coding: utf-8 -*-
#
#  File: products.py
#  Module: ons_productivity_packaging
#
#  Created by cyp@open-net.ch
#
#  Copyright (c) 2014 Open Net Sàrl. All rights reserved.
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields,osv
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp

class product_template(osv.osv):
    _inherit = 'product.template'
    
    # ---------- Fields management
    
    _columns = {
        'pack_price': fields.float('Per pack sale price', digits_compute=dp.get_precision('Product Price'), help="Base price when sold by package, to compute the customer price."),
    }
    
    # ---------- Utilities

    def compute_weighted_average(self, cr, uid, ids, context=None):        
        return False

product_template()
