---
jira_key: "NBWEB-108"
aliases: ["NBWEB-108"]
summary: "Carga de imagenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-11 12:39"
updated: "2022-06-27 09:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-108"
---

# NBWEB-108: Carga de imagenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-11 12:39 |
| Actualizado | 2022-06-27 09:13 |
| Etiquetas | ninguna |
| Jira | [NBWEB-108](https://bluinc.atlassian.net/browse/NBWEB-108) |

## Relaciones

- **Padre:** [[NBWEB-104]] API - Pre ingreso de postventa
- **relates to:** [[NBWEB-110]] APP - Maquetado y desarrollo Postventa

## Descripcion

```
POST {{API_URL}}/v1/postventa/image
```

Retorna



```json
{ 
"id":"257638", //id de la imagen en el servidor de imagenes 
"filename":"dbe70dfcf6c29852ccab46901d912e38.png", //nombre de la imagen en el servidor de imagenes 
"url":"http:\/\/static.nb.com.ar\/img\/dbe70dfcf6c29852ccab46901d912e38.png" //ruta completa de la imagen 
}
```

La galería de imagen funciona de la siguiente manera, en 2 partes.

**En la primera se envía la imagen** al servidor al momento de completar el formulario mediante la galeria en la app, similar al siguiente ejemplo.

Con cada imagen que agrego a la galería, debo enviarla al servidor de imágenes, en caso de éxito el mismo me retorna 

```json
{
"id":"257638", //id de la imagen en el servidor de imagenes
"filename":"dbe70dfcf6c29852ccab46901d912e38.png", //nombre de la imagen en el servidor de imagenes
"url":"http:\/\/static.nb.com.ar\/img\/dbe70dfcf6c29852ccab46901d912e38.png" //ruta completa de la imagen
}
```

[adjunto]
**La segunda es marcar esa imagen**, una vez que se envía el resto de la informacion, como permanente.

Una vez procesado el formualrio se deben mandar ademas las imagenes para guardarlas en la tabla

`postsaleInboundImages`

URL_SERVICE_STATIC=[https://static.libreopcion.com/](https://static.libreopcion.com/)

Pedir  por privado un TOKEN_SERVICE_STATIC a  

Según la clase para el siguiente servicio

```php
<?php

final Class StaticService extends BaseService{

    /**
     * Subir archivo al servidor de fotos
     * @param  CURLFile $imagen Objeto imagen listo para enviar por CURL
     * @param  int $temp
     * @return object ReturnServiceDTO
     */
    
    private static function upload($file, int $temp = 0)
    {

        $URL_PATH = 'u?key='.$_ENV['TOKEN_SERVICE_STATIC'];
        
        $ch = curl_init();
        
        curl_setopt($ch, CURLOPT_POSTFIELDS, [
            'imagen' => $file,
            'temp' => $temp,
        ]);

        curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
        curl_setopt($ch, CURLOPT_URL, $_ENV['URL_SERVICE_STATIC'].$URL_PATH);
        
        $response = curl_exec($ch);
        $codeStatus = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        
        if($codeStatus >= 200 AND $codeStatus < 300){
            return new ReturnServiceDTO(
                true,
                $codeStatus,
                json_decode($response)
            );
        } else {
            return new ReturnServiceDTO(
                false,
                $codeStatus,
                json_decode($response)
            );
        }
    }

    /**
     * Envia al servicio un archivo
     * @param  array $file
     * @param  int $temp
     * @return object ReturnServiceDTO
     */

    public static function uploadFile(array $file, int $temp = 0)
    {
        $file = curl_file_create(
            $file['tmp_name'],
            $file['type'],
            basename($file['name'])
        );
        return self::upload($file, $temp);
    }
    
    /**
     * Envia al servicio un archivo obtenido
     * previamente desde su ruta
     * @param  string $route
     * @param  int $temp
     * @return object ReturnServiceDTO
     */

    public static function uploadUrlFile(string $route, int $temp = 0)
    {
        $file = function_exists('curl_file_create')
        ? curl_file_create($route)
        : "@$route;filename=".basename($route);
        return self::upload($file. $temp);
    }

    /**
    * Marca un archivo temporal como permanente
     * @param string $checksum
     */
    
    private static function markPermanentFile(string $checksum)
    {

        $URL_PATH = 't?key='.$_ENV['TOKEN_SERVICE_STATIC'];
        
        $ch = curl_init();
        
        curl_setopt($ch, CURLOPT_POSTFIELDS, urldecode(http_build_query(([
            'imagen' => $checksum
        ]))));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PATCH');
        curl_setopt($ch, CURLOPT_URL, $_ENV['URL_SERVICE_STATIC'].$URL_PATH);
        
        $response = curl_exec($ch);
        $codeStatus = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        
        curl_close($ch);
        
        if($codeStatus >= 200 AND $codeStatus < 300){
            return new ReturnServiceDTO(
                true,
                $codeStatus,
                json_decode($response)
            );
        } else {
            return new ReturnServiceDTO(
                false,
                $codeStatus,
                json_decode($response)
            );
        }
    }
}

```

---

Creacion de la tabla para las imagenes



```sql
USE [NB_WEB]
GO

/****** Object:  Table [dbo].[postsaleInboundImages]    Script Date: 11/04/2022 04:31:35 p.m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[postsaleInboundImages](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[idStatic] [int] NULL,
	[uri] [varchar](150) NULL,
	[postsaleInboundId] [int] NULL,
	[date] [datetime] NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


```
