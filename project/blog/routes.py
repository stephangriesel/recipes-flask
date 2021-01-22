from . import blog_blueprint
from flask import render_template, abort


blog_post_titles = ['kitchenaid_mixer']


@blog_blueprint.route('/blog/')
def blog():
    return render_template('blog/blog.html')


@blog_blueprint.route('/blog/<blog_title>/')
def posts(blog_title):
    if blog_title not in blog_post_titles:
        abort(404)

    return render_template(f'blog/{blog_title}.html')
