
'use strict';

function gestionarModal (ruta, id_modal) {
    $.ajax({
        url: ruta,
        context: document.body
    }).done(function (response) {
        let modal = $('#' + id_modal);
        if (response.includes("<!DOCTYPE html>")) {
            return false
        }else{
            modal.html(response);
            modal.modal("show");
        }
    });
}