from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from api.SeoulOpenApi import SeoulOpenApi
import datetime

# Create your views here.
class RainfallDrainApi(APIView):
    def get(self, request):
        '''
        구분 코드를 입력받아 하수관로 수위 현황과 강우량 데이터를 결합하여 반환
        :param request: String
        :return: JSON
        '''
        gubn_code = request.GET['gubn']
        try:
            drain_pipe = SeoulOpenApi.get_drain_pip(gubn_code)
            gu_name = drain_pipe[0]['GUBN_NAM'] + '구'
            rainfall = SeoulOpenApi.get_rainfall(gu_name)

            latest_drain_pipe = [row for row in drain_pipe if drain_pipe[0]['MEA_YMD'] == row['MEA_YMD']]
            latest_rainfall = [row for row in rainfall if rainfall[0]['RECEIVE_TIME'] == row['RECEIVE_TIME']]

            res = {
                'REQUEST_TIME': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'GUBN': gubn_code,
                'GU_NAME': gu_name,
                'RAINFALL_DATA': {
                    'DATA_NUM': len(latest_drain_pipe),
                    'ROW': latest_drain_pipe
                },
                'DRAINPIPE_DATA': {
                    'DATA_NUM': len(latest_rainfall),
                    'ROW': latest_rainfall
                }
            }
            return JsonResponse(res)
        except Exception:
            return JsonResponse({'status_code': 400, 'msg': f'{gubn_code}는 없는 코드입니다.'}, status=400)