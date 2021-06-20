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

    // End of Stack Overflow code

    $('.edit-cn-btn').click(function() {
        $('#accordionExample').addClass('d-none');
        $('.edit-cn-area').removeClass('d-none');
    });

    // The Edit Category Button Functions 
    $(".edit-cat-dd").click(function() {
        $('.edit-cat-dd').addClass('d-none');
        $('.edit-cat-area').removeClass('d-none');
        $('.r-u-sure').addClass('d-none');
    });

    // If Cancel Edit Category clicked
    $(".canx-cat-edit").click(function() {
        $(".edit-cat-dd").removeClass('d-none');
        $(".edit-cat-area").addClass('d-none');
        $(".r-u-sure").removeClass('d-none');
    });

    // If Delete selected, R u sure?
    $(".r-u-sure").click(function() {
        $('.delete-area').removeClass('d-none');
    });

    $(".no-del-btn").click(function() {
        $('.delete-area').addClass('d-none');
    });

});