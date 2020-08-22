function to_about(){
    document.location = "about.html";
}
function to_calc(){
    document.location = "calc.html";
}
function to_index(){
    document.location = "index.html";
}
function calc_markavrg(){
    let marks = document.getElementById("marks").value;
    let marklist = marks.split(",");
    let num = 0;
    for(let i = 0; i < marklist.length; i++){
        num += parseInt(marklist[i]);
    }
    let avrg = num/marklist.length;
    avrg = Math.round(avrg);
    document.getElementById("average").innerHTML = String(avrg);
}
