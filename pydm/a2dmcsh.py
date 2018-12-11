import win32com.client
import a1dmbl


dm = win32com.client.Dispatch('dm.dmsoft')
dm.Reg("a5282134e291406b8070224a148e0596e0da1c6d","")


Fhwnd=dm.FindWindow("","雷电模拟器") 
if Fhwnd != 0:
    hwnd=dm.FindWindowEx(Fhwnd,"RenderWindow",'') 
    dm.SetDict(0,"dm_soft.txt")
    dm.SetPicPwd("a123456")
    ck1=dm.BindWindowEx(hwnd,"gdi","windows","windows","",0)
    a1dmbl.dm=dm
    a1dmbl.hwnd=hwnd
    print(ck1)
else:
    print('没开启雷电模拟器')


"""
hwnd=dm.FindWindowEx(Fhwnd,"RenderWindow") 

hell.kk(hwnd)

"""
