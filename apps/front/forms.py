from apps.common.forms import BaseForm
from wtforms import StringField,IntegerField
from wtforms.validators import Regexp,EqualTo,ValidationError,Length,InputRequired,URL
from .models import FrontUser
from utils import xfzcache

class SigninForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"1[345789]\d{9}", message='请输入正确格式的手机号码！'),InputRequired(message='请输入手机号码！')])
    password = StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{6,20}", message='请输入正确格式的密码！'),InputRequired(message='密码不能为空！')])
    remember = StringField()


class SignupForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"1[345789]\d{9}",message='请输入正确格式的手机号码！')])
    username = StringField(validators=[Regexp(r".{2,20}",message='请输入正确格式的用户名！')])
    graph_captcha = StringField(validators=[Regexp(r"\w{4}",message='请输入正确格式验证码！'),InputRequired(message='请输入图形验证码！')])
    password1 = StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{6,20}", message='请输入正确格式的密码！')])
    password2 = StringField(validators=[EqualTo("password1",message='两次输入的密码不一致！')])
    sms_captcha = StringField(validators=[Regexp(r"\w{4}",message='请输入正确格式的短信验证码！'),InputRequired(message='请输入验证码！')])

    def validate_telephone(self,field):
        telephone = field.data
        if FrontUser.query.filter_by(telephone=telephone).first():
            raise ValidationError(message='此手机号已经注册！')

    def validate_graph_captcha(self,field):
        graph_captcha = field.data
        graph_captcha_number = xfzcache.get(graph_captcha.lower())
        if not graph_captcha_number:
            raise ValidationError(message='图形验证码错误！')


    def validate_sms_captcha(self,field):
        sms_captcha = field.data
        telephone = self.telephone.data
        sms_captcha_mumber = xfzcache.get(telephone)
        if not sms_captcha_mumber or sms_captcha_mumber.lower() != sms_captcha.lower():
            raise ValidationError(message='短信验证码错误！')




