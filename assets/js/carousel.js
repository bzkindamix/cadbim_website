/**
 * CAROUSEL.JS — Lightweight vanilla JS carousel
 *
 * Özellikler:
 * - CSS scroll-snap (hardware-accelerated)
 * - Prev/Next button handler
 * - Dot indicator sync
 * - Keyboard navigation (arrow keys)
 * - Touch/mouse scroll support
 * - Responsive breakpoint (data-bp attribute)
 */

(function () {
  'use strict';

  /**
   * Carousel oluştur ve başlat
   * @param {Element} carouselEl - .carousel element
   */
  function initCarousel(carouselEl) {
    const track = carouselEl.querySelector('.carousel-track');
    const slides = track.querySelectorAll('.carousel-slide');
    const btnPrev = carouselEl.querySelector('.carousel-btn-prev');
    const btnNext = carouselEl.querySelector('.carousel-btn-next');
    const dots = carouselEl.querySelectorAll('.carousel-dots button');
    const breakpoint = parseInt(carouselEl.getAttribute('data-bp') || '600', 10);

    if (!track || !slides.length) return;

    let activeIndex = 0;

    /**
     * Scroll to slide
     * @param {number} index - Slide index
     */
    function scrollToSlide(index) {
      if (index < 0 || index >= slides.length) return;

      activeIndex = index;
      const slide = slides[index];
      const slideLeft = slide.offsetLeft;
      const trackPaddingLeft = parseFloat(
        getComputedStyle(track).paddingLeft || 0
      );

      track.scrollLeft = slideLeft - trackPaddingLeft;
      updateDots();
      updateButtons();
    }

    /**
     * Dots sync — aktif dot'u güncelle
     */
    function updateDots() {
      dots.forEach((dot, idx) => {
        const isActive = idx === activeIndex;
        dot.setAttribute('aria-selected', isActive);
      });
    }

    /**
     * Button state — prev/next disable/enable
     */
    function updateButtons() {
      if (btnPrev) {
        btnPrev.disabled = activeIndex === 0;
      }
      if (btnNext) {
        btnNext.disabled = activeIndex === slides.length - 1;
      }
    }

    /**
     * Track scroll position'ndan active index'i tahmin et
     */
    function updateActiveIndexFromScroll() {
      if (!track) return;

      const trackPaddingLeft = parseFloat(
        getComputedStyle(track).paddingLeft || 0
      );
      const scrollLeft = track.scrollLeft;
      let closest = 0;
      let minDistance = Infinity;

      slides.forEach((slide, idx) => {
        const slideLeft = slide.offsetLeft - trackPaddingLeft;
        const distance = Math.abs(scrollLeft - slideLeft);

        if (distance < minDistance) {
          minDistance = distance;
          closest = idx;
        }
      });

      activeIndex = closest;
      updateDots();
      updateButtons();
    }

    /**
     * Prev button click
     */
    if (btnPrev) {
      btnPrev.addEventListener('click', (e) => {
        e.preventDefault();
        scrollToSlide(activeIndex - 1);
      });
    }

    /**
     * Next button click
     */
    if (btnNext) {
      btnNext.addEventListener('click', (e) => {
        e.preventDefault();
        scrollToSlide(activeIndex + 1);
      });
    }

    /**
     * Dot click
     */
    dots.forEach((dot, idx) => {
      dot.addEventListener('click', (e) => {
        e.preventDefault();
        scrollToSlide(idx);
      });
    });

    /**
     * Keyboard navigation (arrow keys)
     */
    carouselEl.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        scrollToSlide(activeIndex - 1);
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        scrollToSlide(activeIndex + 1);
      }
    });

    /**
     * Track scroll event — active index update
     * (scroll-snap'ten sonra index'i güncellemek için)
     */
    let scrollTimeout;
    track.addEventListener('scroll', () => {
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(updateActiveIndexFromScroll, 150);
    });

    /**
     * ARIA: Carousel'e tabindex ekle (keyboard focus için)
     */
    carouselEl.setAttribute('tabindex', '0');

    /**
     * Initial state
     */
    updateDots();
    updateButtons();
  }

  /**
   * Main: Sayfadaki tüm carousel'leri başlat
   */
  function initAllCarousels() {
    const carousels = document.querySelectorAll('.carousel');
    carousels.forEach(initCarousel);
  }

  /**
   * DOM ready check
   */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAllCarousels);
  } else {
    initAllCarousels();
  }

  /**
   * Dynamic carousel'ler için (AJAX, template, vb.)
   * Globale expose et
   */
  window.CarouselInit = initCarousel;
})();
