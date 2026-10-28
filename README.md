# ChilaquiLand Pedidos

App de pedidos para **ChilaquiLand** y **El Burro de Alambre** (Central de Abastos): menú para clientes, seguimiento del pedido en vivo y panel para admins y encargados.

- Se publica gratis con **GitHub Pages**: `https://jlhdelrio-tech.github.io/chilaquiland-app/`
- Los datos viven en **Firebase Firestore** (plan gratuito).
- Sin configurar Firebase, la app abre en **modo demo** (todo se guarda en el mismo celular).

## Roles
- **Admin**: todo (menú y precios, ajustes, equipo, clientes, pedidos). El primer admin se crea en la pantalla *Entrar* la primera vez.
- **Encargado**: ve pedidos, acepta, prepara y despacha; da de alta clientes. Entra con celular + PIN.
- **Cliente**: lo da de alta un admin o encargado con su celular; después entra con ese número y pide.

## Puesta en marcha
1. En Firebase: crear proyecto, **Firestore Database** (modo producción) y **Authentication → Anónimo** habilitado.
2. Pegar la configuración web en `firebase-config.js`.
3. En Firestore → **Reglas**, pegar el contenido de `firestore.rules` y publicar.
4. En GitHub: **Settings → Pages → Deploy from a branch → main / (root)**.
5. Abrir la app, crear el primer admin, y en **Admin** pulsar *Cargar menú* y guardar los ajustes del negocio.

## Archivos
- `index.html`: toda la app.
- `firebase-config.js`: configuración de Firebase.
- `firestore.rules`: reglas de la base de datos.
