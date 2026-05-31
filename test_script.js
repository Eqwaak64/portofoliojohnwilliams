
>     <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
>     <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
>     <script>
      document.addEventListener("DOMContentLoaded", () => {
          // Page Intro Transition
          const pageTl = gsap.timeline();
          const hideElements = [".header", ".work-category", ".work-title"];
          const titleEl = document.querySelector(".work-page-title");
          
          if (titleEl) {
              // 1. Hide everything else
              gsap.set(hideElements, { opacity: 0 });
              
              // 2. Split text preserving HTML
              const childNodes = Array.from(titleEl.childNodes);
              titleEl.innerHTML = '';
              childNodes.forEach(node => {
                  if (node.nodeType === 3) {
                      const chars = node.nodeValue.split('');
                      chars.forEach(char => {
                          if (char.trim() === '') {
                              titleEl.appendChild(document.createTextNode(char));
                          } else {
                              const span = document.createElement('span');
                              span.style.display = 'inline-block';
                              span.className = 'title-char';
                              span.textContent = char;
                              titleEl.appendChild(span);
                          }
                      });
                  } else if (node.nodeType === 1) {
                      node.style.display = 'inline-block';
                      node.classList.add('title-char');
                      titleEl.appendChild(node);
                  }
              });
  
              // Preload Bickham Script font to ensure it's available instantly on hover
              const preloadFont = document.createElement('div');
              preloadFont.style.fontFamily = "'Bickham Script Pro', cursive";
              preloadFont.style.position = 'absolute';
              preloadFont.style.opacity = '0';
              preloadFont.style.pointerEvents = 'none';
              preloadFont.textContent = 'preload';
              document.body.appendChild(preloadFont);
  
              // Split .work-title for letter-by-letter hover color fill
              document.querySelectorAll('.work-title').forEach(title => {
                  const titleChildNodes = Array.from(title.childNodes);
                  title.innerHTML = '';
                  titleChildNodes.forEach(node => {
                      if (node.nodeType === 3) {
                          const chars = node.nodeValue.split('');
                          chars.forEach(char => {
                              if (char.trim() === '') {
                                  title.appendChild(document.createTextNode(char));
                              } else {
                                  const span = document.createElement('span');
                                  span.className = 'hover-char';
                                  span.textContent = char;
                                  title.appendChild(span);
                              }
                          });
                      } else if (node.nodeType === 1) {
                          // Wrap the element in hover-char to isolate GSAP transforms
                          const wrapper = document.createElement('span');
                          wrapper.className = 'hover-char';
                          wrapper.style.display = 'inline-block';
                          wrapper.style.transformStyle = 'preserve-3d';
                          
                          node.style.display = 'inline-block';
                          wrapper.appendChild(node);
                          title.appendChild(wrapper);
                      }
                  });
  
                  const chars = title.querySelectorAll('.hover-char');
                  const swashes = title.querySelectorAll('.swash');
  
                  // Apply transition delays for the stagger effect
                  chars.forEach((char, i) => {
                      const delay = `${i * 0.02}s`;
                      char.style.transitionDelay = delay;
                      const swash = char.querySelector('.swash');
                      if (swash) {
                          swash.style.transitionDelay = delay;
                      }
                  });
  
                  title.addEventListener('mouseenter', () => {
                      // Trigger CSS color and font changes
                      title.classList.add('is-hovered');
  
                      // Playful, Acrobatic 3D Jelly Flip!
                      gsap.to(chars, {
                          keyframes: [
                              // 1. Anticipation (Squat & lean back slightly)
                              { y: 6, scaleY: 0.7, scaleX: 1.2, rotationZ: -10, rotationY: -30, duration: 0.1, ease: 
"power1.inOut" },
                              
                              // 2. Explosive Launch (Stretch up & twist aerodynamics)
                              { y: -35, scaleY: 1.4, scaleX: 0.7, rotationZ: 15, rotationY: 90, duration: 0.15, ease: 
"power2.out" },
                              
                              // 3. Hangtime at Apex (Float, slow down, flip mid-air)
                              { y: -45, scaleY: 1, scaleX: 1, rotationZ: 0, rotationY: 180, duration: 0.2, ease: 
"sine.inOut" },
                              
                              // 4. Heavy Impact (Fall fast and squash hard on the floor)
                              { y: 8, scaleY: 0.6, scaleX: 1.4, rotationY: 270, duration: 0.15, ease: "power2.in" },
                              
                              // 5. Elastic Recoil (Spring back to normal jelly wobble)
                              { y: 0, scaleY: 1, scaleX: 1, rotationZ: 0, rotationY: 360, duration: 0.5, ease: 
"elastic.out(1.5, 0.5)" }
                          ],
                          stagger: { 
                              each: 0.035, 
                              from: "start"
                          },
                          overwrite: "auto"
                      });
                  });
  
                  title.addEventListener('mouseleave', () => {
                      // Remove CSS hover state
                      title.classList.remove('is-hovered');
  
                      // Reset Transforms cleanly
                      gsap.to(chars, {
                          y: 0,
                          rotationZ: 0,
                          rotationY: 0,
                          scale: 1,
                          scaleY: 1,
                          scaleX: 1,
                          duration: 0.4,
                          ease: "power2.out",
                          overwrite: "auto"
                      });
                  });
              });
  
              // 3. Set initial center position
              gsap.set(titleEl, { y: "25vh", perspective: 800 });
              
              // 4. Animate characters thrown in and snapping upright
              pageTl.from(".title-char", {
                  duration: 0.9,
                  opacity: 0,
                  scale: 1.5,
                  x: () => gsap.utils.random(-150, 150),
                  y: () => gsap.utils.random(-100, 200),
                  z: () => gsap.utils.random(100, 300),
                  rotationX: () => gsap.utils.random(70, 110),
                  rotationY: () => gsap.utils.random(-45, 45),
                  rotationZ: () => gsap.utils.random(-45, 45),
                  stagger: 0.08,
                  ease: "back.out(2.5)"
              })
              // 5. Move title up to original position
              .to(titleEl, {
                  y: 0, 
                  duration: 1.2, 
                  ease: "power3.inOut"
              }, "+=0.3")
              // 6. Fade in content
              .to(hideElements, {
                  opacity: 1, duration: 1.2, stagger: 0.1, ease: "power2.out"
              }, "-=0.6");
          }
  
          // Hamburger Menu Logic
          const menuToggle = document.getElementById('menu-toggle');
          const menuOverlay = document.querySelector('.menu-overlay');
  
          menuToggle.addEventListener('click', () => {
              menuOverlay.classList.toggle('open');
              document.body.classList.toggle('menu-active');
          });
  
          // News Sidebar Logic
          const newsBtn = document.getElementById('news-btn');
          const newsSidebar = document.getElementById('news-sidebar');
          const newsClose = document.getElementById('news-close');
  
          const newsBtnSvg = newsBtn.querySelector('svg');
          gsap.set(newsBtnSvg, { transformOrigin: "50% 10%" });
          
          const ringBellAnim = () => {
              if (gsap.isTweening(newsBtnSvg)) return;
              gsap.fromTo(newsBtnSvg, 
                  { rotation: 25 }, 
                  { rotation: 0, duration: 1.5, ease: "elastic.out(1.5, 0.2)", clearProps: "rotation" }
              );
          };
          
          newsBtn.addEventListener('mouseenter', ringBellAnim);
  
          newsBtn.addEventListener('click', () => {
              ringBellAnim();
              newsSidebar.classList.add('open');
              document.body.classList.add('news-active');
          });
  
          newsClose.addEventListener('click', () => {
              newsSidebar.classList.remove('open');
              document.body.classList.remove('news-active');
          });
          
          // Work List Interaction
          const titles = document.querySelectorAll('.work-title');
          const bgImg = document.getElementById('work-bg');
          let currentBgAnim;
  
          // Split text into spans for animation while preserving star-wrapper
          titles.forEach(title => {
              let newHtml = '';
              const childNodes = Array.from(title.childNodes);
              childNodes.forEach(node => {
                  if (node.nodeType === 3) { // Text node
                      const chars = node.textContent.split('');
                      chars.forEach(char => {
                          if(char === ' ') {
                              newHtml += '&nbsp;';
                          } else {
                              newHtml += `<span class="char">${char}</span>`;
                          }
                      });
                  } else {
                      newHtml += `<span class="char" style="display:inline-block">${node.outerHTML}</span>`;
                  }
              });
              title.innerHTML = newHtml;
              
              // Interaction
              title.addEventListener('click', () => {
                  if(title.classList.contains('active')) return;
                  
                  // Remove active from all
                  titles.forEach(t => t.classList.remove('active'));
                  // Add active
                  title.classList.add('active');
                  
                  // Change background with slight zoom
                  const newBgSrc = title.getAttribute('data-bg');
                  
                  if(currentBgAnim) currentBgAnim.kill();
                  
                  // Fade out old bg slightly, swap src, fade in and zoom
                  gsap.to(bgImg, {opacity: 0, duration: 0.3, onComplete: () => {
                      bgImg.src = newBgSrc;
                      
                      // Reset scale and animate to zoom slightly
                      gsap.set(bgImg, {scale: 1, opacity: 0});
                      currentBgAnim = gsap.timeline()
                          .to(bgImg, {opacity: 1, duration: 0.8, ease: "power2.out"})
                          .to(bgImg, {scale: 1.05, duration: 6, ease: "sine.out"}, "<");
                  }});
                  
                  // Text animation: stagger letters
                  const chars = title.querySelectorAll('.char');
                  gsap.fromTo(chars, 
                      { opacity: 0, y: 15 },
                      { opacity: 1, y: 0, duration: 0.6, ease: "back.out(1.5)", stagger: 0.03 }
                  );
              });
          });
          
          // Initial setup for the first item
          const activeTitle = document.querySelector('.work-title.active');
          if(activeTitle) {
              bgImg.src = activeTitle.getAttribute('data-bg');
              gsap.set(bgImg, {scale: 1, opacity: 1});
              currentBgAnim = gsap.to(bgImg, {scale: 1.05, duration: 10, ease: "none"});
          }
  
          // Logo hide on scroll (Handles both Native Scroll and Auto-Scroll Transform)
          let logoHidden = false;
          function toggleLogo(hide) {
              if (hide !== logoHidden) {
                  logoHidden = hide;
                  gsap.to('.logo-text', {
                      y: hide ? -20 : 0,
                      opacity: hide ? 0 : 1,
                      duration: 0.3,
                      ease: "power2.inOut",
                      overwrite: "auto"
                  });
              }
          }
  
          document.querySelector('.work-scroll-container').addEventListener('scroll', (e) => {
              if (e.target.scrollTop > 50) {
                  toggleLogo(true);
              } else {
                  toggleLogo(false);
              }
          });
  
          // Auto Scroll "Movie Credits" Logic (GPU Accelerated)
          const scrollContainer = document.querySelector('.work-scroll-container');
          const workList = document.querySelector('.work-list');
          let autoScrollActive = false;
          let inactivityTimer;
          let autoScrollTween;
          const scrollSpeedPixelsPerSecond = 40; // Cinematic speed
  
          function startAutoScroll() {
              if (autoScrollActive) return;
              autoScrollActive = true;
              
              // Calculate how far we can scroll
              const maxScroll = scrollContainer.scrollHeight - scrollContainer.clientHeight;
              const currentScroll = scrollContainer.scrollTop;
              const remainingScroll = maxScroll - currentScroll;
              
              if (remainingScroll <= 1) {
                  autoScrollActive = false;
                  return; // Already at bottom
              }
              
              // Calculate duration based on constant speed
              const duration = remainingScroll / scrollSpeedPixelsPerSecond;
              
              // Use GPU transform for buttery smooth sub-pixel animation
              autoScrollTween = gsap.to(workList, {
                  y: -remainingScroll,
                  duration: duration,
                  ease: "none",
                  onUpdate: () => {
                      if (Math.abs(gsap.getProperty(workList, "y")) + scrollContainer.scrollTop > 50) {
                          toggleLogo(true);
                      }
                  },
                  onComplete: () => {
                      syncScrollAndResetY();
                      autoScrollActive = false;
                  }
              });
          }
  
          function syncScrollAndResetY() {
              if (!workList) return;
              const currentY = gsap.getProperty(workList, "y");
              if (currentY < 0) {
                  // Instantly apply the fake visual scroll to the real physical scroll
                  scrollContainer.scrollTop += Math.abs(currentY);
                  // Reset fake visual scroll
                  gsap.set(workList, { y: 0 });
              }
          }
  
          function stopAutoScroll() {
              if (!autoScrollActive) return;
              autoScrollActive = false;
              
              if (autoScrollTween) {
                  autoScrollTween.kill();
              }
              // Hand over control back to the native browser scrollbar
              syncScrollAndResetY();
          }
  
          function resetInactivityTimer() {
              stopAutoScroll();
              clearTimeout(inactivityTimer);
              inactivityTimer = setTimeout(() => {
                  startAutoScroll();
              }, 10000); // 10 seconds of inactivity
          }
  
          // Start scrolling immediately once the initial page animations finish
          setTimeout(() => {
              startAutoScroll();
          }, 3000); // Wait 3s for intro anims to fully finish
  
          // Listen for INTENTIONAL user activity to pause the scroll
          window.addEventListener('mousedown', resetInactivityTimer);
          window.addEventListener('keydown', resetInactivityTimer);
          window.addEventListener('touchstart', resetInactivityTimer, { passive: true });
          scrollContainer.addEventListener('wheel', resetInactivityTimer, { passive: true });
          scrollContainer.addEventListener('touchmove', resetInactivityTimer, { passive: true });
      });
  </script>
  </body>
  
  </html>


