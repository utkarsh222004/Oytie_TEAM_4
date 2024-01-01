 validation.js
function validateForm() {
  var name = document.forms["registrationForm"]["name"].value;
  var username = document.forms["registrationForm"]["username"].value;
  var id = document.forms["registrationForm"]["id"].value;
  var mailID = document.forms["registrationForm"]["mailID"].value;
  var address = document.forms["registrationForm"]["address"].value;
  var phone = document.forms["registrationForm"]["phone"].value;
  var subject = document.forms["registrationForm"]["subject"].value;
  var password = document.forms["registrationForm"]["password"].value;
  var confirmPassword = document.forms["registrationForm"]["confirmPassword"].value;

  // Basic non-empty checks
  if (name === "" || username === "" || id === "" || mailID === "" || address === "" || phone === "" || subject === "" || password === "" || confirmPassword === "") {
    alert("All fields must be filled out");
    return false;
  }

  // Email validation
  var emailRegex = /^\S+@\S+\.\S+$/;
  if (!emailRegex.test(mailID)) {
    alert("Please enter a valid email address");
    return false;
  }

  // Phone number validation (assuming 10-digit number)
  var phoneRegex = /^\d{10}$/;
  if (!phoneRegex.test(phone)) {
    alert("Please enter a valid 10-digit phone number");
    return false;
  }

  // Name validation (assuming only letters and spaces)
  var nameRegex = /^[a-zA-Z\s]+$/;
  if (!nameRegex.test(name)) {
    alert("Please enter a valid name (only letters and spaces)");
    return false;
  }

  // Password matching validation
  if (password !== confirmPassword) {
    alert("Passwords do not match");
    return false;
  }

  // Form is validated, you can perform additional actions here
  alert("Form is validated!"); // Replace this with your desired action
  return true;
}