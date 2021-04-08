
// 用来处理导航条的
function FrontBase() {}


FrontBase.prototype.run = function () {
    var self = this;
    self.listenAuthBoxHover();
    self.handleNavStatus();
};

FrontBase.prototype.listenAuthBoxHover = function () {
    var authBox = $(".auth-box");
    var userMoreBox = $(".user-more-box");
    authBox.hover(function () {
        userMoreBox.show();
    },function () {
        userMoreBox.hide();
    });
};

$(function () {
    var frontBase = new FrontBase();
    frontBase.run();
});

FrontBase.prototype.handleNavStatus = function () {
    // http://127.0.0.1:8000/payinfo/
    var url = window.location.href;
    var protocol = window.location.protocol;
    var host = window.location.host;
    // http: + // + 127.0.0.1:8000
    var domain = protocol + '//' + host;
    var path = url.replace(domain,'');
    var navLis = $(".nav li");
    navLis.each(function (index,element) {
        // js => $(js对象)
        var li = $(element);
        var aTag = li.children("a");
        var href = aTag.attr("href");
        if(href === path){
            li.addClass("active");
            return false;
        }
    });
};

