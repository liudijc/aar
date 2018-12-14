var canvas = document.getElementById("myCanvas"); 　　
var context = canvas.getContext("2d"); 
//////////////绘画方块

var Zyanse = null;
var Xyanse = null;

var jushu = null;
var x = 0;//横
var y = 0;//纵
var jishu = null;
var TXKG=true;

var GEZIDGgao=10;     //当个格子高
var GEZIqishiy=228;  //格子起始y
var GEZIqishix=4.5;  //格子起始x
var ZONGJUSHUz=0;  //总局数 Z
var ZONGJUSHUx=0;  //总局数 x

Zyanse="#FF0000";
Xyanse="#0000CD";
jushu = 20;
var xietubiao = function(a,b,c){
   y=c;
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
var tiaojie =function(a,b){
    jishu=jishu+1;
    
    if(jishu == 13){

        x=0;
        
    }
    if(jishu == 25){
        x=0;
        
    }
    if(jishu == 37){
        x=0;
        
    }
    if(jishu == 49){
        x=0;
        
    }
    if(jishu <= 12){
    
        xietubiao(a,b,60);

    }
    else{
        
        if(jishu <=24){

    
            xietubiao(a,b,200);
        }else
        {
            if(jishu <= 36){
    
                xietubiao(a,b,340);
        
            }
            else{
                if(jishu <= 48){
    
                    xietubiao(a,b,480);
            
                }





            }


        }
        



    }

    
    



   

    
  /*  
    
    
    
    else(jishu <=36)
    {

       xietubiao(a,b,340);
       if(jishu <=48){
        xietubiao(a,b,580);
    
    }



        }
*/

        
        

    
    
    

    

    
}

var QKshuzu = function(a){

    jushu = 20;
    x = 0;//横
    y = 0;//纵
    jishu = 0;



}

var huoqubuju= function(){

    GEZIDGgao=10;     //当个格子高
    GEZIqishiy=228;  //格子起始y
    GEZIqishix=4.5;  //格子起始x
    ZONGJUSHUz=0;  //总局数 Z
    ZONGJUSHUx=0;  //总局数 x
    context.clearRect(0,0,2000,1000); 
    
    huagezi();
    

}



////线条调节
var tiaojieXT =function(a,b){
    //alert(a+b+'您确定要删除吗？');
    xietubiaoXT(a,b);
    //xietubiao(a,b,200);
};


var xietubiaoXT = function(a,b){
    context.font = "10px sans-serif";  
    if(a==1){
        context.fillStyle = "#0000FF"; 

        

    }
    else{
        
        context.fillStyle = "#FF0000"; 


    }

    

    
    if(a%2==0){
        //context.fillStyle = "#FF0000"; 　

        let kk=b;
        ZONGJUSHUz=ZONGJUSHUz+kk;
        


        if(kk<10){
            
            context.fillText(kk,GEZIqishix+10,GEZIqishiy+25);


        }
        else if(kk>=10){
            context.fillText(kk,GEZIqishix+6,GEZIqishiy+25);
        }




        for (let i=0;i<kk;i++){
            //context.fillRect(GEZIqishix,GEZIqishiy,25,5); 
            context.fillRect(GEZIqishix,GEZIqishiy-(GEZIDGgao*i),25,5); 
        }


        GEZIqishix=GEZIqishix+30;
        


    }
    else
    {
        //context.fillStyle = "#0000FF"; 
        let kk=b;
        ZONGJUSHUx=ZONGJUSHUx+ kk;
        if(kk<10){
            
            context.fillText(kk,GEZIqishix+10,GEZIqishiy+25);


        }
        else if(kk>=10){
            context.fillText(kk,GEZIqishix+6,GEZIqishiy+25);
        }



        for (let i=0;i<kk;i++){
            //context.fillRect(GEZIqishix,GEZIqishiy,25,5); 
            context.fillRect(GEZIqishix,GEZIqishiy-(GEZIDGgao*i),25,5); 
        }
        GEZIqishix=GEZIqishix+30;

    
    /*
    context.fillStyle = "#000000";
    context.fillRect(0,0,500,500);//背景的绘制
    */

   
    




        
        


    }


    
    
 };





 var huagezi =function(){
    ///线条画图


    //////////////画框区域
   
   
    let KBX_KUANDU=2;//线条宽度
    context.strokeStyle="#C0C0C0";//线条颜色
    context.font = "10px sans-serif";  
    context.fillStyle = "#000000"; 
    context.lineWidth=2;

    let GEZIjiediangao=15;//高度节点   横
    for (let i=0;i<23;i++){
        
        let GEZIgao=GEZIjiediangao+(GEZIDGgao*i);//格子高度
        context.moveTo(2,GEZIgao);
        context.lineTo(700,GEZIgao);
        



    }
    let GEZIjiediankuan=22;//宽度节点  竖

    for (let i=0;i<35;i++){
        let GEZIkuan=GEZIjiediankuan+(30*i)-20;//格子宽度
        
        context.moveTo(GEZIkuan,15);
        context.lineTo(GEZIkuan,236);
        if(i<10){
            context.fillText(i,GEZIkuan+10,15-5);

        }
        else if(i>=10){
            context.fillText(i,GEZIkuan+8,15-5);
        }
        
        



    }

    context.stroke();
    //////画框区域


};



