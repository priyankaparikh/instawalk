$('.add_directions').on('submit', function (evt) {
    evt.preventDefault();
    let formInput = {
        photo: $('#upload_photo').val(),
        directions: $('textarea#directions').val()
    };
    $.post('/add_directions.json', formInput, function (result) {
        $('#myform')[0].reset();
        $('#myModal .close').click();
        console.log(result)
    });
});