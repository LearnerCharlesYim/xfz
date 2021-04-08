from flask import Blueprint,request,make_response,jsonify
from utils.captcha.Captcha import Captcha
from io import BytesIO
from utils import xfzcache,restful
from .forms import SMSCaptchaForm

bp = Blueprint("common",__name__,url_prefix='/c')


@bp.route('/img_captcha/')
def graph_captcha():
    text,image = Captcha.gene_code()
    xfzcache.set(text.lower(), text.lower())
    out = BytesIO()
    image.save(out,'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp



@bp.route('/sms_captcha/',methods=['POST'])
def sms_captcha():
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)
        print('发送的短信验证码是：',captcha)
        xfzcache.set(telephone, captcha)
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())
