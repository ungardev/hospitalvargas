import Lenis from 'lenis';

const lenis = new Lenis({
  duration: 0.8,
  easing: (t: number) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true,
  wheelMultiplier: 1.5,
  touchMultiplier: 2.5,
  infinite: false,
});

function raf(time: number) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}

requestAnimationFrame(raf);

export default lenis;