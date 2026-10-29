# 📋 Software Test Plan - SauceDemo E-Commerce Platform

## 1. Introducción
Este documento define la estrategia, el alcance y la planificación de las pruebas para la plataforma de comercio electrónico **SauceDemo**. 
El objetivo es verificar la calidad del software, identificar defectos funcionales y garantizar una experiencia de usuario fluida durante las operaciones críticas (autenticación, gestión del carrito y checkout).

---

## 2. Alcance de las Pruebas (Scope)

### 2.1 In Scope (Dentro del alcance)
- **Módulo de Autenticación:** Login con diferentes tipos de usuarios (standard, locked-out, problem user, performance glitch user) y Logout.
- **Catálogo de Productos:** Visualización de la lista, ordenación (A-Z, Z-A, Precio ascendente/descendente) y detalle del producto.
- **Gestión del Carrito:** Añadir/eliminar artículos, conteo dinámico en el icono del carrito.
- **Proceso de Checkout:** Formulario de envío, resumen del pedido y confirmación final.
- **Database Consistency (Simulada):** Verificaciones SQL de la integridad de datos de usuarios y pedidos.

### 2.2 Out of Scope (Fuera del alcance)
- Pruebas de rendimiento/carga avanzadas (Load/Stress Testing).
- Pruebas de seguridad y cibernética avanzadas.
- Integración con pasarelas de pago reales (entorno simulado).

---

## 3. Estrategia de Testing & Técnicas Aplicadas
En conformidad con los estándares **ISTQB**, se aplicarán las siguientes técnicas de diseño de pruebas (Black-Box):
- **Equivalence Partitioning (EP):** Para la validación de campos de entrada en el formulario de checkout.
- **Boundary Value Analysis (BVA):** Para verificar el comportamiento de valores límite en campos y límites del carrito.
- **State Transition Testing:** Para verificar los flujos de estado del usuario (No autenticado -> Autenticado -> Checkout completado).

---

## 4. Criterios de Entrada y Salida (Entry & Exit Criteria)

### 4.1 Entry Criteria (Criterios de entrada)
- Entorno de pruebas (`saucedemo.com`) accesible y estable.
- Requisitos del sistema y flujos de usuario documentados.
- Test Plan revisado y aprobado.

### 4.2 Exit Criteria (Criterios de salida)
- 100% de los Test Cases críticos e identificados ejecutados.
- Ningún bug de severidad **Blocker** o **Critical** abierto.
- Reporte de ejecución y documentación completados.

---

## 5. Entorno de Pruebas & Herramientas
- **OS:** Windows 11 / macOS / Android / iOS
- **Navegadores:** Google Chrome, Mozilla Firefox
- **Test Management & Bug Tracking:** Markdown / GitHub Issues (Estilo Jira)
- **Database Testing:** SQL / TablePlus / DBNgin
- **Automation (Opcional):** Python + Selenium / Playwright

---

## 6. Análisis de Riesgos (Risk Analysis)
| Riesgo | Impacto | Mitigación |
| :--- | :--- | :--- |
| Indisponibilidad del sitio web de pruebas | Alto | Utilizar mock data o verificar estado del servidor. |
| Datos incompletos en el checkout | Medio | Aplicar validación rigurosa en los Test Cases con BVA. |
