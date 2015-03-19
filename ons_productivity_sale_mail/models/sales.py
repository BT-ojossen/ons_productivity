# -*- coding: utf-8 -*-
#
#  File: models/sales.py
#  Module: ons_productivity_sale_mail
#
#  Created by cyp@open-net.ch
#
#  Copyright (c) 2015-TODAY Open-Net Ltd. <http://www.open-net.ch>
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-TODAY OpenERP S.A. <http://www.openerp.com>
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

from openerp.osv import fields, osv
from openerp.tools.translate import _
import time

class sale_order(osv.Model):
    _inherit = 'sale.order'
    
    _columns = {
        'ons_validation_flag': fields.boolean('Validated'),
        'ons_validation_by': fields.many2one('res.users', 'By'),
        'ons_validation_date': fields.date('Date'),
    }
    
    def create(self, cr, uid, vals, context=None):
        if vals.get('ons_validation_flag', False):
            vals.update({'ons_validation_by': uid, 'ons_validation_date': time.strftime('%Y-%m-%d')})
        
        return super(sale_order, self).create(cr, uid, vals, context=context)

    def write(self, cr, uid, ids, vals, context=None):
        if vals.get('ons_validation_flag', False):
            vals.update({'ons_validation_by': uid, 'ons_validation_date': time.strftime('%Y-%m-%d')})
        
        return super(sale_order, self).write(cr, uid, ids, vals, context=context)