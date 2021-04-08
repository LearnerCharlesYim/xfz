from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


#权限
# class CMSPermission(object):
#     #255二进制表示 1111 1111
#     ALL_PERMISSION = 0b11111111
#     #1.访问者(无权限)
#     VISITOR        = 0b00000001
#     #2.管理帖子
#     POSTER         = 0b00000010
#     #3.管理评论
#     COMMENTER      = 0b00000100
#     #4.管理板块的权限
#     BOARDER        = 0b00001000
#     #5.管理前台用户的权限
#     FRONTUSER      = 0b00010000
#     #6.管理后台用户的权限
#     CMSUSER        = 0b00100000
#     #7.超级管理员
#     ADMINER        = 0b01000000
#
#     PERMISSION_MAP = {
#         ALL_PERMISSION: '拥有至高无上的权限',
#         CMSUSER :' 管理后台用户',
#         FRONTUSER:'管理前台用户',
#         BOARDER:'管理板块',
#         COMMENTER:'管理评论',
#         POSTER:'管理帖子',
#         VISITOR:'访问者(默认)'
#     }
#
#
# cms_role_user = db.Table(
#     'cms_role_user',
#     db.Column('cms_role_id',db.Integer,db.ForeignKey('cms_role.id'),primary_key=True),
#     db.Column('cms_user_id',db.Integer,db.ForeignKey('cms_user.id'),primary_key=True)
#
# )


# class CMSRole(db.Model):
#     __tablename__ = 'cms_role'
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     name = db.Column(db.String(50),nullable=False)
#     desc = db.Column(db.String(200),nullable=True)
#     create_time = db.Column(db.DateTime,default=datetime.now)
#     permissions = db.Column(db.Integer,default=CMSPermission.VISITOR)
#
#     users = db.relationship('CMSUser',secondary=cms_role_user,backref='roles')
#
#     @property
#     def permission_dicts(self):
#         all_permissions = self.permissions
#         permission_dict_list = []
#
#         # 如果是超级管理员
#         if all_permissions == CMSPermission.ALL_PERMISSION:
#             permission_dict_list = [{CMSPermission.ALL_PERMISSION : CMSPermission.PERMISSION_MAP[CMSPermission.ALL_PERMISSION]}]
#         else:
#             for permission, permission_info in CMSPermission.PERMISSION_MAP.items():
#                 if permission & all_permissions == permission:
#                     permission_dict_list.append({permission: permission_info})
#
#         return permission_dict_list



class CMSUser(db.Model):
    __tabalename__ = 'cms_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    _password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    join_time = db.Column(db.DateTime,default=datetime.now())
    status = db.Column(db.Boolean,default=True)


    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self,raw_password):
        result = check_password_hash(self.password,raw_password)
        return result


    # @property
    # def permissions(self):
    #     if not self.roles:
    #         return 0
    #     all_permissions = 0
    #     for role in self.roles:
    #         permissions = role.permissions
    #         all_permissions |= permissions
    #
    #     return all_permissions


    # def has_permission(self,permission):
    #     all_permissions = self.permissions
    #     result = all_permissions & permission == permission
    #     return result
    #
    # def is_developer(self):
    #     return self.has_permission(CMSPermission.ALL_PERMISSION)








