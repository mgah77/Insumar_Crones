from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    has_reparos = fields.Boolean(
        string='Has Reparos',
        default=False
    )

    def _cron_update_has_reparos(self):
        AccountMove = self.env['account.move']

        companies = self.search([])

        for company in companies:
            count = AccountMove.search_count([
                ('sii_result', '=', 'Reparo'),
                ('company_id', '=', company.id),
                ('state', '=', 'posted'), 
            ])
            company.has_reparos = count > 0