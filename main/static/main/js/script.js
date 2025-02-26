document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.slide');
    const carouselContainer = document.querySelector('.carousel-container');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('nav');
    let currentIndex = 0;
    let interval;

    function updateSlideWidth() {
        return slides[0].clientWidth;
    }

    function showSlide(index) {
        const slideWidth = updateSlideWidth();
        carouselContainer.style.transform = `translateX(-${index * slideWidth}px)`;
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }

    function prevSlide() {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(currentIndex);
    }

    // Botones de navegación manual
    prevButton.addEventListener('click', function() {
        clearInterval(interval);
        prevSlide();
        startAutoPlay();
    });

    nextButton.addEventListener('click', function() {
        clearInterval(interval);
        nextSlide();
        startAutoPlay();
    });

    function startAutoPlay() {
        interval = setInterval(nextSlide, 3000);
    }

    // Actualizar el tamaño de los slides cuando la ventana cambie de tamaño
    window.addEventListener('resize', function() {
        showSlide(currentIndex);
    });

    startAutoPlay();

    // Menú hamburguesa para móviles
    menuToggle.addEventListener('click', function() {
        navMenu.classList.toggle('show');
    });
});
