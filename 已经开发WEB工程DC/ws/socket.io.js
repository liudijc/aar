/**
 * Created by zhouxinyu on 2017/8/24.
 */
const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);
var fs=require('fs');
var aardio=null;
var wangye=null;


/////////////WS

/////////////

 
server.listen(3000, () => {
    console.log('server running at 127.0.0.1:3000');
});
 
app.use(express.static('./public'));
 
/*     socket.io 逻辑     */
 
io.on('connection', (socket) => {
    /*
    socket.on('sendMessage', (data) => {
        data.id = socket.id;
        io.emit('receiveMessage', data);
        //console.log('获取到了'+data);
    });
 
    socket.on('sendImg', (data) => {
        data.id = socket.id;
        io.emit('receiveImg', data);
    })
    */
   console.log(socket);


   socket.on('sendMessage', (data) => {
    data.id = socket.id;
    io.emit('receiveMessage', data);
});

socket.on('sendImg', (data) => {
    data.id = socket.id;
    io.emit('receiveImg', data);
});





/*
   socket.on('sendImg', (data) => {
    //客户端
    let file = Imginput.files[0];       //得到该图片
    let reader = new FileReader();      //创建一个FileReader对象，进行下一步的操作
    reader.readAsDataURL(file);              //通过readAsDataURL读取图片
 
    reader.onload =function () {            //读取完毕会自动触发，读取结果保存在result中
        let data = {img: this.result};
        io.emit('sendImg', data);
    }
    //客户端
    
    

})
*/



    socket.on('buju', function(data) {
        //readFile("danjuLZ.txt")
        
        wangye=socket.id;
        var QJLZlujing='danjuLZ.txt';
        var QJzongjine='ZONGjine.txt';
    
        var danjuLZ = fs.readFileSync(QJLZlujing, 'utf8');
        var ZONGjine = fs.readFileSync(QJzongjine, 'utf8');
        //console.log('获取到了buju:'+ DKwenjian('danjuLZ.txt'));
        JSbuju(wangye,ZONGjine,danjuLZ);
        console.log(wangye);
        


        

        

        //读文件

        



        
        //io.emit('KHDbuju','10');
        //io.to(socket.id).emit('KHDbuju',20);

    });

    socket.on('QRjine', function(data) {

        console.log(data+'确认金额');
        io.to(aardio).emit('KHD-aardio-QRjine','确认金额');


    });


    socket.on('yiyuyan', function(data) {

        console.log(data);
        console.log(socket.id);
        //io.to(socket.id).emit('KHD-yiyuyan',data);
        io.to(socket.id).emit('KHD-yiyuyan',data);


    });

    socket.on('wangye', function(data) {
        wangye=socket.id;
        console.log(wangye);



    });


    socket.on('JS-aardio', function(data) {
        aardio=socket.id;
        //io.to(aardio).emit('KHD-aardio',data);
        console.log(data);




    });
    socket.on('aardio-FSluzi', function(data) {

        //io.to(wangye).emit('KHD-aardio',data);
        JSbuju(wangye,20,data);
        console.log(data);
        io.to(aardio).emit('KHD-aardio','222');




    });




});

var JSbuju=function(id,ZJE,DJLZ){


    var danjuLZ=DJLZ.split(",");
    io.to(id).emit('KHD-buju',0);
    
   


    for (var i=0;i<danjuLZ.length;i++)

    {
        console.log(danjuLZ[i]);
        io.to(id).emit('KHD-ZX',danjuLZ[i]);

    }

    

    io.to(id).emit('KHD-ZONGjine',ZJE);


}
////////////
/////////////////


