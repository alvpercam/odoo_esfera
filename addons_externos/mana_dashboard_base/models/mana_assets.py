# -*- coding: utf-8 -*-

import os
from glob import glob
from logging import getLogger
from werkzeug import urls

import odoo
import odoo.modules.module  # get_manifest, don't from-import it
from odoo import api, fields, models, tools
from odoo.tools import misc
from odoo.addons.base.models.assetsbundle import AssetsBundle, JavascriptAsset
import xw_utils

_logger = getLogger(__name__)

# patch AssetsBundle
SPECIAL_FILES = {
    '/mana_dashboard/static/mana_block_base.js': True
}

class IrAsset(models.Model):
    """
    asset
    """
    _inherit = 'ir.asset'

    def _get_asset_paths(self, bundle, addons=None, css=False, js=False):
        """
        attach our custom assets
        """
        path_list = super(IrAsset, self)._get_asset_paths(bundle, addons, css, js)
        if bundle == 'web.assets_backend':
            for path in SPECIAL_FILES:
                path_list.append((path, 'mana_dashboard', 'web.assets_backend'))
        return path_list

# patch fetch_content
_old_fetch_content = AssetsBundle._fetch_content
def _fetch_content(self):
    """
    get custom countent
    """
    if self._filename in SPECIAL_FILES:
        return xw_utils.get_file_content(self._filename)
    return _old_fetch_content(self)
AssetsBundle._fetch_content = _fetch_content

# patch stat
_old_stat = AssetsBundle._stat
def _stat(self):
    if self._filename in SPECIAL_FILES:
        return
    return _old_stat(self)
AssetsBundle._stat = _stat