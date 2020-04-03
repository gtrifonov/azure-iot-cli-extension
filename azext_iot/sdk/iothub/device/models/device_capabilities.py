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


class DeviceCapabilities(Model):
    """Status of Capabilities enabled on the device.

    :param iot_edge:
    :type iot_edge: bool
    """

    _attribute_map = {
        'iot_edge': {'key': 'iotEdge', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(DeviceCapabilities, self).__init__(**kwargs)
        self.iot_edge = kwargs.get('iot_edge', None)