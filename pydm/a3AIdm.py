import a1dmbl
import time

dm=a1dmbl.dm
hwnd=a1dmbl.hwnd
print(dm.ver())

def MLshizi(x1,y1,x2,y2,color_format,sim):
    
    jg=dm.Ocr(x1,y1,x2,y2,color_format,sim)
    print(jg)
    return jg
def MLzhaotu(x1, y1, x2, y2, pic_name, delta_color,sim, dir1):
    #jg=dm.FindPic(x1, y1, x2, y2, pic_name, delta_color,sim, dir1,intX, intY)


    jg=dm.FindPicE(x1, y1, x2, y2, pic_name, delta_color,sim, dir1)
    
    
    return jg
def MLzhaotuQP(pic_name):
    
    jg=dm.FindPicE(0,0,2000,2000,pic_name,"000000",0.8,0)
    
    if jg == "-1|-1|-1":
        return 0 
    else:
        return jg 
def MLzhaotuDJ(x1, y1, x2, y2, pic_name, delta_color,sim, dir1):
    '''
    intX=0
    intY=1
    '''

    
    a = MLzhaotu(x1, y1, x2, y2, pic_name, delta_color,sim, dir1)
    #print(a)
    
   
    t=a.split('|')
    print(t[1],t[2])
    dm.MoveTo(t[1],t[2])
    dm.LeftClick()
def MLzhaotuDJQP(pic_name):
    a = MLzhaotu(0,0,2000,2000,pic_name,"000000",1,0)
    #print(a)
    
   
    t=a.split('|')
    print(t[1],t[2])
    dm.MoveTo(t[1],t[2])
    dm.LeftClick()
def MLyidongDJ(x,y):
    dm.MoveTo(x,y)
    dm.LeftClick()
def YXMLyaqian(a,b):
    YZXkongzhi=a
    jine=b 
    
    while jine>0:
        if jine>=1000:
            
            MLzhaotuDJQP("bmp/1000.bmp")
            jine=jine-1000
        elif jine>=500:
            MLzhaotuDJQP("bmp/500.bmp")
            jine=jine-500
        elif jine>=100:
            MLzhaotuDJQP("bmp/100.bmp")
            jine=jine-100
        elif jine>=50:
            MLzhaotuDJQP("bmp/50.bmp")
            jine=jine-50
        elif jine>=10:
            MLzhaotuDJQP("bmp/10.bmp")
            jine=jine-10
        time.sleep(1)


        if YZXkongzhi=="YX":
            MLzhaotuDJQP("bmp/x.bmp")
        elif YZXkongzhi=="YZ":
            MLzhaotuDJQP("bmp/z.bmp")
        


    
    MLzhaotuDJQP("bmp/qd.bmp")
def YXMLshiziZXT(a,b):

	
	

	weizhi1=MLshizi(2,717,38,910, "df1316-202020|3735f3-202020|20a10d-202020,"+'\n',0.8)
	weizhi2=MLshizi(33,720,73,909, "df1316-202020|3735f3-202020|20a10d-202020,"+'\n',0.8)
	weizhi3=MLshizi(63,719,99,906, "df1316-202020|3735f3-202020|20a10d-202020,"+'\n',0.8)
	weizhi4=MLshizi(91,717,128,911, "df1316-202020|3735f3-202020|20a10d-202020,"+'\n',0.8)
	weizhi5=MLshizi(120,716,159,912, "df1316-202020|3735f3-202020|20a10d-202020,"+'\n',0.8)
	weizhi6=MLshizi(147,718,188,911, "df1316-202020|3735f3-202020|20a10d-202020,"+'\n',0.8)
	print(weizhi1)
	print(weizhi2)
	print(weizhi3)
	print(weizhi4)
	print(weizhi5)
	print(weizhi6)
def jiekou(a):

    if a == "BDck":
	    #test()
        print(BDSzk)
    elif a == 'BDSzk':
        print(dm.SetDict(0,"res\dm_soft.txt"))
    elif a == "123":
		#test()
        print(dm.SetDict(0,"res\dm_soft.txt"))
    elif a == "SZ": 
        #shizi()
        print("2")
    elif a == "bz1":
        buzou1()
    elif a == "bz2":
        buzou2()
    elif a == "bz3":
        buzou3()
    elif a == "bz4":
        buzou4()
    elif a == "bz5":
        buzou5()
    elif a == "bzall":
        buzou1()
        time.sleep(2)
        buzou2()
        time.sleep(2)
        buzou3()
        time.sleep(2)
        buzou4()
        time.sleep(2)
        buzou5()
    elif a == "kaiqijc":
        kaiqijc()
    elif a == "GJT":
        MLzhaotuDJQP("bmp/GJT.bmp")
    elif a == "OZT":
        MLzhaotuDJQP("bmp/OZT.bmp")
    elif a == "QJT":
        MLzhaotuDJQP("bmp/QJT.bmp")
    elif a.find("YZ") != -1:


        t = a.split('YZ')

        YXMLyaqian("YZ", t[1])

        print(a)
    elif a.find("YX") != -1:
        t = a.split('YX')
        YXMLyaqian("YX", t[1])
        print(a)

