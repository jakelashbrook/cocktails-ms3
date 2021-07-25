$( document ).ready(function() {
    
    // Code idea from stack overflow

    const button = document.body.querySelector('#l-or-d-mode');
    const btnIcon = document.body.querySelector('#l-or-d-icon');

    /*
    Add click event listener where we will provide logic that updates the button text
    */
    button.addEventListener('click', function () {

        /*
        Update the text of the button to toggle beween "Dark" and "Light" when clicked
        */
        if (btnIcon.className=="fas fa-moon") {
            btnIcon.className = 'fas fa-sun';
            button.title = "Light Mode"
        }
        else {
            btnIcon.className = 'fas fa-moon';
            button.title = "Dark Mode";
        }
    });

    // End of Stack Overflow inspired code

    $("#edit-cat-dd").click(function() {
        $("#edit-cat-area").removeClass("d-none");
    });
});