const fish = document.querySelector('.fish'); // GET SINGLE ELEMENT

let x = 0;
let speed = 2;

function swim() {
    x += speed;

    const maxX = window.innerWidth - fish.clientWidth;

    if (x >= maxX) {
        speed = -Math.abs(speed);
        fish.style.transform = "scaleX(-1)";
    }

    if (x <= 0) {
        speed = Math.abs(speed);
        fish.style.transform = "scaleX(1)";
    }

    fish.style.left = x + "px";
    requestAnimationFrame(swim);
}

swim();
