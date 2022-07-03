import os
import datetime
import requests
from dotenv import load_dotenv

load_dotenv()


class SeoulOpenApi:
    KEY = os.environ['SEOUL_OPENAPI_KEY']

    @staticmethod
    def get_rainfall(gu_name: str):
        '''
        구이름을 입력받아 서울시 공공데이터 api를 이용해 강우량 현황 데이터를 받음
        :param gu_name: String
        :return: List
        '''
        url = f'http://openapi.seoul.go.kr:8088/{SeoulOpenApi.KEY}/json/ListRainfallService/1/20/{gu_name}'

        res = requests.get(url).json()
        return list(res['ListRainfallService']['row'])

    @staticmethod
    def get_drain_pip(gubn: str):
        '''
        구분코드를 입력받아 서울시 공공데이터 api를 이용해 하수관로 수위 현황 데이터를 받음
        :param gubn: String
        :return: List
        '''
        now_datetime = datetime.datetime.now()
        before_datetime = (now_datetime - datetime.timedelta(minutes=20)).strftime('%Y%m%d%H')

        url = f'http://openapi.seoul.go.kr:8088/{SeoulOpenApi.KEY}/json/DrainpipeMonitoringInfo/1/1000/{gubn.zfill(2)}/{before_datetime}/{now_datetime.strftime("%Y%m%d%H")}'

        res = requests.get(url).json()
        return list(res['DrainpipeMonitoringInfo']['row'][::-1])
