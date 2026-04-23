from odoo import models, fields

class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    # Activa esta bodega para el proceso de auto-ajuste semanal
    enable_auto_fix = fields.Boolean(string="Activar Ajuste Semanal Automático")