from extra_apps import xadmin
from trade.models import OrderGoods, ShoppingCart, OrderInfo


class ShoppingCartAdmin(object):
    list_display = ['user', 'goods', 'nums']


class OrderInfoAdmin(object):
    list_display = ["user", "order_sn", "trade_no", "pay_status", "post_script", "order_mount",
                    "order_mount", "pay_time", "add_time"]

    class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ['add_time',]
        extra = 1
        style = 'tab'

    inline = [OrderGoodsInline,]


xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)