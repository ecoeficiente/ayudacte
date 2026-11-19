# Contenido pendiente de publicación

## DSB reducido en expedientes — RC8, pendiente de aceptación manual

Fuentes completas preparadas en `editorial/dsb-v2/`: creación y apertura en ambas guías, extracción de DSB, mapa de archivos, revisión, problemas y glosario. Retiran el requisito de bibliotecas XML y explican que CTE conserva el DSB sin modificarlo. Incorporar a las guías al distribuir RC8, después de la aceptación; mantener anclas antiguas y actualizar ambos PDF.


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


## EnergyPlus 23.1/25.1 y recuperación nominal — pendiente de entrega

Aplicación y plugin: al distribuir la adaptación, explicar que Auto toma el menor de las eficacias sensibles nominales de calefacción y refrigeración al 100 %, con la cobertura de ventilación existente. No utiliza el 75 % ni las curvas para la equivalencia de demanda. No garantiza un resultado conservador en todas las condiciones. El usuario puede indicar una efectividad sensible de demanda manual justificada: es el porcentaje final, sin multiplicarlo otra vez por cobertura, y no modifica el recuperador real. Mantener las exclusiones por parada, falta de ventilación y zona no admisible.

Ejemplo: nominales 75/70 %, cobertura 80 %: eficacia automática 56 %. Un manual de 50 % aplica 50 %, no 40 %. En 25.1 el nominal declarado puede diferir del resultado de la curva en el punto 100 %. El edificio objeto conserva sus curvas y controles. Los expedientes 23.1 pueden cambiar respecto al mínimo anterior que también usaba el 75 %: exigir recálculo e indicarlo en las notas de entrega.

Actualizar ambas guías y PDF cuando se entregue; no promover todavía a las fuentes públicas. Soporte completo 25.1, integración EpNet y aceptación del host pendientes. Los PDF publicados permanecen intactos.


Ampliación de la adaptación (04-11-2026), para ambas guías cuando se distribuya: CTE incluye los paquetes 23.1.0.002 y 25.1.0.001 y elige el correspondiente al expediente; también se preparan sus descargas alternativas. Los archivos web aún no se han publicado. No cambiar manualmente la versión escrita en el IDF para convertir un modelo. Las redes de calor por agua y vapor de 25.1 se interpretan como RED1; la red de frío, como RED2, con los factores configurados. Para bombas de calor de planta EIR, un COP explícito se conserva; si está vacío, el valor por defecto es 7,5 en 23.1 y 3,0 en 25.1. Recomendar revisar el valor nominal del equipo. No presentar todavía como completa la aceptación de los modelos exportados por la beta.


Resolución de problemas de aplicación (aplicacion/capitulos/11-resolucion-problemas.qmd): si falta un resultado mensual de una bomba de calor de planta o agua-agua, se detiene la recopilación e indica el equipo y la variable. Volver a simular desde CTE con las solicitudes de resultados actuales; no sustituir una serie ausente por cero. Un equipo simulado con consumo y demanda nulos sigue siendo válido. Para la guía del plugin, remitir a este diagnóstico desde el recorrido de exportación; cambiar parámetros no reconstruye resultados antiguos. Pendiente de distribución, sin cambios en HTML/PDF públicos.


## XML base sin longitudes de puentes — pendiente de entrega

En aplicación/capitulos/11-resolucion-problemas.qmd y plugin/capitulos/02-puentes.qmd: si el XML indica que no hay puentes térmicos con longitud positiva, revisar las longitudes CTE de las zonas interiores de la envolvente. Tener valores Ψ o puentes nativos de DesignBuilder no implica haber cargado esas longitudes en la tabla CTE. En Editar puentes térmicos, seleccionar el ámbito, usar Cargar longitudes de zonas…, revisar la propuesta, Aplicar a la tabla y Guardar. Guardar el DSB, crear un expediente nuevo y recalcular en la aplicación. No introducir longitudes ficticias para superar la validación. Si la vista previa también devuelve ceros, revisar el modelo y los avisos antes de exportar.

