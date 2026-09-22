/* A2CMieux — interactions & panneau d'accessibilité */
(function () {
  "use strict";
  var root = document.documentElement;
  var KEY = "a2c-a11y";
  var MIN = 0.85, MAX = 1.6, STEP = 0.1;

  var state = { scale: 1, grayscale: false, contrast: false, negative: false, lightbg: false, underline: false, readable: false };

  try {
    var saved = JSON.parse(localStorage.getItem(KEY) || "{}");
    for (var k in state) { if (k in saved) state[k] = saved[k]; }
  } catch (e) {}

  function save() { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {} }

  function apply() {
    // Taille du texte
    root.style.fontSize = state.scale === 1 ? "" : (state.scale * 100).toFixed(0) + "%";
    // Filtres visuels (niveaux de gris / contraste négatif)
    var f = [];
    if (state.grayscale) f.push("grayscale(1)");
    if (state.negative) f.push("invert(1) hue-rotate(180deg)");
    root.style.filter = f.join(" ");
    // Modes par classes / attribut
    root.classList.toggle("a11y-lightbg", state.lightbg);
    root.classList.toggle("a11y-underline", state.underline);
    root.classList.toggle("a11y-readable", state.readable);
    if (state.contrast) root.setAttribute("data-contrast", "high");
    else root.removeAttribute("data-contrast");
  }

  // Application immédiate (avant le rendu complet) pour éviter le clignotement
  apply();

  function syncButtons() {
    var map = { grayscale: "grayscale", contrast: "contrast", negative: "negative", lightbg: "lightbg", underline: "underline", readable: "readable" };
    document.querySelectorAll(".a11y-tool[aria-pressed]").forEach(function (btn) {
      var key = btn.getAttribute("data-a11y");
      if (map[key]) btn.setAttribute("aria-pressed", state[map[key]] ? "true" : "false");
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    syncButtons();

    /* --- Panneau d'accessibilité --- */
    var panel = document.getElementById("a11y-panel");
    var overlay = document.getElementById("a11y-overlay");
    var openBtn = document.getElementById("a11y-open");
    var closeBtn = document.getElementById("a11y-close");
    var lastFocus = null;

    function openPanel() {
      lastFocus = document.activeElement;
      panel.hidden = false; overlay.hidden = false;
      openBtn.setAttribute("aria-expanded", "true");
      var first = panel.querySelector("button");
      if (first) first.focus();
      document.addEventListener("keydown", onKey);
    }
    function closePanel() {
      panel.hidden = true; overlay.hidden = true;
      openBtn.setAttribute("aria-expanded", "false");
      document.removeEventListener("keydown", onKey);
      if (lastFocus) lastFocus.focus();
    }
    function onKey(e) { if (e.key === "Escape") closePanel(); }

    if (openBtn) openBtn.addEventListener("click", openPanel);
    if (closeBtn) closeBtn.addEventListener("click", closePanel);
    if (overlay) overlay.addEventListener("click", closePanel);

    /* --- Actions des outils --- */
    document.querySelectorAll("[data-a11y]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var a = btn.getAttribute("data-a11y");
        switch (a) {
          case "text-plus": state.scale = Math.min(MAX, +(state.scale + STEP).toFixed(2)); break;
          case "text-minus": state.scale = Math.max(MIN, +(state.scale - STEP).toFixed(2)); break;
          case "grayscale": state.grayscale = !state.grayscale; break;
          case "contrast": state.contrast = !state.contrast; break;
          case "negative": state.negative = !state.negative; break;
          case "lightbg": state.lightbg = !state.lightbg; break;
          case "underline": state.underline = !state.underline; break;
          case "readable": state.readable = !state.readable; break;
          case "reset":
            state = { scale: 1, grayscale: false, contrast: false, negative: false, lightbg: false, underline: false, readable: false };
            break;
        }
        apply(); save(); syncButtons();
      });
    });

    /* --- Menu mobile --- */
    var toggle = document.querySelector(".nav-toggle");
    var menu = document.getElementById("primary-menu");
    if (toggle && menu) {
      toggle.addEventListener("click", function () {
        var open = menu.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
      menu.addEventListener("click", function (e) {
        if (e.target.tagName === "A" && window.innerWidth <= 960) {
          menu.classList.remove("open");
          toggle.setAttribute("aria-expanded", "false");
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
