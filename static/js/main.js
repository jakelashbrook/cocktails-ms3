$( document ).ready(function() {
    $('#del-ct-btn').click(function(){
        $('#like-ct-btn').addClass('d-none');
        $('#edit-ct-btn').addClass('d-none');
        $('#del-ct-btn').addClass('d-none');
        $('#r-u-sure').removeClass('d-none');
        $('#y-del').removeClass('d-none');
        $('#n-del').removeClass('d-none');
    });
    
    $('#n-del').click(function(){
        $('#like-ct-btn').removeClass('d-none');
        $('#edit-ct-btn').removeClass('d-none');
        $('#del-ct-btn').removeClass('d-none');
        $('#r-u-sure').addClass('d-none');
        $('#y-del').addClass('d-none');
        $('#n-del').addClass('d-none');
    });
    
    $('#edit-cn-btn').click(function() {
        $('#accordionExample').addClass('d-none');
        $('#edit-cn-area').removeClass('d-none');
    });

    // The Edit Category Button Functions 
    $("#edit-cat-dd").click(function() {
        $('#edit-cat-dd').addClass('d-none');
        $('#edit-cat-area').removeClass('d-none');
        $('#del-cat-dd').addClass('d-none');
    });

    // If Cancel Edit Category clicked
    $("#canx-cat-edit").click(function() {
        $("#edit-cat-dd").removeClass('d-none');
        $("#edit-cat-area").addClass('d-none');
        $("#del-cat-dd").removeClass('d-none');
    });

    // If Delete category clicked, Are you sure?
    $("#del-cat-dd").click(function() {
        $('#del-cat-dd').addClass('d-none');
        $('#del-cat-area').removeClass('d-none');
    });

    // If no category deletion selected 
    $("#del-cat-no").click(function() {
        $('#del-cat-dd').removeClass('d-none');
        $('#del-cat-area').addClass('d-none');
    });

    // If Delete user recipe clicked, Are you sure?
    $("#del-rec-dd").click(function() {
        $('#del-rec-dd').addClass('d-none');
        $('#del-rec-area').removeClass('d-none');
    });

    // If no user recipe deletion selected 
    $("#del-rec-no").click(function() {
        $('#del-rec-dd').removeClass('d-none');
        $('#del-rec-area').addClass('d-none');
    });

});