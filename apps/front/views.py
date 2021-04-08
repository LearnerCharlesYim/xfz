from flask import Blueprint,render_template,request,session,redirect,url_for
from utils import restful
from .forms import SigninForm,SignupForm
from .models import FrontUser
import config
from exts import db
bp = Blueprint('front',__name__)


@bp.route('/')
def index():
    return render_template('news/index.html')


@bp.route('/news/detail/')
def news_detail():
    return render_template('news/news_detail.html')


@bp.route('/course/')
def course():
    return render_template('course/course_index.html')


@bp.route('/course/detail')
def course_detail():
    return render_template('course/course_detail.html')


@bp.route('/search/')
def search():
    return render_template('search/search.html')


@bp.route('/payinfo/')
def payinfo():
    return render_template('payinfo/payinfo.html')


@bp.route('/account/signin/',methods=['POST'])
def signin():
    form = SigninForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        password = form.password.data
        remember = form.remember.data
        user = FrontUser.query.filter_by(telephone=telephone).first()
        if user and user.check_password(password):
            if user.status:
                session[config.FRONT_USER_ID] = user.id
                if remember:
                    session.permanent = True
                return restful.success()
            else:
                return restful.params_error(message='您已被禁用此账号，请联系管理员！')
        else:
            return restful.params_error(message='手机号或密码错误！')
    else:

        return restful.params_error(form.get_error())


@bp.route('/account/signout/')
def signout():
    del session[config.FRONT_USER_ID]
    return redirect(url_for('front.index'))


@bp.route('/account/signup/',methods=['POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        username = form.username.data
        password = form.password1.data
        user = FrontUser(telephone=telephone,username=username,password=password)
        db.session.add(user)
        db.session.commit()
        session[config.FRONT_USER_ID] = user.id
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())
