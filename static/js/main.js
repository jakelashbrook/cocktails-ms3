$( document ).ready(function() {

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