$( document ).ready(function() {

    $('#l-or-d-mode').click(function() {
  if ($('body').hasClass('light-mode')){
    $('body').removeClass('light-mode');
    $('body').addClass('dark-mode');
    $('#log-nav a').addClass('btn button m-2');
    $('h3').addClass('dm-h3');
    $('hr').addClass('hr-dm')
    $('footer h6').addClass('dm-f-txt');
    $('#l-or-d-mode').html('<i class="fas fa-moon"></i>');
  }
  else if ($('body').hasClass('dark-mode')){
    $('body').removeClass('dark-mode');
    $('body').addClass('light-mode');
    $('#log-nav a').removeClass('btn button');
    $('h3').removeClass('dm-h3');
    $('hr').removeClass('hr-dm');
    $('footer h6').removeClass('dm-f-txt');
    $('#l-or-d-mode').html('<i class="fas fa-sun"></i>');
  }
});

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