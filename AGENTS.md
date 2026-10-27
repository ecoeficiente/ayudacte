# Mantenimiento de la ayuda de DesignBuilder CTE

Este repositorio, https://github.com/ecoeficiente/ayudacte, es la **fuente principal de las dos guías**, por decisión del usuario del 27-10-2026. Leer también README.md.

- `aplicacion/`: guía del programa. `plugin/`: guía del plugin. `site/`: portada común. Editar fuentes QMD, capturas y estilos; no salidas `_site/` ni compilaciones temporales `_work/`.
- Las copias `manual/`, `manual-v3/`, `manual/plugin/` y MANUAL.md del repositorio del programa son históricas/auxiliares. No sincronizarlas ni usarlas como entrada obligatoria para las novedades. IMPORTACION.json es evidencia histórica; no regenerarlo para ocultar cambios posteriores.
- Cada cambio funcional del programa o del plugin requiere revisar ambas guías y actualizar en la misma tarea los apartados afectados, ejemplos, solución de problemas y capturas pertinentes. No añadir detalles internos sin utilidad para el usuario. Si no hay impacto documental, indicarlo brevemente.
- La ayuda pública debe corresponder a las funciones distribuidas. No presentar como disponible un cambio aún no entregado; preparar la documentación y coordinar su publicación con la versión del software. No inventar números de versión.
- Conservar rutas de capítulos y anclas enlazadas desde el software. Si es imprescindible cambiarlas, conservar destinos compatibles y comprobar los enlaces anteriores.
- Antes de editar, comprobar remoto, rama, estado Git e instrucciones aplicables; preservar trabajo ajeno. Ejecutar `python scripts/build.py` y revisar visualmente las páginas modificadas, navegación y búsqueda. Para cambios exclusivamente internos de Markdown que no afecten al sitio, basta revisar el diff y los enlaces/rutas documentados; no es necesario regenerar las guías.
- El flujo genera HTML, no PDF. Cuando cambie contenido, actualizar y revisar también el PDF correspondiente, manteniendo el nombre de descarga. No publicar silenciosamente un PDF desactualizado; registrar y resolver cualquier pendiente antes de presentar la edición completa como actualizada.
- Hacer staging explícito y commits coherentes. No subir sin autorización de la sesión. Un push a main ejecuta la comprobación y publicación de Pages; las PR solo comprueban. Verificar Actions y el sitio antes de afirmar que se publicó. Dominio y DNS son configuración inicial, no pasos de cada actualización.
- Al terminar, resumir guías/apartados cambiados, comprobaciones, estado de PDF y publicación y pendientes. Si falta acceso o validación, dejar una continuidad concreta. No modificar credenciales globales ni registrar secretos para resolver autenticación.

La copia inicial se encuentra en `C:\Dev\DesignBuilderCTE\output\ayudacte`: es un repositorio independiente, **no una salida desechable**. No eliminarlo al limpiar output. Si se traslada, actualizar las referencias operativas en las instrucciones del programa y del plugin.
