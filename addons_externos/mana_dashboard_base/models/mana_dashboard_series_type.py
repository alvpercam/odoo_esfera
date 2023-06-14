
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ManaDashboardSeriesType(models.Model):
    '''
    Model Project
    '''
    _name = 'mana_dashboard.series_type'
    _description = 'false'

    name = fields.Char(string='name')


