import hashlib
import requests


# Función para calcular el hash SHA-256 de datos binarios
def hash_data(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return int.from_bytes(sha256.digest(), byteorder='big')


# Función para firmar datos binarios
def sign_data(private_key, data):
    d, n = private_key
    hash_value = hash_data(data)
    signature = pow(hash_value, d, n)
    return signature


# Módulo inverso
def modinv(a, m):
    return pow(a,-1, m)


# Genera las claves RSA
def generate_rsa_keys():
    # Uso de pequeños primos para ejemplo, cambia estos número lio
    p = 104729
    q = 103991
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    d = modinv(e, phi_n)
    return (e, n), (d, n)


def sign_pdfs_from_urls(pdf_urls, private_key):
    signatures = {}
    
    for url in pdf_urls:
        try:
            # Obtener el contenido del PDF desde la URL
            response = requests.get(url)
            response.raise_for_status()  # Lanza un error si la descarga falla
            
            # Obtener datos binarios del PDF
            pdf_data = response.content
            
            # Firmar los datos del PDF
            signature = sign_data(private_key, pdf_data)
            signatures[url] = signature
            
            print(f"PDF obtenido de {url} y firmado.")
        
        except requests.RequestException as e:
            print(f"Error al obtener {url}: {str(e)}")
        except Exception as e:
            print(f"Error al firmar {url}: {str(e)}")
    
    return signatures

