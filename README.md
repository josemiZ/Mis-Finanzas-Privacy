# Política de privacidad — Mis Finanzas

Sitio estático independiente para publicar la política de privacidad de la aplicación Android **Mis Finanzas** mediante GitHub Pages.

## Características

- HTML y CSS nativos, sin dependencias ni proceso de compilación.
- Diseño responsive con modos claro y oscuro según la preferencia del sistema.
- Navegación por teclado, enlace para saltar al contenido y estilos de foco visibles.
- Metadatos básicos para buscadores y redes sociales.
- Hoja de estilos de impresión integrada.

## Desarrollo local

Puede abrirse `index.html` directamente en un navegador. Para comprobarlo mediante un servidor local:

```sh
python3 -m http.server 8000
```

Después, visita `http://localhost:8000`.

## Fuente y revisión por versión

El proyecto Android **MisFinanzas** es la fuente del texto. El contenido canónico
está en `app/src/main/java/com/mickyonmotion/misfinanzas/privacy/viewmodel/PrivacyPolicyUiState.kt`.
Su herramienta `scripts/sync_privacy_policy.py` genera `docs/privacy-policy/index.html`.
Consulta también `docs/guides/TelemetryPrivacy.md` en ese proyecto. Si hay cambios
sin commit, compara el working tree actual, no solamente la última versión de Git.

En cada versión de Android evalúa los cambios en datos recopilados y sus finalidades,
permisos, SDK, terceros, conservación y eliminación. Actualiza la política **solo si
esos cambios afectan lo que declara**; una versión de código no exige por sí sola una
nueva fecha ni una publicación. Registra el resultado de la revisión en la tarea o PR.

La decisión vigente es mantener Analytics y Crashlytics activos desde el primer inicio
en producción. No inventes un consentimiento, un interruptor ni el periodo configurado
de retención de Analytics. Las configuraciones de consola pendientes deben verificarse
por separado; esta herramienta no accede a Firebase ni a Play.

## Comprobar y sincronizar

Desde este repositorio, con Python 3 y sin instalar dependencias:

```sh
python3 scripts/check_privacy_policy.py /ruta/al/proyecto/Android/docs/privacy-policy/index.html
```

La ruta fuente es un argumento, sin rutas personales incorporadas. El destino por
omisión es el `index.html` de este repositorio, incluso desde otro directorio; puede
indicarse otro mediante `--target /ruta/index.html`. La comprobación es de solo lectura:
compara los títulos y párrafos de las nueve secciones en orden, el resumen y la fecha
visible, y comprueba el atributo `datetime` del sitio. Normaliza espacios, entidades
HTML y la presentación de la numeración. Salidas: **0** coincide, **1** diferencias,
**2** archivo ilegible o estructura no admitida. Si cambia el número o estructura de
secciones, adapta el comprobador y revisa manualmente el contenido.

Cuando existan diferencias justificadas:

1. Revisa primero el texto canónico y su HTML generado en Android, siguiendo su guía
   y sus pruebas de consistencia. No sobrescribas cambios ajenos del working tree.
2. Traslada el texto necesario a este sitio, conservando CSS, diseño, IDs, índice,
   enlaces internos, favicon, contacto y aviso del alojamiento. Revisa también los
   metadatos y los mensajes destacados si el cambio afecta sus afirmaciones.
3. Actualiza juntos la fecha visible y el `datetime` cuando cambie la política.
4. Ejecuta el comprobador, revisa `git diff` y abre el HTML en navegador si lo editaste.
   El comprobador valida texto, no destinos de enlaces, metadatos ni apariencia.

Pruebas del comprobador:

```sh
python3 -m unittest discover -s tests
```

## Publicación existente

Repositorio: https://github.com/josemiZ/Mis-Finanzas-Privacy

Sitio: https://josemiz.github.io/Mis-Finanzas-Privacy/

GitHub Pages publica desde `main`, carpeta raíz. `.nojekyll` conserva el sitio
estático sin compilación. Revisa el diff antes de integrar cambios y, tras publicar
contenido, verifica el acceso HTTPS sin autenticación y la revisión visible en esa
misma URL. No crees otro sitio ni automatices publicaciones por cada cambio Android.
Si el contenido ya coincide, no hagas commits ni pushes vacíos. Las herramientas y
documentación se revisan como cambios independientes del contenido de la política.

## Privacidad del propio sitio

El sitio no incluye JavaScript, formularios, analítica, cookies, fuentes remotas ni recursos de terceros. Incluye enlaces de contacto y a la documentación de privacidad de Firebase. La recopilación de Analytics y Crashlytics descrita corresponde a la aplicación Android, no a esta página web.

## Última comprobación

Las nueve secciones, resumen y fecha del 26 de septiembre de 2026 coinciden con el
HTML y el texto de la aplicación Android revisados el 27 de septiembre de 2026.
La política ya fue publicada mediante `d65acb4`; esta mejora de mantenimiento no
modifica el HTML ni requiere republicarlo.
