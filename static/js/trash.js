const trashItems = document.querySelectorAll('.trash');

trashItems.forEach(item => {
    // Get full page height dynamically
    const pageHeight = document.documentElement.scrollHeight;

    // Random starting position
    let x = Math.random() * (window.innerWidth - 50);
    let y = Math.random() * (pageHeight - 50);

    // Random velocity
    let vx = (Math.random() * 4) - 2; // horizontal speed
    let vy = (Math.random() * 4) - 2; // vertical speed

    // Random rotation speed (degrees per frame)
    let rotation = Math.random() * 360; // starting rotation
    let rotationSpeed = (Math.random() * 4) - 2; // clockwise or counterclockwise

    // Vertical limits
    const minY = 150;                   // don’t go above 100px from top
    const maxY = pageHeight - 50;       // bottom of scrollable page

    function animate() {
        x += vx;
        y += vy;

        // bounce off edges
        if (x <= 0 || x >= window.innerWidth - 50) vx *= -1;
        if (y <= minY || y >= maxY) vy *= -1;

        // clamp vertical position strictly
        y = Math.max(minY, Math.min(maxY, y));

        // update rotation
        rotation += rotationSpeed;

        // apply transform
        item.style.left = x + 'px';
        item.style.top = y + 'px';
        item.style.transform = `rotate(${rotation}deg)`;

        requestAnimationFrame(animate);
    }

    animate();
});