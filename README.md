# RETO Firmas Digitales

Autores: [Miguel Peréz](https://www.linkedin.com/in/miguelpergg/), [Leonardo Cumplido](https://www.linkedin.com/in/leonardocumplido21/), [Manuel Solano](https://www.linkedin.com/in/manuelsolan-o/)

## Sistema de Firma Digital para Documentos PDF

Este proyecto se centra en el desarrollo de un sistema de firma digital para documentos PDF. Buscamos proporcionar un sistema que permita a la organización siguealcongreso.org firmar digitalmente sus documentos con la finalidad de que no sean alterados y se pueda verificar que fueron firmados por esta misma organización. Utilizamos técnicas de extracción de PDFs de su sitio web, así como algoritmos de firma digital para garantizar la autenticidad e integridad de los documentos.

## Proceso de Extracción de PDFs

Desarrollamos un script de web scraping para extraer los enlaces de PDFs de su sitio web automáticamente. Esto nos permite recopilar los documentos relevantes para su posterior firma digital. Realiza parsing toda la sección que elegimos y entra a buscar los PDFs.

<div style="text-align: center;">
  <img src="images/mancha_urbana_hermosillo.jpeg" alt="Hermosillo">
</div>

## Proceso de Firma Digital

Implementamos un script que utiliza algoritmos de firma digital, específicamente RSA, para firmar los documentos PDF obtenidos previamente. Esto asegura que los documentos estén autenticados y protegidos contra modificaciones no autorizadas.

## Estado Actual del Proyecto

### Extracción y firma

Hemos completado con éxito la extracción de PDFs relevantes y la firma digital de los mismos.

### Uso práctico 

El sistema cuenta con la capacidad de almacenar y descargar los PDFs firmados para su uso en la página web.
