from sys import argv
import re
import markdown
import widths

if(len(argv) == 1):
    print("need file as first argument 😴")
    exit()

with open(argv[1], 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

img_tag = re.compile(".*<img [^>]*src=\"([^\"]+)\"")

img_classes = "lazyload blur-up"
img_attributes = "data-zoomable"

for line in (html.split("\n")):
    if(img_tag.match(line)):

        src = img_tag.search(line).group(1)
        # src_lazysizes = src.replace("_480x480.", "_{width}x.")
        src_original = src.replace("_480x480.", ".")
        src_lazysizes = src_original.replace(".png", "_{width}x.png").replace(".jpg", "_{width}x.jpg")
        src_4140 = src.replace("_480x480.", "_4140x.")
        src_900 = src_original.replace(".png", "_900x.png").replace(".jpg", "_900x.jpg")

        filesize, (width, height) = widths.getsizes(src_original)

        max_width = width if width <= 4140 else 4140
        max_height =  int(max_width * height / width)
    
        if "data-zoom" in line:
            
            line = f"<img class='{img_classes}' width='{max_width}' height='{max_height}' {img_attributes} data-src='{src_original}' src='{src_900}'>"

        else:
            itterations = -(-max_width // 180)
            data_widths = []

            # itterations - 1 to append max_width later, giving the full resolution picture at the end
            for i in range(1, itterations-1):
                data_widths.append(str(180 * i))

            data_widths.append(str(max_width))

            data_widths = ", ".join(data_widths)
            line = f"<img class='{img_classes}' width='{max_width}' height='{max_height}' data-widths='[{data_widths}]' data-src='{src_lazysizes}' data-sizes='auto'>"

    print(line)
