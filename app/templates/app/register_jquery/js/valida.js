

$(document).ready(function () {
    let nombre = $("#nombrer");
    let email = $("#em");
    let password = $("#pass");


    $("#formulario1").validate({

        rules: {
            nombrer: { required: true,minlength: 1, maxlength: 50 },

            email: { required: true, minlength: 1, maxlength: 50 },

            pass:{required: true, minlength: 1, maxlength: 50},
            

        },
        messages:
        {
            nombrer: "Ingrese una  nombre valido.",
            email: "Ingrese una correo valido.",
            pass:"Ingresa uuna contraseña ",
       
        }


    })

    $("#guardar1").click(function () {
        if ($("#formulario1").valid() == false) {

            Swal.fire({
                title: 'Error!',
                text: 'Vuelve a internarlo',
                icon: 'error',
                confirmButtonText: 'Cerrar'
            })
            return;
        }
    })
})