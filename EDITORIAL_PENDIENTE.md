# Contenido pendiente de publicación

Documento interno, excluido del sitio y de los PDF. Revisión editorial: 28-10-2026.

Los textos de apertura desde Windows, comprobación del plugin y plantilla, cámaras sanitarias, tabla 3.2, conservación de datos e importación se han integrado en las guías para la entrega 1.0.0-rc.4 solicitada por el usuario. Su historial anterior permanece en Git.

Instalador generado y verificado; ambas guías revisadas en HTML y PDF, con 1.583 referencias locales comprobadas sin errores. Publicación autorizada por el usuario para esa entrega.

## Solicitud de expediente y menú del plugin — pendiente de distribución

Corrección local posterior a RC4. No incorporarla al sitio ni a los PDF hasta distribuir el plugin correspondiente. No publicar por la autorización anterior de RC4.

Apartados revisados y destinos de los textos:

- `plugin/index.qmd`: sustituir la explicación de estados alternativos de Crear/Cancelar.
- `plugin/capitulos/04-expediente.qmd`: preparación, cancelación y comprobación de la exportación.
- `aplicacion/capitulos/05-plugin.qmd`: menú y recorrido de generación del expediente.
- `aplicacion/capitulos/11-resolucion-problemas.qmd`: fila «El expediente queda pendiente».

Texto para el menú y el recorrido de ambas guías:

> Con un modelo abierto, el menú ofrece **Crear expediente DBCTE** y **Cancelar creación del expediente**. Son comandos: su presencia no indica que haya una solicitud pendiente. Al pulsar **Crear expediente DBCTE**, se elige el destino; si ya hay una solicitud pendiente, el plugin muestra su ruta y explica cómo completarla o cancelarla.
>
> Cada solicitud genera un solo expediente. Compruebe el mensaje **Expediente creado correctamente** y la ruta indicada. Para volver a generarlo, prepare una nueva solicitud con **Crear expediente DBCTE** antes de exportar el IDF de simulación. Puede elegir el mismo destino si desea actualizarlo. Cancelar una solicitud no elimina un expediente ya creado; si no hay ninguna pendiente, el plugin lo indica.

Texto de resolución de problemas:

> Si falta el aviso de creación, pulse **Crear expediente DBCTE** para comprobar el estado: si muestra una solicitud pendiente, revise el destino y complete la exportación IDF de **Simulación**; si abre el selector de destino, prepare una nueva solicitud. Compruebe la fecha del archivo antes de utilizarlo. Si la primera exportación de una solicitud sigue sin generar el expediente, conserve la hora del intento y cualquier mensaje de error para comunicar la incidencia.

Comprobación editorial: rutas existentes revisadas y diff comprobado. Los textos están fuera de las fuentes publicadas: no se regeneran HTML ni PDF en esta tarea. Al distribuir, integrar los textos, revisar la captura del menú afectada y regenerar/revisar ambos PDF y HTML. No atribuir la incidencia al tiempo de espera o al cambio de ventana: no se ha demostrado esa causa.
