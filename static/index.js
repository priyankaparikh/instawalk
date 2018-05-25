$('.add_directions').on('submit', function (evt) {
    evt.preventDefault();
    let formInput = {
        photo: $('#uploadPhoto').val(),
        directions: $('#directions').val()
    };
    $.post('/add_directions.json', formInput, function (result) {
        $('#myModal .close').click();
        console.log(result)
    });
});