dict_wuxing={'甲':'木','乙':'木','丙':'火','丁':'火','戊':'土','己':'土','庚':'金','辛':'金','壬':'水','癸':'水','子':'水','丑':'土','寅':'木','卯':'木','辰':'土','巳':'火','午':'火','未':'土','申':'金','酉':'金','戌':'土','亥':'水'}

print('请输入生辰八字（格式为“庚子己卯壬戌辛丑”，无需双引号和空格）')

bazi=str(input())

if bazi == '':
    bazi='庚子己卯壬戌辛丑'
else:
    bazi=bazi

wuxing=[]
for i in range(8):
    wuxing.append(dict_wuxing[bazi[i]])

j=wuxing.count('金')
m=wuxing.count('木')
s=wuxing.count('水')
h=wuxing.count('火')
t=wuxing.count('土')

#木生火,火生土,土生金,金生水,水生木
#金克木,木克土,土克水,水克火,火克金

print('金：'+str(j))
print('木：'+str(m))
print('水：'+str(s))
print('火：'+str(h))
print('土：'+str(t))