from flask import url_for, redirect
from flask_admin import expose, BaseView, AdminIndexView
from sqlalchemy import desc


from models import Post


class MyMainView(AdminIndexView):
    @expose('/')
    def admin_main(self):
        posts = Post.query.order_by(desc(Post.date)).all()
        image = url_for('static', filename=f'storage/post_img')
        return self.render('admin/index.html', posts=posts, image=image)
