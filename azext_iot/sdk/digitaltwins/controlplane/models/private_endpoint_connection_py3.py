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


class PrivateEndpointConnection(Model):
    """The private endpoint connection of a Digital Twin.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param properties: Required.
    :type properties: ~controlplane.models.PrivateEndpointConnectionProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^(?![0-9]+$)(?!-)[a-zA-Z0-9-]{2,49}[a-zA-Z0-9]$'},
        'type': {'readonly': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'PrivateEndpointConnectionProperties'},
    }

    def __init__(self, *, properties, **kwargs) -> None:
        super(PrivateEndpointConnection, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = properties
