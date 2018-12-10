import dmdx
import time
dm=dmdx.dm

print(dm.ver())

def MLshizi(x1,y1,x2,y2,color_format,sim):
    
    jg=dm.Ocr(x1,y1,x2,y2,color_format,sim)
    print(jg)
    return jg
def MLzhaotu(x1, y1, x2, y2, pic_name, delta_color,sim, dir):
    #jg=dm.FindPic(x1, y1, x2, y2, pic_name, delta_color,sim, dir,intX, intY)


    jg=dm.FindPicE(x1, y1, x2, y2, pic_name, delta_color,sim, dir)
    
    
    return jg
def MLzhaotuQP(pic_name):
    
    jg=dm.FindPicE(0,0,2000,2000,pic_name,"000000",1,0)
    
    if jg == "-1|-1|-1":
        return 0; 
    elif num == 0:
        return jg; 
def MLzhaotuDJ(x1, y1, x2, y2, pic_name, delta_color,sim, dir):
    '''
    intX=0
    intY=1
    '''

    
    a=MLzhaotu(x1, y1, x2, y2, pic_name, delta_color,sim, dir)
    #print(a)
    
   
    t=a.split('|')
    print(t[1],t[2])
    dm.MoveTo(t[1],t[2])
    dm.LeftClick()
def MLzhaotuDJQP(pic_name):
    a=MLzhaotu(0,0,2000,2000,pic_name,"000000",1,0)
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
            
            MLzhaotuDJQP("1000.bmp")
            jine=jine-1000
        elif jine>=500:
            MLzhaotuDJQP("500.bmp")
            jine=jine-500
        elif jine>=100:
            MLzhaotuDJQP("100.bmp")
            jine=jine-100
        elif jine>=50:
            MLzhaotuDJQP("50.bmp")
            jine=jine-50
        elif jine>=10:
            MLzhaotuDJQP("10.bmp")
            jine=jine-10
        time.sleep(1)


        if YZXkongzhi=="YX":
            MLzhaotuDJQP("x.bmp")
        elif YZXkongzhi=="YZ":
            MLzhaotuDJQP("z.bmp")
        time.sleep(1)


    
    MLzhaotuDJQP("qd.bmp")
def YXMLshiziZX(a,b):

	
	

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




 
  
    
   

    
    
    
    
    
    
    
    
    
    
    
    
   

    
    








