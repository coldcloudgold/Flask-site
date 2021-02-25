from posts import posts
from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from forms import CreatePost, CreateComment
from models import Comment, Post, Tag
from app import db


@posts.route('/<int:number_post>', methods=['GET', 'POST'])
def post(number_post):
    post = Post.query.filter_by(id=number_post).first()
    form = CreateComment()
    if form.validate_on_submit():
        get_comment = Comment.query.filter(
            Comment.body == form.body.data, Comment.user == current_user, Comment.post == post).first()
        if not get_comment:
            comment = Comment(body=form.body.data,
                              user=current_user, post=post)
            db.session.add(comment)
            db.session.commit()
            return render_template(template_name_or_list='posts/post.html', post=post, form=form)
    if post:
        return render_template(template_name_or_list='posts/post.html', post=post, form=form)
    abort(status=404)


@posts.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreatePost()
    if form.validate_on_submit():
        if not Post.query.filter_by(title=form.title.data).first():
            post = Post(title=form.title.data,
                        body=form.body.data, user=current_user)
            db.session.add(post)
            db.session.commit()
            return redirect(location=url_for(endpoint='index'))
        flash('Статья с таким заголовком есть')
        return render_template(template_name_or_list='posts/create.html', form=form)
    return render_template(template_name_or_list='posts/create.html', form=form)


@posts.route('/delete/<int:number_post>')
@login_required
def delete(number_post):
    post = Post.query.filter_by(id=number_post).first()
    if post.user == current_user or current_user.admin:
        db.session.delete(post)
        db.session.commit()
    return redirect(location=url_for(endpoint='users.profile'))


@posts.route('/edit/<int:number_post>', methods=['GET', 'POST'])
@login_required
def edit(number_post):
    post = Post.query.filter_by(id=number_post).first()
    if post.user == current_user or current_user.admin:
        form = CreatePost(obj=post)
        if form.validate_on_submit():
            if not Post.query.filter_by(title=form.title.data).first():
                post.title = form.title.data
                post.body = form.body.data
                db.session.add(post)
                db.session.commit()
                return redirect(location=url_for(endpoint='users.profile'))
            flash('Статья с таким заголовком есть')
            return render_template(template_name_or_list='posts/edit.html', form=form)
        return render_template(template_name_or_list='posts/edit.html', form=form)
    return redirect(location=url_for(endpoint='posts.create'))


@posts.route('/tag/<title_tag>')
def tag(title_tag):
    tag = Tag.query.filter_by(title=title_tag).first()
    if tag:
        posts = Post.query.filter(Post.tag.contains(tag)).all()
        return render_template(template_name_or_list='posts/tag.html', posts=posts, tag=tag)
    abort(status=404)
