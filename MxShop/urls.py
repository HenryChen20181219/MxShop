"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from MxShop.settings import MEDIA_ROOT
from apps.goods.views import GoodsListViewSet, CategoryViewset, HotSearchsViewset, BannerViewset, IndexCategoryViewset
from apps.user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from apps.users.views import SmsCodeViewset, UserViewset
from extra_apps import xadmin

router = DefaultRouter()

router.register(r'goods', GoodsListViewSet, base_name='goods')
router.register(r'category', CategoryViewset, base_name='category')
router.register(r'codes', SmsCodeViewset, base_name='codes')
router.register(r'hotsearchs', HotSearchsViewset, base_name='hotsearchs')
router.register(r'users', UserViewset, base_name='users')
router.register(r'userfavs', UserFavViewset, base_name='userfavs')
router.register(r'messages', LeavingMessageViewset, base_name='messages')
router.register(r'address', AddressViewset, base_name='address')
router.register(r'banners', BannerViewset, base_name='banners')
router.register(r'indexgoods', IndexCategoryViewset, base_name='indexgoods')
#购物车url
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")

#订单相关url
router.register(r'orders', OrderViewset, base_name="orders")

goods_list = GoodsListViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^', include(router.urls)),
    url(r'^index/', TemplateView.as_view(template_name='index_html',name='index')),
    url(r'^docs/', include_docs_urls(title='暮雪生鲜')),

    url(r'^api_token_auth/', views.obtain_auth_token),
    url(r'^login', obtain_jwt_token),
    url(r'alipay/return/', AlipayViews.as_view(), name='alipay')

]
