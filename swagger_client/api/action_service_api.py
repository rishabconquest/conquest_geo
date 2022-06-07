# coding: utf-8

"""
    Conquest API v4

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ActionServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def action_service_apply_standard_action(self, body, **kwargs):  # noqa: E501
        """action_service_apply_standard_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_apply_standard_action(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiApplyStandardActionCommand body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_service_apply_standard_action_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.action_service_apply_standard_action_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def action_service_apply_standard_action_with_http_info(self, body, **kwargs):  # noqa: E501
        """action_service_apply_standard_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_apply_standard_action_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiApplyStandardActionCommand body: (required)
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
                    " to method action_service_apply_standard_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `action_service_apply_standard_action`")  # noqa: E501

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
            '/api/actions/apply_standard_action', 'POST',
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

    def action_service_complete_action(self, body, **kwargs):  # noqa: E501
        """action_service_complete_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_complete_action(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiCompleteActionCommand body: (required)
        :return: ConquestApiCompleteActionResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_service_complete_action_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.action_service_complete_action_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def action_service_complete_action_with_http_info(self, body, **kwargs):  # noqa: E501
        """action_service_complete_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_complete_action_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiCompleteActionCommand body: (required)
        :return: ConquestApiCompleteActionResult
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
                    " to method action_service_complete_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `action_service_complete_action`")  # noqa: E501

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
            '/api/actions/complete_action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConquestApiCompleteActionResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def action_service_create_succeeding_action(self, body, **kwargs):  # noqa: E501
        """action_service_create_succeeding_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_create_succeeding_action(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiCreateSucceedingActionCommand body: (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_service_create_succeeding_action_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.action_service_create_succeeding_action_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def action_service_create_succeeding_action_with_http_info(self, body, **kwargs):  # noqa: E501
        """action_service_create_succeeding_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_create_succeeding_action_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiCreateSucceedingActionCommand body: (required)
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
                    " to method action_service_create_succeeding_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `action_service_create_succeeding_action`")  # noqa: E501

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
            '/api/actions/create_succeeding_action', 'POST',
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

    def action_service_delete_action(self, body, **kwargs):  # noqa: E501
        """action_service_delete_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_delete_action(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiDeleteActionCommand body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_service_delete_action_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.action_service_delete_action_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def action_service_delete_action_with_http_info(self, body, **kwargs):  # noqa: E501
        """action_service_delete_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_delete_action_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiDeleteActionCommand body: (required)
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
                    " to method action_service_delete_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `action_service_delete_action`")  # noqa: E501

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
            '/api/actions/delete_action', 'POST',
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

    def action_service_get_action(self, value, **kwargs):  # noqa: E501
        """action_service_get_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_get_action(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int value: The int32 value. (required)
        :return: ConquestApiActionEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_service_get_action_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.action_service_get_action_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def action_service_get_action_with_http_info(self, value, **kwargs):  # noqa: E501
        """action_service_get_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_get_action_with_http_info(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int value: The int32 value. (required)
        :return: ConquestApiActionEntity
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
                    " to method action_service_get_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `action_service_get_action`")  # noqa: E501

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

        # Authentication setting
        auth_settings = ['Api Key from App']  # noqa: E501

        return self.api_client.call_api(
            '/api/actions/{value}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConquestApiActionEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def action_service_get_action_completion_details(self, body, **kwargs):  # noqa: E501
        """action_service_get_action_completion_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_get_action_completion_details(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiGetActionCompletionDetailsRequest body: (required)
        :return: ConquestApiGetActionCompletionDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_service_get_action_completion_details_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.action_service_get_action_completion_details_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def action_service_get_action_completion_details_with_http_info(self, body, **kwargs):  # noqa: E501
        """action_service_get_action_completion_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_get_action_completion_details_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiGetActionCompletionDetailsRequest body: (required)
        :return: ConquestApiGetActionCompletionDetailsResponse
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
                    " to method action_service_get_action_completion_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `action_service_get_action_completion_details`")  # noqa: E501

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
            '/api/actions/completion_details', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConquestApiGetActionCompletionDetailsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def action_service_move_action(self, body, **kwargs):  # noqa: E501
        """action_service_move_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_move_action(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiMoveActionCommand body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_service_move_action_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.action_service_move_action_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def action_service_move_action_with_http_info(self, body, **kwargs):  # noqa: E501
        """action_service_move_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_move_action_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiMoveActionCommand body: (required)
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
                    " to method action_service_move_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `action_service_move_action`")  # noqa: E501

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
            '/api/actions/move_action', 'POST',
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

    def action_service_reverse_action_completion(self, body, **kwargs):  # noqa: E501
        """action_service_reverse_action_completion  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_reverse_action_completion(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiReverseActionCompletionCommand body: (required)
        :return: ConquestApiReverseActionCompletionResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_service_reverse_action_completion_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.action_service_reverse_action_completion_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def action_service_reverse_action_completion_with_http_info(self, body, **kwargs):  # noqa: E501
        """action_service_reverse_action_completion  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_reverse_action_completion_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiReverseActionCompletionCommand body: (required)
        :return: ConquestApiReverseActionCompletionResult
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
                    " to method action_service_reverse_action_completion" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `action_service_reverse_action_completion`")  # noqa: E501

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
            '/api/actions/reverse_action_completion', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConquestApiReverseActionCompletionResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def action_service_update_action(self, body, **kwargs):  # noqa: E501
        """action_service_update_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_update_action(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiActionRecordChangeSet body: (required)
        :return: ConquestApiChangeSetResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.action_service_update_action_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.action_service_update_action_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def action_service_update_action_with_http_info(self, body, **kwargs):  # noqa: E501
        """action_service_update_action  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.action_service_update_action_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConquestApiActionRecordChangeSet body: (required)
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
                    " to method action_service_update_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `action_service_update_action`")  # noqa: E501

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
            '/api/actions/update_action', 'POST',
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
