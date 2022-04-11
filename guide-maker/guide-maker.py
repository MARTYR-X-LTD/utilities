from bs4 import BeautifulSoup, Tag
from zipfile import ZipFile
import http.server
import socketserver
import os, sys


if len(sys.argv) > 1:
   html_file_path = sys.argv[1]
else:
   html_file_path = 'index-notion.html'

working_dir = os.path.dirname(os.path.abspath(html_file_path))
html_file = os.path.basename(html_file_path)
# script_dir will be used to get the .zip assets
script_dir = os.path.dirname(__file__)

print(f"Processing {html_file}")

try:
	with open(f"{working_dir}/{html_file}") as fp:
		html = BeautifulSoup(fp, 'html.parser')
except:
	print('No html file to process')
	sys.exit(1)

try:
   with open(f'{working_dir}/title.txt') as fp:
      title = fp.readline()
except:
   title = input("title?\n")
   with open(f'{working_dir}/title.txt', 'w') as fp:
      fp.write(title)

print("Replacing stuff...")

head_new = BeautifulSoup(f"""<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="icon" href="favicon.svg" type="image/svg+xml">
    <title>{title} › martyr⁠—</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="styles.css">
    </head>
    """, 'html.parser')
   

header_new = BeautifulSoup(f"""
    <header>
    	<div class='logo-header'>
    			<a target="_blank" href="https://martyr.shop">
    				<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1959.12 419.94">
    					<path d="M732.14,322.41V62.32H788.7V98.71h2.93c5.12-14.34,14.23-21.2,27-29.33S846,58.43,862.44,58.43c3.43,0,7.44.11,12.09.33A84.6,84.6,0,0,1,885.87,60v51a107.34,107.34,0,0,0-12.27-2.2,126,126,0,0,0-17-1.18q-19.05,0-33.94,7.43a59,59,0,0,0-23.53,20.59,53.39,53.39,0,0,0-8.6,29.89v157Z" />
    					<path d="M0,322.41V62.32H56v37.4h3.49C65.34,85.16,73.57,78.23,86.93,70s30.69-11.1,49.23-11.1q28.36,0,47.68,12.36c12.87,8.24,22.29,14,28.28,28.42H215c6.47-14.11,15.67-20.93,30.37-29.33s33.62-11.45,54-11.45q38.44,0,62.68,22.35T386.34,148V322.41H328V154.27q0-25.72-15-37.42t-36.24-11.69q-25.8,0-40.26,14.74T222,157.66V322.41H164.17V151.23q0-20.83-13.91-33.45T114.2,105.16a54.63,54.63,0,0,0-27.81,7.28,55.77,55.77,0,0,0-20.32,20.24q-7.68,13-7.69,30.06V322.41Z" />
    					<path d="M528.62,328q-26.91,0-48.32-9.08t-33.94-26.66q-12.56-17.59-12.55-43.18,0-22,9.06-36.31a65.31,65.31,0,0,1,24.54-22.7A134.33,134.33,0,0,1,502,177.38,330.12,330.12,0,0,1,541.25,171q25.25-2.7,40.81-4.57c10.36-1.24,17.94-3.22,22.68-5.93s7.14-7,7.14-13V146.3q0-21.17-13.08-32.85t-38.52-11.67q-26.53,0-41.91,10.84c-10.26,7.21-16.54,15.3-20.33,24.33l-56.14-.15c1.66-16.12,13.32-35.41,25.93-48,11.52-11.53,26-18,41.66-22.73a172.43,172.43,0,0,1,50.06-7.1,190.28,190.28,0,0,1,37.34,3.89,114,114,0,0,1,35.94,13.71,76.33,76.33,0,0,1,27,27.52q10.44,17.7,10.44,45.13V322.41H613.54V286.85h-2.2q-5.31,10-16,19.48T568.05,321.9Q551.49,328,528.62,328Zm13.54-42q21.78,0,37.51-8t24.08-21.08a51.36,51.36,0,0,0,8.32-28.11V196.09C610,197.9,606.31,199.53,601,201a167.32,167.32,0,0,1-18.12,3.8q-10.17,1.6-20,2.79t-16.37,2a137.84,137.84,0,0,0-28.19,6.18q-12.63,4.31-20.13,12.37t-7.5,21.08q0,18.1,14.45,27.42T542.16,286Z" />
    					<path d="M1069.52,62.32v42.84H913.4V62.32ZM954.21,0h58.38V245.53q0,13.91,4.58,21a22.85,22.85,0,0,0,11.89,9.65,49.28,49.28,0,0,0,16.12,2.53,67.5,67.5,0,0,0,11.42-.85q5-.84,7.79-1.34l10.25,43.69a121.28,121.28,0,0,1-14,3.54A129.78,129.78,0,0,1,1038,326a108,108,0,0,1-41.74-7.2,68.45,68.45,0,0,1-30.65-23.28Q954,279.74,954.21,255.86Z" />
    					<path d="M1160.52,419.94a134.09,134.09,0,0,1-23.24-1.85,91.82,91.82,0,0,1-16.11-4.06l13.92-43.36a95.63,95.63,0,0,0,26.44,3.31,34,34,0,0,0,20.59-7.62q9-7.22,15.56-23.63l6.39-16.26L1101.59,62.32h62.22L1233,262.47h2.93L1305.1,62.32l62.78.51L1252.77,356.12q-7.89,20.49-20.51,34.79a81.8,81.8,0,0,1-30.37,21.68Q1184.13,419.94,1160.52,419.94Z" />
    					<path d="M1406.07,322.41V62.32h56.57V98.71h2.92c5.13-14.34,14.24-21.2,27-29.33s27.3-10.95,43.77-10.95c3.42,0,7.44.11,12.09.33A84.79,84.79,0,0,1,1559.81,60v51a107.78,107.78,0,0,0-12.27-2.2,126.25,126.25,0,0,0-17-1.18q-19,0-34,7.43a59.13,59.13,0,0,0-23.53,20.59,53.38,53.38,0,0,0-8.59,29.89v157Z" />
    					<path d="M1959.12,153.42v46.07H1559.81V153.42Z" />
    				</svg>
    			</a></div>
    	<div class="page-title">{title}</div>
    </header>
    """, 'html.parser')

