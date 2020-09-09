# -*- coding: utf-8 -*-
# @File  : download.py
# @Author: LVFANGFANG
# @Date  : 2020/7/17 9:48
# @Desc  :

import datetime
import hashlib

import pandas as pd
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from sqlalchemy_test import create_engine

from config.config import mysqlcfg, retry, proxy
# from log import logger

# proxies = {'http': proxy, 'https': proxy}


def login(username, password, retry=10):
    url = 'http://220.160.52.221:12120/fjpm/ajaxLogin.do'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '114',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': '220.160.52.221:12120',
        'Origin': 'http://220.160.52.221:12120',
        'Referer': 'http://220.160.52.221:12120/fjpm/main.do',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    m = hashlib.md5()
    m.update(password.encode())

    data = {
        'username': username,
        'password': m.hexdigest(),
        'captcha': ''
    }
    count = 0
    while count < retry:
        try:
            response = requests.post(url, headers=headers, data=data, proxies=proxies)
            cookies = response.cookies.get_dict()
            # print(cookies)
            print(f'{username}登录成功')
            return cookies
        except Exception as e:
            count += 1
            print('登录失败')


def download_file(username, password):
    today = datetime.date.today()

    task_list = [
        {
            'filename': f"项目报表{today.strftime('%Y-%m-%d')}.xls",
            'tablename': 'basicdata_project_report',
            'url': 'http://220.160.52.221:12120/fjpm/fzpm-register/item/doExprot.do',
            'payload': '------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="clsDigitalCityType"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemName"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemCodeCountry"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemIndustry"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemCountyCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemDivision"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="respDeptCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="subRespDeptCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemAmt"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="flowState"\r\n\r\n99\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemType"\r\n\r\nCLS_DIGITAL_ITEM_PRO\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="startState"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="endState"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="planStartDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="planStartDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="planEndDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="planEndDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="realStartDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="realStartDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="realEndDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="realEndDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="ideaDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="ideaDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="signDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="signDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="startDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="startDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="partProductDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="partProductDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="productDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="productDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="increaseDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="increaseDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="parentState"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemYear"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="industryCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="industryItemCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="industryThirdCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="gradeMngType"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemEcoContinue"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="owner"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="orgScope"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="respFlagScope"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="clsFiveBatchExamine"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="clsFiveBatchNewCity"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="trackDeptCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="trackDeptName"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="leadDeptCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="subLeadDeptCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="reportDeptCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="primaryInvestNature"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="enterDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="enterDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="clsCatchPromoteStartCheck"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="sszjjSearch"\r\n\r\n1\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemStateBack"\r\n\r\n0\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="clsAmtFocusQuery"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="flowEndDate"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="isItemAmt"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="isPorxy"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="viewItemType"\r\n\r\nclsDigitalItemPro\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="clsDigitalItemProExport"\r\n\r\n1\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="header"\r\n\r\n[{"name":"序号","value":"itemCode"},{"name":"项目名称","value":"itemName"},{"name":"项目所属地区","value":"itemDivision"},{"name":"项目所属县区","value":"itemCountyName"},{"name":"建设地点","value":"consLocation"},{"name":"建设年限起始","value":"itemStartYear"},{"name":"建设年限结束","value":"itemEndYear"},{"name":"项目类型","value":"itemCategory"},{"name":"项目状态","value":"clsDigitalItemProState"},{"name":"招商日期","value":"attractDate"},{"name":"在谈日期","value":"talkDate"},{"name":"签约日期","value":"pickDate"},{"name":"在建日期","value":"makeDate"},{"name":"建成日期","value":"buildDate"},{"name":"是否补助项目","value":"isSubsidy"},{"name":"项目分类","value":"itemTypeName"},{"name":"资金来源","value":"itemFundProName"},{"name":"总投资(万元)","value":"itemAmt"},{"name":"2019年计划投资","value":"yearPlanAmt2019"},{"name":"2020年计划投资","value":"yearPlanAmt2020"},{"name":"2020年工作目标","value":"yearPlanInfo2020"},{"name":"目前完成投资(万元)","value":"itemUsedAmt"},{"name":"计划开工日期","value":"planStartDate"},{"name":"计划完成日期","value":"planEndDate"},{"name":"责任单位","value":"respDeptName"},{"name":"责任人","value":"respDeptUser"},{"name":"责任人联系方式","value":"respDeptLink"},{"name":"二级责任部门","value":"subRespDeptName"},{"name":"二级部门联系人","value":"subRespDeptUser"},{"name":"二级部门联系方式","value":"subRespDeptLink"},{"name":"项目联系人单位","value":"trackDeptName"},{"name":"项目联系人","value":"trackDeptUser"},{"name":"项目联系人电话","value":"trackDeptLink"},{"name":"建设内容及规模","value":"consContent"},{"name":"备注","value":"memo"},{"name":"是否省重点","value":"clsProFocusExport"},{"name":"是否五个一批","value":"clsFiveBatchExport"},{"name":"设备投资(万元)","value":"fundFacility"},{"name":"其他投资(万元)","value":"fundRest"},{"name":"土建投资(万元)","value":"fundCivil"},{"name":"资金下达年份","value":"fundYear"},{"name":"资金下达批次","value":"fundNext"},{"name":"资金下达金额","value":"fundAmtPro"},{"name":"本年度已审核通过投资","value":"yearRealAmt"},{"name":"本次上报后投资完成率","value":"yearAmtRate"},{"name":"本年计划投资","value":"newYearPlanAmt"},{"name":"本月上报投资","value":"realAmt"},{"name":"项目累计投资","value":"itemRealAmt"},{"name":"本年到位资金","value":"yearRealArrive"},{"name":"本月到位资金","value":"itemRealArrive"},{"name":"实际形象进度","value":"itemEvovle"},{"name":"计划形象进度","value":"newYearPlanInfo"},{"name":"企业名称","value":"proprietorName"},{"name":"统一社会信用代码","value":"proprietorCode"},{"name":"联系人和联系方式","value":"proprietorUserTel"},{"name":"企业地址","value":"proprietorAddr"},{"name":"法人名称","value":"proprietorPerson"}]\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="isTick"\r\n\r\nfalse\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="year"\r\n\r\n%s\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="month"\r\n\r\n%02d\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS--\r\n' % (
                today.year, today.month)
        },
        {
            'filename': f"项目进度报表{today.strftime('%Y-%m-%d')}.xls",
            'tablename': 'basicdata_process_report',
            'url': 'http://220.160.52.221:12120/fjpm/fzpm-track/schedule/doExprot.do',
            'payload': '''------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemName"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="scheduleLevel"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemAmt"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="yearRealAmt"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="respDeptCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="respDeptName"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="subRespDeptCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="subRespDeptName"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="fromDate"\r\n\r\n%s01\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="toDate"\r\n\r\n%s12\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="problemFlag"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="flowState"\r\n\r\n99\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemType"\r\n\r\nCLS_DIGITAL_ITEM_PRO\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="startState"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="endState"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="endSearch"\r\n\r\n0\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemYear"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="industryCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="industryItemCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="industryThirdCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="gradeMngType"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemEcoContinue"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="parentItemCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="orgScope"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="respFlagScope"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="clsFiveBatchExamine"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="clsFiveBatchNewCity"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="trackDeptCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="trackDeptName"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="ideaDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="ideaDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="signDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="signDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="partProductDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="partProductDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="productDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="productDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="increaseDateBegin"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="increaseDateEnd"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="ini"\r\n\r\n1\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="subLeadDeptCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="leadDeptCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="reportDeptCode"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="primaryInvestNature"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="flowEndDate"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="itemDivision"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="isPorxy"\r\n\r\n\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="viewItemType"\r\n\r\nclsDigitalItemPro\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS\r\nContent-Disposition: form-data; name="header"\r\n\r\n[{"name":"项目名称","value":"itemName"},{"name":"序号","value":"itemCode"},{"name":"本月到位资金","value":"realArrive"},{"name":"总投资","value":"itemAmt"},{"name":"审核状态","value":"curState"},{"name":"申报年度","value":"scheduleYear"},{"name":"申报月份","value":"scheduleMonth"},{"name":"申报月段","value":"scheduleLevel"},{"name":"责任单位","value":"respDeptName"},{"name":"责任领导","value":"respDeptLeader"},{"name":"二级责任部门","value":"subRespDeptName"},{"name":"二级责任部门联系人","value":"subRespDeptUser"},{"name":"二级责任部门联系方式","value":"subRespDeptLink"},{"name":"全年计划投资金额","value":"planAmtAll"},{"name":"本年度已审核通过投资","value":"yearPassAmt"},{"name":"本次上报后投资完成率","value":"yearAmtRate"},{"name":"本月上报投资","value":"realAmt"},{"name":"本年上报投资","value":"yearRealAmt"},{"name":"项目累计投资","value":"itemRealAmt"},{"name":"本年到位资金","value":"yearRealArrive"},{"name":"项目到位资金","value":"itemRealArrive"},{"name":"实际形象进度","value":"itemEvovle"},{"name":"计划形象进度","value":"planInfoAll"},{"name":"是否有附件","value":"attFlag"},{"name":"是否纳统","value":"wholeState"},{"name":"纳统编码","value":"wholeCode"},{"name":"是否上报问题","value":"problemState"},{"name":"问题名称","value":"problemName"},{"name":"问题出现阶段","value":"problemLevel"},{"name":"问题类型","value":"problemType"},{"name":"涉及层面","value":"problemInvolve"},{"name":"问题描述","value":"problemDescribe"},{"name":"是否需要协调解决","value":"coordinateFlag"},{"name":"问题是否解决","value":"solveState"},{"name":"问题解决日期","value":"solveDate"},{"name":"问题解决结果","value":"solveResult"},{"name":"开工状态","value":"startState"},{"name":"竣工状态","value":"endState"},{"name":"实际开工时间","value":"realStartDate"},{"name":"实际竣工时间","value":"realEndDate"},{"name":"计划开工时间","value":"planStartDate"},{"name":"计划竣工时间","value":"planEndDate"},{"name":"全年计划形象进度","value":"planInfoAll"},{"name":"本年计划用地","value":"planLand"},{"name":"本年计划用林","value":"planForest"},{"name":"本年计划用海","value":"planSea"},{"name":"建设内容及规模","value":"consContent"},{"name":"是否跨区县","value":"itemCrossCounty"},{"name":"所属区县","value":"itemCountyName"},{"name":"所属区划","value":"itemDivision"},{"name":"归属街道","value":"itemStreetName"},{"name":"所属行业","value":"industryName"},{"name":"细分行业","value":"industryItemName"},{"name":"产业分类","value":"itemIndustry"},{"name":"三大产业","value":"industryType"},{"name":"全国统一编码","value":"itemCodeCountry"},{"name":"主投单位","value":"primaryInvest"},{"name":"业主单位","value":"owner"},{"name":"建设地点","value":"consLocation"},{"name":"一抓一促","value":"clsCatchPromote"},{"name":"一抓一促开工项目","value":"clsCatchPromoteStartState"},{"name":"一抓一促竣工项目","value":"clsCatchPromoteEndState"},{"name":"省重点项目","value":"clsProFocus"},{"name":"省重点项目类别","value":"clsProFocusState"},{"name":"省五个一批","value":"clsFiveBatch"},{"name":"五个一批类别","value":"clsFiveBatchState"},{"name":"市重点项目","value":"clsCityFocus"},{"name":"市建设阶段","value":"clsCityFocusState"},{"name":"重中之重","value":"clsFocusOnFocus"},{"name":"重中之重状态","value":"clsFocusOnFocusState"},{"name":"民间投资","value":"clsFolkIvst"},{"name":"赶超项目","value":"clsCatchItem"},{"name":"赶超项目状态","value":"clsCatchItemState"},{"name":"特色小镇","value":"clsFeatureTown"},{"name":"数字经济","value":"clsDigitalItem"},{"name":"数字经济类型","value":"clsDigitalItemType"},{"name":"数字经济建设类型","value":"clsDigitalItemBuildType"},{"name":"是否为总项目","value":"parentState"},{"name":"总项目序号","value":"parentItemCode"},{"name":"经度","value":"itemLng"},{"name":"纬度","value":"itemLat"},{"name":"投资主体性质","value":"primaryInvestNature"},{"name":"本次上报开工状态","value":"scStartState"},{"name":"管理类型","value":"gradeMngType"},{"name":"本次上报竣工状态","value":"scEndState"},{"name":"本次上报实际开工时间","value":"scRealStartDate"},{"name":"本次上报实际竣工时间","value":"scRealEndDate"},{"name":"本次上报部分竣工时间","value":"scPartProductDate"},{"name":"项目起始年度","value":"itemStartYear"},{"name":"项目结束年度","value":"itemEndYear"},{"name":"项目业主","value":"itemOwner"},{"name":"业主联系方式","value":"ownerLinkTel"},{"name":"业主联系人","value":"ownerLink"},{"name":"当月钢材采购量(吨)","value":"realRebar"},{"name":"当月省内钢材采购量(吨)","value":"realRebarInPro"},{"name":"当年钢材采购量(吨)","value":"yearRealRebar"},{"name":"年计划钢材采购量","value":"scNextYearPlanAmt"},{"name":"当月水泥采购量(吨)","value":"realCement"},{"name":"当月省内水泥采购量(吨)","value":"realCementInPro"},{"name":"当年水泥采购量(吨)","value":"yearRealCement"},{"name":"年计划水泥采购量(吨)","value":"scThirdYearPlanAmt"},{"name":"砂石当月需求量(方)","value":"realSandNeed"},{"name":"砂石当月实际采购量(方)","value":"realSand"}]\r\n------WebKitFormBoundaryCNXlvY8Sc7rM6LHS--\r\n''' % (
                today.year, today.year)
        }
    ]
    cookies = login(username, password)
    if not cookies:
        return
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '9769',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryCNXlvY8Sc7rM6LHS',
        'Host': '220.160.52.221:12120',
        'Origin': 'http://220.160.52.221:12120',
        'Referer': 'http://220.160.52.221:12120/fjpm/main.do',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    }

    for task in task_list:
        count = 0
        success = False
        while count < retry:
            try:
                response = requests.post(
                    task.get('url'),
                    headers=headers,
                    cookies=cookies,
                    data=task.get('payload').encode(),
                    proxies=proxies,
                    timeout=2 * 60
                )
                # print(response)
                # print(response.content)
                success = True
                break
            except Exception as e:
                count += 1

                logger.exception(e)
                continue

        if success:
            with open(task.get('filename'), 'wb') as f:
                f.write(response.content)
                logger.info(f"{task.get('filename')}下载成功")
            save2mysql(task.get('filename'), task.get('tablename'), created_by=username)
        else:
            logger.error(f"{task.get('filename')}下载失败")


