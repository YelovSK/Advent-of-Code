from PIL import Image

def count_stuff(image: Image):
    pixels = image.load()
    pixelshit = image.convert("RGB")
    width, height = image.size

    count = 0
    for i in range(height):
        for j in range(width):
            p = pixelshit.getpixel((j, i))
            all_surr_black = True
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == dy == 0:
                        continue
                    x = j + dx
                    y = i + dy
                    if x < 0 or y < 0 or x >= width or y >= height:
                        continue

                    try:
                        pp = pixelshit.getpixel((x, y))
                        if pp != (0, 0, 0):
                            all_surr_black = False
                            break
                    except IndexError:
                        pass
            if p == (100, 100, 100) and all_surr_black:
                count += 1

    return count

image1 = Image.open("2023/10/output_filled.png")
print(count_stuff(image1))
