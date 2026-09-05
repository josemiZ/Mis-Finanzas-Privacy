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

## Publicación en GitHub Pages

1. Crea un repositorio vacío en GitHub.
2. Inicializa Git en este directorio, añade la URL SSH del repositorio y sube el contenido a la rama `main`.
3. En GitHub, abre **Settings → Pages**.
4. En **Build and deployment**, selecciona **Deploy from a branch**.
5. Elige la rama `main`, la carpeta `/ (root)` y guarda los cambios.

El archivo `.nojekyll` indica a GitHub Pages que debe servir el contenido tal como está.

## Mantenimiento del contenido legal

La fecha visible y el atributo `datetime` del elemento `<time>` deben actualizarse juntos cuando cambie la política. Cualquier modificación legal debe revisarse también en la versión incluida dentro de la aplicación.

## Privacidad del propio sitio

El sitio no incluye JavaScript, formularios, analítica, cookies, fuentes remotas ni recursos de terceros. El único enlace externo funcional es el contacto mediante correo electrónico.
