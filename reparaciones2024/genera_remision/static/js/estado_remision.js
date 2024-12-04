function cambiarEstado(id, estado) {
    const fila = document.getElementById("estado-" + id);
    const boton = fila.querySelector("button");
    // Cambiar el color de la fila según el estado
    if (estado === 'Pasado') {
        fila.style.borderColor = 'red';
        boton.textContent = 'En Proceso'; // Cambiar el estado
    } else if (estado === 'En Proceso') {
        fila.style.borderColor = 'yellow';
        boton.textContent = 'Solucionado'; // Cambiar el estado
    } else if (estado === 'Solucionado') {
        fila.style.borderColor = 'green';
        boton.textContent = 'Pasado'; // Cambiar el estado
        }
    }