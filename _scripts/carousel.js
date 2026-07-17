/*
  Rotating carousel for project cards (and any .carousel with a .carousel-track
  of slides). Slides are the direct .card children of the track, so anything
  rendered into the track — e.g. cards from _data/projects.yaml — auto-populates
  the carousel with no extra wiring.
*/

{
  const INTERVAL = 6000;

  const initCarousel = (carousel) => {
    const track = carousel.querySelector(".carousel-track");
    if (!track) return;

    const slides = [...track.children].filter((el) =>
      el.classList.contains("card")
    );
    if (slides.length === 0) {
      carousel.remove();
      return;
    }

    const prev = carousel.querySelector(".carousel-prev");
    const next = carousel.querySelector(".carousel-next");
    const dotsBox = carousel.querySelector(".carousel-dots");

    // single slide: static, hide controls
    if (slides.length < 2) {
      carousel.dataset.single = "";
      return;
    }

    let index = 0;

    // build dots
    const dots = slides.map((_, i) => {
      const dot = document.createElement("button");
      dot.className = "carousel-dot";
      dot.setAttribute("aria-label", `Go to project ${i + 1}`);
      dot.addEventListener("click", () => {
        go(i);
        restart();
      });
      dotsBox?.append(dot);
      return dot;
    });

    const go = (i) => {
      index = (i + slides.length) % slides.length;
      track.style.transform = `translateX(-${index * 100}%)`;
      dots.forEach((dot, d) =>
        d === index
          ? dot.setAttribute("data-active", "")
          : dot.removeAttribute("data-active")
      );
    };

    prev?.addEventListener("click", () => {
      go(index - 1);
      restart();
    });
    next?.addEventListener("click", () => {
      go(index + 1);
      restart();
    });

    // autoplay, pause on hover
    let timer = null;
    const start = () => {
      timer = window.setInterval(() => go(index + 1), INTERVAL);
    };
    const stop = () => {
      if (timer) window.clearInterval(timer);
      timer = null;
    };
    const restart = () => {
      stop();
      start();
    };

    carousel.addEventListener("mouseenter", stop);
    carousel.addEventListener("mouseleave", start);

    go(0);
    start();
  };

  window.addEventListener("load", () => {
    document.querySelectorAll(".carousel").forEach(initCarousel);
  });
}
