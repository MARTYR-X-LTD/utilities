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
