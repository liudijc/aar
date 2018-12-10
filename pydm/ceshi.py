import win32com.client
import dmdx


dm = win32com.client.Dispatch('dm.dmsoft')
dm.Reg("a5282134e291406b8070224a148e0596e0da1c6d","")

Fhwnd=dm.FindWindow("","雷电模拟器") 
hwnd=dm.FindWindowEx(Fhwnd,"RenderWindow",'') 
dm.SetPicPwd("a123456")
ck1=dm.BindWindowEx(hwnd,"dx.graphic.opengl","windows","windows","",0)
dmdx.dm=dm
dmdx.hwnd=hwnd
print(ck1)

"""
hwnd=dm.FindWindowEx(Fhwnd,"RenderWindow") 

hell.kk(hwnd)

"""
