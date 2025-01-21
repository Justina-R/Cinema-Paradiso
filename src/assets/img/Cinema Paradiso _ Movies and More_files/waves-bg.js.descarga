document.addEventListener("DOMContentLoaded", () => {
    // Seleccionar todos los contenedores de SVG
    const svgContainers = document.querySelectorAll(".svg-container");
  
    svgContainers.forEach((container) => {
      // Obtener el siguiente elemento después del contenedor del SVG
      const nextElement = container.nextElementSibling;
  
      if (nextElement) {
        // Obtener el color de fondo del siguiente elemento
        const bgColor = window.getComputedStyle(nextElement).backgroundColor;
  
        // Aplicar el color de fondo al contenedor del SVG
        container.style.backgroundColor = bgColor;
      }
    });
  });