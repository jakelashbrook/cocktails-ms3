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
    
});