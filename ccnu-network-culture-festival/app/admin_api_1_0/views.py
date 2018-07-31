# coding: utf-8
from flask import jsonify, request
from app.admin_api_1_0 import admin_api
from app.models import Anime, Article, User, Movie, Course, Notice, Photo, Startup, db


@admin_api.route("/user/<int:id>/manage/", methods=["DELETE", "PATCH"])
def manage_user(id):
    """user manage api"""
    user = User.query.filter_by(id=id).first_or_404()
    if request.method == "DELETE":
        """删除具有指定id的用户"""
        db.session.delete(user)
        db.session.commit()
        return jsonify({"msg": "ok"}), 200
    elif request.method == "PATCH":
        """更改该用户的权限"""
        role_id = int(request.form.get("jurisdiction"))
        user.role_id = role_id
        db.session.add(user)
        db.session.commit()
        return jsonify({"msg": "ok"}), 200


@admin_api.route("/movie/<int:id>/manage/", methods=["DELETE", "PATCH"])
def manage_movie(id):
    """movie manage api"""
    movie = Movie.query.filter_by(id=id).first_or_404()
    if request.method == "DELETE":
        """删除具有指定id的微视频"""
        db.session.delete(movie)
        db.session.commit()
        return jsonify({"msg": "ok"})
    elif request.method == "PATCH":
        """更改审核状态"""
        movie.is_confirm = False if movie.is_confirm else True
        db.session.add(movie)
        db.session.commit()
        return jsonify({"msg": "ok"})


@admin_api.route("/anime/<int:id>/manage/", methods=["DELETE", "PATCH"])
def manage_anime(id):
    """anime manage api"""
    anime = Anime.query.filter_by(id=id).first_or_404()
    if request.method == "DELETE":
        """删除具有指定id的动漫"""
        db.session.delete(anime)
        db.session.commit()
        return jsonify({"msg": "ok"})
    elif request.method == "PATCH":
        """更改审核状态"""
        anime.is_confirm = False if anime.is_confirm else True
        db.session.add(anime)
        db.session.commit()
        return jsonify({"msg": "ok"})


@admin_api.route("/article/<int:id>/manage/", methods=["DELETE", "PATCH"])
def manage_article(id):
    """article manage api"""
    article = Article.query.filter_by(id=id).first_or_404()
    if request.method == "DELETE":
        """删除具有指定id的网文"""
        db.session.delete(article)
        db.session.commit()
        return jsonify({"msg": "ok"})
    elif request.method == "PATCH":
        """更改审核状态"""
        article.is_confirm = False if article.is_confirm else True
        db.session.add(article)
        db.session.commit()
        return jsonify({"msg": "ok"})


@admin_api.route("/course/<int:id>/manage/", methods=["DELETE", "PATCH"])
def manage_course(id):
    """course manage api"""
    course = Course.query.filter_by(id=id).first_or_404()
    if request.method == "DELETE":
        """删除具有指定id的微课"""
        db.session.delete(course)
        db.session.commit()
        return jsonify({"msg": "ok"})
    elif request.method == "PATCH":
        """更改审核状态"""
        course.is_confirm = False if course.is_confirm else True
        db.session.add(course)
        db.session.commit()
        return jsonify({"msg": "ok"})


@admin_api.route("/photo/<int:id>/manage/", methods=["DELETE", "PATCH"])
def manage_photo(id):
    """photo manage api"""
    photo = Photo.query.filter_by(id=id).first_or_404()
    if request.method == "DELETE":
        """删除具有指定id的摄影作品"""
        db.session.delete(photo)
        db.session.commit()
        return jsonify({"msg": "ok"})
    elif request.method == "PATCH":
        """更改审核状态"""
        photo.is_confirm = False if photo.is_confirm else True
        db.session.add(photo)
        db.session.commit()
        return jsonify({"msg": "ok"})


@admin_api.route("/startup/<int:id>/manage/", methods=["DELETE", "PATCH"])
def manage_startup(id):
    """startup manage api"""
    startup = Startup.query.filter_by(id=id).first_or_404()
    if request.method == "DELETE":
        """删除具有指定id的网络创新创业作品"""
        db.session.delete(startup)
        db.session.commit()
        return jsonify({"msg": "ok"})
    elif request.method == "PATCH":
        """更改审核状态"""
        startup.is_confirm = False if startup.is_confirm else True
        db.session.add(startup)
        db.session.commit()
        return jsonify({"msg": "ok"})
