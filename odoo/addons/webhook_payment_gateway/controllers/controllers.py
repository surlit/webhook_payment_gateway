# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/webhookPaymentGateway(http.Controller):
#     @http.route('//mnt/extra-addons/webhook_payment_gateway//mnt/extra-addons/webhook_payment_gateway', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/webhook_payment_gateway//mnt/extra-addons/webhook_payment_gateway/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/webhook_payment_gateway.listing', {
#             'root': '//mnt/extra-addons/webhook_payment_gateway//mnt/extra-addons/webhook_payment_gateway',
#             'objects': http.request.env['/mnt/extra-addons/webhook_payment_gateway./mnt/extra-addons/webhook_payment_gateway'].search([]),
#         })

#     @http.route('//mnt/extra-addons/webhook_payment_gateway//mnt/extra-addons/webhook_payment_gateway/objects/<model("/mnt/extra-addons/webhook_payment_gateway./mnt/extra-addons/webhook_payment_gateway"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/webhook_payment_gateway.object', {
#             'object': obj
#         })

