from wtforms import Form
from wtforms import StringField
from wtforms.validators import regexp,InputRequired,ValidationError
from apps.front.models import FrontUser

class BaseForm(Form):
    def get_error(self):
        message = self.errors.popitem()[1][0]
        return message

    def get_errors(self):
       errors = self.errors
       message = []
       for message_dicts in errors.values():
           for message_dict in message_dicts:
               message.append(message_dict)
       return message


class SMSCaptchaForm(BaseForm):
    telephone = StringField(validators=[regexp(r'1[345789]\d{9}',message='请输入正确格式的手机号'),InputRequired(message='请输入正确手机号！')])

    def validate_telephone(self,field):
        telephone = field.data
        if FrontUser.query.filter_by(telephone=telephone).first():
            raise ValidationError(message='此手机号已经注册！')







