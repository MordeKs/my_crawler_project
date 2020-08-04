# -*- encoding: utf-8 -*-
"""
@File    : bangyun.py
@Time    : 2020/7/28 16:37
@Author  : Morde
@Software: PyCharm
@Description:
"""
import pymongo
ent_list = ['56B4AA21F5F211E39186ED1292A4829C',
'97C87947A83311E8A6B1643E8CBE5BBC',
'5720031EF5F211E39186ED1292A4829C',
'57158F20F5F211E39186ED1292A4829C',
'55A71F2CF5F211E39186ED1292A4829C',
'53A9C9B0F5F211E39186ED1292A4829C',
'55842704F5F211E39186ED1292A4829C',
'56220CA9F5F211E39186ED1292A4829C',
'58DFEE3CF5F211E39186ED1292A4829C',
'5585C737F5F211E39186ED1292A4829C',
'58AEA6AEF5F211E39186ED1292A4829C',
'558AC331F5F211E39186ED1292A4829C',
'58BFC5C4F5F211E39186ED1292A4829C',
'ADDBB928ADFD11E58FE94A158A77B72E',
'55975DDAF5F211E39186ED1292A4829C',
'D30F6890E9AE11E9BB74643E8CBE5BBC',
'58A416D0F5F211E39186ED1292A4829C',
'56D936F1F5F211E39186ED1292A4829C',
'52BBAE13F5F211E39186ED1292A4829C',
'56ACB0E9F5F211E39186ED1292A4829C',
'56D2D25DF5F211E39186ED1292A4829C',
'5583D46EF5F211E39186ED1292A4829C',
'545EE23BF5F211E39186ED1292A4829C',
'5588D64CF5F211E39186ED1292A4829C',
'B4586EB7A83311E8A6B1643E8CBE5BBC',
'545F83E4F5F211E39186ED1292A4829C',
'ADDF5F49ADFD11E58FE94A158A77B72E',
'58AB202BF5F211E39186ED1292A4829C',
'580D306FF5F211E39186ED1292A4829C',
'58B9A0DBF5F211E39186ED1292A4829C',
'5450EED3F5F211E39186ED1292A4829C',
'56589FE2F5F211E39186ED1292A4829C',
'55D32453F5F211E39186ED1292A4829C',
'58BA93F0F5F211E39186ED1292A4829C',
'570BE3CDF5F211E39186ED1292A4829C',
'54BBD31DF5F211E39186ED1292A4829C',
'5581115CF5F211E39186ED1292A4829C',
'55876787F5F211E39186ED1292A4829C',
'5730BC26F5F211E39186ED1292A4829C',
'58C1D892F5F211E39186ED1292A4829C',
'1A95C92B3F4311E8894A000C290957E9',
'2C7C18AE3F4311E8894A000C290957E9',
'5583C4B7F5F211E39186ED1292A4829C',
'58BA37EDF5F211E39186ED1292A4829C',
'58D19272F5F211E39186ED1292A4829C',
'548A9F07F5F211E39186ED1292A4829C',
'56118EEFF5F211E39186ED1292A4829C',
'284CAEFE3F4311E8894A000C290957E9',
'549949DDF5F211E39186ED1292A4829C',
'55895D01F5F211E39186ED1292A4829C',
'544795E7F5F211E39186ED1292A4829C',
'58A707FAF5F211E39186ED1292A4829C',
'58D09682F5F211E39186ED1292A4829C',
'3E08BB2F3F4311E8894A000C290957E9',
'5887AB10F5F211E39186ED1292A4829C',
'58BA8699F5F211E39186ED1292A4829C',
'580A1D8CF5F211E39186ED1292A4829C',
'56B4BEEBF5F211E39186ED1292A4829C',
'54593219F5F211E39186ED1292A4829C',
'58BD44C1F5F211E39186ED1292A4829C',
'58E0B6DBF5F211E39186ED1292A4829C',
'558471FDF5F211E39186ED1292A4829C',
'56AFDC3DF5F211E39186ED1292A4829C',
'58A8A551F5F211E39186ED1292A4829C',
'58DA7B52F5F211E39186ED1292A4829C',
'5820D6E9F5F211E39186ED1292A4829C',
'55ECE663F5F211E39186ED1292A4829C',
'56D31A70F5F211E39186ED1292A4829C',
'9C1B4D34A83311E8A6B1643E8CBE5BBC',
'4F5668AF3F4311E8894A000C290957E9',
'544DA7F0F5F211E39186ED1292A4829C',
'58CDE9EBF5F211E39186ED1292A4829C',
'55D616BEF5F211E39186ED1292A4829C',
'1A9ACFB63F4311E8894A000C290957E9',
'5583B91FF5F211E39186ED1292A4829C',
'571B23E4F5F211E39186ED1292A4829C',
'57C3D6BBF5F211E39186ED1292A4829C',
'559A1196F5F211E39186ED1292A4829C',
'58A9FB02F5F211E39186ED1292A4829C',
'58B4870EF5F211E39186ED1292A4829C',
'56FEE291F5F211E39186ED1292A4829C',
'5461C480F5F211E39186ED1292A4829C',
'5588420AF5F211E39186ED1292A4829C',
'5456643EF5F211E39186ED1292A4829C',
'583CEFFEF5F211E39186ED1292A4829C',
'58E3DF36F5F211E39186ED1292A4829C',
'580DB939F5F211E39186ED1292A4829C',
'5457B67AF5F211E39186ED1292A4829C',
'5587E1B4F5F211E39186ED1292A4829C',
'58E3AFAFF5F211E39186ED1292A4829C',
'55990DECF5F211E39186ED1292A4829C',
'58D850AAF5F211E39186ED1292A4829C',
'558BD2DCF5F211E39186ED1292A4829C',
'58A4A6DDF5F211E39186ED1292A4829C',
'58B43C84F5F211E39186ED1292A4829C',
'543FDB63F5F211E39186ED1292A4829C',
'5582E461F5F211E39186ED1292A4829C',
'572A548BF5F211E39186ED1292A4829C',
'562209C4F5F211E39186ED1292A4829C',
'58C59FA2F5F211E39186ED1292A4829C']
table = ['psds-ycyj-fljf','psds-ycyj-fljf-cpws','psds-ycyj-fljf-fygg','psds-ycyj-fljf-ktgg',
         'psds-ycyj-fljf-sfxz','psds-ycyj-fljf-sx','psds-ycyj-fljf-sxbzxr','psds-ycyj-jyyc-blacklist',
         'psds-ycyj-jyyc-dzswyzsxhmd','psds-ycyj-jyyc-ffjz','psds-ycyj-jyyc-hbcf','psds-ycyj-jyyc-jyzxxx',
         'psds-ycyj-jyyc-qs','psds-ycyj-jyyc-sfpm','psds-ycyj-jyyc-sswf','psds-ycyj-jyyc-tcdy',
         'psds-ycyj-jyyc-tddy','psds-ycyj-jyyc-xzcf','psds-ycyj-jyyc-xzcf(xyzg)','psds-ycyj-jyyc-ycjy',
         'psds-ycyj-jyyc-yzwfxx','psds-ycyj-jyyc-zdgzmd','psds-ycyj-jyyc-zdsswf']
sourceClient = pymongo.MongoClient('mongodb://pszx:ps#123456@10.2.1.64:27019/?authSource=credit_negative')
tagartClient = pymongo.MongoClient('mongodb://credit_test:credit_test@10.2.1.64:27019/?authSource=credit_test')
# sourceTable = sourceClient['credit_negative']['psds-ycyj-jyyc-zdsswf']
tagartTable = tagartClient['credit_test']['negativeInfo_top100']

for t in table:
    sourceTable = sourceClient['credit_negative'][t]
    result = sourceTable.find({'entUid': {'$in': ent_list}})
    try:
        tagartTable.insert_many(result)
        print(t, '完成...')
    except:
        print(t, '无数据...')
sourceClient.close()
tagartClient.close()
# print(result)
"InvalidOperation"

