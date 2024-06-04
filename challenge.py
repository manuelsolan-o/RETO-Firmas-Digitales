import hashlib
import requests
from bs4 import BeautifulSoup
from firmaDigital import *
from webscrap import *



# URL of the webpage
url = "https://siguealcongreso.org/areas/lxiii/"

proposal_links = find_proposal_links(url)
pdf_links = get_all_pdf_links(proposal_links=proposal_links)

public_key, private_key = generate_rsa_keys()

# Firmar todos los PDFs desde las URLs y guardar las firmas
signatures = sign_pdfs_from_urls(pdf_urls=pdf_links, private_key=private_key)
