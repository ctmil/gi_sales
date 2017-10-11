# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate
from datetime import datetime, timedelta, date
from dateutil import relativedelta
#Get the logger
_logger = logging.getLogger(__name__)

class sale_order(models.Model):
        _inherit = 'sale.order'

	@api.multi
	def _compute_amount_untaxed_nt(self):
		for so in self:
			so.amount_untaxed_nt = sol.amount_untaxed / 1.21

        amount_untaxed_nt = fields.Float('amount_untaxed_nt',compute=_compute_amount_untaxed_nt)

class sale_order_line(models.Model):
        _inherit = 'sale.order.line'

	@api.multi
	def _compute_price_unit_nt(self):
		for sol in self:
			sol.price_unit_nt = sol.price_unit / 121

	@api.multi
	def _compute_price_subtotal_nt(self):
		for sol in self:
			sol.price_subtotal_nt = sol.price_subtotal / 1.21

        price_unit_nt = fields.Float('price_unit_nt',compute=_compute_price_unit_nt)
        price_subtotal_nt = fields.Float('price_subtotal_nt',compute=_compute_price_subtotal_nt)

