# coding: utf-8

"""
    admin site

    use: Flask-Admin
    -- https://flask-admin.readthedocs.org/en/latest/

"""

# import flask_login as login
# import flask_admin as admin
# from flask_login import current_user
# from flask_admin import Admin, BaseView, expose
# from flask_admin.contrib.sqla import ModelView
# from app import app, db
# from app.models import AnonymousUser
# from flask import redirect, flash, url_for
#
#
# class MyAdminIndexView(admin.AdminIndexView):
#     def is_accessible(self):
#         return login.current_user.is_admin()
#
#     def inaccessible_callback(self, name, **kwargs):
#         return redirect(url_for('auth.login'))
#
#
# admin = Admin(
#     app,
#     name="admin site",
#     template_mode="bootstrap3",
#     index_view=MyAdminIndexView(),
#     base_template='admin/logout.html'
# )
#
#
# # sql models management
# from app.models import User
# admin.add_view(ModelView(User, db.session))
#
# from app.models import Role
# admin.add_view(ModelView(Role, db.session))
#
# from app.models import Movie
# admin.add_view(ModelView(Movie, db.session))
#
# from app.models import Anime
# admin.add_view(ModelView(Anime, db.session))
#
# from app.models import Course
# admin.add_view(ModelView(Course, db.session))
#
# from app.models import Photo
# admin.add_view(ModelView(Photo, db.session))
#
# from app.models import Article
# admin.add_view(ModelView(Article, db.session))
#
# from app.models import Startup
# admin.add_view(ModelView(Startup, db.session))

# from app.models import W_Startup
# admin.add_view(ModelView(W_Startup, db.session))
#
# from app.models import W_Movie
# admin.add_view(ModelView(W_Movie, db.session))
#
# from app.models import W_Anime
# admin.add_view(ModelView(W_Anime, db.session))
#
# from app.models import W_Course
# admin.add_view(ModelView(W_Course, db.session))
#
# from app.models import W_Photo
# admin.add_view(ModelView(W_Photo, db.session))
#
# from app.models import W_Article
# admin.add_view(ModelView(W_Article, db.session))
#
# from app.models import Notice
# admin.add_view(ModelView(Notice, db.session))


from app import db
from . import admin
from app.admin.forms import UserForm
from flask_login import current_user, login_required
from flask import render_template, request, current_app, abort
from app.models import Anime, Article, User, Movie, Course, Photo, Startup


@admin.route('/', methods=["GET"])
@login_required
def index():
    """home page of the management backend"""
    if current_user.role_id == 3:
        return abort(403)
    return render_template("admin/home.html", current_user=current_user)


@admin.route("/user/", methods=["GET"])
@login_required
def user_manage():
    """用户管理"""
    if current_user.role_id == 3:
        return abort(403)
    page = request.args.get("page", 1, int)
    pagination = User.query.paginate(page, error_out=False,
                                     per_page=current_app.config["RESOURCES_PER_PAGE"])
    users = pagination.items
    return render_template("admin/user.html",
                           current_user=current_user,
                           users=users, pagination=pagination)


@admin.route("/movie/")
@login_required
def movie_manage():
    """微视频作品管理"""
    if current_user.role_id == 3:
        return abort(403)
    page = request.args.get("page", 1, int)
    pagination = Movie.query.paginate(page, error_out=False,
                                      per_page=current_app.config["RESOURCES_PER_PAGE"])
    movies = pagination.items
    return render_template("admin/movie.html",
                           current_user=current_user,
                           movies=movies, pagination=pagination)


@admin.route("/anime/")
@login_required
def anime_manage():
    """动漫作品管理"""
    if current_user.role_id == 3:
        return abort(403)
    page = request.args.get("page", 1, int)
    pagination = Anime.query.paginate(page, error_out=False,
                                      per_page=current_app.config["RESOURCES_PER_PAGE"])
    animes = pagination.items
    return render_template("admin/anime.html", current_user=current_user,
                           animes=animes, pagination=pagination)


@admin.route("/course/")
@login_required
def course_manage():
    """微课作品管理"""
    if current_user.role_id == 3:
        return abort(403)
    page = request.args.get("page", 1, int)
    pagination = Course.query.paginate(page, error_out=False,
                                       per_page=current_app.config["RESOURCES_PER_PAGE"])
    courses = pagination.items
    return render_template("admin/course.html", current_user=current_user,
                           courses=courses, pagination=pagination)


@admin.route("/photo/")
@login_required
def photo_manage():
    """摄影作品管理"""
    if current_user.role_id == 3:
        return abort(403)
    page = request.args.get("page", 1, int)
    pagination = Photo.query.paginate(page, error_out=False,
                                      per_page=current_app.config["RESOURCES_PER_PAGE"])
    photos = pagination.items
    return render_template("admin/photo.html", current_user=current_user,
                           photos=photos, pagination=pagination)


@admin.route("/article/")
@login_required
def article_manage():
    """网文作品管理"""
    if current_user.role_id == 3:
        return abort(403)
    page = request.args.get("page", 1, int)
    pagination = Article.query.paginate(page, error_out=False,
                                        per_page=current_app.config["RESOURCES_PER_PAGE"])
    articles = pagination.items
    return render_template("admin/article.html", current_user=current_user,
                           articles=articles, pagination=pagination)


@admin.route("/startup/")
@login_required
def startup_manage():
    """网络创新创业作品管理"""
    if current_user.role_id == 3:
        return abort(403)
    page = request.args.get("page", 1, int)
    pagination = Startup.query.paginate(page, error_out=False,
                                        per_page=current_app.config["RESOURCES_PER_PAGE"])
    startups = pagination.items
    return render_template("admin/startup.html", current_user=current_user,
                           startups=startups, pagination=pagination)


@admin.route("/new-user/", methods=["GET", "POST"])
@login_required
def new_user():
    """管理后台创建新用户"""
    form = UserForm()
    if current_user.role_id == 3:  # 普通用户无权创建用户
        return abort(403)
    if request.method == "POST":
        password = form.password.data
        password2 = form.password2.data
        email = form.email.data
        user_kind = form.user_kind.data
        username = form.username.data
        if password2 == password and email and user_kind and username:
            new_user = User(username=username, password=password, email=email, role_id=int(user_kind))
            db.session.add(new_user)
            db.session.commit()
            return "OK"
    return render_template("admin/create_user.html", form=form)