#步骤区域
def buzou1():
    MLzhaotuDJQP("bmp/vialiulanqi.bmp")
def buzou2():
    MLzhaotuDJQP("bmp/DC.bmp")
def buzou3():
    MLzhaotuDJQP("bmp/denglu.bmp")
def buzou4():
    MLyidongDJ(161,425)
    time.sleep(1) 
    dm.SendString(hwnd,"liudijkk") 
    time.sleep(2) 
    #密码
    MLyidongDJ(125,488)
    time.sleep(1) 
    dm.SendString(hwnd,"hcy365") 
def buzou5():

    from aip import AipOcr
    #pip install baidu-aip  C:\Python34\Scripts处执行
    """ 你的 APPID AK SK """
    APP_ID = '11162073'
    API_KEY = 'lhs6TtdPPDZNzjFRNRzL1LCG'
    SECRET_KEY = 'GlytSOQz4sCIinzlr2IUn5RTHsCj6nX4'
    dm.Capture(332,539,409,576,"bmp/screen.bmp")
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    """ 调用通用文字识别, 图片为远程url图片 """#res=client.basicGeneralUrl(url);
    """ 调用通用文字识别, 图片为本地图片 """
    '''
    filePath = "bmp/screen.bmp"
    res = client.general('bmp/screen.bmp')
    print(res.words_result[1].words)
    MLyidongDJ(157,554)
    time.sleep(1) 
    dm.SendString(hwnd,res.words_result[1].words)
    time.sleep(1) 
    MLzhaotuDJQP("bmp/bz5-denglu.bmp")
    '''
    # 读取图片
    filePath = "bmp/screen.bmp"
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


    # 定义参数变量
    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
    }

    #调用通用文字识别接口
    result = client.basicAccurate(get_file_content(filePath), options)
    print(result['words_result'][0]['words'])
    MLyidongDJ(157,554)
    time.sleep(1) 
    dm.SendString(hwnd,result['words_result'][0]['words'])
    MLzhaotuDJQP("bmp/bz5-denglu.bmp")
    '''
    a={'words_result': [{'words': '1987'}], 'direction': 0, 'log_id': 2586040403978915370, 'words_result_num': 1}
    '''
def kaiqijc():
    i=0
    kaiqijc__i=1
    while (kaiqijc__i == 1) :
        if MLzhaotuQP("bmp/vialiulanqi.bmp")!= 0:
        	print("步骤一  浏览器")
        	buzou1()
        elif MLzhaotuQP("bmp/DC.bmp")!= 0:
            print("步骤二  打开标签")
            buzou2()
        elif MLzhaotuQP("bmp/jg.bmp")!= 0:
            print("确认警告")
            MLzhaotuDJQP("bmp/bz3queding.bmp")
        elif MLzhaotuQP("bmp/denglu.bmp")!= 0:
            print("步骤三 点击登录")
            buzou3()
        elif MLzhaotuQP("bmp/bz4.bmp")!= 0:
            print("步骤四 进入登录")
            buzou4()
        elif MLzhaotuQP("bmp/bz5.bmp")!= 0:
            print("步骤五 填写验证码")
            buzou5()
        elif MLzhaotuQP("bmp/yzmcw.bmp")!= 0 or MLzhaotuQP("bmp/yzmcw_1.bmp")!= 0:
            print("验证码错误")
            MLyidongDJ(271,312)
        elif MLzhaotuQP("bmp/ydl.bmp") != 0 and MLzhaotuQP("bmp/AG.bmp") == 0:
            print("已经登陆")
            MLyidongDJ(521,310)
        elif MLzhaotuQP("bmp/AG.bmp")!= 0:
            print("进入AG厅")
            MLyidongDJ(521,310)
            time.sleep(5) 
            MLzhaotuDJQP("bmp/AG.bmp")
        elif MLzhaotuQP("bmp/cg5fz.bmp")!= 0:
            print("超过5分钟")
            MLyidongDJ(237,535)
            #MLzhaotuDJQP("bmp/cg5fz-qd.bmp")
        elif MLzhaotuQP("bmp/ozt.bmp")!= 0 and MLzhaotuQP("bmp/gjt.bmp")!= 0:
            print("已经进入大厅")
            kaiqijc__i=0
        time.sleep(2) 
        i=i+1
        print("正在判断循环")
        if i==6:
            name = input('继续请按1 停止请按NO\n')
            if name == 'NO':
                kaiqijc__i=0
            else:
                i=0

#已经进入大厅  实行控制区域
def jinruQJT():
    MLzhaotuDJQP("bmp/qjt.bmp")
def jinruOZT():
    MLzhaotuDJQP("bmp/ozt.bmp")
def jinruGJT():
    MLzhaotuDJQP("bmp/gjt.bmp")

def YXN_sbzt():#识别ZUO台

    A=MLshizi(56,96,233,148,"d6af8e-606060",0.9)
    print(A)
def YXN_sbzjs():#识别总J数

    Z=MLshizi(17,647,59,682,"fffefe-808080",0.8)
    X=MLshizi(72,645,108,682,"fffefe-808080",0.8)
    H=MLshizi(125,644,160,684,"fffefe-808080",0.8)
    #ZS=Z+X+H
    print(Z,X,H)

