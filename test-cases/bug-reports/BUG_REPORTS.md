# 🐛 Bug Reports - SauceDemo

Este documento recopila los informes de defectos (Bug Reports) identificados durante la ejecución de las pruebas en la plataforma **SauceDemo**, siguiendo el estándar de documentación profesional (estilo Jira).

---

## 📑 Lista de Defectos Registrados
- [BUG-001: El usuario 'locked_out_user' no puede iniciar sesión (Comportamiento esperado/Test de Bloqueo)](#bug-001-el-usuario-locked_out_user-no-puede-iniciar-sesión)
- [BUG-002: Las imágenes de los productos no cargan correctamente con 'problem_user'](#bug-002-las-imágenes-de-los-productos-no-cargan-correctamente-con-problem_user)
- [BUG-003: Error al intentar completar el apellido en el Checkout con 'problem_user'](#bug-003-error-al-intentar-completar-el-apellido-en-el-checkout-con-problem_user)

---


### BUG-001: El usuario 'locked_out_user' no puede iniciar sesión

* **ID del Bug:** `BUG-001`
* **Título:** Error de bloqueo de cuenta al intentar acceder con credenciales de `locked_out_user`
* **Severidad:** Alta
* **Prioridad:** Alta
* **Componente:** Autenticación / Login
* **Entorno:** Chrome / Windows 11 - Web Application (`https://www.saucedemo.com`)

#### 📝 Descripción
Al intentar iniciar sesión utilizando las credenciales válidas del usuario bloqueado (`locked_out_user`), el sistema impide el acceso mostrando un mensaje de error explícito.

#### 🔄 Pasos para Reproducir
1. Navegar a `https://www.saucedemo.com`.
2. Introducir el usuario: `locked_out_user`.
3. Introducir la contraseña: `secret_sauce`.
4. Hacer clic en el botón **"Login"**.

#### 🎯 Resultado Esperado
El usuario debería recibir un mensaje informativo sobre el estado de su cuenta o ser redirigido a una página de soporte para desbloqueo.

#### ❌ Resultado Actual
Aparece un mensaje de error en rojo: `"Epic sadface: Sorry, this user has been locked out."` y se deniega el acceso a la plataforma.

---

### BUG-002: Las imágenes de los productos no cargan correctamente con 'problem_user'

* **ID del Bug:** `BUG-002`
* **Título:** Imágen genérica (Broken Image) mostrada para todos los artículos en el catálogo al autenticarse como `problem_user`
* **Severidad:** Media
* **Prioridad:** Media
* **Componente:** Catálogo de Productos (`/inventory.html`)
* **Entorno:** Firefox / Windows 11

#### 📝 Descripción
Tras iniciar sesión con la cuenta `problem_user`, todas las imágenes del catálogo de productos muestran el mismo recurso roto/genérico (`sl-404.jpg`), impidiendo la correcta visualización de los artículos.

#### 🔄 Pasos para Reproducir
1. Ir a `https://www.saucedemo.com`.
2. Iniciar sesión con `problem_user` / `secret_sauce`.
3. Observar la lista de productos en `/inventory.html`.

#### 🎯 Resultado Esperado
Cada producto debe mostrar su imagen correspondiente (ej. la mochila debe mostrar la imagen de la mochila).

#### ❌ Resultado Actual
Todos los productos muestran la misma imagen de un perro con gafas (`/static/media/sl-404.jpg`), rompiendo la experiencia visual del catálogo.

---

### BUG-003: Error al intentar completar el apellido en el Checkout con 'problem_user'

* **ID del Bug:** `BUG-003`
* **Título:** Imposibilidad de sobrescribir o ingresar el campo 'Last Name' en el formulario de envío
* **Severidad:** Crítica (Blocker para el flujo de compra)
* **Prioridad:** Alta
* **Componente:** Checkout (`/checkout-step-one.html`)
* **Entorno:** Chrome / Android / Windows 11

#### 📝 Descripción
Durante el proceso de pago con el usuario `problem_user`, el campo de texto "Last Name" borra automáticamente lo ingresado o no permite completar el formulario, impidiendo avanzar al resumen del pedido.

#### 🔄 Pasos para Reproducir
1. Iniciar sesión con `problem_user`.
2. Añadir cualquier producto al carrito e ir a `/cart.html`.
3. Hacer clic en **"Checkout"**.
4. Rellenar "First Name" (`Federico`).
5. Intentar escribir en el campo "Last Name" (`Polo`).
6. Hacer clic en **"Continue"**.

#### 🎯 Resultado Esperado
El sistema debe aceptar el apellido ingresado y permitir avanzar a `/checkout-step-two.html`.

#### ❌ Resultado Actual
Aparece el mensaje de error `"Error: Last Name is required"` debido a que el campo no registra la entrada del usuario.
