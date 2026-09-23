// RPI IEEE Student Branch — shared site behavior

document.addEventListener("DOMContentLoaded", () => {
  /* Mobile nav toggle */
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", () => {
      const isOpen = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
    links.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => links.classList.remove("open"))
    );
  }

  /* Highlight active nav link */
  const path = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach((a) => {
    const href = a.getAttribute("href");
    if (href === path || (path === "" && href === "index.html")) {
      a.classList.add("active");
    }
  });

  /* Fade-in on load. Staggered slightly per element, but always resolves —
     content is never left permanently hidden regardless of scroll behavior. */
  const revealEls = document.querySelectorAll(".reveal");
  revealEls.forEach((el, i) => {
    const delay = Math.min(i * 40, 400);
    setTimeout(() => el.classList.add("is-visible"), delay);
  });
  // Safety net: guarantee visibility even if something above throws.
  window.addEventListener("load", () => {
    revealEls.forEach((el) => el.classList.add("is-visible"));
  });

  /* Footer year */
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* Newsletter form (static placeholder — wire up to a real provider later) */
  document.querySelectorAll(".newsletter-form").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const msg = form.querySelector(".newsletter-msg");
      const input = form.querySelector("input[type=email]");
      if (msg) {
        msg.textContent = "Thanks — you're on the list! (Connect this form to Mailchimp/ConvertKit/etc. to make it live.)";
      }
      if (input) input.value = "";
    });
  });
});
