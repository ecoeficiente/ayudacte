# Contenido pendiente de publicación

## Indicador al abrir los editores — 29-10-2026, pendiente de distribución

Destinos: `plugin/capitulos/01-parametros.qmd` (Seleccionar el destino), `plugin/capitulos/02-puentes.qmd` (apertura del editor), `aplicacion/capitulos/05-plugin.qmd` (parámetros y puentes) y `aplicacion/capitulos/11-resolucion-problemas.qmd` (espera al abrir el plugin).

Texto para ambas guías:

Al abrir **Asignar parámetros CTE** o **Editar puentes térmicos**, aparece un aviso con una barra animada mientras se preparan los datos. El mensaje identifica el editor que se está cargando. En modelos complejos la preparación puede tardar; espere a que termine para editar. El aviso se cierra automáticamente al finalizar la preparación. Si esta falla, el aviso se retira y se muestra el error.

La barra indica actividad; no representa un porcentaje ni estima el tiempo restante. No permite cancelar la lectura del modelo. Una vez abierto el editor, siguen disponibles sus acciones habituales de Guardar y Cancelar.

Cambio local sin distribuir. Incorporar estos textos y la captura del aviso al entregar el plugin; regenerar y revisar HTML y ambos PDF entonces. Las guías y los PDF públicos permanecen en la edición distribuida.

## Asignación múltiple de parámetros — pendiente de distribución (29-10-2026)

Destinos: `plugin/capitulos/01-parametros.qmd` y `aplicacion/capitulos/05-plugin.qmd`, apartados de selección y herencia.

Junto a cada parámetro, **Asignar a varios…** permite copiar el valor mostrado a otros elementos del mismo nivel del edificio actual. Por ejemplo, seleccione un cerramiento, indique su intervención HE y pulse el botón del campo. Marque en el árbol los cerramientos que deban recibir ese valor, aunque pertenezcan a otros bloques o zonas.

El filtro busca por nombre sin distinguir mayúsculas ni tildes. **Seleccionar todo** y **Deseleccionar todo** afectan a los resultados del filtro. Al cambiarlo se conservan las selecciones anteriores: revise el contador de seleccionados ocultos antes de aplicar. El origen también puede seleccionarse. Las zonas hijas agrupadas no son destinos zonales independientes, pero sus cerramientos y huecos siguen disponibles.

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
