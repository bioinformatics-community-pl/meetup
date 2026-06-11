from PIL import Image
paths = [
    ('assets/organisers/Agata_Mikołaj.jpg', 'assets/organisers/Agata.jpg', 'assets/organisers/Mikolaj.jpg'),
    ('assets/organisers/Kaja_Zofia.jpg', 'assets/organisers/Kaja.jpg', 'assets/organisers/Zofia.jpg'),
    ('assets/organisers/Amelia_Ewa.jpg', 'assets/organisers/Amelia.jpg', 'assets/organisers/Ewa.jpg')
]
for src, left_out, right_out in paths:
    try:
        img = Image.open(src)
    except Exception as e:
        print(f'ERROR opening {src}: {e}')
        continue
    w, h = img.size
    left = img.crop((0, 0, w//2, h))
    right = img.crop((w//2, 0, w, h))
    left.save(left_out)
    right.save(right_out)
    print(f'Created {left_out} and {right_out}')
