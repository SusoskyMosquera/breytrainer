// Este script se ejecuta en el panel de administrador de Django
// para mostrar los campos relevantes según el tipo de post seleccionado.

window.addEventListener("load", function() {
    (function($) {
        function toggleFields() {
            var postType = $("#id_post_type").val();
            
            // Ocultar todos los campos específicos por defecto
            $('.form-row.field-video').hide();

            // Mostrar campos según el tipo seleccionado
            if (postType === 'RUTINA') {
                $('.form-row.field-video').show();
            }
        }

        // Ejecutar al cargar la página
        toggleFields();

        // Ejecutar cuando cambie el selector de tipo
        $("#id_post_type").change(function() {
            toggleFields();
        });
    })(django.jQuery);
});