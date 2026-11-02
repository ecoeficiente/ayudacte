# Contenido pendiente de publicación

## Asignación a todos los niveles compatibles — 02-11-2026

Integrado en los apartados «Buscar y asignar a varios destinos» de ambas guías para RC7. HTML y PDF regenerados; comprobar el despliegue tras publicar.

## Integración de la revisión 1.0.0-rc.6 — 02-11-2026

Los textos de los apartados históricos siguientes sobre revisión de campos, aspecto, carga, lotes, búsqueda, zonas agrupadas y entrada única se han integrado en las dos guías para RC6. Las notas originales se conservan como historial de preparación y sus indicaciones de pendiente quedan sustituidas por este estado. HTML y PDF se regeneran y revisan en esta tarea; comprobar el despliegue antes de considerarlos publicados.

## Aspecto de la ventana — 02-11-2026, pendiente de distribución

Por decisión final del usuario, el menú lateral conserva un fondo limpio, sin ilustración decorativa. Se retira la propuesta del edificio con escala A–G, que no debe incorporarse a las capturas de la ayuda. Los botones de minimizar, maximizar/restaurar y cerrar recuperan contraste con la barra del título, también con la ventana inactiva.

Capturas de la interfaz sin ilustración en `C:/Dev/DesignBuilderCTE/output/sidebar-removal-20261102/`: light.png, dark.png, collapsed.png y compact.png. La comprobación anterior de los botones de ventana permanece en `C:/Dev/DesignBuilderCTE/output/shell-appearance/`. No cambia el recorrido de uso. Revisada la guía del plugin: no requiere cambios por esta mejora exclusiva de la ventana de la aplicación. HTML y ambos PDF públicos conservados; renovar las capturas de la guía de la aplicación y su PDF al distribuir, sin publicación en esta tarea.

## Revisión bajo demanda — 01-11-2026, pendiente de distribución

Sustituye las indicaciones anteriores sobre resúmenes automáticos. Destinos: aplicación 06-aplicacion, 08-documentacion y 11-resolucion-problemas; revisar el enlace desde la guía del plugin a la aplicación, sin cambios de funcionamiento del plugin.

Se retiran los apartados «Revisar campos». Los campos permanecen siempre en su posición y mantienen los errores locales al editarlos. Solo al solicitar HE, XML base o reprocesado, con un proyecto abierto y tras comprobar los requisitos previos, aparece Campos pendientes si faltan datos. Cada entrada identifica apartado, campo y error; al pulsarla se abre el campo original. Para errores generales aparece «Abrir apartado». Cerrar no continúa la generación: corrija y vuelva a solicitarla. Calcular y HE1 conservan sus requisitos actuales, sin exigir datos adicionales del certificador.

La revisión visual se reinicia al sustituir el proyecto, quedar sin modelo o importar correctamente el formulario afectado; cancelar o fallar sin sustitución conserva el estado. No se duplican editores.

Capturas locales en output/simplify-qa y pruebas en output/usability-review/simplified-final del repositorio de aplicación. HTML y ambos PDF públicos no modificados; integrar textos y capturas y regenerar al distribuir.


## Carga de la calculadora de puentes — pendiente de distribución

Añadir en `plugin/capitulos/03-calculadora.qmd` y `aplicacion/capitulos/05-plugin.qmd`: al abrir **Calculadora de puentes térmicos**, el aviso **Cargando calculadora de puentes…** muestra una barra animada mientras se preparan los datos del edificio y su conjunto de cálculos. Espere a que aparezca la calculadora; el aviso se retira automáticamente al terminar o antes de mostrar un error. La barra indica actividad, sin porcentaje ni tiempo estimado.

Integrar con la entrega de esta revisión. HTML y ambos PDF pendientes de actualización coordinada; sin publicación en esta tarea.

## Revisión de campos, lotes y búsqueda — 29-10-2026, pendiente de distribución

Cambios locales sin instalar ni publicar. Destinos: aplicación, capítulos 06-aplicacion (formularios), 08-documentacion y 11-resolucion-problemas; plugin, capítulos 01-parametros y 02-puentes; aplicación, capítulo 05-plugin.

Texto para la aplicación: al generar el informe HE o el XML base, y al reprocesar documentación, si faltan datos aparece **Campos pendientes**, con los errores de edificio y certificador juntos. Pulse una entrada para abrir el formulario, seleccionar la sección y enfocar el campo. Corrija los datos y repita la generación. Las referencias catastrales incompatibles remiten al registro y a su lista para revisarlas o eliminarlas. Se mantienen las reglas existentes; los datos del certificador no se exigen adicionalmente al informe HE1.

