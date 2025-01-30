const containers = document.querySelectorAll(".container");

containers.forEach(container => {
  container.addEventListener("touchstart", () => {
    if (!container.classList.contains("active")) {
      container.classList.add("active");
    } else {
      container.classList.remove("active");
    }
  });
});


document.addEventListener("touchstart", (event) => {
  containers.forEach(container => {
    if (!container.contains(event.target)) {
      container.classList.remove("active");
    }
  });
});