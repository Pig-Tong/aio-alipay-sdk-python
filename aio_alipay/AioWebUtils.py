# _*_ coding:utf-8 _*_
# @Time : 2022/12/12 15:30 
# @Author : zhut96
# @File : AioWebUtils.py
# @Software: PyCharm
import aiohttp
from aiohttp import ClientTimeout
from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.CommonConstants import THREAD_LOCAL
from alipay.aop.api.exception.Exception import RequestException, ResponseException
from alipay.aop.api.util.WebUtils import get_http_connection, url_encode, MultiPartForm


async def do_post(url, query_string=None, headers=None, params=None, charset='utf-8', timeout=15):
    url, connection = get_http_connection(url, query_string, timeout)
    body = None
    if params:
        body = url_encode(params, charset)
    try:
        async with aiohttp.ClientSession(headers=headers, connector=connection, timeout=ClientTimeout(total=2 * 60)) as session:
            async with session.post(url, data=body) as res:
                response_status = res.status  # 获取返回的状态码
                response = await res.read()  # 获取返回内容
    except Exception as e:
        raise RequestException('[' + THREAD_LOCAL.uuid + ']post request failed. ' + str(e))
    if response_status != 200:
        raise ResponseException('[' + THREAD_LOCAL.uuid + ']invalid http status ' + str(response_status) + ',detail body:' + response.decode(encoding=charset))
    return response


async def do_multipart_post(url, query_string=None, headers=None, params=None, multipart_params=None, charset='utf-8', timeout=30):
    url, connection = get_http_connection(url, query_string, timeout)

    form = MultiPartForm(charset)
    for key, value in params.items():
        form.add_field(key, value)
    for key, value in multipart_params.items():
        file_item = value
        if file_item and isinstance(file_item, FileItem):
            form.add_file(field_name=key, file_name=file_item.get_file_name(),
                          file_content=file_item.get_file_content(), mimetype=file_item.get_mime_type())
    body = form.build_body()
    if not headers:
        headers = {}
    headers['Content-type'] = form.get_content_type()

    try:
        async with aiohttp.ClientSession(headers=headers, connector=connection, timeout=ClientTimeout(total=2 * 60)) as session:
            async with session.post(url, data=body) as res:
                response_status = res.status  # 获取返回的状态码
                response = await res.read()  # 获取返回内容
    except Exception as e:
        raise RequestException('[' + THREAD_LOCAL.uuid + ']post request failed. ' + str(e))
    if response_status != 200:
        raise ResponseException('[' + THREAD_LOCAL.uuid + ']invalid http status ' + str(response_status) + ',detail body:' + response.decode(encoding=charset))
    return response