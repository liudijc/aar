//var mess = document.getElementById("mess");
/*
var ZXjilu=null;//ZX最后显示记录
var ZXjiluJS=null//ZX最后显示计数
*/
if(window.WebSocket){
    var ws = new WebSocket('ws://192.168.111.29:8001');

    ws.onopen = function(e){
        console.log("连接服务器成功");
        var h4= document.getElementsByTagName("h4")[0];
        h4.innerHTML = "初始化成功";
        //ws.send("game2");
    }
    ws.onclose = function(e){
        console.log("服务器关闭");
    }
    ws.onerror = function(){
        console.log("连接出错");
    }

    ws.onmessage = function(e){///链接完成提示 收到服务端信息
        var zifu = e.data
        var SFYZONGjine = zifu.indexOf("jineZONG");
        
        if(SFYZONGjine>=0){
            var fg=zifu.split(",")//////，号分割
            var h2= document.getElementsByTagName("h2")[0];
            h2.innerHTML = "--------------------------"+fg[1];



        }else if(zifu === "QKcanvas"){
            context.clearRect(0,0,canvas.width,canvas.height);  
            QKshuzu(0);


        }
        else if(zifu.charAt(0) == "Z"){
            var fg=zifu.split("Z")//////，号分割
            tiaojie(fg[1],Zyanse);

        }
        else if(zifu.charAt(0) == "X"){  
            var fg=zifu.split("X")//////，号分割
            tiaojie(fg[1],Xyanse);

        }
        
        /*//未改进代码
        if(zifu === "QKcanvas"){
            context.clearRect(0,0,canvas.width,canvas.height);  
            QKshuzu(0);
           
        }
        
        



        

        
        if(zifu.charAt(0) == "Z"){
            var fg=zifu.split("Z")//////，号分割
            tiaojie(fg[1],Zyanse);
            //tiaojie(zifu.length,Zyanse);
            




        }
        if(zifu.charAt(0) == "X"){
            var fg=zifu.split("X")//////，号分割
            tiaojie(fg[1],Xyanse);
            //tiaojie(zifu.length,Xyanse);


        }
        *///未改进代码
        /*mess.innerHTML = "连接成功"
        
        document.querySelector(".kuang").onclick = function(e){
            var time = new Date();
            //ws.send(time + "  game2点击了“" + e.target.innerHTML+"”");
        }
        */
    }

}


var FSquerenjine2 = function(a){
    ws.send(a);

}


