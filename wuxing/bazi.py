dict_wuxing={'甲':'木','乙':'木','丙':'火','丁':'火','戊':'土','己':'土','庚':'金','辛':'金','壬':'水','癸':'水','子':'水','丑':'土','寅':'木','卯':'木','辰':'土','巳':'火','午':'火','未':'土','申':'金','酉':'金','戌':'土','亥':'水'}

print('请输入生辰八字（格式为“庚子己卯丁未己酉”，无需双引号和空格）')

bazi=str(input())

if bazi == '':
    bazi='庚子己卯丁未己酉'
else:
    bazi=bazi

wuxing=[]
for i in range(8):
    print({bazi[i]:dict_wuxing[bazi[i]]})
    wuxing.append(dict_wuxing[bazi[i]])



j=wuxing.count('金')
m=wuxing.count('木')
s=wuxing.count('水')
h=wuxing.count('火')
t=wuxing.count('土')
print('初始八字五行分布：')
print({'金':j,'木':m,'水':s,'火':h,'土':t})

#木生火,火生土,土生金,金生水,水生木
h_s=m
t_s=h
j_s=t
s_s=j
m_s=s
#金克木,木克土,土克水,水克火,火克金
m_k=j
t_k=m
s_k=t
h_k=s
j_k=h
#最终
j_z=j+j_s-j_k
m_z=m+m_s-m_k
s_z=s+s_s-s_k
h_z=h+h_s-h_k
t_z=t+t_s-t_k
print('结合相生相克之后五行分布：')
print({'金':j_z,'木':m_z,'水':s_z,'火':h_z,'土':t_z})

if j_z <= 0:
    j=j+1
    print('金+1')
if m_z <= 0:
    m=m+1
    print('木+1')
if s_z <= 0:
    s=s+1
    print('水+1')
if h_z <= 0:
    h=h+1
    print('火+1')
if t_z <= 0:
    t=t+1
    print('土+1')
print('调整之后五行分布：')
print({'金':j,'木':m,'水':s,'火':h,'土':t})

#木生火,火生土,土生金,金生水,水生木
h_s=m
t_s=h
j_s=t
s_s=j
m_s=s

#金克木,木克土,土克水,水克火,火克金
m_k=j
t_k=m
s_k=t
h_k=s
j_k=h
#最终
j_z=j+j_s-j_k
m_z=m+m_s-m_k
s_z=s+s_s-s_k
h_z=h+h_s-h_k
t_z=t+t_s-t_k

print('调整结合相生相克之后五行分布：')
print({'金':j_z,'木':m_z,'水':s_z,'火':h_z,'土':t_z})

