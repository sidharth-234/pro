let display=document.getElementById('show')
function addvalue(value){
    display.value+=value

}
function calculate(){
    display.value=eval(display.value)
}


function cleardisplay(){
    display.value=''
}

