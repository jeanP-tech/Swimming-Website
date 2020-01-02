var note_contents = document.getElementsByClassName("note_contents");
var note = document.getElementsByClassName("note");

Array.from(note).forEach((note, index) => {
  note.addEventListener("click", showNoteContents(note, index));
});

function showNoteContents(note, index){
  const contents = note_contents[index];
  if(!contents.style.display || contents.style.display === "none"){
    note.innerHTML = "접기";
    contents.style.display = "block";
  }
  else{
    note.innerHTML = "자세히";
    contents.style.display = "none";
  }
}

//
// for(let i=0; i<note.length; i++){
//     note.addEventListener("click", function() {
//       if(!contents.style.display || contents.style.display === "none"){
//         note.innerHTML = "접기";
//         contents.style.display = "block";
//       }
//       else{
//         note.innerHTML = "자세히";
//         contents.style.display = "none";
//       }
//     });
// }

// for(let i=0; i<note.length; i++) {
//   note.addEventListener("click", noteClick(i));
//  }
//
// function noteClick(i) {
//  if(!contents.style.display || contents.style.display === "none"){
//    note.innerHTML = "접기";
//    contents.style.display = "block";
//  }
//  else{
//    note.innerHTML = "자세히";
//    contents.style.display = "none";
//  }
// }
