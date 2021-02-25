from flask import render_template, redirect, url_for, request
from app import app, login_manager
from models import Post, User


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    user_query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.id.desc()) if not user_query else Post.query.filter(
        Post.title.contains(user_query) | Post.body.contains(user_query))
    pages = posts.paginate(page=page, per_page=app.config['POSTS_PER_PAGE'])
    prev_page = pages.prev_num if pages.has_prev else None
    next_page = pages.next_num if pages.has_next else None
    return render_template(template_name_or_list='index.html',
                           posts=pages.items,
                           page=[prev_page, next_page],
                           user_query=user_query)


@app.errorhandler(404)
def page_not_found(error):
    return render_template(template_name_or_list='page_not_found.html'), 404


@app.errorhandler(401)
def authorization_protect(error):
    return redirect(location=url_for(endpoint='users.authorization')), 401
