# Ayuda de DesignBuilder CTE

Repositorio independiente de documentación para **https://ayudacte.ecoeficiente.es**.

- `/`: portada con acceso a las dos guías.
- `/plugin/`: parámetros, puentes térmicos, calculadora y expediente.
- `/aplicacion/`: manual de usuario, caso práctico, cálculo, informes y revisión.

## Generar y revisar

Requisitos: Quarto **1.10.18**, Python **3.13** y Git. Python solo usa su biblioteca estándar; no requiere instalar paquetes ni disponer del código de DesignBuilder CTE.

```powershell
python scripts/build.py
python -m http.server 8878 --bind 127.0.0.1 --directory _site
```

Abra http://127.0.0.1:8878/ y pruebe ambas guías, su buscador y los PDF. Para comprobar una compilación existente: `python scripts/check.py`.

`_site/` es una salida reemplazable: no edite allí. `_work/` aloja las compilaciones temporales. Ambas carpetas están excluidas de Git. La publicación contiene únicamente el sitio, nunca README, manifiestos ni scripts internos.

## Editar

Edite `aplicacion/` y `plugin/`: los `.qmd` son las fuentes; `assets/` contiene las capturas y `styles/` sus estilos. La portada está en `site/`. Las dos guías mantienen buscadores independientes y enlaces de navegación entre ellas.

No cambie rutas de capítulos ni identificadores de apartados sin conservar los enlaces anteriores: estas URL se usarán desde los botones del plugin y F1 en la aplicación. Esos accesos en el software todavía no están implementados por este repositorio.

Los PDF incluidos son las ediciones verificadas el **27 de octubre de 2026**, copiadas sin modificar. Este flujo genera HTML; **no regenera los PDF**. Cuando cambie contenido, genere y revise también el PDF correspondiente con el proceso editorial original y sustituya el archivo manteniendo su nombre. No publique un PDF antiguo como si reflejara una revisión nueva.

**Este repositorio es la fuente principal de las dos guías**, por decisión del usuario del 27-10-2026. Las fuentes iniciales proceden de `manual-v3` y `manual/plugin` del repositorio de desarrollo. `IMPORTACION.json` conserva sus hashes previos a las adaptaciones web. Las copias antiguas y MANUAL.md se conservan como referencia histórica/auxiliar, sin sincronización paralela ni obligación de incorporar primero allí las novedades.

La copia local inicial está en `C:\Dev\DesignBuilderCTE\output\ayudacte`. Es un repositorio Git independiente, no una salida desechable: no eliminarlo al limpiar `output`. Si se traslada, actualizar las referencias en AGENTS.md del programa y del plugin.

## Procedimiento cuando cambia una función

1. Revisar el cambio de la aplicación o del plugin y localizar su explicación en **ambas guías**. Actualizar directamente los QMD afectados, ejemplos, resolución de problemas y capturas cuando corresponda. Si el cambio es exclusivamente interno y no afecta al usuario, documentar brevemente que no requiere modificar la ayuda.
2. Mantener la ayuda pública acorde con la versión distribuida. Si la función aún no se ha entregado, preparar la actualización y coordinar su publicación con esa entrega; no presentarla como disponible antes de tiempo.
3. Comprobar `git status --short --branch` y el remoto antes de editar. Preservar trabajo ajeno y mantener estables las rutas y anclas utilizadas desde el software.
4. Ejecutar `python scripts/build.py`. Servir `_site` con el comando anterior y revisar las páginas modificadas, imágenes, navegación y búsqueda. Si solo cambian instrucciones internas como README o AGENTS.md, revisar el diff sin regenerar el sitio.
5. Si cambia el contenido, actualizar y revisar también el PDF afectado. El flujo HTML no lo hace; dejar explícito cualquier pendiente y no presentar esa edición como completamente actualizada mientras exista una discrepancia.
6. Revisar el diff y hacer staging únicamente de los archivos propios. Crear un commit de documentación separado del commit de código del otro repositorio:

   ```powershell
   git diff --check
   git add <archivos-modificados>
   git commit -m "Actualizar ayuda sobre la función modificada"
   ```

7. Cuando la sesión autorice publicar, ejecutar `git push origin main`, comprobar GitHub Actions y revisar el resultado en `https://ayudacte.ecoeficiente.es`. No reconfigurar DNS ni el dominio en cada actualización. Si falla, consultar el trabajo que falló; no afirmar que está publicado por el mero hecho de haber subido el commit.
8. Cerrar la tarea indicando apartados actualizados, comprobaciones, PDF, si está local/subido/publicado y cualquier pendiente. Si falta acceso, registrar los apartados concretos a actualizar para continuar sin usar las copias antiguas como sustituto.

## Primera publicación en GitHub Pages

Repositorio creado: `ecoeficiente/ayudacte`. Las fuentes ya están subidas. Los pasos siguientes documentan la configuración inicial; no repetir la creación ni añadir otra vez un remoto existente. Comprobar el estado real de Pages y DNS antes de continuar una configuración pendiente.

1. Crear un repositorio **público vacío**, sin README ni licencia generados. Revisar las fuentes y capturas antes de subirlas; no se incluye código del programa ni material interno de control editorial.
2. Conectar esta copia y subir la rama principal:

   ```powershell
   git remote add origin https://github.com/ecoeficiente/ayudacte.git
   git push -u origin main
   ```

3. En **Settings → Pages → Build and deployment**, seleccionar **GitHub Actions**. En **Custom domain**, introducir `ayudacte.ecoeficiente.es`. El archivo `site/CNAME` documenta el dominio; con un workflow personalizado no sustituye esta configuración de GitHub.
4. Verificar el dominio en las opciones Pages de la cuenta de GitHub mediante el registro TXT que GitHub indique.
5. En el proveedor DNS de `ecoeficiente.es`, crear únicamente el registro del subdominio:

   | Tipo | Nombre | Destino |
   | --- | --- | --- |
   | CNAME | ayudacte | ecoeficiente.github.io |

   El destino presupone que el propietario es **ecoeficiente**. Si cambia la cuenta, usar `<propietario>.github.io`. No incluir el repositorio ni `https://`. No cambiar los registros de la web principal ni del correo.
6. En **Actions → Comprobar y publicar ayuda**, ejecutar **Run workflow** sobre `main` si el primer despliegue falló antes de configurar Pages. Esperar a la validación DNS y al certificado y activar **Enforce HTTPS** cuando esté disponible.
7. Comprobar en el dominio final la portada, las dos guías, capítulos, búsqueda, PDF y una ruta inexistente (404).

La navegación usa rutas desde la raíz del subdominio; el destino definitivo es el dominio personalizado, no la ruta provisional `github.io/ayudacte/`.

## Actualizaciones y recuperación

Cada push a `main` genera y comprueba el sitio antes de publicarlo. Las pull requests solo compilan y comprueban; no despliegan. Si la compilación falla, no se ejecuta el despliegue y se conserva el sitio publicado anterior. Para retirar una actualización, revertir el commit con `git revert` y subir el nuevo commit.

El workflow publica exclusivamente `_site/`, con permisos de escritura de Pages limitados al trabajo de despliegue. No necesita tokens personales ni secretos adicionales.

Referencias: [Quarto y GitHub Pages](https://quarto.org/docs/publishing/github-pages.html), [workflows de Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), [dominio personalizado](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).
