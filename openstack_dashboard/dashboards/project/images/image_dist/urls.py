'''
Created on May 20, 2014

@author: rd
'''
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from openstack_dashboard.dashboards.project.images.image_dist import views 


VIEWS_MOD = 'openstack_dashboard.dashboards.project.images.image_dist.views'


urlpatterns = patterns(VIEWS_MOD,
    #url(r'^createsite/$', views.CreateView.as_view(), name='createsite'),
    url(r'^createsite/$', views.CreateView2, name='createsite'),
    url(r'^(?P<image_id>[^/]+)/update/$',
        views.UpdateView.as_view(), name='update'),
    #url(r'^(?P<image_id>[^/]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<image_id>[^/]+)/$', views.CreateView2, name='detail'),
)