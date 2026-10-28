# Contenido pendiente de publicación

Documento interno, excluido del sitio y de los PDF. Revisión editorial: 28-10-2026.

Los siguientes textos estaban incluidos en las guías pese a indicar que sus funciones no se habían distribuido. Se conservan para revisarlos y reincorporarlos únicamente después de confirmar la entrega y validar el comportamiento. Antes de publicarlos, quitar las notas de pruebas y redactar las instrucciones para el usuario final. No se ha confirmado una nueva distribución en esta tarea.

Los avisos RC1 de las portadas se han retirado; su historial permanece en Git. Los accesos a la ayuda y el cálculo de puentes conservan sus instrucciones de uso, sin la nota de entrega de pruebas del 27 de octubre.

## Fuente: `plugin/index.qmd`

::: {.callout-note title="Comprobar el plugin instalado" icon=false}
**Próxima actualización, pendiente de distribución; no incluida en el MSI RC3 ya entregado.** DesignBuilder CTE comprobará al iniciar que el plugin y la plantilla coincidan con los de su instalación. Si avisa de una diferencia, cierre DesignBuilder, pulse **Abrir Configuración** y después **Reparar o reinstalar plugin y plantilla**. Vuelva a abrir DesignBuilder para cargar el plugin actualizado. **Ahora no** permite continuar y posponer la reparación.

