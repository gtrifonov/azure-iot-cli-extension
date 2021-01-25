# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PrivateEndpointConnectionsResponse(Model):
    """The available private link connections for a Digital Twin.

    :param value: The list of available private link connections for a Digital
     Twin.
    :type value: list[~controlplane.models.PrivateEndpointConnection]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PrivateEndpointConnection]'},
    }

    def __init__(self, **kwargs):
        super(PrivateEndpointConnectionsResponse, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
