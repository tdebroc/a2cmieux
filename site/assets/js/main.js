/* A2CMieux — interactions & accessibilité */
(function () {
  "use strict";
  var root = document.documentElement;

  /* --- Préférences persistantes (contraste + taille du texte) --- */
  try {
    if (localStorage.getItem("a2c-contrast") === "high") root.setAttribute("data-contrast", "high");
    if (localStorage.getItem("a2c-textsize") === "large") root.setAttribute("data-textsize", "large");
  } catch (e) {}

  function bindToggle(id, attr, value, storageKey) {
    var btn = document.getElementById(id);
    if (!btn) return;
    function sync() {
      var on = root.getAttribute(attr) === value;
      btn.setAttribute("aria-pressed", on ? "true" : "false");
    }
    sync();
    btn.addEventListener("click", function () {
      var on = root.getAttribute(attr) === value;
      if (on) { root.removeAttribute(attr); try { localStorage.removeItem(storageKey); } catch (e) {} }
      else { root.setAttribute(attr, value); try { localStorage.setItem(storageKey, value); } catch (e) {} }
      sync();
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    bindToggle("toggle-contrast", "data-contrast", "high", "a2c-contrast");
    bindToggle("toggle-textsize", "data-textsize", "large", "a2c-textsize");

    /* --- Menu mobile --- */
    var toggle = document.querySelector(".nav-toggle");
    var menu = document.getElementById("primary-menu");
    if (toggle && menu) {
      toggle.addEventListener("click", function () {
        var open = menu.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        document.body.style.overflow = open && window.innerWidth <= 960 ? "hidden" : "";
      });
      menu.addEventListener("click", function (e) {
        if (e.target.tagName === "A" && window.innerWidth <= 960) {
          menu.classList.remove("open");
          toggle.setAttribute("aria-expanded", "false");
          document.body.style.overflow = "";
        }
      });
    }

    /* --- Sous-menus déroulants --- */
    document.querySelectorAll(".has-sub").forEach(function (item) {
      var btn = item.querySelector("button");
      if (!btn) return;
      btn.addEventListener("click", function () {
        var open = item.getAttribute("data-open") === "true";
        document.querySelectorAll('.has-sub[data-open="true"]').forEach(function (o) {
          if (o !== item) { o.setAttribute("data-open", "false"); o.querySelector("button").setAttribute("aria-expanded", "false"); }
        });
        item.setAttribute("data-open", open ? "false" : "true");
        btn.setAttribute("aria-expanded", open ? "false" : "true");
      });
    });
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".has-sub")) {
        document.querySelectorAll('.has-sub[data-open="true"]').forEach(function (o) {
          o.setAttribute("data-open", "false"); o.querySelector("button").setAttribute("aria-expanded", "false");
        });
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        document.querySelectorAll('.has-sub[data-open="true"]').forEach(function (o) {
          o.setAttribute("data-open", "false"); o.querySelector("button").setAttribute("aria-expanded", "false");
        });
      }
    });

    /* --- Animations d'apparition au défilement --- */
    var reveals = document.querySelectorAll(".reveal");
    if ("IntersectionObserver" in window && reveals.length) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
        });
      }, { threshold: 0.12 });
      reveals.forEach(function (el) { io.observe(el); });
    } else {
      reveals.forEach(function (el) { el.classList.add("in"); });
    }

    /* --- Année du pied de page --- */
    var y = document.getElementById("year");
    if (y) y.textContent = new Date().getFullYear();
  });
})();
