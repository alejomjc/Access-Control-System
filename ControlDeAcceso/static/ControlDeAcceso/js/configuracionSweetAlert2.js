'use strict';

function confirmarAccion(url) {
    Swal.fire({
        title: '¿Está seguro de realizar esta acción?',
        text: "Usted no podrá revertirla",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#dd773b',
        cancelButtonColor: '#827c7c',
        confirmButtonText: 'Confirmar!',
        cancelButtonText: 'Cancelar',
    }).then((result) => {
        if (result.isConfirmed) {
            confirmacion(url)
        }
    })
}

function confirmarAccionConJustificacion(url, mensaje=null) {
    Swal.fire({
        title: '¿Está seguro de realizar esta acción?',
        text: "Usted no podrá revertirla",
        icon: 'warning',
        input: 'text',
        inputPlaceholder: '¿Por qué desea hacerlo?',
        inputValue: '',
        showCancelButton: true,
        inputAttributes: {'maxlength': 100},
        confirmButtonColor: '#dd773b',
        cancelButtonColor: '#827c7c',
        confirmButtonText: mensaje ? mensaje : 'Eliminar!',
        cancelButtonText: 'Cancelar',
        inputValidator: (value) => {
            if (!value) {
              return '¡Debes justificar esta acción!'
            }
        }
    }).then((result) => {
        if (result.isConfirmed) {
            confirmacion(url, result.value)
        }
    })
}

function confirmacion(url, valor = null) {
    $.ajax({
        url: url,
        type: 'POST',
        data:{'valor': valor},
        context: document.body,
        success: function (data) {
            if(data.estado === "OK") {
                confirmado()
            }else if(data.estado === "error"){
                errado(data.mensaje)
            }
            else {
                errado()
            }
        },
        failure: function (errMsg) {
            errado()
            console.log(errMsg)
        }
    });
}

function confirmado() {
    Swal.fire({
        title: 'Realizado',
        icon: 'success',
    }).then((result) => {
        if (result.isConfirmed) {
            location.reload();
        }
    })
}

function errado(mensaje = null) {
    let texto = '';
    if (mensaje){
        texto = mensaje
    }else{
        texto = 'Ha ocurrido un error realizando la acción!'
    }
    Swal.fire({
        title: 'Error!',
        text: texto,
        icon: 'error',
    }).then((result) => {
        if (result.isConfirmed) {
            location.reload();
        }
    })
}

function confirmarFechaEjecucion(url) {
    Swal.fire({
        title: '¿Está seguro de realizar esta acción?',
        text: "Indique la fecha de finalización de la tarea",
        icon: 'warning',
        input: 'text',
        inputPlaceholder: '¿Por qué desea hacerlo?',
        inputValue: '',
        showCancelButton: true,
        inputAttributes: {'maxlength': 100, 'id': 'inputSweetAlert'},
        confirmButtonColor: '#dd773b',
        cancelButtonColor: '#827c7c',
        confirmButtonText: 'Finalizar!',
        cancelButtonText: 'Cancelar',
        inputValidator: (value) => {
            if (!value) {
              return '¡Debes ingresar una fecha de finalización!'
            }
        }
    }).then((result) => {
        if (result.isConfirmed) {
            confirmacion(url, result.value)
        }
    })
        $('#inputSweetAlert').get(0).type = 'date';
}