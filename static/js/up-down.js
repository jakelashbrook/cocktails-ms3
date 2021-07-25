// Start of code based on W3schools Back to the top button page
//Get the back to top button
let mybutton = document.getElementById("back-to-top-btn");
let bottombutton = document.getElementById("bottom-btn");
// let footer = document.getElementById("footer");

// When the user scrolls down 120px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};
// button appears after page has been scrolled
function scrollFunction() {
  if (document.body.scrollTop > 240 || document.documentElement.scrollTop > 240) {
    mybutton.style.display = "block";
    bottombutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
    bottombutton.style.display = "none";
  } 
  // End of Code
  }


/* 

THIS CODE IS COMMENTED OUT AFTER JSHINT VALIDATION, as is the let footer variable

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
// End of code based on w3 Schools

function bottomFunction() {
    window.scrollTo(0,document.body.footer);
} 

*/