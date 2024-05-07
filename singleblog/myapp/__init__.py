from django.apps import AppConfig
# default_app_config = 'myapp.My'


class Myappconfig(AppConfig):
    name = 'myapp'
    verbose_name = '我的博客'


default_app_config = 'myapp.Myappconfig'
