import requests
import shutil
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import multiprocessing.dummy as mp 
from PIL import Image

links_to_process = []
images_to_process = []

def main():
  main_urls = ['https://martyr.shop/collections/all?page=1','https://martyr.shop/collections/all?page=2','https://martyr.shop/collections/all?page=3']
  
  global links_to_process
  global images_to_process

  for main_url in main_urls:
    page = requests.get(main_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find("div", class_="collection-container")
    
    for product_a_tag in products.findAll("a"):
      product_url = formaturlProduct(product_a_tag.get('href'))
      links_to_process.append(product_url)

      # product_title = product_a_tag.find("span", class_="product-card-title").text

      # print(f'########## {product_title}')
  print(len(links_to_process))
  
  p=mp.Pool(10)
  p.map(get_img_urls, links_to_process)
  p.close()
  p.join()

  print(len(images_to_process))

  r=mp.Pool(10)
  r.map(download_image, images_to_process)
  r.close()
  r.join()



def get_img_urls(product_url):
  global images_to_process

  product_page = requests.get(product_url)
  soup_product = BeautifulSoup(product_page.content, 'html.parser')
  images = soup_product.find("div", class_="product-images")
  images_mobile = soup_product.find("div", class_="product-images-mobile")

  for image_link in images.findAll("img"):
    low_res_url = formaturlImage(image_link.get('src'))
    images_to_process.append(low_res_url)
    high_res_url = formaturlImage(image_link.get('data-src'))
    images_to_process.append(high_res_url)
  
  for image_link in images_mobile.findAll("img", class_="only-mobile"):
    mobile_res_url = formaturlImage(image_link.get('data-flickity-lazyload'))
    images_to_process.append(mobile_res_url)



def download_image(url):
  # only 'accept' is important. Just to make sure nothing breaks in the future, I place 'user-agent' as well.
  header_webp = {'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}

  header_png = {'accept': 'image/avif,image/apng,image/svg+xml,image/*,*/*;q=0.8', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}

  try:
    with requests.get(url, headers=header_webp, stream=True) as r:

      if r.status_code == 200:
        file_extension = r.headers['content-type'].split("/")[-1]
        file_name_no_ext = '.'.join(url.split("/")[-1].split(".")[:-1])
        file_name = f'{file_name_no_ext}.{file_extension}'
        
        
        r.raw.decode_content = True
        img = Image.open(r.raw)

        print(f'Processed {file_name_no_ext[0:6]}...{file_extension} // {img.width}x{img.height}')

        # print(f'Saving {file_name}')
        # r.raw.decode_content = True
        # with open(f'./{file_name}', 'wb') as f:
        #   shutil.copyfileobj(r.raw, f)
      else:
        print(r)

  except (requests.exceptions.RequestException, ConnectionError) as e:
    print(e)


def formaturlImage(url):
  return urlparse(url)._replace(scheme='https').geturl()

def formaturlProduct(url):
  return urlparse(url)._replace(scheme='https', netloc='martyr.shop').geturl()

if __name__=='__main__':
    main()

