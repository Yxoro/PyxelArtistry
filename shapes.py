def draw_rectangle(canvas, x, y, width, height, color):
    """Dessine un rectangle plein."""
    for i in range(x, x + width):
        for j in range(y, y + height):
            canvas.set_pixel(i, j, color)
