//////前段按钮声明
let btn = document.getElementById('msgbtn');
let msginput = document.getElementById('msginput');
let showbox = document.getElementById('showbox');
btn.addEventListener('click', (event) => {
    let msg = msginput.value;
    //let data = {msg: msg};
    let data = {msg: "ss"};
    socket.emit('sendMessage', data);
});

/////前段按钮声明函数结束
socket.on('receiveMessage', (data) => {
    console.log('收到');
    let message = document.createElement('div');
    message.innerHTML = `${data.id}: ${data.msg}`;
    showbox.appendChild(message);
});
let sendImg = () => {
    let Imginput = document.getElementById('tupian');
    let file = Imginput.files[0];       //得到该图片
    let reader = new FileReader();      //创建一个FileReader对象，进行下一步的操作
    reader.readAsDataURL(file);              //通过readAsDataURL读取图片

    reader.onload =function () {            //读取完毕会自动触发，读取结果保存在result中
        let data = {img: this.result};
        socket.emit('sendImg', data);
    }
};

socket.on('receiveImg', (data) => {
    let ImgDIV = document.createElement('div');
    ImgDIV.innerHTML = `<div>${data.id}: <img src="${data.img}" /></div>`;
    showbox.appendChild(ImgDIV);
});
/*
socket.on('KHDbuju', (data) => {
    tiaojie(3,Xyanse);

});
*/
socket.on('KHDbuju',function(data){
    alert(data)
});



/*socket.on('buju',function(msg){
    tiaojie(msg,Xyanse);
});
*/
