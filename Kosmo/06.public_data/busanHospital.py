'''
공공 데이터 중에서 부산 광역시의 병원 정보를 읽어 들여 본다
다운로드 형태 : json
'''
import json     # 제이슨 형태의 자료를 처리해주는 라이브러리
import math
import urllib.request

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as err:
        print(err)
        return None
# end def getRequestUrl(url)

def getHospitalData(pageNo, numOfRows):
    end_point = 'http://apis.data.go.kr/6260000/MedicInstitService/MedicalInstitInfo'
    access_key = 'aIYaDwLOtfCs48OgGYcVcY%2Bpn1cv6xNhT6AUOz6tMEa4N%2Fmv0yUf%2BdgRcxsfhndiNzC6oJIOsIA%2Fl8Kdf9i63g%3D%3D'\

    parameters = ''
    parameters += '?resultType=json'    # 제이슨 타입으로 반환 
    parameters += '&serviceKey=' + access_key   # 인증키
    parameters += '&pageNo=' + str(pageNo)      # 페이지 번호
    parameters += '&numOfRows=' + str(numOfRows)    # 한 페이지 결과 수
    url = end_point+parameters

    result = getRequestUrl(url)
    if result == None :
        return None
    else :
        # 문자열 형식의 데이터를 사전 형태로 반환해 준다.
        return json.loads(result)
# end def getHospitalData()

pageNo = 1 # 페이지 번호
numOfRows = 100 # 한 페이지 결과 수
nPage = 0 # 현재 페이지
jsonResult = []     # 전체 결과를 저장할 리스트

while True :
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))
    jsonData = getHospitalData(pageNo, numOfRows)
    #print(jsonData)

    if jsonData['MedicalInstitInfo']['header']['code'] == '00':
        totalCount = jsonData['MedicalInstitInfo']['totalCount']
        print('데이터 총 개수 : ', totalCount)

        for item in jsonData['MedicalInstitInfo']['item']:
            jsonResult.append(item)

        if totalCount == 0:
            break

        nPage = math.ceil(totalCount/numOfRows)
        if(pageNo == nPage):
            break   # 마지막 페이지에 도달

        pageNo += 1
    else:
        break

# 최종 결과를 json 형식의 파일로 저장하도록 한다.
savedFilename = '부산시 의료 기관, 약국 운영시간 정보.json'

# with 구문은 파일 입출력시 close() 함수를 암시적으로 사용하기 위한 구문이다.
# 'w' 는 쓰기 모드, outfile은 해당 파일의 별칭
with open(savedFilename, 'w', encoding='utf-8') as outfile:
    # dumps() 함수는 데이터를 읽어서 문자열 형태로 변환해 준다.
    retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(retJson) # 파일에 기록한다.

print(savedFilename + '이 저장 되었다.')
# emd while