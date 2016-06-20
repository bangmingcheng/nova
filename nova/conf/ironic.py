# needs:fix_opt_description
# needs:check_deprecation_status
# needs:check_opt_group_and_type
# needs:fix_opt_description_indentation


# Copyright 2015 Intel Corporation
# All Rights Reserved.
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

from oslo_config import cfg

ironic_group = cfg.OptGroup(
    'ironic',
    title='Ironic Options')

ironic_options = [
    cfg.IntOpt('api_version',
        default=1,
        deprecated_for_removal=True,
        help='Version of Ironic API service endpoint. '
             'DEPRECATED: Setting the API version is not possible anymore.'),
    cfg.StrOpt(
        'api_endpoint',
        help='URL for Ironic API endpoint.'),
    cfg.StrOpt(
        'admin_username',
        help='Ironic keystone admin name'),
    cfg.StrOpt(
        'admin_password',
        secret=True,
        help='Ironic keystone admin password.'),
    cfg.StrOpt(
        'admin_auth_token',
        secret=True,
        deprecated_for_removal=True,
        help='Ironic keystone auth token.'
             'DEPRECATED: use admin_username, admin_password, and '
             'admin_tenant_name instead'),
    cfg.StrOpt(
        'admin_url',
        help='Keystone public API endpoint.'),
    cfg.StrOpt(
        'cafile',
        help='PEM encoded Certificate Authority to use when verifying HTTPs '
             'connections.'),
    cfg.StrOpt(
        'admin_tenant_name',
        help='Ironic keystone tenant name.'),
    cfg.IntOpt(
        'api_max_retries',
        default=60,
        help='How many retries when a request does conflict. '
              'If <= 0, only try once, no retries.'),
    cfg.IntOpt(
        'api_retry_interval',
        default=2,
        help='How often to retry in seconds when a request '
             'does conflict'),
]


def register_opts(conf):
    conf.register_group(ironic_group)
    conf.register_opts(ironic_options, group=ironic_group)


def list_opts():
    return {ironic_group: ironic_options}
