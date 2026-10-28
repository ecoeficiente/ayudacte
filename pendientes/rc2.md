# Corrección 1.0.0-rc.2 — pendiente de distribución
En ambas guías, sustituir el aviso de candidata RC1 por RC2 al entregar la corrección. Añadir en diagnóstico: si RC1 falla al abrir con MissingMethodException para EpNet.IdfReader.AddObject, instalar RC2; no modificar el modelo ni copiar DLL de otras versiones.
La corrección reemplaza una DLL protegida antigua reutilizada por el empaquetador y corrige la resolución del host bajo .NET 8. La comprobación de host y la protección se conservan.
Regenerar/revisar HTML y ambos PDF al integrar esta nota. No se ha publicado esta documentación.
