/* YouTube facade (O9, DK-2026-08-03-17)
   Sayfa yükünde ağır YouTube iframe'i yerine hafif küçük resim + oynat düğmesi gösterir;
   tıklamada videoyu youtube-nocookie.com üzerinden başlatır (KVKK: onay öncesi çerez yok).
   Kendi CSS'ini enjekte eder; öğeler dinamik eklense de çalışır (event delegation). */
(function () {
  var css = '.yt-lite{position:relative;display:block;width:100%;height:100%;aspect-ratio:16/9;background:#000;cursor:pointer;}' +
    '.yt-lite img{width:100%;height:100%;object-fit:cover;display:block;}' +
    '.yt-lite-btn{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:64px;height:46px;background:rgba(10,18,37,.85);border:1px solid rgba(255,255,255,.3);border-radius:12px;transition:background .2s,border-color .2s;}' +
    '.yt-lite-btn::after{content:"";position:absolute;top:50%;left:50%;transform:translate(-40%,-50%);border-style:solid;border-width:9px 0 9px 15px;border-color:transparent transparent transparent #fff;}' +
    '.yt-lite:hover .yt-lite-btn,.yt-lite:focus-visible .yt-lite-btn{background:#00c8f0;border-color:#00c8f0;}' +
    '.yt-lite-frame{width:100%;height:100%;aspect-ratio:16/9;border:0;display:block;}';
  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);

  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('.yt-lite') : null;
    if (!a) return;
    var id = a.getAttribute('data-yt');
    if (!id) return;
    e.preventDefault();
    var ifr = document.createElement('iframe');
    ifr.className = 'yt-lite-frame';
    ifr.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1&rel=0';
    ifr.title = a.getAttribute('data-title') || 'YouTube video';
    ifr.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
    ifr.setAttribute('allowfullscreen', '');
    if (a.replaceWith) { a.replaceWith(ifr); } else { a.parentNode.replaceChild(ifr, a); }
  });
})();
