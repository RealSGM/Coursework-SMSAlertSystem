const buttons = document.getElementsByClassName("language-button");
const khmer = document.getElementsByClassName("khmer");
const english = document.getElementsByClassName("english");

let language = 0;
// button_texts = ["Click for English", "ចុចដើម្បីខ្មែរ"]

function changelanguage(){
    if (language === 0) {
        language = 1;
    
        for (const b of buttons) {
            b.innerHTML = "ចុចដើម្បីខ្មែរ"
        }
    
        for (const e of english) {e.style.display = "inherit"}
        for (const e of khmer) {e.style.display = "none"}
    
    }

    else {
        language = 0;
    
        for (const b of buttons) {
            b.innerHTML = "Click for English"
        }
    
        for (const e of english) {e.style.display = "none"}
        for (const e of khmer) {e.style.display = "inherit"}
    } 
}

for (const b of buttons) {
    b.addEventListener("click", changelanguage)
}