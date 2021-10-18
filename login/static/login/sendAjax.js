function Sendajax(title, content, confirm, url, parameters,urlList) {
    $.confirm({
        icon: 'fas fa-exclamation-triangle',
        theme: 'modern',
        title: title,
        content: content,
        type: 'orange',
        animation: 'zoom',
        buttons: {
            save: {
                text: '<i class="fa fa-save"></i> Guardar',
                action: function () {
                    $.ajax({
                        url: url, //window.location.pathname
                        type: 'POST',
                        data: parameters,
                        dataType: 'json',
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            $('input').removeClass('is-invalid');
                            $.alert({
                                icon: 'fas fa-check',
                                theme: 'modern',
                                type: 'green',
                                title: 'Éxito!!',
                                animation: 'zoom',
                                content: confirm,
                                buttons: {
                                    save: {
                                        text: 'Aceptar',
                                        action: function () {
                                            location.href = window.location.pathname;
                                        }
                                    },
                                    /*list: {
                                        text: '<i class="fa fa-home"></i> Página principal',
                                        action: function () {
                                            location.href = urlList
                                        }
                                    }*/
                                }
                            });
                            return false;
                        }
                        //Llamada a la funcion que maneja el error
                        errorMessage(data.error);
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    }).always(function (data) {

                    });
                }
            },
            cancel: {
                text: '<i class="fa fa-times"></i> Cancelar',
                btnClass: 'btn-danger',
                close: function () {
                }
            }
        }
    });

}