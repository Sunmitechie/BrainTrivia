let correctSound = new Audio("static/correct.mp3");
let wrongSound = new Audio("static/wrong.mp3");

document.querySelectorAll("button[name='answer']").forEach(button => {
    button.addEventListener("click", function() {
        let userChoice = this.value;
        let correctAnswer = document.getElementById("correct-answer").value;

        if (userChoice === correctAnswer) {
            correctSound.play();
        } else {
            wrongSound.play();
        }
    });
});
