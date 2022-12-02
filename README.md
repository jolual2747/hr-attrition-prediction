# hr-attrition-prediction
Aplicación de algoritmos de machine learning en problemas de clasificación

Una gran empresa llamada XYZ emplea, tiene en un momento dado, alrededor de 4000 empleados. Sin embargo, cada año, alrededor del 15% de sus empleados abandonan la empresa y necesitan ser reemplazados por la reserva de talento disponible en el mercado laboral. La gerencia cree que este nivel de deserción (empleados que se van, ya sea por su propia cuenta o porque fueron despedidos) es malo para la empresa.

Como usted es uno de los analistas estrella de la firma, este proyecto le ha sido entregado. El objetivo del estudio es modelar la probabilidad de deserción. Los resultados así obtenidos serán utilizados por la gerencia para comprender qué cambios deben hacer en su lugar de trabajo, para lograr que la mayoría de sus empleados se queden.

## Introducción

Las empresas dependen de múltiples factores para alcanzar sus objetivos de venta de bienes y servicios, entre ellos el capital y la mano de obra empleada en cada área. Se presenta un caso de estudio de *Kaggle: [HR Analytics Case Study*](https://www.kaggle.com/datasets/vjchoudhary7/hr-analytics-case-study)  de una compañía donde cada año, alrededor del 15% de sus empleados renuncian y necesitan ser reemplazados por la reserva de talento disponible en el mercado laboral. Este nivel de deserción es malo para el cumplimiento de objetivos de la empresa puesto que los proyectos de los ex empleados se retrasan, resultando en una pérdida de reputación entre los consumidores. La mayoría de las veces los nuevos empleados tienen que estar capacitados para el trabajo por lo que es crucial mantener índices de rotación bajos.

## Objetivo

Analizar qué factores deben ser enfocados a fin de frenar el desgaste administrativo y saber qué cambios deben hacerse en la compañía para que la mayoría de empleados prefiera permanecer en ella en lugar de desertar. De esa manera poder anticiparse a la salida de un colaborador.


## Pasos para reproducir el proyecto

Se debe correr los siguientes comandos de Linux, el archivo kaggle_download.py descargará y descomprimirá los datasets, y borrará después los archivos .zip, pero se debe crear una carpeta llamada .kaggle donde se debe ubicar la ssh key en un archivo llamado kaggle.json para hacer la petición a la API de Kaggle.

```
git clone <ssh_code>
pip3 install -r requirements.txt -U
sudo apt-get install unzip
python3 kaggle_download.py
```