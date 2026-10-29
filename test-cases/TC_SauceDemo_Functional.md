# 🧪 Casos de Prueba Funcionales - SauceDemo

Este documento contiene los casos de prueba diseñados para la plataforma **SauceDemo**, aplicando las técnicas de diseño de pruebas ISTQB (**Partición de Equivalencia** y **Análisis de Valores Límite**).

---

## 📑 Índice de Módulos
1. [Módulo 1: Autenticación (Login)](#módulo-1-autenticación-login)
2. [Módulo 2: Catálogo y Carrito](#módulo-2-catálogo-y-carrito)
3. [Módulo 3: Formulario de Checkout (Aplicando BVA y EP)](#módulo-3-formulario-de-checkout-aplicando-bva-y-ep)

---

## Módulo 1: Autenticación (Login)

| ID | Título | Precondición | Pasos de Ejecución | Resultado Esperado | Prioridad |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-LOG-001** | Login exitoso con usuario estándar | Navegador en `saucedemo.com` | 1. Ingresar `standard_user`<br>2. Ingresar `secret_sauce`<br>3. Clic en "Login" | Redirección a `/inventory.html` y visualización del catálogo. | Alta |
| **TC-LOG-002** | Login fallido con usuario bloqueado | Navegador en `saucedemo.com` | 1. Ingresar `locked_out_user`<br>2. Ingresar `secret_sauce`<br>3. Clic en "Login" | Mensaje de error: *"Epic sadface: Sorry, this user has been locked out."* | Alta |
| **TC-LOG-003** | Login fallido con credenciales inválidas | Navegador en `saucedemo.com` | 1. Ingresar `invalid_user`<br>2. Ingresar `wrong_password`<br>3. Clic en "Login" | Mensaje de error: *"Epic sadface: Username and password do not match..."* | Media |

---

## Módulo 2: Catálogo y Carrito

| ID | Título | Precondición | Pasos de Ejecución | Resultado Esperado | Prioridad |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-CRT-001** | Añadir producto al carrito | Usuario autenticado en `/inventory.html` | 1. Clic en "Add to cart" en el primer producto | El botón cambia a "Remove" y el contador del carrito muestra `1`. | Alta |
| **TC-CRT-002** | Eliminar producto del carrito | Producto añadido previamente al carrito | 1. Clic en el icono del carrito<br>2. Clic en "Remove" | El producto se elimina de la lista y el contador disminuye/desaparece. | Alta |
| **TC-CRT-003** | Ordenar productos por precio (Ascendente) | Usuario autenticado en `/inventory.html` | 1. Seleccionar el filtro "Price (low to high)" | Los productos se ordenan de menor a mayor precio correctamente. | Media |

---

## Módulo 3: Formulario de Checkout (Aplicando BVA y EP)

> **Técnicas aplicadas:**
> - **EP (Equivalence Partitioning):** Clases válidas (cadenas alfanuméricas) e inválidas (campos vacíos).
> - **BVA (Boundary Value Analysis):** Validación de longitud de código postal/ZIP.

| ID | Título | Precondición | Pasos de Ejecución | Resultado Esperado | Prioridad |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-CHK-001** | Checkout exitoso con datos válidos (EP) | Usuario en `/checkout-step-one.html` con productos en el carrito | 1. Ingresar First Name: `Federico`<br>2. Ingresar Last Name: `Polo`<br>3. Ingresar Zip Code: `28001`<br>4. Clic en "Continue" | Redirección a `/checkout-step-two.html` mostrando el resumen del pedido. | Alta |
| **TC-CHK-002** | Validación de campo First Name vacío (EP) | Usuario en `/checkout-step-one.html` | 1. Dejar First Name vacío<br>2. Ingresar Last Name y Zip<br>3. Clic en "Continue" | Mensaje de error: *"Error: First Name is required"*. | Alta |
| **TC-CHK-003** | Validación de límite de caracteres en Zip Code (BVA) | Usuario en `/checkout-step-one.html` | 1. Ingresar First Name y Last Name válidos<br>2. Ingresar Zip Code con valor límite (ej. 5 dígitos vs 10+ caracteres)<br>3. Clic en "Continue" | El sistema acepta o valida según el formato del país correctamente. | Media |
