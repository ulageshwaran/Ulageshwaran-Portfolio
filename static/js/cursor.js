document.addEventListener('DOMContentLoaded', () => {
    // Check if device is mobile - don't render on mobile
    if (window.matchMedia("(pointer: coarse)").matches) return;

    // Create cursor elements
    const cursor = document.createElement('div');
    const innerDot = document.createElement('div');

    cursor.id = 'custom-cursor';
    innerDot.id = 'cursor-dot';

    cursor.appendChild(innerDot);
    document.body.appendChild(cursor);

    // Initial styles
    Object.assign(cursor.style, {
        position: 'fixed',
        top: '0',
        left: '0',
        width: '24px',
        height: '24px',
        borderRadius: '50%',
        border: '2px solid',
        pointerEvents: 'none',
        zIndex: '9999',
        transform: 'translate(-50%, -50%)',
        mixBlendMode: 'difference',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        transition: 'transform 0.1s ease-out, width 0.1s, height 0.1s' // Removed background/border transition for snappy feel
    });

    Object.assign(innerDot.style, {
        width: '4px',
        height: '4px',
        borderRadius: '50%',
        transition: 'background-color 0.2s'
    });

    // State
    let mouseX = 0;
    let mouseY = 0;
    let cursorX = 0;
    let cursorY = 0;
    let isHovering = false;

    // Spring configuration (Speed increased)
    const lerpFactor = 1;

    // Get color
    const style = getComputedStyle(document.body);
    const red = style.getPropertyValue('--dev-red').trim() || '#dc2626';

    // Apply Static Red Styles
    cursor.style.borderColor = red;
    cursor.style.backgroundColor = 'rgba(220, 38, 38, 0.2)';
    innerDot.style.backgroundColor = red;

    // Update Transform
    function updateTransform() {
        if (isHovering) {
            cursor.style.transform = `translate(${cursorX}px, ${cursorY}px) translate(-50%, -50%) scale(2.5)`;
        } else {
            cursor.style.transform = `translate(${cursorX}px, ${cursorY}px) translate(-50%, -50%) scale(1)`;
        }
    }

    // Animation Loop
    function animate() {
        // Smooth movement (Lerp)
        cursorX += (mouseX - cursorX) * lerpFactor;
        cursorY += (mouseY - cursorY) * lerpFactor;

        updateTransform();
        requestAnimationFrame(animate);
    }

    // Event Listeners
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    // Hover detection
    document.addEventListener('mouseover', (e) => {
        const target = e.target;
        if (
            target.tagName === 'BUTTON' ||
            target.tagName === 'A' ||
            target.closest('button') ||
            target.closest('a') ||
            target.classList.contains('cursor-pointer') ||
            target.classList.contains('project-card') ||
            window.getComputedStyle(target).cursor === 'pointer'
        ) {
            isHovering = true;
        } else {
            isHovering = false;
        }
    });

    // Hide default cursor
    document.documentElement.style.cursor = 'none';
    document.body.style.cursor = 'none';

    // Start loop
    animate();
});
