from generate_favicon import GenerateFavicon
import fire

# Makes CLI for GenerateFavicon 
# Call: python fire_favicon.py convert_png_to_ico test_images\test_image.png

if __name__ == '__main__':
    fire.Fire(GenerateFavicon)