script = BeautifulSoup("""
<script>
	function openimg(element) {
		const base64ImageData = element.src

		const contentType = base64ImageData.substr(5, base64ImageData.indexOf(";base64") - 5);
		const byteCharacters = atob(base64ImageData.substr(contentType.length + 13));
		const byteArrays = [];

		for (let offset = 0; offset < byteCharacters.length; offset += 1024) {
			const slice = byteCharacters.slice(offset, offset + 1024);

			const byteNumbers = new Array(slice.length);
			for (let i = 0; i < slice.length; i++) {
				byteNumbers[i] = slice.charCodeAt(i);
			}

			const byteArray = new Uint8Array(byteNumbers);

			byteArrays.push(byteArray);
		}
		const blob = new Blob(byteArrays, { type: contentType });
		const blobUrl = URL.createObjectURL(blob);

		window.open(blobUrl, '_blank');
	}

	[...document.getElementsByClassName("image")].forEach(element => {
		[...element.getElementsByTagName("IMG")].forEach(element => {
			element.onclick = () => { openimg(element) };
		});
	});
</script>
""", 'html.parser')

## deleting links from img tags
for img in html.find_all('img'):
   img.parent.replaceWith(img)


html.head.replaceWith(head_new.head)
html.body.article.header.replaceWith(header_new.header)
html.body.append(script.script)


final_html = str(html).replace('white-space:pre-wrap', 'white-space:pre-line')

print("Saving index.html...")

with open(f'{working_dir}/index.html', 'w') as fp:
    fp.write(final_html)


print("Unziping style.css and favicon.svg...")

with ZipFile(f'{script_dir}/styles-favicon.zip', 'r') as zipObj:
	zipObj.extractall(working_dir)
	print('Done!\n')


PORT = 8000
DIRECTORY = working_dir


class Handler(http.server.SimpleHTTPRequestHandler):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
   print(f"serving at http://localhost:{PORT}")
   try:
      httpd.serve_forever()
   # kill server safely with control+c
   # will stop listen to the port like a ghost process
   except KeyboardInterrupt:
      pass
   print()
   httpd.server_close()