import json
from pyquery import PyQuery as pq
import requests
from lxml import etree
import json

html_str = """
Andorra
安道尔
AD
376
0.446


United Arab Emirates
阿拉伯联合酋长国
AE
971
0.284


Afghanistan
阿富汗
AF
93
0.501


Antigua and Barbuda
安提瓜和巴布达
AG
1268
0.535


Anguilla
安圭拉
AI
1264
0.311


Albania
阿尔巴尼亚
AL
355
0.650


Armenia
亚美尼亚
AM
374
0.557


Angola
安哥拉
AO
244
0.434


Argentina
阿根廷
AR
54
0.4247


American Samoa
美属萨摩亚
AS
1684
0.754


Austria
奥地利
AT
43
0.882


Australia
澳大利亚
AU
61
0.551


Aruba
阿鲁巴
AW
297
0.379


Azerbaijan
阿塞拜疆
AZ
994
1.001


Bosniaand Herzegovina
波斯尼亚和黑塞哥维那
BA
387
0.529


Barbados
巴巴多斯
BB
1246
0.357


Bangladesh
孟加拉国
BD
880
0.580


Belgium
比利时
BE
32
0.565


Burkina Faso
布基纳法索
BF
226
0.532


Bulgaria
保加利亚
BG
359
0.505


Bahrain
巴林
BH
973
0.157


Burundi
布隆迪
BI
257
0.262


Benin
贝宁
BJ
229
0.341


Bermuda
百慕大群岛
BM
1441
0.375


Brunei
文莱
BN
673
0.119


Bolivia
玻利维亚
BO
591
0.445


Caribisch Nederland
荷兰加勒比
BQ
599
0.303


Brazil
巴西
BR
55
0.114


Bahamas
巴哈马
BS
1242
0.267


Bhutan
不丹
BT
975
0.271


Botswana
博茨瓦纳
BW
267
0.292


Belarus
白俄罗斯
BY
375
0.5823


Belize
伯利兹
BZ
501
0.226


Canada
加拿大
CA
1
0.1028


Democratic Republic of theCongo
刚果民主共和国
CD
243
0.351


Central African Republic
中非共和国
CF
236
0.434


Republic Of The Congo
刚果共和国
CG
242
0.455


Switzerland
瑞士
CH
41
0.488


Ivory Coast
象牙海岸
CI
225
0.561


Cook Islands
库克群岛
CK
682
0.276


Chile
智利
CL
56
0.466


Cameroon
喀麦隆
CM
237
0.375


Colombia
哥伦比亚
CO
57
0.284


CostaRica
哥斯达黎加
CR
506
0.475


Cape Verde
开普
CV
238
0.595


Curacao
库拉索
CW
599
0.335


Cyprus
塞浦路斯
CY
357
0.229


Czech
捷克
CZ
420
0.549


Germany
德国
DE
49
0.685


Djibouti
吉布提
DJ
253
0.758


Denmark
丹麦
DK
45
0.364


Dominica
多米尼加
DM
1767
0.377


dominican republic
多米尼加共和国
DO
1809
0.356


Algeria
阿尔及利亚
DZ
213
1.134


Ecuador
厄瓜多尔
EC
593
0.732


Estonia
爱沙尼亚
EE
372
0.782


Egypt
埃及
EG
20
0.546


Eritrea
厄立特里亚
ER
291
0.627


Spain
西班牙
ES
34
0.677


Ethiopia
埃塞俄比亚
ET
251
0.591


Finland
芬兰
FI
358
0.952


Fiji
斐济
FJ
679
0.251


Micronesia
密克罗尼西亚
FM
691
1.021


Faroe Islands
法罗群岛
FO
298
0.108


France
法国
FR
33
0.533


Gabon
加蓬
GA
241
0.245


United Kingdom
英国
GB
44
0.318


Grenada
格林纳达
GD
1473
0.335


Georgia
格鲁吉亚
GE
995
0.798


French Guiana
法属圭亚那
GF
594
1.038


Ghana
加纳
GH
233
0.524


Gibraltar
直布罗陀
GI
350
0.138


Greenland
格陵兰岛
GL
299
0.088


Gambia
冈比亚
GM
220
0.311


Guinea
几内亚
GN
224
0.606


Guadeloupe
瓜德罗普岛
GP
590
1.899


Equatorial Guinea
赤道几内亚
GQ
240
0.591


Greece
希腊
GR
30
0.694


Guatemala
瓜地马拉
GT
502
0.380


Guam
关岛
GU
1671
0.386


Guinea-Bissau
几内亚比绍共和国
GW
245
0.670


Guyana
圭亚那
GY
592
0.497


Hong Kong
中国香港
HK
852
0.307


Honduras
洪都拉斯
HN
504
0.442


Croatia
克罗地亚
HR
385
0.549


Haiti
海地
HT
509
0.581


Hungary
匈牙利
HU
36
0.820


Indonesia
印度尼西亚
ID
62
0.8220


Ireland
爱尔兰
IE
353
0.564


Israel
以色列
IL
972
0.5343


India
印度
IN
91
0.2055


Iraq
伊拉克
IQ
964
0.551


Iceland
冰岛
IS
354
0.228


Italy
意大利
IT
39
0.564


Jamaica
牙买加
JM
1876
0.256


Jordan
约旦
JO
962
0.480


Japan
日本
JP
81
0.514


Kenya
肯尼亚
KE
254
0.290


Kyrgyzstan
吉尔吉斯斯坦
KG
996
0.873


Cambodia
柬埔寨
KH
855
0.557


Kiribati
基里巴斯
KI
686
0.349


Comoros
科摩罗
KM
269
0.314


Saint Kitts and Nevis
圣基茨和尼维斯
KN
1869
0.649


South Korea
韩国
KR
82
0.245


Kuwait
科威特
KW
965
0.468


Cayman Islands
开曼群岛
KY
1345
0.317


Kazakhstan
哈萨克斯坦
KZ
7
0.536


Laos
老挝
LA
856
0.312


Lebanon
黎巴嫩
LB
961
0.318


Saint Lucia
圣露西亚
LC
1758
0.284


Liechtenstein
列支敦士登
LI
423
0.203


Sri Lanka
斯里兰卡
LK
94
0.6097


Liberia
利比里亚
LR
231
0.486


Lesotho
莱索托
LS
266
0.403


Lithuania
立陶宛
LT
370
0.287


Luxembourg
卢森堡
LU
352
0.108


Latvia
拉脱维亚
LV
371
0.477


Libya
利比亚
LY
218
0.686


Morocco
摩洛哥
MA
212
0.570


Monaco
摩纳哥
MC
377
0.437


Moldova
摩尔多瓦
MD
373
0.653


Montenegro
黑山
ME
382
0.245


Madagascar
马达加斯加
MG
261
0.502


Marshall Islands
马绍尔群岛
MH
692
0.906


Macedonia
马其顿
MK
389
0.208


Mali
马里
ML
223
1.320


Myanmar
缅甸
MM
95
0.644


Mongolia
蒙古
MN
976
0.442


Macau
中国澳门
MO
853
0.183


Mauritania
毛里塔尼亚
MR
222
0.548


Montserrat
蒙特塞拉特岛
MS
1664
0.469


Malta
马耳他
MT
356
0.216


Mauritius
毛里求斯
MU
230
0.349


Maldives
马尔代夫
MV
960
0.233


Malawi
马拉维
MW
265
0.333


Mexico
墨西哥
MX
52
0.227


Malaysia
马来西亚
MY
60
0.248


Mozambique
莫桑比克
MZ
258
0.216


Namibia
纳米比亚
NA
264
0.294


New Caledonia
新喀里多尼亚
NC
687
1.614


Niger
尼日尔
NE
227
0.527


Nigeria
尼日利亚
NG
234
0.553


Nicaragua
尼加拉瓜
NI
505
0.497


Netherlands
荷兰
NL
31
1.071


Norway
挪威
NO
47
0.645


Nepal
尼泊尔
NP
977
0.705


Nauru
拿鲁岛
NR
674
0.577


New Zealand
新西兰
NZ
64
0.796


Oman
阿曼
OM
968
0.514


Panama
巴拿马
PA
507
0.495


Peru
秘鲁
PE
51
0.301


French Polynesia
法属波利尼西亚
PF
689
0.854


Papua New Guinea
巴布亚新几内亚
PG
675
0.474


Philippines
菲律宾
PH
63
0.243


Pakistan
巴基斯坦
PK
92
0.4932


Poland
波兰
PL
48
0.282


Saint Pierreand Miquelon
圣彼埃尔和密克隆岛
PM
508
0.397


Puerto Rico
波多黎各
PR
1787
0.386


Portugal
葡萄牙
PT
351
0.358


Palau
帕劳
PW
680
0.586


Paraguay
巴拉圭
PY
595
0.210


Qatar
卡塔尔
QA
974
0.360


Réunion Island
留尼汪
RE
262
1.444


Romania
罗马尼亚
RO
40
0.510


Serbia
塞尔维亚
RS
381
0.323


Russia
俄罗斯
RU
7
0.399


Rwanda
卢旺达
RW
250
0.251


Saudi Arabia
沙特阿拉伯
SA
966
0.245


Solomon Islands
所罗门群岛
SB
677
0.208


Seychelles
塞舌尔
SC
248
0.441


Sudan
苏丹
SD
249
0.461


Sweden
瑞典
SE
46
0.730


Singapore
新加坡
SG
65
0.260


Slovenia
斯洛文尼亚
SI
386
0.262


Slovakia
斯洛伐克
SK
421
0.684


Sierra Leone
塞拉利昂
SL
232
0.209


San Marino
圣马力诺
SM
378
0.402


Senegal
塞内加尔
SN
221
0.493


Somalia
索马里
SO
252
0.598


Suriname
苏里南
SR
597
0.339


Sao Tome and Principe
圣多美和普林西比
ST
239
0.787


ElSalvador
萨尔瓦多
SV
503
0.393


Swaziland
斯威士兰
SZ
268
0.512


Turksand Caicos Islands
特克斯和凯科斯群岛
TC
1649
0.282


Chad
乍得
TD
235
0.259


Togo
多哥
TG
228
0.238


Thailand
泰国
TH
66
0.132


Tajikistan
塔吉克斯坦
TJ
992
0.664


East Timor
东帝汶
TL
670
0.449


Turkmenistan
土库曼斯坦
TM
993
0.397


Tunisia
突尼斯
TN
216
0.860


Tonga
汤加
TO
676
0.254


Turkey
土耳其
TR
90
0.062


Trinidadand Tobago
特立尼达和多巴哥
TT
1868
0.263


Taiwan
中国台湾
TW
886
0.370


Tanzania
坦桑尼亚
TZ
255
0.561


Ukraine
乌克兰
UA
380
0.520


Uganda
乌干达
UG
256
0.532


United States
美国
US
1
0.043


Uruguay
乌拉圭
UY
598
0.749


Uzbekistan
乌兹别克斯坦
UZ
998
0.967


Saint Vincent and The Grenadines
圣文森特和格林纳丁斯
VC
1784
0.424


Venezuela
委内瑞拉
VE
58
0.247


VirginIslands,British
英属处女群岛
VG
1284
0.329


Vietnam
越南
VN
84
0.343


Vanuatu
瓦努阿图
VU
678
0.419


Samoa
萨摩亚
WS
685
0.530


Yemen
也门
YE
967
0.435


Mayotte
马约特
YT
269
1.088


South Africa
南非
ZA
27
0.219


Zambia
赞比亚
ZM
260
0.289


Zimbabwe
津巴布韦
ZW
263
0.173


Kosovo
科索沃共和国
XK
383
0.594


Virgin Islands, US
美属维尔京群岛
VI
1340
0.043


Sint Maarten (Dutch Part)
英属圣马丁
SX
1721
0.438


South Sudan
南苏丹
SS
211
0.548


Palestinian Territory
巴勒斯坦
PS
970
0.635


Martinique
马丁尼克
MQ
596
0.806


Northern Mariana Islands
北马利安纳群岛
MP
1670
0.343


Western Sahara
西撒哈拉
EH
212
0.428


Netherlands Antilles
荷属安的列斯
AN
599
0.404


Ascension Island
阿森松岛
AC
247
0.363
"""
item_list = html_str.split('\n\n')

items = [i.split('\n') for i in item_list]
item_one_list = []
for i in items:
	del i[0]
	i[3] = f"+{i[3]}"
	i[4] = float(i[4])
	item_one_list.append(i)
print(item_one_list)
item_twos = []
for i in item_one_list:
	item_two = {
		"code": i[2],
		"areacode": i[3],
		"price": i[4]
	}
	item_twos.append(item_two)
with open('tencent.json', 'a', encoding='utf-8') as fw:
	json.dump(item_twos, fw, ensure_ascii=False)