def save2mysql(filename, table_name, created_by=None):
    try:
        columns = {
            'basicdata_project_report': [
                '2020年计划投资',
                # 'process',
                # 'row_id',
                '企业名称',
                # '创建人',
                '序号',
                '建设内容及规模',
                '建设地点',
                '建设年限结束',
                '建设年限起始',
                '总投资(万元)',
                '是否补助项目',
                '目前完成投资(万元)',
                '签约日期',
                '统一社会信用代码',
                '联系人和联系方式',
                '项目分类',
                '项目名称',
                '项目所属县区',
                '项目状态',
            ],
            'basicdata_process_report': [
                # 'process',
                # 'row_id',
                '全年计划形象进度',
                '全年计划投资金额',
                # '创建人',
                '审核状态',
                '序号',
                '总投资',
                '本年上报投资',
                '本月上报投资',
                '本次上报实际开工时间',
                '本次上报实际竣工时间',
                '本次上报开工状态',
                '本次上报竣工状态',
                '申报年度',
                '申报月份',
                '项目名称',
                '项目累计投资',
            ]
        }
        df = pd.read_excel(filename, usecols=columns[table_name])
        df['创建人'] = created_by
        # print(df)

        db_conn = f"""mysql+pymysql://{'psdsstaff'}:{'Psdsstaff#123'}@{'10.2.13.251'}:{3306}/{
        'ent_data_working'}?charset=utf8"""
        engine = create_engine(db_conn)

        if created_by is None:
            delete = """delete from {} where process=2 and `创建人` is NULL""".format(table_name)
        else:
            delete = """delete from {} where process=2 and `创建人`='{}'""".format(table_name, created_by)

        engine.execute(delete)

        df.to_sql(table_name, engine, if_exists='append', index=None)
        print(f'{filename}导入成功')
        engine.dispose()

    except Exception as e:
        print(f'{filename}导入失败')


if __name__ == '__main__':
    # scheduler = BlockingScheduler()
    # scheduler.add_job(download_file, 'cron', args=('泉州数字经济', '111111'), day_of_week='*', hour=5, minute=0, second=0,
    #                   misfire_grace_time=600)
    # scheduler.start()
    # download_file('泉州数字经济', '111111')
    save2mysql(r'..\file\项目进度报表2020-07-17 (1).xls', 'basicdata_project_report','泉州数字经济')