La mejora preparada muestra directamente el motivo de validación en el diálogo de generación documental. No publicada ni incluida todavía en el paquete de ensayo ep251.1. Las instrucciones de carga ya existen en la guía actual; ambos PDF públicos permanecen intactos.


## Qsol en edificios con controles y grupos de zonas — pendiente de entrega (19-11-2026)

Para el capítulo de resolución de problemas de la aplicación. Si el registro de Qsol menciona una zona que existe en DesignBuilder junto a un control de CO₂ o humedad, una fuente de CO₂, un equipo eléctrico o una lista de zonas, conserva esos datos en el edificio. Con la versión que incorpore la corrección basta volver a calcular el expediente existente. La aplicación retira esos objetos al preparar el modelo auxiliar de control solar. La exportación desde el plugin sigue el procedimiento habitual.

Si el registro de Qsol señala un control de protección solar móvil que apunta a una ventana fuera de la envolvente térmica, conserva la protección en DesignBuilder y vuelve a calcular con la versión corregida. Qsol aplica el control a los huecos que participan en el cálculo solar.

## Diagnóstico del cierre de simulación y de la copia de resultados — pendiente de entrega (19-11-2026)

Para [Consultar el archivo de registro del expediente](aplicacion/capitulos/11-resolucion-problemas.qmd#sec-log-expediente). Si falla una simulación, busca en el registro el tipo de cálculo y las entradas de cierre de EnergyPlus y de copia de resultados. El cierre muestra el código de salida y el resumen del motor. Si la copia falla, el registro indica el archivo, la ruta de destino y el error de Windows. Conserva estas líneas junto con el mensaje de la aplicación al comunicar la incidencia.

## Regulación por luz natural en residencial — pendiente de entrega

Para [Edificios residenciales](aplicacion/capitulos/04-preparar-designbuilder.qmd) en la guía de la aplicación. Al calcular en residencial, DesignBuilder CTE aplica el perfil residencial de iluminación sin regulación por sensores de luz natural. El edificio objeto y el cálculo de demanda prescinden de los sensores y de sus puntos de referencia. Las reglas de sombra que dependen exclusivamente de esos sensores dan paso al sombreado del procedimiento residencial. Los controles por radiación o por horario siguen siendo aplicables. Puede volver a calcular el expediente existente con la versión corregida.

La exportación desde el plugin sigue el proceso habitual. Incorporar el texto al capítulo de la aplicación y regenerar su PDF cuando se distribuya la corrección.

## Qsol con tablas TAB/HTML — pendiente de entrega (04-11-2026)

Aplicación, resolución de problemas: corregida la recogida de Qsol cuando el IDF de origen solicita tablas TAB o HTML. EnergyPlus podía terminar correctamente y CTE indicar error al no encontrar el CSV esperado. La aplicación prepara ahora la salida CSV para Qsol; basta recalcular con la versión corregida, sin modificar geometría ni parámetros solares. No se convierten resultados antiguos de forma manual.

Plugin, recorrido de exportación: no requiere cambiar el formato de tablas en DesignBuilder para este cálculo con la versión corregida de CTE. No es una modificación del plugin ni de la reducción de bibliotecas. Preparar estas notas para ambas guías al distribuir la corrección; HTML y PDF públicos permanecen sin cambios.

## XML 3.0 — recursos 29/10/2026

Próxima edición en `editorial/xml-20261029/aplicacion/capitulos/`: sustituir los cuatro capítulos homónimos al distribuir la actualización. Incluye NIF de entidad opcional, códigos de inmueble sin asignar, nombres con puntos y revisión de cogeneración. Guía del plugin revisada: sin cambios funcionales derivados de esta actualización. HTML/PDF de vista previa y aceptación integral pendientes; no publicar aún.
