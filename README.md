# 📦Sistema de Gestión de Inventarios (Versión Mejorada)
Elaborado por: Pablo Ramón Mosquera

Este programa es una aplicación de consola desarrollada en **Python** que permite gestionar el inventario de una tienda. En esta versión mejorada, el sistema implementa **persistencia de datos** mediante archivos de texto y un **manejo robusto de excepciones** para garantizar que el programa no se detenga ante errores inesperados.

## Características Principales

Además de las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) básicas, esta versión incluye:

* **Almacenamiento en Archivo (`inventario.txt`):** Los productos añadidos, modificados o eliminados se guardan automáticamente en el disco duro. Al iniciar el programa, el inventario se reconstruye leyendo este archivo.
* **Creación Automática:** Si el archivo de inventario no existe al iniciar el sistema, el programa lo crea automáticamente.
* **Manejo de Excepciones:**
  * Control de errores de lectura/escritura (`FileNotFoundError`, `PermissionError`).
  * Validación de entradas de usuario para evitar que el programa falle al ingresar letras en lugar de números (`ValueError`).
  * Notificaciones claras al usuario sobre el éxito o fallo de las operaciones.
* **Búsqueda Flexible:** Permite localizar productos por nombre, incluyendo coincidencias parciales.

## Estructura del Proyecto

El código mantiene una arquitectura modular orientada a objetos.

