function Auth() {
    var self = this;
    self.maskWrapper = $('.mask-wrapper');
    self.scrollWrapper = $(".scroll-wrapper");
    self.smsCaptcha = $('.sms-captcha-btn');
}

Auth.prototype.run = function () {
    var self = this;
    self.listenShowHideEvent();
    self.listenSwitchEvent();
    self.listenSigninEvent();
    self.listenImgCaptchaEvent();
    self.listenSmsCaptchaEvent();
    self.listenSignupEvent();
};

Auth.prototype.showEvent = function () {
    var self = this;
    self.maskWrapper.show();
};

Auth.prototype.hideEvent = function () {
    var self = this;
    self.maskWrapper.hide();
};

Auth.prototype.smsSuccessEvent = function () {
    var self = this;
    messageBox.showSuccess('短信验证码发送成功！');
    // self.smsCaptcha.addClass('disabled');
    self.smsCaptcha.css({"cursor":"not-allowed"});
    var count = 60;
    self.smsCaptcha.unbind('click');
    var timer = setInterval(function () {
        self.smsCaptcha.text(count+'s');
        count -= 1;
        if(count <= 0){
            clearInterval(timer);
            self.smsCaptcha.css({"cursor":"pointer"});
            self.smsCaptcha.text('发送验证码');
            self.listenSmsCaptchaEvent();
        }
    },1000);
};


Auth.prototype.listenShowHideEvent = function () {
    var self = this;
    var signinBtn = $('.signin-btn');
    var signupBtn = $('.signup-btn');
    var closeBtn = $('.close-btn');

    signinBtn.click(function () {
        self.showEvent();
        self.scrollWrapper.css({"left":0});
    });

    signupBtn.click(function () {
        self.showEvent();
        self.scrollWrapper.css({"left":-400});
    });

    closeBtn.click(function () {
        self.hideEvent();
    });
};

Auth.prototype.listenSwitchEvent = function () {
    var self = this;
    var switcher = $(".switch");
    switcher.click(function () {
        var currentLeft = self.scrollWrapper.css("left");
        currentLeft = parseInt(currentLeft);
        if(currentLeft < 0){
            self.scrollWrapper.animate({"left":'0'});
        }else{
            self.scrollWrapper.animate({"left":"-400px"});
        }
    });
};

Auth.prototype.listenImgCaptchaEvent = function () {
    var imgCaptcha = $('.img-captcha');
    imgCaptcha.click(function () {
        imgCaptcha.attr("src","/c/img_captcha/"+"?random="+Math.random())
    });
};

Auth.prototype.listenSigninEvent = function () {
    var self = this;
    var signinGroup = $('.signin-group');
    var telephoneInput = signinGroup.find("input[name='telephone']");
    var passwordInput = signinGroup.find("input[name='password']");
    var rememberInput = signinGroup.find("input[name='remember']");

    var submitBtn = signinGroup.find(".submit-btn");
    submitBtn.click(function () {
        var telephone = telephoneInput.val();
        var password = passwordInput.val();
        var remember = rememberInput.prop("checked");

        xfzajax.post({
            'url': '/account/signin/',
            'data': {
                'telephone': telephone,
                'password': password,
                'remember': remember?1:0
            },
            'success': function (result) {
                if(result['code'] == 200){
                    self.hideEvent();
                    xfzalert.alertSuccessToast('恭喜您登录成功！');
                    setTimeout(function () {
                        window.location.reload();
                    },1200);
                }else{
                    var messageObject = result['message'];
                    if(typeof messageObject == 'string' || messageObject.constructor == String){
                        window.messageBox.show(messageObject);
                    }else{
                        for(var key in messageObject){
                            var messages = messageObject[key];
                            var message = messages[0];
                            window.messageBox.show(message);
                        }
                    }
                }
            },
            'fail': function (error) {
                console.log(error);
            }
        });
    });
};

Auth.prototype.listenSmsCaptchaEvent = function () {
    var self = this;
    var smsCaptcha = $(".sms-captcha-btn");
    var telephoneInput = $(".signup-group input[name='telephone']");
    smsCaptcha.click(function () {
        var telephone = telephoneInput.val();
        xfzajax.post({
            'url': '/c/sms_captcha/',
            'data':{
                'telephone': telephone
            },
            'success': function (result) {
                if(result['code'] == 200){
                    self.smsSuccessEvent();
                }
            },
            'fail': function (error) {
                console.log(error);
            }
        });
    });
};

Auth.prototype.listenSignupEvent = function () {
    var self = this;
    var signupGroup = $('.signup-group');
    var submitBtn = signupGroup.find('.submit-btn');
    submitBtn.click(function (event) {
        event.preventDefault();
        var telephoneInput = signupGroup.find("input[name='telephone']");
        var usernameInput = signupGroup.find("input[name='username']");
        var imgCaptchaInput = signupGroup.find("input[name='graph_captcha']");
        var password1Input = signupGroup.find("input[name='password1']");
        var password2Input = signupGroup.find("input[name='password2']");
        var smsCaptchaInput = signupGroup.find("input[name='sms_captcha']");

        var telephone = telephoneInput.val();
        var username = usernameInput.val();
        var graph_captcha = imgCaptchaInput.val();
        var password1 = password1Input.val();
        var password2 = password2Input.val();
        var sms_captcha = smsCaptchaInput.val();

        xfzajax.post({
            'url': '/account/signup/',
            'data': {
                'telephone': telephone,
                'username': username,
                'graph_captcha': graph_captcha,
                'password1': password1,
                'password2': password2,
                'sms_captcha': sms_captcha
            },
            'success': function (result) {
                    if(result['code'] == 200){
                    self.hideEvent();
                    xfzalert.alertSuccessToast('恭喜您注册成功！');
                    setTimeout(function () {
                        window.location.reload();
                    },1200);
                }else{
                    var messageObject = result['message'];
                    if(typeof messageObject == 'string' || messageObject.constructor == String){
                        window.messageBox.show(messageObject);
                    }else{
                        for(var key in messageObject){
                            var messages = messageObject[key];
                            var message = messages[0];
                            window.messageBox.show(message);
                        }
                    }
                }
            },
            'fail': function (error) {
                console.log(error);
            }
        });
    });
};


$(function () {
    var auth = new Auth();
    auth.run();
});

