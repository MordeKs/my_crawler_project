# -*- encoding: utf-8 -*-
"""
@File    : with_yield.py
@Time    : 2020/8/12 15:32
@Author  : Morde
@Software: PyCharm
@Description: 使用yield提升kafka性能
"""

import time
from pykafka import KafkaClient

client = KafkaClient(hosts='127.0.0.1:9092')
topic = client.topics[b'test']


def consumer():
    with topic.get_producer(delivery_reports=True) as producer:
        print('init finished')
        next_data = ''
        while True:
            if next_data:
                producer.produce(str(next_data).encode())
            next_data = yield True


def feed():
    c = consumer()
    next(c)
    for i in range(1000):
        c.send(i)


start = time.time()
feed()
end = time.time()
print(f'共耗时{end-start}秒')