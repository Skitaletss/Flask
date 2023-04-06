from flask import url_for, redirect
from flask_admin import expose, BaseView, AdminIndexView
from sqlalchemy import desc


from models import Post


class MyMainView(AdminIndexView):
    @expose('/')
    def admin_main(self):
        post = Post.query.order_by(Post.date).all()
        image = url_for('static', filename=f'storage/post_img')
        return self.render('admin/index.html', post=post, image=image)
