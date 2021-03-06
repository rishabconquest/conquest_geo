# coding: utf-8

"""
    Conquest API v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


# from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ..api_client import ApiClient


class DefectServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def defect_service_calculate_defect_response_date(self, body, **kwargs):  # noqa: E501
        """defect_service_calculate_defect_response_date  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.defect_service_calculate_defect_response_date(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiCalculateDefectResponseDateRequest body: (required)
        :return: ConquestApiCalculateDefectResponseDateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.defect_service_calculate_defect_response_date_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.defect_service_calculate_defect_response_date_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def defect_service_calculate_defect_response_date_with_http_info(self, body, **kwargs):  # noqa: E501
        """defect_service_calculate_defect_response_date  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.defect_service_calculate_defect_response_date_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiCalculateDefectResponseDateRequest body: (required)
        :return: ConquestApiCalculateDefectResponseDateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method defect_service_calculate_defect_response_date" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `defect_service_calculate_defect_response_date`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Api Key from App']  # noqa: E501

        return self.api_client.call_api(
            '/api/defects/calculate_defect_response_date', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConquestApiCalculateDefectResponseDateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def defect_service_complete_defect(self, body, **kwargs):  # noqa: E501
        """defect_service_complete_defect  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.defect_service_complete_defect(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiCompleteDefectCommand body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.defect_service_complete_defect_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.defect_service_complete_defect_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def defect_service_complete_defect_with_http_info(self, body, **kwargs):  # noqa: E501
        """defect_service_complete_defect  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.defect_service_complete_defect_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiCompleteDefectCommand body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method defect_service_complete_defect" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `defect_service_complete_defect`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Api Key from App']  # noqa: E501

        return self.api_client.call_api(
            '/api/defects/complete_defect', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def defect_service_create_action_for_defect(self, body, **kwargs):  # noqa: E501
        """defect_service_create_action_for_defect  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.defect_service_create_action_for_defect(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiCreateActionForDefectCommand body: (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.defect_service_create_action_for_defect_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.defect_service_create_action_for_defect_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def defect_service_create_action_for_defect_with_http_info(self, body, **kwargs):  # noqa: E501
        """defect_service_create_action_for_defect  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.defect_service_create_action_for_defect_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiCreateActionForDefectCommand body: (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method defect_service_create_action_for_defect" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `defect_service_create_action_for_defect`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Api Key from App']  # noqa: E501

        return self.api_client.call_api(
            '/api/defects/create_action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def defect_service_delete_defect(self, body, **kwargs):  # noqa: E501
        """defect_service_delete_defect  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.defect_service_delete_defect(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiDeleteDefectCommand body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.defect_service_delete_defect_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.defect_service_delete_defect_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def defect_service_delete_defect_with_http_info(self, body, **kwargs):  # noqa: E501
        """defect_service_delete_defect  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.defect_service_delete_defect_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiDeleteDefectCommand body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method defect_service_delete_defect" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `defect_service_delete_defect`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Api Key from App']  # noqa: E501

        return self.api_client.call_api(
            '/api/defects/delete_defect', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def defect_service_get_defect(self, value, **kwargs):  # noqa: E501
        """defect_service_get_defect  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.defect_service_get_defect(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int value: The int32 value. (required)
        :return: ConquestApiDefectEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.defect_service_get_defect_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.defect_service_get_defect_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def defect_service_get_defect_with_http_info(self, value, **kwargs):  # noqa: E501
        """defect_service_get_defect  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.defect_service_get_defect_with_http_info(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int value: The int32 value. (required)
        :return: ConquestApiDefectEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method defect_service_get_defect" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if self.api_client.client_side_validation and ('value' not in params or
                                                       params['value'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `value` when calling `defect_service_get_defect`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'value' in params:
            path_params['value'] = params['value']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Api Key from App']  # noqa: E501

        return self.api_client.call_api(
            '/api/defects/{value}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConquestApiDefectEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def defect_service_update_defect(self, body, **kwargs):  # noqa: E501
        """defect_service_update_defect  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.defect_service_update_defect(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiDefectRecordChangeSet body: (required)
        :return: ConquestApiChangeSetResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.defect_service_update_defect_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.defect_service_update_defect_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def defect_service_update_defect_with_http_info(self, body, **kwargs):  # noqa: E501
        """defect_service_update_defect  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.defect_service_update_defect_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiDefectRecordChangeSet body: (required)
        :return: ConquestApiChangeSetResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method defect_service_update_defect" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `defect_service_update_defect`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Api Key from App']  # noqa: E501

        return self.api_client.call_api(
            '/api/defects/update_defect', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConquestApiChangeSetResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
