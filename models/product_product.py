from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Campos en la Plantilla (para que se vean en la vista principal)
    enable_auto_fix = fields.Boolean(string="Activar Ajuste Automático")
    fixed_stock_quantity = fields.Float(string="Cantidad Fija Objetivo", default=1000, help="Cantidad a la que se reseteará el stock")

class ProductProduct(models.Model):
    _inherit = 'product.product'

    # Relacionamos los campos para que la lógica pueda leerlos desde la variante
    enable_auto_fix = fields.Boolean(related='product_tmpl_id.enable_auto_fix', readonly=False)
    fixed_stock_quantity = fields.Float(related='product_tmpl_id.fixed_stock_quantity', readonly=False)

    def action_weekly_stock_adjustment(self):
        """
        Ejecutado por el Cron.
        """
        # Buscamos bodegas habilitadas
        warehouses = self.env['stock.warehouse'].search([('enable_auto_fix', '=', True)])
        
        # Buscamos plantillas habilitadas (porque los campos ahora están ahí)
        templates = self.env['product.template'].search([('enable_auto_fix', '=', True), ('type', '=', 'product')])

        # Expandimos a variantes para procesar el stock real
        products = templates.mapped('product_variant_ids')

        for wh in warehouses:
            location_id = wh.lot_stock_id.id
            
            for product in products:
                # Obtener stock actual
                current_qty = product.with_context(location=location_id).qty_available
                target_qty = product.fixed_stock_quantity

                # Lógica: Diferente al objetivo Y distinto de cero
                if current_qty != target_qty and current_qty > 0:
                    
                    # Realizar el ajuste
                    self.env['stock.quant'].with_context(inventory_mode=True).create({
                        'product_id': product.id,
                        'location_id': location_id,
                        'inventory_quantity': target_qty,
                    })._apply_inventory()

                    # Mensaje en el chatter
                    product.message_post(
                        body=_(f"Ajuste Automático: Bodega <b>{wh.name}</b>. "
                               f"Cantidad actualizada de <b>{current_qty}</b> a <b>{target_qty}</b>.")
                    )