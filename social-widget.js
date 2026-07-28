(function () {
  var LINKS = [
    { name: "LinkedIn", url: "https://www.linkedin.com/company/cadbim/", color: "#0A66C2",
      svg: '<svg viewBox="0 0 24 24" width="18" height="18" fill="#fff" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.03-1.85-3.03-1.85 0-2.14 1.45-2.14 2.94v5.66H9.36V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.38-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.11 20.45H3.56V9h3.55v11.45z"/></svg>' },
    { name: "YouTube", url: "https://www.youtube.com/c/CadbimTeknikDestek", color: "#FF0000",
      svg: '<svg viewBox="0 0 24 24" width="19" height="19" fill="#fff" aria-hidden="true"><path d="M23.5 6.19a2.94 2.94 0 0 0-2.07-2.08C19.55 3.6 12 3.6 12 3.6s-7.55 0-9.43.51A2.94 2.94 0 0 0 .5 6.19 30.7 30.7 0 0 0 0 12a30.7 30.7 0 0 0 .5 5.81 2.94 2.94 0 0 0 2.07 2.08c1.88.51 9.43.51 9.43.51s7.55 0 9.43-.51a2.94 2.94 0 0 0 2.07-2.08A30.7 30.7 0 0 0 24 12a30.7 30.7 0 0 0-.5-5.81zM9.55 15.57V8.43L15.82 12l-6.27 3.57z"/></svg>' },
    { name: "Instagram", url: "https://www.instagram.com/cadbim_izmir/", color: "linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888)",
      svg: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#fff" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="0.9" fill="#fff" stroke="none"/></svg>' },
    { name: "Facebook", url: "https://www.facebook.com/cadbimizmir", color: "#1877F2",
      svg: '<svg viewBox="0 0 24 24" width="18" height="18" fill="#fff" aria-hidden="true"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5 3.66 9.15 8.44 9.94v-7.03H7.9v-2.9h2.54V9.8c0-2.5 1.49-3.89 3.77-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.87h2.78l-.44 2.9h-2.34V22c4.78-.79 8.44-4.93 8.44-9.94z"/></svg>' }
  ];

  var rail = document.createElement("div");
  rail.id = "social-rail";
  rail.setAttribute("aria-label", "Sosyal medya hesaplarımız");
  rail.style.cssText =
    "position:fixed;left:0;top:50%;transform:translateY(-50%);z-index:9990;" +
    "display:flex;flex-direction:column;gap:6px;";

  LINKS.forEach(function (item) {
    var a = document.createElement("a");
    a.href = item.url;
    a.target = "_blank";
    a.rel = "noopener";
    a.setAttribute("aria-label", item.name);
    a.style.cssText =
      "width:36px;height:36px;display:flex;align-items:center;justify-content:center;" +
      "background:" + item.color + ";border-radius:0 8px 8px 0;box-shadow:2px 2px 10px rgba(0,0,0,.3);" +
      "transition:width .18s ease,transform .18s ease;overflow:hidden;";
    a.innerHTML = item.svg;
    a.addEventListener("mouseenter", function () {
      a.style.width = "42px";
      a.style.transform = "translateX(2px)";
    });
    a.addEventListener("mouseleave", function () {
      a.style.width = "36px";
      a.style.transform = "translateX(0)";
    });
    rail.appendChild(a);
  });

  var style = document.createElement("style");
  style.textContent =
    "@media (max-width:600px){#social-rail a{width:30px!important;height:30px!important;}#social-rail a svg{width:15px!important;height:15px!important;}}";
  document.head.appendChild(style);

  function mount() {
    document.body.appendChild(rail);
  }

  if (document.body) {
    mount();
  } else {
    window.addEventListener("DOMContentLoaded", mount);
  }
})();
