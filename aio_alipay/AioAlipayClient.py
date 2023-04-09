# _*_ coding:utf-8 _*_
# @Time : 2022/12/12 11:23 
# @Author : zhut96
# @File : AioAlipayClient.py 
# @Software: PyCharm
import uuid

from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.constant.CommonConstants import THREAD_LOCAL, ALIPAY_SDK_PYTHON_VERSION

from aio_alipay.AioWebUtils import do_multipart_post, do_post


class AioAlipayClient(DefaultAlipayClient):
    """
    异步支付宝支付接入客户端
    """

    def __init__(self, alipay_client_config, logger=None):
        super().__init__(alipay_client_config, logger)
        self.__config = alipay_client_config
        self.__logger = logger

    async def execute(self, request):
        THREAD_LOCAL.uuid = str(uuid.uuid1())
        headers = {
            'Content-type': 'application/x-www-form-urlencoded;charset=' + self.__config.charset,
            "Cache-Control": "no-cache",
            "Connection": "Keep-Alive",
            "User-Agent": ALIPAY_SDK_PYTHON_VERSION,
            "log-uuid": THREAD_LOCAL.uuid,
        }

        query_string, params = self.__prepare_request(request)
        multipart_params = request.get_multipart_params()

        if multipart_params and len(multipart_params) > 0:
            response = await do_multipart_post(self.__config.server_url, query_string, headers, params, multipart_params,
                                               self.__config.charset, self.__config.timeout)
        else:
            response = await do_post(self.__config.server_url, query_string, headers, params, self.__config.charset,
                                     self.__config.timeout)

        return self.__parse_response(response)
