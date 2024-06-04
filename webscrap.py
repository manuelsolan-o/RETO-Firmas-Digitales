import requests
from bs4 import BeautifulSoup


def find_pdf_links(url):

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    pdf_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.lower().endswith('.pdf'):
            pdf_links.append(href)
    return pdf_links


def find_proposal_links(url):
        
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the links on the page
        links = soup.find_all('a')

        # Retrieve and save only the links with the specified structure in a list
        target_links = [
            link.get('href')
            for link in links
            if link.get('href') is not None and "/monitoreo/iniciativas/lxiii/" in link.get('href')
        ]

    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

    target_links = set(target_links)
    useful_links = set()
    for link in target_links:
        if "https://siguealcongreso.org/monitoreo/iniciativas/lxiii/" in link:
            useful_links.add(link)

    return useful_links


def get_all_pdf_links(proposal_links):

    pdf_links = set()
    for link in proposal_links:
        #print(f"link:{link}")
        pdfs = find_pdf_links(link)
        #print(f"pdf: {pdf_link}")
        for pdf in pdfs:
            pdf_links.add(pdf)

    # Clean pdf links
    cleaned_pdf_links = set()
    for pdf in pdf_links:
        if pdf[-3:] == "pdf":
            cleaned_pdf_links.add(pdf)
    
    return cleaned_pdf_links