from odoo import http
from odoo.http import request

class PracticeController(http.Controller):

    @http.route(['/input_test'], type="http", auth="public", website="True")
    def input_test(self, **post):
        input_sale_order = request.env['sale.order'].sudo().search([])
        print(input_sale_order, '-------sale order -----------------')
        values = {
            'input_sale_order': input_sale_order,
            'partner_id': 3
        }

        return request.render("practice_controllers.website_input_customer_sale_order", values)


    @http.route(['/output_test'], type="http", auth="public", website="True")
    def output_test(self, **post):
        print(post, '--------')
        store = {'partner_shipping_id': 1, 'partner_invoice_id': 1, 'pricelist_id': 1}
        post.update(store)

        input_sale_order = request.env['sale.order'].sudo().create(post)
        print(input_sale_order, '-------------------------')
        return request.render("practice_controllers.website_output_sale_order")