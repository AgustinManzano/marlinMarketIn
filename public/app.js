// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function () {
    // Obtener referencias a los elementos del DOM
    const callForm = document.getElementById('call-form');
    const phoneNumberInput = document.getElementById('phone-number');
    const submitBtn = document.getElementById('submit-btn');
    const messageDiv = document.getElementById('message');

    // URL de la API (ruta relativa, Vercel la enrutará correctamente)
    const API_URL = '/api/trigger-call';

    // Agregar event listener al envío del formulario
    callForm.addEventListener('submit', async function (event) {
        // Prevenir el comportamiento por defecto del formulario
        event.preventDefault();

        // Obtener el número de teléfono
        const phoneNumber = phoneNumberInput.value.trim();

        // Validación básica del cliente
        if (!phoneNumber) {
            showMessage('Por favor, ingresá un número de teléfono.', 'error');
            return;
        }

        // Deshabilitar el botón y mostrar estado de carga
        submitBtn.disabled = true;
        messageDiv.textContent = 'Llamando...';
        messageDiv.className = 'loading';

        try {
            // Realizar la llamada fetch a la API
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    phoneNumber: phoneNumber,
                }),
            });

            // Parsear la respuesta JSON
            const data = await response.json();

            // Manejar la respuesta
            if (data.success) {
                showMessage(
                    '¡Listo! Mirá tu teléfono. El agente de IA te llamará en segundos. ¡Que disfrutes!',
                    'success'
                );
                // Limpiar el input
                phoneNumberInput.value = '';
                // Habilitar el botón después de 5 segundos para permitir otra llamada
                setTimeout(() => {
                    submitBtn.disabled = false;
                }, 5000);
            } else {
                showMessage(
                    data.message || 'Ocurrió un error. Intentá de nuevo.',
                    'error'
                );
                submitBtn.disabled = false;
            }
        } catch (error) {
            console.error('Error al hacer la solicitud:', error);
            showMessage(
                'Error de conexión. Por favor, intentá de nuevo.',
                'error'
            );
            submitBtn.disabled = false;
        }
    });

    /**
     * Función auxiliar para mostrar mensajes al usuario
     * @param {string} message - El mensaje a mostrar
     * @param {string} type - El tipo de mensaje ('success', 'error', 'loading')
     */
    function showMessage(message, type) {
        messageDiv.textContent = message;
        messageDiv.className = type;
    }
});