La reparación reconocerá las ubicaciones `User Plugins/DesignBuilder CTE` y `User Plugins/DBCTE`: reutiliza la antigua cuando es la única existente y actualiza ambas si ya coexisten. Una copia antigua puede explicar que falten opciones nuevas aunque se haya instalado una versión reciente de la aplicación. Consulte [Instalar el plugin y la plantilla](https://ayudacte.ecoeficiente.es/aplicacion/capitulos/02-instalacion.html#instalar-el-plugin-y-la-plantilla).
:::

## Fuente: `aplicacion/capitulos/02-instalacion.qmd`

::: {.callout-note title="Comprobación al iniciar: próxima actualización" icon=false}
**Pendiente de distribución; no incluida en el MSI RC3 ya entregado.** En cada inicio, DesignBuilder CTE comparará el contenido del plugin y de la plantilla instalados con los archivos incluidos en la aplicación. Si falta alguno, es diferente o no puede leerse, mostrará un aviso con **Abrir Configuración** y **Ahora no**. El aviso aparece antes de abrir un expediente solicitado desde el Explorador. Posponerlo permite continuar y vuelve a comprobarse en el siguiente inicio.

La comprobación y la reparación reconocerán también la ubicación antigua del plugin, `User Plugins/DBCTE`. Si es la única existente, se reutiliza. Si existen copias en `DBCTE` y en `DesignBuilder CTE`, se comprueban y actualizan ambas. No se crean duplicados ni se eliminan respaldos. Por ejemplo, una copia antigua puede ocultar la opción **Tipo de espacio no habitable: Cámara sanitaria** aunque la aplicación se haya actualizado.

Cierre DesignBuilder antes de reparar y vuelva a abrirlo después. Si no puede comprobarse algún recurso, revise el detalle del aviso y los permisos. Si falta el archivo distribuido en la propia aplicación, reinstale DesignBuilder CTE con el paquete oficial. La comprobación de la plantilla no modifica los modelos DSB existentes.
:::

## Fuente: `aplicacion/capitulos/06-aplicacion.qmd`

### Apertura desde el Explorador de Windows {#abrir-desde-windows}

**Próxima actualización, pendiente de distribución y de validación del instalador:** los archivos `.dbcte` mostrarán el icono de DesignBuilder CTE y podrán abrirse con doble clic. Esta apertura corresponde a la aplicación de expedientes, no al programa de modelado DesignBuilder.

Si la aplicación está cerrada, se iniciará y abrirá el expediente. Si ya está abierta, se utilizará la misma ventana, restaurándola si estaba minimizada. Abrir de nuevo el mismo archivo solo activa la ventana; no vuelve a leerlo ni descarta lo que se esté editando.

Al abrir otro proyecto, tanto mediante doble clic como desde **Abrir proyecto**, se ofrecerán tres opciones:

- **Guardar:** elegir el destino y guardar el proyecto actual antes de abrir el siguiente. Si se cancela el guardado o este falla, no se cambia de proyecto.
- **Descartar:** continuar sin guardar las modificaciones del proyecto actual.
- **Cancelar:** conservar el proyecto abierto.

La pregunta se mostrará siempre que haya otro proyecto abierto, aunque no recuerde haberlo modificado. Si hay un cálculo, una apertura u otra operación en curso, espere a que termine y repita el doble clic.

Si Windows abre otra aplicación o muestra un icono diferente, pulse con el botón derecho sobre un `.dbcte`, elija **Abrir con > Elegir otra aplicación**, seleccione **DesignBuilder CTE** y confirme que desea usarla siempre para ese formato. La instalación respeta una elección anterior de aplicación predeterminada. Si el icono no se actualiza, cierre y vuelva a abrir la ventana del Explorador. Esta asociación no afecta a los archivos `.idf`.

## Fuente: `plugin/capitulos/04-expediente.qmd`

### Abrir el expediente creado desde Windows

**Próxima actualización, pendiente de distribución y de validación del instalador:** una vez completada la exportación, podrá abrir el `.dbcte` con doble clic desde el Explorador. El archivo mostrará el icono de DesignBuilder CTE y se abrirá en la aplicación de expedientes. Para recuperar el modelo en DesignBuilder, siga usando **Importar modelo desde DBCTE**, explicado más abajo.

Si DesignBuilder CTE ya tiene otro proyecto abierto, ofrecerá **Guardar**, **Descartar** o **Cancelar**. Cancelar el guardado o un fallo al guardar impide cambiar de proyecto. Si el mismo expediente ya está abierto, solo se activa su ventana. Si hay una operación en curso, espere a que termine y repita la apertura.

Si Windows no lo abre en DesignBuilder CTE, use **Abrir con > Elegir otra aplicación** y selecciónela como aplicación habitual para `.dbcte`. Conserve el expediente exportado y compruebe su estado después de abrirlo; el icono no acredita que el contenido sea válido.

## Fuente: `plugin/capitulos/01-parametros.qmd`

## Cámaras sanitarias {#sec-camaras-sanitarias}

**Preparado para la próxima entrega de pruebas; todavía no distribuido.** En una zona no habitable, seleccione **Tipo de espacio no habitable: Cámara sanitaria**. Mantenga **Pertenencia a la envolvente térmica** conforme al límite térmico definido en el proyecto. La selección de cámara no cambia esa pertenencia ni convierte el espacio en habitable.

| Campo | Nivel | Cómo utilizarlo |
|---|---|---|
| Tipo de espacio no habitable | Zona | General o Cámara sanitaria; General es el valor inicial |
| Profundidad de la cámara (m) | Zona | Auto toma el terreno en Z = 0; introduzca la profundidad real en metros si esa referencia no corresponde al proyecto |
| Método U del suelo sanitario | Superficie de suelo | Automático o Justificada |
| U justificada del suelo sanitario | Superficie de suelo | U equivalente positiva en W/(m²·K), solo para Justificada |
| Método de justificación de U sanitaria | Superficie de suelo | Método contrastado utilizado para obtener esa U |
| Referencia documental de U sanitaria | Superficie de suelo | Documento y apartado que justifican el valor |

No es necesario introducir área, altura, perímetro ni resistencia del forjado: se obtienen de la geometría y de las capas del IDF. El cálculo automático admite suelo y techo horizontales, altura uniforme y contorno reconstruible; los casos restantes requieren U justificada.

En **Auto**, un suelo de cámara en Z = −0,50 m tiene profundidad 0,50 m; a cota cero o superior se considera profundidad cero. Se utilizan cotas globales, después de transformar las coordenadas de zona. **Los bloques de componente de tipo terreno por encima de Z = 0 no se reconocen como una elevación del terreno para esta profundidad.** En esos modelos, compruebe y corrija la profundidad en el plugin, vuelva a exportar y calcular, y revise los resultados y justificaciones de los informes HE/HE1. Si la geometría no permite el cálculo automático, utilice U justificada. No basta con dibujar el bloque de terreno para que el informe incorpore esa corrección.

**Estanqueidad** es la fuente de renovación de aire de la cámara. Los niveles 1–5 corresponden a 0; 0,5; 1; 5 y 10 renovaciones por hora. Los niveles 3–5 declaran aberturas o juntas abiertas y permiten seleccionar el procedimiento de cámara ventilada. No añada otro dato de ventilación para esta comprobación ni confunda Estanqueidad con n50 o con la clase de permeabilidad de ventanas.

Con la cámara fuera de la envolvente, el programa comprueba la U del forjado superior. Para una cámara ventilada de altura ≤ 1 m y profundidad ≤ 0,5 m utiliza la tabla 9 del DA DB-HE/1. Si Rf > 3 m²·K/W, considera Rf = 3 como simplificación conservadora, despreciando el exceso de resistencia sin extrapolar. El DOCX muestra la Rf real y la considerada. B′ < 1 m sigue requiriendo U justificada. Las cámaras más altas o más profundas utilizan la resistencia real y los procedimientos indicados en [el cálculo de cámaras sanitarias](https://ayudacte.ecoeficiente.es/aplicacion/capitulos/07-calculo.html#sec-camaras-sanitarias).

Ejemplo: una cámara de 8 × 8 m y 0,50 m de altura aporta A = 64 m², P = 32 m y B′ = 4 m. Con Estanqueidad 3 se considera 1 renovación/hora. Si la profundidad es 0,50 m y el forjado tiene Rf ≈ 4,28, el cálculo automático adopta Rf = 3 en la tabla 9 y obtiene U = 0,27 W/(m²·K). No reduzca el aislamiento ni altere las capas físicas: la simplificación solo afecta al cálculo reglamentario. Cumplir esta U no acredita por sí solo todo HE1.

Para **Justificada**, complete valor, método y referencia; no se aceptan los textos iniciales «Sin indicar». Guarde los parámetros y el DSB, vuelva a crear el expediente y calcule en DesignBuilder CTE. El DOCX identifica los valores adoptados por el técnico.

## Fuente: `aplicacion/capitulos/07-calculo.qmd`

### Cámaras sanitarias {#sec-camaras-sanitarias}

**Preparado para la próxima entrega de pruebas; todavía no distribuido.** Identifique **Cámara sanitaria** en los parámetros de zona del plugin. Esta selección es independiente de **Pertenencia a la envolvente térmica**:

- Si la cámara está dentro, se comprueban sus cerramientos exteriores y contra el terreno; el forjado hacia la vivienda queda como separación interior.
- Si está fuera, se comprueba la U del suelo sobre la cámara. Esa partición no cuenta para K ni para la superficie de compacidad del procedimiento simplificado.

El programa obtiene del IDF superficie, altura, perímetro expuesto, longitud característica B′ = 2A/P y resistencia de las capas Rf. Admite suelo y techo horizontales, altura uniforme y contorno reconstruible. No suma las aristas de subdivisiones interiores ni agrupa cámaras independientes por compartir cota.

La renovación de aire procede exclusivamente de **Estanqueidad**: los niveles 1, 2, 3, 4 y 5 representan respectivamente 0; 0,5; 1; 5 y 10 renovaciones por hora. Los horarios de ventilación del modelo no sustituyen esta selección. Para el procedimiento de cámara ventilada se utilizan los niveles 3–5; los niveles 1–2 no declaran aberturas de ventilación al exterior.

Con **Profundidad de la cámara (m): Auto**, el programa adopta el terreno en **Z = 0 del modelo**. Calcula la profundidad desde esa cota hasta el suelo de la cámara, después de aplicar las transformaciones de zona del IDF. Un suelo en Z = −0,50 m tiene profundidad 0,50 m; a cota cero o superior se considera profundidad cero.

**Terrenos elevados:** los bloques de componente de tipo terreno dibujados por encima de Z = 0 no elevan esta referencia automática. Si los ha utilizado, revise la profundidad real y el método y resultado de U de la cámara en los informes HE/HE1. Introduzca la profundidad correcta en el plugin, vuelva a exportar y calcular, y regenere el DOCX; si el caso queda fuera del procedimiento automático, documente una U justificada y corrija las justificaciones del informe. El DOCX identifica la referencia de profundidad utilizada.

| Cámara ventilada fuera de la envolvente | Procedimiento |
|---|---|
| Altura ≤ 1 m y profundidad ≤ 0,5 m | Tabla 9 del DA DB-HE/1 |
| Altura > 1 m y profundidad ≤ 0,5 m | Apartado 2.1.1 del DA DB-HE/1 |
| Profundidad > 0,5 m | Balance general del coeficiente b, con renovación obtenida de Estanqueidad |

La tabla 9 se interpola dentro de su dominio. Si la resistencia real del forjado supera 3 m²·K/W, el programa considera Rf = 3 como **simplificación conservadora**: desprecia el exceso de resistencia, sin extrapolar la tabla ni modificar las capas físicas de EnergyPlus. El DOCX muestra la Rf real, la considerada y el motivo. Esta simplificación del programa se aplica exclusivamente a la tabla 9; las ramas de cámara alta y balance general utilizan la resistencia real.

B′ < 1 m sigue requiriendo U justificada; B′ ≥ 36 m utiliza la fila prevista. Por ejemplo, con B′ = 4 m y Rf real = 4,28 se considera Rf = 3 y se obtiene U = 0,27 W/(m²·K). Toda la columna Rf = 3 da valores entre 0,23 y 0,29, inferiores al límite UT más exigente de HE1 (0,59). Esto permite verificar la U de este suelo dentro del dominio del procedimiento; no acredita por sí solo el cumplimiento íntegro de HE1 ni el de los cerramientos exteriores de una cámara incluida en la envolvente.

Si el diagnóstico indica geometría no soportada, falta de aberturas según Estanqueidad o parámetros fuera de tabla, seleccione en la superficie de suelo **Método U del suelo sanitario: Justificada**. Complete una U equivalente positiva, el método contrastado y la referencia del documento justificativo. No se adopta otro método automáticamente. Esta U no sustituye las capas físicas del modelo de EnergyPlus.

El DOCX detalla parámetros, método y procedencia de U. Al cambiar geometría, Estanqueidad, profundidad o justificación, exporte de nuevo, calcule y regenere la documentación. Consulte [los parámetros de cámara en el plugin](https://ayudacte.ecoeficiente.es/plugin/capitulos/01-parametros.html#sec-camaras-sanitarias).

## Fuente: `aplicacion/capitulos/08-documentacion.qmd`

### Tabla 3.2 y verificación del técnico {#sec-tabla32}

**Preparado para la próxima entrega de pruebas; todavía no distribuido.** Los informes HE y HE1 en DOCX incluyen **Limitación de descompensaciones**, con estado **Verificación a cargo del técnico**. Este estado identifica una justificación externa; no significa que la partición cumpla ni que se haya determinado su no aplicabilidad.

Revise las divisorias entre unidades del mismo o distinto uso y entre unidades de uso y zonas comunes. El informe presenta los límites de la tabla 3.2 de HE1 para la zona climática de invierno y una tabla editable para documentar partición, unidades o zonas que separa, aplicabilidad, U, límite y resultado con su justificación. Complete esa tabla o adjunte una justificación identificada. En reformas, revise también qué particiones están afectadas por la intervención.

La aplicación no identifica unidades de uso. La habitabilidad de una zona y su pertenencia a la envolvente no bastan para decidir esta condición. Una partición interior puede necesitar esta comprobación aunque no intervenga en U de envolvente o K. Los campos vacíos no acreditan cumplimiento; el documento requiere completar las verificaciones externas antes de integrarlo en la justificación de HE1.


## Conservación de datos y ámbito HE — pendiente de distribución

Texto preparado para `aplicacion/capitulos/06-aplicacion.qmd`, apartados de importación y ámbito HE:

Al guardar, reabrir o importar los datos del edificio se conservan el alcance completo o parcial, la altitud introducida y la zona climática seleccionada. Una parte del edificio no sustituye la superficie total indicada para HE. La normativa de edificación, la de instalaciones y Otra normativa se recuperan independientemente. Si el origen no contiene una normativa o un registro catastral, el campo queda sin seleccionar: revise y complete esos datos.

Seleccione la actuación, el ámbito representado por el modelo y el uso del edificio. Los informes HE/HE1 recogen expresamente esas selecciones; no hay una casilla adicional de confirmación. Revise su correspondencia con el modelo antes de utilizar los informes. Los datos incompletos y los ámbitos incompatibles con la actuación siguen dando lugar a comprobaciones pendientes.

En expedientes guardados con versiones anteriores puede faltar la altitud personalizada o el alcance parcial. En ese caso se toma la altitud del municipio y aparece Edificio completo. Revise ambos campos y guarde el expediente: los valores que no llegaron a guardarse no pueden recuperarse automáticamente.

Revisión de la guía del plugin: el recorrido de exportación no cambia. La revisión y cumplimentación del ámbito corresponde a la aplicación; no se añade una confirmación en el plugin. Al distribuir, sustituir las instrucciones anteriores de confirmación en la guía de aplicación y regenerar y revisar su HTML y PDF. Esta preparación editorial no cambia las guías ni los PDF publicados.


## Importación y preparación de informes — pendiente de distribución

Añadir al apartado de importación de la guía de aplicación:

Al importar datos de otro expediente o cambiar los datos del edificio, el programa vuelve a preparar el modelo necesario para los informes. Si los cambios afectan a la simulación, deberá calcular de nuevo antes de generar documentación que dependa de sus resultados.

Las imágenes y los planos incorporados a un DBCTE se recuperan desde sus adjuntos, incluso si los datos conservan un nombre anterior o una ruta del equipo de origen. Se mantienen al importar, guardar y volver a abrir el proyecto.

Revisada también la guía del plugin: no cambia la exportación ni se añade ningún paso. Integrar estos textos con la distribución de la corrección; HTML y PDF actuales permanecen sin cambios.