Texto para ambas guías sobre el plugin: **Aplicar a seleccionados** abre una vista previa con la ruta de cada destino, su valor anterior y si era local o heredado, y el nuevo valor local. Para VEEI también muestra el uso. **Volver** o cerrar la vista previa no aplica el lote y permite ajustar la selección. **Aplicar lote** prepara los cambios; todavía debe pulsar **Guardar** en el editor y guardar el DSB en DesignBuilder.

**Deshacer último lote** revierte solo la última asignación múltiple de la sesión, recuperando valores anteriores o herencia y conservando los demás parámetros editados. Solo hay un nivel de deshacer. Si después del lote se modifica el mismo parámetro en alguno de sus destinos, se avisa y no se revierte nada, para conservar esas ediciones. Cancelar el editor sigue descartando toda la sesión.

Los selectores principales de parámetros y puentes incluyen **Buscar por nombre o ruta**, sin distinguir mayúsculas ni tildes. El contador indica las coincidencias. El destino activo permanece disponible aunque no coincida con la búsqueda; escribir no cambia el elemento editado. Vacíe el filtro para recuperar la lista completa.

Al distribuir: integrar estos textos, añadir las capturas de campos pendientes, vista previa y buscadores, y regenerar/revisar HTML y ambos PDF. El sitio y los PDF públicos permanecen sin cambios. Capturas y pruebas locales: output/usability-review del repositorio de la aplicación.

## Indicador al abrir los editores — 29-10-2026, pendiente de distribución

Destinos: `plugin/capitulos/01-parametros.qmd` (Seleccionar el destino), `plugin/capitulos/02-puentes.qmd` (apertura del editor), `aplicacion/capitulos/05-plugin.qmd` (parámetros y puentes) y `aplicacion/capitulos/11-resolucion-problemas.qmd` (espera al abrir el plugin).

Texto para ambas guías:

Al abrir **Asignar parámetros CTE** o **Editar puentes térmicos**, aparece un aviso con una barra animada mientras se preparan los datos. El mensaje identifica el editor que se está cargando. En modelos complejos la preparación puede tardar; espere a que termine para editar. El aviso se cierra automáticamente al finalizar la preparación. Si esta falla, el aviso se retira y se muestra el error.

La barra indica actividad; no representa un porcentaje ni estima el tiempo restante. No permite cancelar la lectura del modelo. Una vez abierto el editor, siguen disponibles sus acciones habituales de Guardar y Cancelar.

Cambio local sin distribuir. Incorporar estos textos y la captura del aviso al entregar el plugin; regenerar y revisar HTML y ambos PDF entonces. Las guías y los PDF públicos permanecen en la edición distribuida.

## Asignación múltiple de parámetros — pendiente de distribución (29-10-2026)

Destinos: `plugin/capitulos/01-parametros.qmd` y `aplicacion/capitulos/05-plugin.qmd`, apartados de selección y herencia.

El pequeño icono de árbol situado a la derecha del campo permite **Asignar a varios…**: copiar el valor mostrado a otros elementos del mismo nivel del edificio actual. El nombre de la acción aparece al pasar el cursor y el botón también es accesible mediante el teclado. En VEEI está junto al selector, antes de las unidades. Por ejemplo, seleccione un cerramiento, indique su intervención HE y pulse el icono del campo. Marque en el árbol los cerramientos que deban recibir ese valor, aunque pertenezcan a otros bloques o zonas.

El filtro busca por nombre sin distinguir mayúsculas ni tildes. El botón situado a su derecha muestra **Seleccionar todo** si falta algún resultado por marcar, y **Deseleccionar todo** cuando todos los resultados están marcados. Solo afecta a los resultados del filtro y se deshabilita si no hay coincidencias. Al cambiar el filtro se conservan las selecciones anteriores: revise el contador de seleccionados ocultos antes de aplicar. El origen también puede seleccionarse. Las zonas hijas agrupadas no son destinos zonales independientes, pero sus cerramientos y huecos siguen disponibles.

**Aplicar a seleccionados** fija una excepción local del parámetro en los destinos. VEEI copia también el uso elegido. Las excepciones de los descendientes se conservan. Si algún destino resulta incompatible, el mensaje identifica su ruta y no se aplica el lote. **Cancelar** en esta ventana descarta solo la selección; **Guardar** en el editor principal acepta las ediciones pendientes y **Cancelar** las descarta todas. Guarde después el DSB en DesignBuilder.

La función se limita a Asignar parámetros CTE; no afecta al editor de puentes térmicos ni a otros edificios. Pendientes de distribución: integrar el texto, capturar la ventana y regenerar/verificar HTML y ambos PDF. La ayuda pública y los PDF permanecen sin cambios.

Documento interno, excluido del sitio y de los PDF. Revisión editorial: 28-10-2026.

Los textos de apertura desde Windows, comprobación del plugin y plantilla, cámaras sanitarias, tabla 3.2, conservación de datos e importación se integraron y publicaron con la entrega 1.0.0-rc.4. Su historial permanece en Git.

