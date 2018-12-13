var dier = function(a,b){
   
    y=200;
    var kuandu = 20;
    var textX = null;
 
 
     context.fillStyle = b;
     y=y+30;
 
 
     context.fillRect(x,y-(a*4),kuandu,a*4);  
 
 
     
     x=x+kuandu+10;
     textX=x-kuandu-10
          /////设置文字
 //设置字体样式
 context.font = "20px 宋体";
 //设置字体填充颜色
 //从坐标点(50,50)开始绘制文字
 if(a<10){
     textX=textX+5
 
 }
 context.fillText(a, textX, y+25);
 //////////设置文字结束

 

 

 }












var cshjs2 = function(a,b){
    　y=0;
    for (var i=0;i<a;i++)

    {
        context.fillStyle = b;
        y=y+30;


        context.fillRect(x,y,20,20);  

    }
    x=x+30;
    

}




/*
cshjs(16,Xyanse);
cshjs(1,Zyanse);
cshjs(2,Xyanse);
cshjs(6,Zyanse);
cshjs(16,Xyanse);
cshjs(1,Zyanse);
cshjs(2,Xyanse);
cshjs(6,Zyanse);
cshjs(16,Xyanse);
cshjs(1,Zyanse);
cshjs(2,Xyanse);
cshjs(6,Zyanse);
cshjs(16,Xyanse);
cshjs(1,Zyanse);
cshjs(2,Xyanse);
cshjs(6,Zyanse);
cshjs(16,Xyanse);
cshjs(1,Zyanse);
cshjs(2,Xyanse);
cshjs(6,Zyanse);*/
/*   for (var i=0;i<11;i++)

    {
        cshjs(i,Xyanse);
        
        


         

    
*/
//////////////绘画方块结束
