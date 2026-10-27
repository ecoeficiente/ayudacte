# Puentes exportados por el plugin: actualización preparada

Estado: código preparado localmente en `DesignBuilderCTE`, rama `codex/informes-he-docx`, el 27-10-2026. Todavía no distribuido ni instalado. No publicar esta aclaración como comportamiento de las versiones anteriores.

La aplicación deja de recalcular geométricamente las longitudes de los expedientes antiguos mediante la biblioteca externa Thermal Bridges. Tanto esos expedientes como los actuales utilizan las longitudes y los valores Ψ exportados por el plugin. Se conserva la prioridad de PuentesTermicosV2; si ese bloque está presente pero es inválido, el cálculo se detiene sin utilizar las listas antiguas como alternativa. En terciario se conservan las longitudes y el procedimiento existente de Ψ del edificio de referencia.

## Textos listos para integrar al distribuir la actualización

El parche `puentes-exportados.patch`, relativo a la raíz de este repositorio, prepara los apartados siguientes sin modificar todavía la ayuda publicada:

- Aplicación, `capitulos/07-calculo.qmd`: origen de longitudes y Ψ, coherencia de simulación/HE/XML, ejemplo y necesidad de recálculo.
- Aplicación, `capitulos/11-resolucion-problemas.qmd`: datos ausentes o inválidos y resultados anteriores pendientes de recálculo.
- Plugin, `capitulos/02-puentes.qmd`: revisión de los datos exportados y ausencia de un segundo cálculo de longitudes en la aplicación.

Antes de aplicar, comprobar que los contextos siguen vigentes con `git apply --check pendientes/puentes-exportados.patch`. La nueva sección usa el ancla `sec-puentes-exportados`; no modifica ni retira las anclas existentes.

## Verificación y entrega

Parche comprobado con `git apply --check` y aplicado a una copia temporal: `python scripts/build.py` correcto, 13 páginas de aplicación y 5 de plugin, 1.557 referencias locales comprobadas sin errores. Revisadas las tres páginas modificadas a 1.440 y 390 px sin desbordamientos; inspección visual de las capturas correcta. Evidencias locales en el repositorio de la aplicación: `output/puentes-plugin/help-build.log` y `output/puentes-plugin/help-qa/`.

Las fuentes públicas, la web y los PDF actuales se conservan sin cambios mientras la nueva aplicación no esté entregada. Al coordinar la entrega:

1. Aplicar el parche y ejecutar `python scripts/build.py`.
2. Revisar visualmente las tres páginas afectadas y comprobar enlaces/búsqueda.
3. Regenerar y revisar los PDF de **ambas guías**, conservando los nombres de descarga. `build.py` no genera los PDF.
4. Publicar únicamente cuando se autorice y esté distribuida la nueva aplicación; verificar Actions y las páginas públicas.

No se requieren capturas nuevas: no se añaden controles ni cambia el editor del plugin. El cambio de resultados en expedientes antiguos es intencionado; antes de recalcular deben revisarse sus datos exportados o generarse de nuevo el expediente desde el plugin.
