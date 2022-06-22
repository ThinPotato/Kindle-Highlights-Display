from random import random
import sys
from PIL import Image, ImageDraw, ImageFont
import json
import random
import textwrap
import requests
from io import BytesIO

out = Image.new("RGB", (800, 480), (255, 255, 255))
d = ImageDraw.Draw(out)

vertical_pixels = 10
padding = 16

# Load Book
f = open("books.json")
books = json.load(f)
book = random.choice(books)

# Load Title
title_fnt = ImageFont.truetype("bodoni-72-oldstyle-bold.ttf", 40)
title_text = textwrap.fill(text=book["title"], width=40, max_lines=1)
d.multiline_text(
    (20, vertical_pixels), title_text, font=title_fnt, fill=(65, 56, 57))

# Load subtitle
vertical_pixels = vertical_pixels + padding + 30
subtitle_fnt = ImageFont.truetype("bodoni-72-oldstyle-bold.ttf", 22)
subtitle_text = textwrap.fill(text=book["subtitle"], width=70, max_lines=1)
subtitle_size = d.multiline_textsize(
    text=book["subtitle"], font=subtitle_fnt, spacing=25)
# Load Author
author_fnt = ImageFont.truetype("bodoni-72-oldstyle-book.ttf", 22)
print(subtitle_size[0])
if(subtitle_size[0] < 600):
    author_text = textwrap.fill(text=book["author"], width=70, max_lines=1)
    d.text((subtitle_size[0] + 32, vertical_pixels),
           "By " + author_text, font=author_fnt, fill=(0, 0, 0), align='center', spacing=25)
else:
    author_text = textwrap.fill(text=book["author"], width=30, max_lines=1)
    d.text((subtitle_size[0] - 105, vertical_pixels),
           "By " + author_text, font=author_fnt, fill=(0, 0, 0), align='center', spacing=25)


# load subtitle
d.multiline_text((20, vertical_pixels),
                 subtitle_text, font=subtitle_fnt, fill=(65, 56, 57))

# Load line
shape = [(0, 86), (800, 86)]
d.line(shape, fill="Grey", width=0)

# Load Highlight
fnt = ImageFont.truetype("georgia.ttf", 28)
highlight = random.choice(book['highlights'])
text = textwrap.fill(text="\"" + highlight + "\"", width=40, max_lines=7)

vertical_pixels = 240 + 30
d.multiline_text((273, vertical_pixels),
                 text, font=fnt, fill=(0, 0, 0), align='center', anchor="mm", spacing=25)


# Download and place image
response = requests.get(book["cover"])
img = Image.open(BytesIO(response.content)).convert("L")
out.paste(img, (550, 110))

out.show()
