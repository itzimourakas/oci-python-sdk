# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeAnalyticsInstanceNetworkEndpointDetails(object):
    """
    Input payload to update an Analytics instance endpoint details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeAnalyticsInstanceNetworkEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_endpoint_details:
            The value to assign to the network_endpoint_details property of this ChangeAnalyticsInstanceNetworkEndpointDetails.
        :type network_endpoint_details: NetworkEndpointDetails

        """
        self.swagger_types = {
            'network_endpoint_details': 'NetworkEndpointDetails'
        }

        self.attribute_map = {
            'network_endpoint_details': 'networkEndpointDetails'
        }

        self._network_endpoint_details = None

    @property
    def network_endpoint_details(self):
        """
        **[Required]** Gets the network_endpoint_details of this ChangeAnalyticsInstanceNetworkEndpointDetails.

        :return: The network_endpoint_details of this ChangeAnalyticsInstanceNetworkEndpointDetails.
        :rtype: NetworkEndpointDetails
        """
        return self._network_endpoint_details

    @network_endpoint_details.setter
    def network_endpoint_details(self, network_endpoint_details):
        """
        Sets the network_endpoint_details of this ChangeAnalyticsInstanceNetworkEndpointDetails.

        :param network_endpoint_details: The network_endpoint_details of this ChangeAnalyticsInstanceNetworkEndpointDetails.
        :type: NetworkEndpointDetails
        """
        self._network_endpoint_details = network_endpoint_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other