document.getElementsByClassName("type").innerHTML="Hello World";
function greet(){
    let total_class_in_html =getElementsByClassName("type").lenght;
    console.log(total_class_in_html);
    for(let i=0;i<total_class_in_html;i++){
        document.getElementsByClassName("type")[i]innerHTML="Every one fine......."
    }
}
function show_alert(){
    alert("Focus On Study");
}