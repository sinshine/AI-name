print('请输入金木水火土')

wx=input()

j=int(wx[0])
m=int(wx[1])
s=int(wx[2])
h=int(wx[3])
t=int(wx[4])
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