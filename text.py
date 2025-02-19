from PIL import ImageDraw, ImageFont

def draw_text(canvas, x, y, text, color, font_size=10):
    """Dessine du texte pixelisé."""
    draw = ImageDraw.Draw(canvas.image)
    font = ImageFont.load_default()
    draw.text((x * canvas.pixel_size, y * canvas.pixel_size), text, fill=color, font=font)
