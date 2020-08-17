# -*- encoding: utf-8 -*-
"""
@File    : baiduFaceIdentify.py
@Time    : 2020/8/17 9:43
@Author  : Morde
@Software: PyCharm
@Description: 调用百度识别接口
"""

import base64
import urllib
import json
import logging
import requests
from PIL import Image


class BaiduFaceIdentify:
    """
        此函数用于获取access_token，返回access_token的值
        此函数被parse_face_pic调用
    """
    def get_access_token(self):
        post_data = {
            "grant_type": "client_credentials",
            "client_id": "70pnkVuYCdhcu45bi1eBhR6x",                # 此变量赋值成自己API Key的值
            "client_secret": "MFa6pIGCKN76cOC8V20MjZtz0ZT0Gbqz"    # 此变量赋值成自己Secret Key的值
        }
        # auth_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
        auth_url = 'https://aip.baidubce.com/oauth/2.0/token'
        response_at = requests.post(auth_url,data=post_data)
        json_result = json.loads(response_at.text)
        access_token = json_result['access_token']
        return access_token

    @staticmethod
    def identify_faces(url_pic, url_fi):
        """
        此函数进行人脸识别，返回识别到的人脸列表
        此函数被parse_face_pic调用
        """
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        # 因为提交URL让baidu去读取图片，总是返回图片下载错了
        # 所以我们这里将读取URL指向的图片，将图片转成BASE64编码，改用提交BASE64编码而不是提交URL
        # pic_obj = urllib.request.urlopen(url_pic)
        pic_obj = requests.get(url_pic)
        pic_base64 = base64.b64encode(pic_obj.content)
        # pic_base64 = url_pic
        post_data = {
            # 'image': url_pic,
            # 'image_type' : 'URL',
            'image': pic_base64,
            'image_type': 'BASE64',
            'face_field': 'facetype,gender,age,beauty', #expression,faceshape,landmark,race,quality,glasses
            'max_face_num': 1
        }

        response_fi = requests.post(url_fi,headers=headers,data=post_data)
        json_fi_result = json.loads(response_fi.text)
        # 有些图片是没有人脸的，或者识别有问题，这个我们不细管直接捕获异常就返回空列表
        try:
            # if json_fi_result['result'] is None:
            #     return []
            # else:
                return json_fi_result['result']['face_list']
        except:
            return []
        # 下边的print也许是最直观，你最想要的
        # print(json_fi_result['result']['face_list'][0]['age'])
        # print(json_fi_result['result']['face_list'][0]['beauty'])

    def parse_face_pic(self, url_pic):
        """
        此函数用于解析进行人脸图片，返回图片中人物颜值
        此函数调用get_access_token、identify_faces
        """
        # 调用get_access_token获取access_token
        access_token = self.get_access_token()
        url_fi = 'https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=' + access_token
        # 调用identify_faces，获取人脸列表
        json_faces = self.identify_faces(url_pic, url_fi)
        # 如果没有人脸，那么就以0.0为颜值评分返回
        if len(json_faces) == 0:
            logging.warning('未识别到人脸')
            return 0.0
        else:
            for json_face in json_faces:
                logging.debug('种类：'+json_face['face_type']['type'])
                logging.debug('性别：'+json_face['gender']['type'])
                logging.debug('年龄：'+str(json_face['age']))
                logging.debug('颜值：'+str(json_face['beauty']))
                # 如果识别到的不是妹子，也以1.0为颜值评分返回
                # 如果识别到的是妹子，直接以值颜值返回
                if json_face['gender']['type'] != 'female':
                    logging.info('图片不是妹子')
                    return 1.0
                else:
                    return json_face['beauty']

    def face_comparing(self,pic1,pic2):
        """
        人脸对比
        """
        access_token = self.get_access_token()
        headers = {'content-type': 'application/json'}
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match?access_token=" + access_token
        post_data = [{"image": pic1, "image_type": "BASE64", "face_type": "LIVE", "quality_control": None},
                     {"image": pic2, "image_type": "BASE64", "face_type": "LIVE", "quality_control": None}]
        post_data1 = json.dumps(post_data)
        response = requests.post(request_url, data=post_data1, headers=headers)
        if response:
            print(response.json())


if __name__ == '__main__':
    #uil_pic赋值成自己要测试的图片的url地址
    url_pic = 'https://bkimg.cdn.bcebos.com/pic/5243fbf2b21193133b7906f76b380cd791238dbb?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2UxMTY=,g_7,xp_5,yp_5'
    bfi = BaiduFaceIdentify()
    # print(bfi.parse_face_pic(url_pic))
    with open('../imgs/pic4.jpg','rb') as f:
        pic4 = base64.b64encode(f.read()).decode()
        print(pic4)
    with open('../imgs/pic5.jpg','rb') as f:
        pic5 = base64.b64encode(f.read()).decode()
    bfi.face_comparing(pic4,pic5)


    # decodepic4 = base64.b64decode(pic4) bytes转为图片保存
    # file = open('test.jpg', 'wb')
    # with open('../imgs/test.jpg', 'wb') as f:
    #     f.write(decodepic4)