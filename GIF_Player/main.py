from PIL import Image

image_paths = [
    "image1.jpeg", "image2.jpeg", "image3.jpeg",
    "image4.jpeg", "image5.jpeg", "image6.jpeg"
]
images = [Image.open(path) for path in image_paths]

base_size = images[0].size
images = [img.resize(base_size) for img in images]

images[0].save(
    'animation.gif',
    save_all=True,
    append_images=images[1:],
    optimize=False,
    duration=1000,
    loop=0
)
