function postLoad(){
    // retrieved the clarification input
    var clarification = document.getElementById("new_clarification");

    // retrieve the remaining time input
    var remaining_time = document.getElementById("time_text")

    if (clarification){
    clarification.addEventListener("keypress", function(event) {
        if (event.keyCode === 13) {
            document.getElementById("text_clarification").submit()
            clarification.value = '';
        }
        clarification.style.height = 'auto'
        clarification.style.height = (clarification.scrollHeight) + 'px'
    })

    }

    if(remaining_time){

    remaining_time.addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            var time = remaining_time.value;
            if (new RegExp('\\d?\\d:\\d\\d').test(time)) {
                remaining_time.value = ""
            }
        }
    })

    }
    
    
}
window.onload = function () {
    postLoad();
}
