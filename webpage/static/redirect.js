function to_about(){
    document.location = "about.html";
}
function to_calc(){
    document.location = "calc.html";
}
function calc_markavrg(){
    let marks = String(document.getElementById("marks").value);
    marks = marks.split(",");
    let num = 0;
    for(let i;i<marks.length;i++ ){
        num += Number(marks[i]);
    }
    let avrg = num/marks.length;
    document.getElementById("average").innerHTML = String(avrg);
}