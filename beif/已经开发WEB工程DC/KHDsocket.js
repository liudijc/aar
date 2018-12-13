var socket = io.connect('http://liudi.e1.luyouxia.net:25705');
KKSDDS=null;
var FSxinxi = function(a,b){


    socket.emit(a,b);


}
var CEshi222 =function(a){
    


}



//接收来自服务端的信息事件c_hi
socket.on('KHD-buju',function(msg){
    //alert(msg)
     
    huoqubuju();
    




    
    //tiaojie(10,Xyanse)
})

//接受ZX
socket.on('KHD-ZX',function(msg){

    if(msg.charAt(0)==="Z"){
        msg=msg.split("Z");
        let data=msg[1]*1
        tiaojieXT(2,data);

    }else{

        msg=msg.split("X");
        let data=msg[1]*1
        tiaojieXT(1,data);
    


    }
    context.fillStyle = "#FFFFFF";
    context.fillRect(320,260,35,35);//背景的绘制
    context.fillRect(280,260,35,35);//背景的绘制

    context.font = "20pt Microsoft JhengHei";  
    context.fillStyle = "#0000FF"; 
    context.fillText(ZONGJUSHUx,320,280);
    context.fillStyle = "#FF0000"; 　
    context.fillText(ZONGJUSHUz,280,280);



    

 
})

///接受总金额
socket.on('KHD-ZONGjine',function(msg){
    //alert(msg)
     
    
    var h2= document.getElementsByTagName("h2")[0];
    h2.innerHTML = "-----------------------"+msg;
    




    
    //tiaojie(10,Xyanse)
})