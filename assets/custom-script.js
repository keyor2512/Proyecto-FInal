var checkbox;
var tipo=0
function recursive(){
    
    var bb=document.getElementsByClassName('checkFiltro');
    if(!bb.length){

        setTimeout(recursive,100);
    }
    else{
        checkbox=bb[0];
        console.log("dd");
       var a =document.querySelectorAll('input[type=checkbox]');
        for (let i = 0; i < a.length; i++) {
            a[i].onclick = function() { if(this.checked==false){
            var num=i+2;
            var lp=document.getElementsByClassName('column-'+num.toString());
            for(let o=0;i<lp.length;o++){
                    lp[o].classList.add("Hide");
            }
            }else{
                var num=i+2;
            var lp=document.getElementsByClassName('column-'+num.toString());
            for(let o=0;i<lp.length;o++){
                    lp[o].classList.remove("Hide");
            }
        } }
        }
    }
}
function recursive2(){
    
    var bb=document.getElementById('tipoGraphTitulo');
    if(bb==null){
        setTimeout(recursive2,100);
    }
    else{
        bb.disabled=true;
    }
}

function recursive3(){
    
    var bb=document.getElementById('botonReg');
    if(bb==null){
        setTimeout(recursive3,100);
    }
    else{
        var inpu=document.getElementById('search');
        bb.onclick = function(){if (tipo==0){
            tipo=1;
            this.innerText = "Ver por Pais";
            inpu.placeholder = "Buscar por región";
        }else{
            tipo=0;
            this.innerText = "Ver por Regiones";
            inpu.placeholder = "Buscar por país";
        }};
    }
}
function recursive4(){
    
    var bb=document.getElementById('search');
    if(bb==null){
        setTimeout(recursive4,100);
    }
    else{
        bb.placeholder = "Buscar por país";
        
    }
}
recursive4();
recursive();
recursive2();
recursive3();

