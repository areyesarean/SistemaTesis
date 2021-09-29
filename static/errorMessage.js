function errorMessage(obj) {
    var html = '';
    $('input').removeClass('is-invalid');
    var inpError = [];
    if (typeof (obj) === 'object') {
        $.each(obj, function (key, value) {
            html += '<p>' + value + '</p>';
            inpError.push('#id_'+key);
        });
    } else {
        html = '<p>' + obj + '</p>';
    }
    //console.log(inpError);
    inpError.forEach(function (el) {
        $(el).addClass('is-invalid');
    })
    $.alert({
        icon: 'fa fa-times-circle',
        theme: 'modern',
        animation: 'zoom',
        type: 'red',
        title: 'Error!',
        content: html
    });
}
