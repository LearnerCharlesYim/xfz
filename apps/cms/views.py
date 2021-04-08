from flask import Blueprint,views,render_template,request,session
from utils import restful
from .models import CMSUser
from .forms import LoginForm
import config

bp = Blueprint('cms',__name__,url_prefix='/cms')

class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template('cms/login.html',message=message)
    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                if user.status:
                    session[config.CMS_USER_ID] = user.id
                    if remember:
                        #默认过期时间31天
                        session.permanent = True
                    return restful.success()
                else:
                    return restful.params_error(message='您已被禁止登入，请于管理员联系！')
            else:
                return restful.params_error(message='邮箱或密码错误')
        else:
            return restful.params_error(message=form.get_errors())


bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))