# project-gabby

En este proyecto hemos querido realizar un Dashboard sobre un archivo CSV el cual contenía información sobre las ventas de videojuegos fisicos (https://www.kaggle.com/datasets/gregorut/videogamesales).

Los datos con los que se ha trabajado están ubicados en **Cloud Storage** mediante la conexión que nos ofrece la librería de Google.

~~~ python
from google.cloud import storage

# autentificacion
storage_client = storage.Client.from_service_account_json('credentials/creds.json')
~~~

Para obtener el fichero de credenciales tenemos que seguir los pasos que aparecen en https://cloud.google.com/docs/authentication/client-libraries .


### Subida de archivo a GCS Bucket

Para subir nuestro archivo hemos usado la función que integra la librería de Google Cloud (el código se encuentra en ` videogames/gcp/storage.py ` y disponemos de un fichero para guardar todas las variables de configuración en `videogames/gcp/config.py `):

~~~ python
from google.cloud import storage


# Añadir un fichero a un bucket de cloud storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )
~~~

### Cargar archivo de GCS a BigQuery

Para guardar los datos en **BigQuery** se puede hacer de diversas maneras, nosotros lo hemos realizado lanzando el siguiente código en BigQuery:

~~~ SQL
CREATE OR REPLACE EXTERNAL TABLE `project-gabby-dev.videogames_data.mytable`
OPTIONS (
  format = 'CSV',
  uris = ['gs://project-gabby-data/*.csv']
)
~~~
Para ello hemos necesitado crear un DataSet en el proyecto y saber el nombre del Bucket donde tenemos guardado el CSV. Una vez que ya disponemos de los datos en BigQuery pasamos a su visualización.

### Visualización en Data Studio

Para su posible explotación y análisis de los datos hemos creado un Dashboard con **Data Studio**. El enlace del DashBoard es el siguiente https://datastudio.google.com/reporting/d525e562-f000-48fc-bdde-570be5ee5a95 (para acceder a él se solicita pedir acceso), sin embargo, en la carpeta ` docs/Dashboard_videojuegos.pdf` disponemos del mismo en formato PDF.

## Siguientes pasos

De cara a seguir trabajando con los datos se van a realizar una serie de funciones con las que obtener los valores más significativos del DataSet y posibles transformaciones que añadan información esencial para el estudio futuro de los datos. La idea es ejecutar dichas funciones en Cloud Functions, y ver si tiene sentido disponer de un evento que cada vez que se actualicen los datos en el bucket se lance la función específica.