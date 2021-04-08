from wtforms import StringField,IntegerField
from wtforms.validators import Email,InputRequired,Length,EqualTo
from apps.common.forms import BaseForm
from wtforms import ValidationError
from flask import g


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确邮箱格式'),InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(6,20,message='请输入正确格式密码(6-20位字符)')])
    remember = IntegerField()