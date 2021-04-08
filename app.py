from flask import Flask
from apps.front import bp as front_bp
from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from exts import db
import config


def create_app():
    app = Flask(import_name=__name__,
                static_folder='front/dist',  # 配置静态文件的文件夹
                template_folder='front/templates')  # 配置模板文件的文件夹
    app.config.from_object(config)
    app.register_blueprint(front_bp)
    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    db.init_app(app)
    return app


app = create_app()



if __name__ == '__main__':
    app.run()
