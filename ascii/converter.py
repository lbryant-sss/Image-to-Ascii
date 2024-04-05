from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from .models import ImageUpload


ASCII_CHARS = ['#', '@', '%', '?', 'S', '^', ';', '.']

def downscale(my_image):
    smaller_width = 100
    width, height = my_image.size
    ratio = height / width
    smaller_height = int(smaller_width * ratio)
    downscaled_image = my_image.resize((smaller_width, smaller_height))
    return downscaled_image

def greyimage(my_image):
    grey_image = my_image.convert('L')
    return grey_image

def ascii_image(my_image):
    pixels = my_image.getdata()
    chars = ''.join([ASCII_CHARS[pixel // 32] for pixel in pixels])
    return chars

def generate_ascii_art():
    # Getting the last uploaded image
    last_uploaded = ImageUpload.objects.last()
    if last_uploaded:
        image_path = settings.MEDIA_ROOT + last_uploaded.my_image.url[len('/media'):]
        my_image = Image.open(image_path)

        new_image_data = ascii_image(greyimage(downscale(my_image)))
        smaller_width = 100
        pixel_data = len(new_image_data)

        final_image = "\n".join(new_image_data[i:(i+smaller_width)] for i in range(0, pixel_data, smaller_width))
        
        # Creating new image to draw the ASCII art
        font_size = 8
        font = ImageFont.truetype("arial.ttf", font_size)  # Changed font name to "arial.ttf"
        text_width, text_height = font.getsize(final_image.split('\n')[0])
        
        img_width = text_width * smaller_width
        img_height = text_height * (pixel_data // smaller_width)
        ascii_img = Image.new('RGB', (img_width, img_height), color='white')
        d = ImageDraw.Draw(ascii_img)

        # Draw the ASCII image on the new image
        d.text((0, 0), final_image, fill='black', font=font)

        # Saving the ASCII art image
        ascii_img.save(settings.MEDIA_ROOT + '/ascii_images/generated_ascii_art.png')  # Adjusted file path


if __name__ == "__main__":
    generate_ascii_art()