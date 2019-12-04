from apps.user_operation.models import UserFav, UserAddress, UserLeavingMessage
from extra_apps import xadmin


class UserFavAdmin(object):
    list_play = ['user', 'goods', 'add_time']


class UserleavingMessageAdmin(object):
    list_play = ['user', 'message_type', 'message', 'add_time']


class UserAddressAdmin(object):
    list_play = ['signer_name', 'signer_mobile', 'district', 'address']


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserleavingMessageAdmin)