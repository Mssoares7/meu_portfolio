document.addEventListener("DOMContentLoaded", () => {
  // Abas do currículo
  const tabLinks = document.querySelectorAll(".tab-link");
  const tabContents = document.querySelectorAll(".tab-content");

  tabLinks.forEach(link => {
    link.addEventListener("click", () => {
      const target = link.dataset.target;
      tabContents.forEach(content => content.style.display = "none");
      tabLinks.forEach(link => link.classList.remove("active"));
      document.getElementById(target).style.display = "block";
      link.classList.add("active");
    });
  });

  if (tabLinks.length > 0) {
    tabLinks[0].click();
  }

  // Filtro de projetos por tecnologia
  const filterButtons = document.querySelectorAll(".filter-btn");
  const projetos = document.querySelectorAll(".projeto");

  function applyFadeIn() {
    projetos.forEach(el => {
      el.classList.remove("show");
      void el.offsetWidth; // força reflow
      if (el.style.display !== "none") {
        el.classList.add("show");
      }
    });
  }

  filterButtons.forEach(button => {
    button.addEventListener("click", () => {
      const tecnologia = button.dataset.tecnologia.toLowerCase();

      filterButtons.forEach(btn => btn.classList.remove("active"));
      button.classList.add("active");

      projetos.forEach(proj => {
        const tags = proj.dataset.tecnologias.toLowerCase();
        if (tecnologia === "all" || tags.includes(tecnologia)) {
          proj.style.display = "block";
        } else {
          proj.style.display = "none";
        }
      });

      applyFadeIn();
    });
  });

  applyFadeIn();
});
