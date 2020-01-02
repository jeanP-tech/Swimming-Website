var note_contents = document.querySelectorAll(".note_contents");
var note = document.querySelectorAll(".note");

for(let i=0; i<note.length; i++){
    note[i].addEventListener("click", function() {
      if(!note_contents[i].style.display || note_contents[i].style.display === "none"){
        note[i].innerHTML = "접기";
        note_contents[i].style.display = "block";
      }
      else{
        note[i].innerHTML = "자세히";
        note_contents[i].style.display = "none";
      }
    });
}

function init(){
  console.log("hi");
}

init();
