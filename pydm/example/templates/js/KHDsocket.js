namespace = '/test';
var socket = io.connect('http://192.168.111.29:5000' + namespace);

socket.on('connect', function() {//链接成功时 触发
    socket.emit('my_event', {data: 'I\'m connected!'});
});


socket.on('my_response', function(msg) {
    $('#log').append('<br>' + $('<div/>').text('Received #' + msg.count + ': ' + msg.data).html());
});
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



    

 
});
socket.on('KHD-ZONGjine',function(msg){
    //alert(msg)
     
    
    var h2= document.getElementsByTagName("h2")[0];
    h2.innerHTML = "-----------------------"+msg;
    




    
    //tiaojie(10,Xyanse)
});
socket.on('KHD-buju',function(msg){
    //alert(msg)
     
    huoqubuju();
    




    
    //tiaojie(10,Xyanse)
});
var FSxinxi = function(a,b){


    socket.emit(a,b);


}

var JSbuju=function(id,ZJE,DJLZ){


    var danjuLZ=DJLZ.split(",");
    huoqubuju();
    
   


    for (var i=0;i<danjuLZ.length;i++)

    {
        console.log(danjuLZ[i]);
        io.to(id).emit('KHD-ZX',danjuLZ[i]);

    }

    

    io.to(id).emit('KHD-ZONGjine',ZJE);


}