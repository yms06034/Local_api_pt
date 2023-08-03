# -*- coding: utf-8 -*-

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import api as api
from datetime import datetime
import traceback

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

main_ui = Ui_MainWindow()
NAME = 'LocalData API'

# --------------------------------------------------------------------------------------------------------------------


class MainWindow(QMainWindow):
    def __init__(self):
        self.addr = [
                    ['전체','종로구','중구','용산구','성동구','광진구','동대문구','중랑구','성북구','강북구','도봉구','노원구','은평구','서대문구','마포구','양천구','강서구','구로구','금천구','영등포구','동작구','관악구','서초구','강남구','송파구','강동구']
                    
                    ,['전체','중구','서구','동구','영도구','부산진구','동래구','남구','북구','해운대구','사하구','금정구','강서구','연제구','수영구','사상구','기장군']
                    
                    ,['전체','중구','동구','서구','남구','북구','수성구','달서구','달성군','군위군']
                    
                    ,['전체','중구','동구','미추홀구','연수구','남동구','부평구','계양구','서구','강화군','옹진군']
                    
                    ,['전체','동구','서구','남구','북구','광산구']
                    
                    ,['전체','동구','중구','서구','유성구','대덕구']
                    
                    ,['전체','중구','남구','동구','북구','울주군']
                    
                    ,['전체']
                    
                    ,['전체','수원시','성남시','의정부시','안양시','부천시','광명시','평택시','동두천','안산시','고양시','과천시','구리시','남양주','오산시','시흥시','군포시','의왕시','하남시','용인시','파주시','이천시','안성시','김포시','연천군','가평군','양평군','화성시','광주시','양주시','포천시','여주시']
                    
                    ,['전체','춘천시','원주시','강릉시','동해시','태백시','속초시','삼척시','홍천군','횡성군','영월군','평창군','정선군','철원군','화천군','양구군','인제군','고성군','양양군']
                    
                    ,['전체','충주시','제천시','보은군','옥천군','영동군','진천군','괴산군','음성군','단양군','증평군','청주시']
                    
                    ,['전체','천안시','공주시','보령시','아산시','서산시','논산시','금산군','연기군','부여군','서천군','청양군','홍성군','예산군','태안군','계룡시','당진시']
                    
                    ,['전체','전주시','군산시','익산시','정읍시','남원시','김제시','완주군','진안군','무주군','장수군','임실군','순창군','고창군','부안군']
                    
                    ,['전체','목포시','여수시','순천시','나주시','광양시','담양군','곡성군','구례군','고흥군','보성군','화순군','장흥군','강진군','해남군','영암군','무안군','함평군','영광군','장성군','완도군','진도군','신안군']
                    
                    ,['전체','포항시','경주시','김천시','안동시','구미시','영주시','영천시','상주시','문경시','경산시','의성군','청송군','영양군','영덕군','청도군','고령군','성주군','칠곡군','예천군','봉화군','울진군','울릉군']
                    
                    ,['전체','진주시','통영시','사천시','김해시','밀양시','거제시','양산시','의령군','함안군','창녕군','고성군','남해군','하동군','산청군','함양군','거창군','합천군','창원시']
                    
                    ,['전체','제주시','서귀포시']
                    ]
        
        self.addrCode = [
                        ['6110000','3000000','3010000','3020000','3030000','3040000','3050000','3060000','3070000','3080000','3090000','3100000','3110000','3120000','3130000','3140000','3150000','3160000','3170000','3180000','3190000','3200000','3210000','3220000','3230000','3240000']
                        
                        ,['6260000','3250000','3260000','3270000','3280000','3290000','3300000','3310000','3320000','3330000','3340000','3350000','3360000','3370000','3380000','3390000','3400000']
                        
                        ,['6270000','3410000','3420000','3430000','3440000','3450000','3460000','3470000','3480000','5141000']
                        
                        ,['6280000','3490000','3500000','3510500','3520000','3530000','3540000','3550000','3560000','3570000','3580000']
                        
                        ,['6290000','3590000','3600000','3610000','3620000','3630000']
                        
                        ,['6300000','3640000','3650000','3660000','3670000','3680000']
                        
                        ,['6310000','3690000','3700000','3710000','3720000','3730000']
                        
                        ,['5690000']
                        
                        ,['6410000','3740000','3780000','3820000','3830000','3860000','3900000','3910000','3920000','3930000','3940000','3970000','3980000','3990000','4000000','4010000','4020000','4030000','4040000','4050000','4060000','4070000','4080000','4090000','4140000','4160000','4170000','5530000','5540000','5590000','5600000','5700000']
                        ,['6530000','4181000','4191000','4201000','4211000','4221000','4231000','4241000','4251000','4261000','4271000','4281000','4291000','4301000','4311000','4321000','4331000','4341000','4351000']
                        
                        ,['6430000','4390000','4400000','4420000','4430000','4440000','4450000','4460000','4470000','4480000','5570000','5710000']
                        
                        ,['6440000','4490000','4500000','4510000','4520000','4530000','4540000','4550000','4560000','4570000','4580000','4590000','4600000','4610000','4620000','5580000','5680000']
                        
                        ,['6450000','4640000','4670000','4680000','4690000','4700000','4710000','4720000','4730000','4740000','4750000','4760000','4770000','4780000','4790000']
                        
                        ,['6460000','4800000','4810000','4820000','4830000','4840000','4850000','4860000','4870000','4880000','4890000','4900000','4910000','4920000','4930000','4940000','4950000']
                        
                        ,['6470000','5020000','5050000','5060000','5070000','5080000','5090000','5100000','5110000','5120000','5130000','5150000','5160000','5170000','5180000','5190000','5200000']
                        
                        ,['6480000','5310000','5330000','5340000','5350000','5360000','5370000','5380000','5390000','5400000','5410000','5420000','5430000','5440000','5450000','5460000','5470000']
                        
                        ,['6500000','6510000','6520000']
                        ]
        
        self.uptae = [['병원','의원','부속의료기관','산후조리업','안전상비의약품 판매업소','약국','응급환자이송업','의료법인','의료유사업','안경업','의료기기수리업','의료기기판매(임대)업','치과기공소']
                    
                    ,['동물병원','동물약국','동물용의료용구판매업','동물용의약품도매상','동물장묘업','동물생산업','동물판매업','동물수입업','동물전시업','동물위탁관리업','동물미용업','동물운송업','가축사육업','가축인공수정소','도축업','부화업','사료제조업','종축업']
                    
                    ,['게임물배급업','게임물제작업','복합영상물제공업','복합유통게임제공업','인터넷컴퓨터게임시설제공업','일반게임제공업','청소년게임제공업','공연장','관광공연장업','관광극장유흥업','관광궤도업','관광사업자','관광유람선업','국제회의시설업','박물관, 미술관','시내순환관광업','유원시설업(기타)','일반유원시설업','전문휴양업','전통사찰','종합유원시설업','종합휴양업','지방문화원','국제회의기획업','대중문화예술기획업','문화예술법인','노래연습장업','비디오물감상실업','비디오물배급업','비디오물소극장업','비디오물시청제공업','비디오물제작업','관광숙박업','관광펜션업','숙박업','외국인관광도시민박업','자동차야영장업','한옥체험업','일반야영장업','농어촌민박업','국내여행업','국내외여행업','종합여행업','영화배급업','영화상영관','영화상영업','영화수입업','영화제작업','온라인음악서비스제공업','음반.음악영상물배급업','음반.음악영상물제작업','음반물배급업','음반물제작업']
                    
                    ,['미용업','이용업','세탁업','의료기관세탁물처리업','대규모점포','다단계판매업체','방문판매업','전화권유판매업','통신판매업','후원방문판매업체','골프연습장업','골프장','등록체육시설업','당구장업','무도장업','무도학원업','빙상장업','수영장업','스키장','종합체육시설업','승마장업','썰매장업','요트장업','체육도장업','체력단련장업','목욕장업']
                    
                    ,['위탁급식영업','집단급식소','집단급식소식품판매업','건강기능식품유통전문판매업','건강기능식품일반판매업','축산판매업','축산가공업','식육포장처리업','식품냉동냉장업','식품소분업','식품운반업','식품자동판매기업','식품제조가공업','식품첨가물제조업','식품판매업(기타)','옹기류제조업','용기·포장지제조업','용기냉동기특정설비','유통전문판매업','제과점영업','즉석판매제조가공업','집유업','식용얼음판매업','축산물보관업','축산물운반업','단란주점영업','유흥주점영업','관광식당','관광유흥음식점업','외국인전용유흥음식점업','일반음식점','휴게음식점']
                    
                    ,['목재수입유통업','원목생산업','제재업','계량기수리업','계량기수입업','계량기제조업','계량기증명업','고압가스업','석연탄제조업','석유및석유대체연료판매업체','석유판매업','액화석유가스용품제조업체','일반도시가스업체','전기사업업체','전력기술감리업체','전력기술설계업체','특정고압가스업','지하수시공업체','지하수영향조사기관','지하수정화업체','가축분뇨 수집운반업','가축분뇨배출시설관리업(사업장)','개인하수처리시설관리업(사업장)','건물위생관리업','건설폐기물처리업','급수공사대행업','단독정화조/오수처리시설설계시공업','대기오염물질배출시설설치사업장','배출가스전문정비사업자(확인검사대행자)','분뇨수집운반업','소독업','수질오염원설치시설(기타)','쓰레기종량제봉투판매업','저수조청소업','환경관리대행기관','환경전문공사업','환경측정대행업','환경컨설팅회사']
                    
                    ,['옥외광고업','인쇄사','출판사','담배도매업','담배소매업','담배수입판매업체','국제물류주선업','물류창고업체','민방위급수시설','민방위대피시설','상조업','승강기유지관리업체','승강기제조및수입업체','요양보호사교육기관','장례지도사 교육기관','무료직업소개소','유료직업소개소','행정사업']
                    ]
        
        self.uptaeCode = [['01_01_01_P','01_01_02_P','01_01_03_P','01_01_04_P','01_01_05_P','01_01_06_P','01_01_07_P','01_01_08_P',         '01_01_10_P','01_02_01_P','01_02_02_P','01_02_03_P','01_02_04_P']
                        
                        ,['02_03_01_P','02_03_02_P','02_03_03_P','02_03_04_P','02_03_05_P','02_03_06_P','02_03_07_P','02_03_08_P','02_03_09_P','02_03_10_P','02_03_11_P','02_03_12_P','02_04_01_P','02_04_02_P','02_04_03_P','02_04_04_P','02_04_05_P','02_04_06_P']
                        
                        ,['03_05_01_P','03_05_02_P','03_05_03_P','03_05_04_P','03_05_05_P','03_05_06_P','03_05_07_P','03_06_01_P','03_06_02_P','03_06_03_P','03_07_01_P','03_07_02_P','03_07_03_P','03_07_04_P','03_07_05_P','03_07_06_P','03_07_08_P','03_07_09_P','03_07_10_P','03_07_11_P','03_07_12_P','03_07_13_P','03_07_14_P','03_08_01_P','03_08_02_P','03_08_03_P','03_09_01_P','03_10_01_P','03_10_02_P','03_10_03_P','03_10_04_P','03_10_05_P','03_11_01_P','03_11_02_P','03_11_03_P','03_11_04_P','03_11_05_P','03_11_06_P','03_11_07_P','03_11_08_P','03_12_01_P','03_12_02_P','03_12_03_P','03_13_01_P','03_13_02_P','03_13_03_P','03_13_04_P','03_13_05_P','03_14_01_P','03_14_02_P','03_14_03_P','03_14_04_P','03_14_05_P']
                        
                        ,['05_18_01_P','05_19_01_P','06_20_01_P','06_20_02_P','08_25_01_P','08_26_01_P','08_26_02_P','08_26_03_P','08_26_04_P','08_26_05_P','10_31_01_P','10_31_02_P','10_31_03_P','10_32_01_P','10_33_01_P','10_33_02_P','10_34_01_P','10_35_01_P','10_36_01_P','10_37_01_P','10_38_01_P','10_39_01_P','10_40_01_P','10_41_01_P','10_42_01_P','11_44_01_P']
                        
                        ,['07_21_01_P','07_21_02_P','07_22_01_P','07_22_02_P','07_22_03_P','07_22_04_P','07_22_05_P','07_22_06_P','07_22_07_P','07_22_08_P','07_22_09_P','07_22_10_P','07_22_11_P','07_22_12_P','07_22_13_P','07_22_14_P','07_22_15_P','07_22_16_P','07_22_17_P','07_22_18_P','07_22_19_P','07_22_20_P','07_22_21_P','07_22_24_P','07_22_25_P','07_23_01_P','07_23_02_P','07_24_01_P','07_24_02_P','07_24_03_P','07_24_04_P','07_24_05_P']
                        
                        ,['09_27_01_P','09_27_02_P','09_27_03_P','09_28_01_P','09_28_02_P','09_28_03_P','09_28_04_P','09_28_05_P','09_28_06_P','09_28_07_P','09_28_08_P','09_28_09_P','09_28_10_P','09_28_11_P','09_28_12_P','09_28_13_P','09_28_14_P','09_29_01_P','09_29_02_P','09_29_03_P','09_30_01_P','09_30_02_P','09_30_03_P','09_30_04_P','09_30_05_P','09_30_06_P','09_30_07_P','09_30_08_P','09_30_09_P','09_30_10_P','09_30_11_P','09_30_12_P','09_30_13_P','09_30_14_P','09_30_15_P','09_30_16_P','09_30_17_P','09_30_18_P']
                        
                        ,['04_15_01_P','04_16_01_P','04_17_01_P','11_43_01_P','11_43_02_P','11_43_03_P','11_45_01_P','11_45_02_P','11_46_01_P','11_46_02_P','11_47_01_P','11_48_01_P','11_48_02_P','11_49_01_P','11_49_02_P','11_50_01_P','11_50_02_P','11_50_03_P']
                        ]


        super().__init__()
        main_ui.setupUi(self)     
        self.show()
        self.setWindowTitle(NAME)

        window_ico = resource_path('favicon.ico')
        self.setWindowIcon(QIcon(window_ico))

        main_ui.cb_addr2.addItems(self.addr[0])
        main_ui.cb_addr1.currentIndexChanged.connect(self.ch_cb_addr1)

        main_ui.cb_uptae2.addItems(self.uptae[0])
        main_ui.cb_uptae1.currentIndexChanged.connect(self.ch_cb_uptae1)

        main_ui.btn_start.clicked.connect(self.btn_startClicked)


    def ch_cb_addr1(self):
        main_ui.cb_addr2.clear()
        main_ui.cb_addr2.addItems(self.addr[main_ui.cb_addr1.currentIndex()])
        return
    
    def ch_cb_uptae1(self):
        main_ui.cb_uptae2.clear()
        main_ui.cb_uptae2.addItems(self.uptae[main_ui.cb_uptae1.currentIndex()])
        return
        
    def btn_startClicked(self):
        localCode = self.addrCode[main_ui.cb_addr1.currentIndex()][main_ui.cb_addr2.currentIndex()]
        opnSvcId = self.uptaeCode[main_ui.cb_uptae1.currentIndex()][main_ui.cb_uptae2.currentIndex()]

        api.start(main_ui.cb_addr1.currentText(), main_ui.cb_addr2.currentText(), main_ui.cb_uptae1.currentText(), main_ui.cb_uptae2.currentText(), localCode, opnSvcId)
        QMessageBox.information(self, NAME,'작동이 완료되었습니다!')



# --------------------------------------------------------------------------------------------------------------------


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

