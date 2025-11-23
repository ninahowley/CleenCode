const fish = document.querySelector('.fish');

let x = 0;                    
let y = 200;  // start somewhere down the page
let speedX = 2;               
let speedY = 0.5;             

function clamp(value, min, max) {
    return Math.max(min, Math.min(max, value));
}

// Helper: get angle but clamp it to [-30, +30] so fish never flips upside down
function getTiltAngle(sx, sy) {
    const angle = Math.atan2(sy, sx) * (180 / Math.PI);
    return clamp(angle, -30, 30);
}

function swim() {
    x += speedX;
    y += speedY;

    const maxX = window.innerWidth - fish.clientWidth;

    // get full scrollable page height
    const pageHeight = document.documentElement.scrollHeight;
    const minY = 150;                  // minimum distance from top
    const maxY = pageHeight - fish.clientHeight; // bottom of page

    // bounce horizontally
    if (x >= maxX || x <= 0) {
        speedX = -speedX;
    }

    // bounce vertically within scrollable page
    if (y <= minY || y >= maxY) {
        speedY = -speedY;
    }

    // random small vertical wiggle
    speedY += (Math.random() - 0.5) * 0.2;
    speedY = clamp(speedY, -1, 1);

    // clamp vertical position
    y = clamp(y, minY, maxY);

    fish.style.left = x + "px";
    fish.style.top = y + "px";

    // rotate only slightly based on movement
    let angle = getTiltAngle(speedX, speedY);

    // flip horizontally if moving left
    const flip = speedX < 0 ? -1 : 1;
    fish.style.transform = `scaleX(${flip}) rotate(${angle}deg)`;

    requestAnimationFrame(swim);
}

// initial orientation
fish.style.transform = "rotate(0deg)";
swim();
