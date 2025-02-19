from PIL import Image

class Canvas:
    def __init__(self, width, height, pixel_size=10, bg_color=(255, 255, 255)):
        """Initialise un canevas pour le pixel art."""
        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.bg_color = bg_color
        self.image = Image.new("RGB", (width * pixel_size, height * pixel_size), bg_color)

    def set_pixel(self, x, y, color):
        """Colorie un pixel aux coordonnées (x, y)."""
        for i in range(self.pixel_size):
            for j in range(self.pixel_size):
                self.image.putpixel((x * self.pixel_size + i, y * self.pixel_size + j), color)

    def save(self, filename):
        """Sauvegarde l'image au format PNG."""
        self.image.save(filename)
