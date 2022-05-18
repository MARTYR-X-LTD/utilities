# images-to-lazysizes // martyr⁠—

Script to turn Shopify images into [lazysizes](https://github.com/aFarkas/lazysizes) compatible format. I use it for images uploaded in blog articles, pages and random assets around the site.

### Usage

```bash
$ python description_lazy.py file.md > output.html
```

It turns markdown into html as well, but I just use it for images in plain html tags.

Accepts PNG and JPG files. It will automatically get the exact sizes for each picture.

If the attribute `data-zoom` is present, it will make it compatible with [medium-zoom](https://github.com/francoischalifour/medium-zoom), which I use in the site as well.

### Line example in file.md

```html
<img
   data-zoom
   src="https://cdn.shopify.com/s/files/1/0056/3766/8898/files/1-after.jpg?v=1652451658"
   alt=""
/>
```

### Output

With `data-zoom`:

```html
<img
   class="lazyload blur-up"
   width="3840"
   height="1992"
   data-zoomable
   data-src="https://cdn.shopify.com/s/files/1/0056/3766/8898/files/1-after.jpg?v=1652451658"
   src="https://cdn.shopify.com/s/files/1/0056/3766/8898/files/1-after_900x.jpg?v=1652451658"
/>
```

Without `data-zoom`:

```html
<img
   class="lazyload blur-up"
   width="3840"
   height="1992"
   data-widths="[180, 360, 540, 720, 900, 1080, 1260, 1440, 1620, 1800, 1980, 2160, 2340, 2520, 2700, 2880, 3060, 3240, 3420, 3600, 3840]"
   data-src="https://cdn.shopify.com/s/files/1/0056/3766/8898/files/1-after_{width}x.jpg?v=1652451658"
   data-sizes="auto"
/>
```