## Solicitud de expediente y menú del plugin — entrega RC5

Integrados en ambas guías los textos sobre los comandos Crear/Cancelar, la consulta del estado real de la solicitud, la confirmación de creación y la necesidad de preparar una nueva solicitud para cada exportación. Incluida la resolución de problemas para versiones anteriores y para la ausencia del aviso de creación. Se han retirado de las páginas las referencias a la captura antigua del menú, conservando los archivos de imagen.

Apartados actualizados:

- `plugin/index.qmd`: comandos del menú.
- `plugin/capitulos/04-expediente.qmd`: preparación, cancelación y comprobación de la exportación.
- `aplicacion/capitulos/05-plugin.qmd`: menú y recorrido de generación del expediente.
- `aplicacion/capitulos/11-resolucion-problemas.qmd`: resolución de incidencias de exportación.

Ambos PDF regenerados y páginas afectadas revisadas visualmente. HTML generado y revisado en navegador; 1.581 referencias locales comprobadas sin errores. Publicación solicitada expresamente por el usuario junto con el instalador 1.0.0-rc.5. No quedan textos de esta corrección pendientes de integrar.

No se atribuye la incidencia al tiempo de espera o al cambio de ventana: no se ha demostrado esa causa. La comprobación manual del nuevo instalador corresponde al usuario.

## Zonas agrupadas — pendiente de distribución (29-10-2026)

Destinos: plugin/capitulos/01-parametros.qmd, 02-puentes.qmd y 04-expediente.qmd; aplicacion/capitulos/05-plugin.qmd y 11-resolucion-problemas.qmd.

Texto para parámetros y expediente:
Las zonas hijas agrupadas no aparecen como zonas independientes en los selectores ni en el expediente. Si abre los parámetros desde una hija, el plugin abre su zona padre e indica el destino. Seleccionar directamente un cerramiento o hueco de la hija permite seguir editando ese elemento con su herencia habitual. Los datos zonales anteriores de las hijas se conservan para una eventual desagrupación.

Texto para puentes:
Cada conjunto agrupado tiene una fila, correspondiente al padre. El volumen y la superficie incluyen las zonas agrupadas; los totales por bloque atribuyen el conjunto al bloque del padre. Tras cambiar las agrupaciones, revise los valores manuales y utilice Cargar longitudes de zonas para actualizar las longitudes. No se suman automáticamente las longitudes manuales antiguas de las hijas. Si la geometría individual no permite estimar la conversión interior del conjunto, se conservan las longitudes nativas con un aviso. Revise su compatibilidad con los valores Ψ utilizados.

No distribuido ni publicado. HTML y ambos PDF permanecen en la edición pública anterior; integrar estos textos y regenerarlos al entregar la corrección.

Ampliación para ambos apartados de herencia: al aplicar Heredar hasta nivel de superficie o hueco, también se retira la excepción de ese parámetro guardada en las zonas hijas de esa rama. Los parámetros exclusivos de zona permanecen intactos. Los cambios se aplican al guardar; cancelar conserva los valores anteriores.


## Entrada única de expediente — 29-10-2026, pendiente de distribución

Preparado para ambas guías; incorporar al distribuir esta revisión, manteniendo las anclas existentes. Actualizar HTML y ambos PDF y revisar páginas/capturas afectadas entonces.

- En plugin/index.qmd y aplicacion/capitulos/05-plugin.qmd, retirar la fila «Cancelar creación del expediente» del menú y denominar la entrada «Crear expediente DBCTE…».
- Sustituir la explicación de ambos comandos en esas páginas por: «Con un modelo abierto, Crear expediente DBCTE… permite elegir el destino. Si ya existe una solicitud pendiente, muestra su ruta y el aviso Pendiente de exportar el IDF. Volver a DesignBuilder, Escape o cerrar la ventana conservan la solicitud; Cancelar creación la retira. Elegir el destino prepara la solicitud: exporta el IDF de simulación para completar el expediente».
- En plugin/capitulos/04-expediente.qmd y aplicacion/capitulos/05-plugin.qmd, explicar la cancelación así: «Abre Crear expediente DBCTE… y pulsa Cancelar creación. La siguiente exportación ya no completará esa solicitud. Puedes volver a Crear expediente DBCTE… para elegir otro destino. Cancelar no borra un expediente ya creado».
- En plugin/capitulos/04-expediente.qmd y aplicacion/capitulos/11-resolucion-problemas.qmd, sustituir la recomendación de actualizar para disponer de ambos comandos por actualizar para disponer de la entrada única que consulta el estado real. Tras terminar, esa misma entrada permite preparar otro expediente.
- Revisar capturas del menú y añadir el diálogo pendiente cuando se distribuya. HTML/PDF públicos conservan el comportamiento de la versión distribuida.
