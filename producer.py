import requests
from time import sleep

class Producer:
   def __init__(self, id, addr):
    self.id = id
    self.addr = addr

    def get_addr(self, topic_name):
        lead = requests.get(self.addr + '/' +  topic_name)
        return lead

    
    def ping(self, topic_name, msg):
        leader_addr = self.get_addr(topic_name)
        flag = '408'
        while(flag == '408'):
            result = requests.post(leader_addr.text, data = {topic_name, msg}, timeout = 2.4).text
            flag = result.status_code

        


        