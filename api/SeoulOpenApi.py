import os
import requests
from dotenv import load_dotenv

load_dotenv()


class SeoulOpenApi:
    KEY = os.environ['SEOUL_OPENAPI_KEY']

    def get_rainfall(self, gu_name: str):
        '''
        구이름을 입력받아 서울시 공공데이터 api를 이용해 강우량 현황 데이터를 받음
        :param gu_name: String
        :return: List
        '''
        url = f'http://openapi.seoul.go.kr:8088/{self.KEY}/json/ListRainfallService/1/20/{gu_name}'

        res = requests.get(url).json()
        return list(res['ListRainfallService']['row'])