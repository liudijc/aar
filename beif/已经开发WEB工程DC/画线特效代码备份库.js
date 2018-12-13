//////////////////////直线

x1=5;
    y1=220;
    /////    context.beginPath();   

    //x1=x1+6;




    //context.fillStyle = b;
    a=20;
    y=200;

    x1=5;
    y1=220;
    context.lineWidth=5;
    JG=10;
    for (var i=0;i<70;i++)
    {






         
        if(i%2==0)
        {
            

            context.beginPath();   
            context.strokeStyle=b;
            
            context.moveTo(x1,y1);
            //a=a+10;
            //y=y-i-2;
            let kk=Math.ceil(Math.random()*12); 

            context.lineTo(x1,y1-(kk*10));
            context.stroke();
            x1=x1+JG;
            


            
        }
    else
        {

            context.beginPath();   
            context.strokeStyle="red";

            context.moveTo(x1,y1);
            let kk=Math.ceil(Math.random()*12); 

            context.lineTo(x1,y1-(kk*10));
            context.stroke();
            //context.fillText(i,x1,y1+10);
            x1=x1+JG;

            
            

            
        }



    }
    //////////////////////直线






    ////////////////画格子

    let KBX_KUANDU=2;//线条宽度
    context.strokeStyle="#C0C0C0";//线条颜色
    context.lineWidth=2;
    
    
    let GEZIjiediangao=15;//高度节点   横
    for (let i=0;i<23;i++){
        let GEZIgao=GEZIjiediangao+(10*i);//格子高度
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
    ////////////////画格子








    ///////////////画格子加画方条

    
    var GEZIDGgao=10;     //当个格子高
    var GEZIqishiy=228;  //格子起始y
    var GEZIqishix=4.5;  //格子起始x
    var ZONGJUSHUz=0;  //总局数 Z
    var ZONGJUSHUx=0;  //总局数 x

    

    for (let i=0;i<20;i++){


        if(i%2==0){
            context.fillStyle = "#FF0000"; 　

            let kk=Math.ceil(Math.random()*12); 
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
            context.fillStyle = "#0000FF"; 
            let kk=Math.ceil(Math.random()*12);
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




        }
    /////////////