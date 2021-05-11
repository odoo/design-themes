import werkzeug
from openerp.addons.web import http
from openerp.addons.web.http import request

class snippet_latest_posts_controller(http.Controller):

    # @http.route(['/snippet_latest_posts/fetch'], type='json', auth='public', website=True)
    # def fetch_latest_posts(self, fields, domain, limit=None, order='create_date desc', context={}):
    #     return request.env['blog.post'].search_read(domain, fields, limit=limit, order=order, context=context)

    @http.route(['/snippet_latest_posts/render'], type='json', auth='public', website=True)
    def render_latest_posts(self, template, domain, limit=None, order='create_date desc'):
        posts = request.env['blog.post'].search(domain, limit=limit, order=order)
        return request.registry['ir.ui.view'].render(request.cr, request.uid, template, {'posts': posts}, context=request.context)