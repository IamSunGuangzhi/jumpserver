from django.conf.urls import patterns, include, url


urlpatterns = patterns('juser.views',
    # Examples:
    # url(r'^$', 'jumpserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^user_add/$', 'user_add'),
    (r'^user_list/$', 'user_list'),
    (r'^group_add/$', 'group_add'),
    (r'^group_add_ajax/$', 'group_add_ajax'),
    (r'^group_list/$', 'group_list'),
    (r'^dept_list/$', 'dept_list'),
    (r'^dept_add/$', 'dept_add'),
    (r'^user_detail/$', 'user_detail'),
    (r'^user_del/$', 'user_del'),
    (r'^user_edit/$', 'user_edit'),
    (r'^group_detail/$', 'group_detail'),
    (r'^group_del/$', 'group_del'),
    (r'^group_edit/$', 'group_edit'),
    (r'^profile/$', 'profile'),
    (r'^chg_pass/$', 'chg_pass'),
)
