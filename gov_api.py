import requests
import json


def get_geb_info(date:int)->dict:
    with open('config/key.json') as f:
        json_file = json.load(f)
    api_key = f"KEY={json_file['api-key']}"
    url = f"https://open.neis.go.kr/hub/mealServiceDietInfo?{api_key}&Type=json&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7531374&MLSV_YMD={date}"
    res = requests.get(url)
    json_res = res.json()
    data1 = json_res['mealServiceDietInfo']
    data2 = data1[1]
    data3 = data2['row']
    data4 = data3[0]
    data5 = data4['DDISH_NM'].split('<br/>')
    return_list = []
    for i in data5:
        try:
            start = i.index('(')
            end = i.rindex(')')
            cut_val = i[start:end+1]
            menu = (i.rstrip(cut_val))
            return_list.append(menu.strip())
        except ValueError:
            menu = (i)
            return_list.append(menu.strip())
    return return_list

def get_school_info(school_name:str)->dict:
    """
    https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17020190531110010104913&infSeq=2
    명세서 대로 값을 반환함
    """
    with open('config/key.json') as f:
        json_file = json.load(f)
    api_key = f"KEY={json_file['api-key']}"
    SCH_INFO_url = 'schoolInfo'
    url = f"https://open.neis.go.kr/hub/{SCH_INFO_url}?{api_key}&Type=json&SCHUL_NM={school_name}"
    res = requests.get(url)
    json_res = res.json()
    data1 = json_res['schoolInfo']
    data2 = data1[1]
    data3 = data2['row']
    data3 = data3[0]
    return data3