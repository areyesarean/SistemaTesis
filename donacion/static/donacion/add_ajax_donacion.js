function SendajaxD(title, content, url, parameters, urlList) {
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
                                title: 'Éxito!!!',
                                animation: 'zoom',
                                content: 'Datos guardados correctamente',
                                buttons: {
                                    save: {
                                        text: '<i class="fa fa-plus"></i> Agregar otro',
                                        action: function () {
                                            location.href = window.location.pathname;
                                        }
                                    },
                                    list: {
                                        text: '<i class="fa fa-list"></i> listado',
                                        action: function () {
                                            location.href = urlList
                                        }
                                    }
                                }
                            });
                            return false;
                        }
                        //Llamada a la funcion que maneja el error
                        console.log(data.error)
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

function DelAjax(title, content, url, parameters, callback) {
    $.confirm({
        icon: 'fas fa-exclamation-triangle',
        theme: 'modern',
        title: title,
        content: content,
        type: 'orange',
        animation: 'zoom',
        buttons: {
            save: {
                text: '<i class="fa fa-trash"></i> Eliminar',
                action: function () {
                    $.ajax({
                        url: url, //window.location.pathname
                        type: 'POST',
                        data: parameters,
                        dataType: 'json',
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback()
                        } else {
                            errorMessage(data.error);
                        }
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert('Metodo Fail de Ajax: ' + textStatus + ': ' + errorThrown);
                    }).always(function (data) {

                    });
                }
            },
            cancel: {
                text: '<i class="fa fa-times-circle"></i> Cancelar',
                btnClass: 'btn-danger',
                close: function () {
                }
            }
        }
    });

}

function SendajaxE(title, content, url, parameters, callback) {
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
                                title: 'Éxito!!!',
                                animation: 'zoom',
                                content: 'Datos guardados correctamente',
                                buttons: {
                                    confirm: {
                                        text: '<i class="fa fa-check-circle"></i> Aceptar',
                                        btnClass: 'btn-default',
                                        action: function () {
                                            callback()
                                        }
                                    }
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