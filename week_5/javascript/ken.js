function checkAge() {
    const age = prompt("Enter your age:");
    let output = "";
    if (age < 18) {
      output = "Sorry, you cannot join.";
    } else {
      output = "Congratulations, you can join!";
    }
    document.getElementById("output").innerHTML = output;
  }
  