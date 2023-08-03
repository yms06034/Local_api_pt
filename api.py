from bs4 import BeautifulSoup as BS
from datetime import datetime

import urllib.request
import json
import pandas as pd
import requests, time, math
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os


def start(addr1, addr2, uptae1, uptae2, localCode, opnSvcId):
    now = datetime.now()

    lastBgn = now - relativedelta(months=1)
    month = lastBgn.strftime("%m")
    year = lastBgn.strftime("%Y")
    lastModTsBgn = f'{year}{month}24'

    lastEnd = now - relativedelta(days=2)
    lastModTsEnd = lastEnd.strftime("%Y%m%d")  

    # localCode = "6110000" # select
    # ###  localcode의 경우에는 https://github.com/yms06034/local_api_readme/blob/master/README.md 확인 가능 ###
    # opnSvcId = "07_24_04_P" #select

    AUTHKEY = "hJ7LoPXB7CoIC9Ir8WWJq0boAmbgmaWSPWA/rrg9Szg=" # required

    url = f"http://www.localdata.go.kr/platform/rest/TO0/openDataApi?authKey={AUTHKEY}" + \
            "&pageSize=10000" + "&resultType=json" + "&pageIndex=1" + f"&localcode={localCode}" + f"&lastModTsEnd={lastModTsEnd}" + f"&lastModTsBgn={lastModTsBgn}"

    url += f"&state=01"

    if opnSvcId:
        url += f"&opnSvcId={opnSvcId}" 
        
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    status_code = response.getcode()

    if (status_code == 200):
        response_body = response.read()
        response_json = json.loads(response_body)
    else:
        print("Error Code : " + status_code)

    result = response_json

    totalCount = result['result']['header']['paging']['totalCount']
    total_page_num = math.ceil(totalCount/10000)

    # result add (All Page)

    list_add = []

    for i in range(total_page_num):
        url = f"http://www.localdata.go.kr/platform/rest/TO0/openDataApi?authKey={AUTHKEY}" + \
            "&pageSize=10000" + "&resultType=json" + f"&pageIndex={i + 1}"
        
        if localCode != "":
            url += f"&localcode={localCode}"

        if all([lastModTsBgn, lastModTsEnd]):
            url += f"&lastModTsBgn={lastModTsBgn}"
            url += f"&lastModTsEnd={lastModTsEnd}"
            
        url += f"&state=01"

        if opnSvcId:
            url += f"&opnSvcId={opnSvcId}"
            
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)

        status_code = response.getcode()

        if (status_code == 200):
            response_body = response.read()
            response_json = json.loads(response_body)
        else:
            print("Error Code : " + status_code)

        result = response_json
        result_df = result['result']['body']['rows'][0]['row']
        list_add.append(result_df)

    data = []

    header = result['result']['header']['columns'][0]

    h_opnSvcNm = header['opnSvcNm']
    h_dtlStateNm = header['dtlStateNm']
    h_siteTel = header['siteTel']
    h_siteWhlAddr = header['siteWhlAddr']
    h_rdnWhlAddr = header['rdnWhlAddr']
    h_bplcNm = header['bplcNm']
    h_uptaeNm = header['uptaeNm']

#     print(opnSvcNm, dtlStateNm, siteTel, siteWhlAddr, rdnWhlAddr, bplcNm, uptaeNm, '추출날짜')

    final_list = [item for sublist in list_add for item in sublist]

    if len(final_list) > 0:     # 데이터 추출
        for item in final_list:
            opnSvcNm = item['opnSvcNm']
            dtlStateNm = item['dtlStateNm']
            siteTel = item['siteTel']
            siteWhlAddr = item['siteWhlAddr']
            rdnWhlAddr = item['rdnWhlAddr']
            bplcNm = item['bplcNm']
            uptaeNm = item['uptaeNm']
            
            today_str = now.strftime("%Y%m%d")  
            
            data.append([opnSvcNm, dtlStateNm, siteTel, siteWhlAddr, rdnWhlAddr, bplcNm, uptaeNm, today_str])
            
    folder = f'LocalDataFile/'

    if not os.path.exists(folder):
        os.makedirs(folder)
        
    # result

    df = pd.DataFrame(data)
    df.columns = [h_opnSvcNm, h_dtlStateNm, h_siteTel, h_siteWhlAddr, h_rdnWhlAddr, h_bplcNm, h_uptaeNm, '추출날짜']
    df.index += 1 
    
    df.to_csv(f'{folder}{today_str}_LocalData_{addr1}_{addr2}_{uptae1}_{uptae2}.csv', encoding='utf-8-sig', index=False)