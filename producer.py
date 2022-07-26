# -*- coding: utf-8 -*-
"""Producer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jEYHXw1zYt7WY8gUuItujsmDeNWakIEY
"""

from kafka import KafkaProducer
from json import dumps
import csv
import time

producer = KafkaProducer(bootstrap_servers='172.31.87.125:9092', value_serializer=lambda K:dumps(K).encode('utf-8'))

with open('tweets.csv', 'r') as file:
  reader = csv.reader(file)
  for messages in reader:
    producer.send('data', messages)
    producer.flush()
    time.sleep(0.1)