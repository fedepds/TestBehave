# 🎭 Proyecto de Pruebas Automatizadas con Behave y Playwright

Este proyecto contiene pruebas automatizadas end-to-end utilizando **Behave** (BDD) y **Playwright** para automatización de navegadores.

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Ejecución de Tests](#ejecución-de-tests)


## 📝 Descripción

Este proyecto incluye dos suites de pruebas principales:

1. **Operación Grinch**: Validación de información de películas en IMDB
2. **Login**: Pruebas de autenticación en SauceDemo

Las pruebas están escritas en formato Gherkin (BDD) utilizando Behave y automatizadas con Playwright.

## 🔧 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8 o superior**: [Descargar Python](https://www.python.org/downloads/)
- **pip**: Gestor de paquetes de Python (incluido con Python)
- **Git**: Para clonar el repositorio (opcional)

Verifica las instalaciones:

```bash
python --version
pip --version
```

## 📥 Instalación

### 1. Clonar o descargar el proyecto

**Opción A: Clonar con Git**
```bash
git clone <URL_DEL_REPOSITORIO>
cd PruebasBehave
```

**Opción B: Descargar ZIP**
- Descarga el proyecto como ZIP
- Extrae el contenido
- Abre la terminal en la carpeta del proyecto

### 2. Crear un entorno virtual (recomendado)

**En macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**En Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Instalar los navegadores de Playwright

```bash
playwright install
```

Este comando descargará los navegadores necesarios (Chromium, Firefox, WebKit).

## 📁 Estructura del Proyecto

```
PruebasBehave/
├── features/                       # Archivos de features (Gherkin)
│   ├── environment.py             # Hooks de Behave (before/after)
│   ├── login.feature              # Tests de login
│   ├── operacion_grinch.feature   # Tests de validación IMDB
│   └── steps/                     # Implementación de los steps
│       ├── login_steps.py
│       └── grinch_steps.py
├── pages/                         # Page Object Model
│   ├── base_page.py              # Clase base para páginas
│   ├── login_page.py             # Página de login
│   ├── inventory_page.py         # Página de inventario
│   └── imdb_page.py              # Página de IMDB
├── reports/                       # Reportes generados
│   └── screenshots/              # Capturas de pantalla 
├── behave.ini                     # Configuración de Behave
├── requirements.txt               # Dependencias del proyecto
└── README.md                      # Este archivo
```

## 🚀 Ejecución de Tests

### Ejecutar todos los tests

```bash
behave
```

### Ejecutar un feature específico

**Test de Operación Grinch:**
```bash
behave features/operacion_grinch.feature
```

**Test de Login:**
```bash
behave features/login.feature
```


### Opciones adicionales de ejecución

**Modo verboso:**
```bash
behave -v
```

**Ejecutar escenarios específicos por tags:**
```bash
behave --tags=@smoke
```

**Mostrar outputs en consola:**
```bash
behave --no-capture
```

## 🧪 Tests Disponibles

### 1. Operación Grinch (operacion_grinch.feature)

**Objetivo**: Validar información de la película "Mi Pobre Angelito" en IMDB

**Pasos del test:**
1. Navega a IMDB (https://www.imdb.com)
2. Busca "mi pobre angelito"
3. Hace clic en la primera película de los resultados
4. Valida que el director sea "Chris Columbus"
5. Valida que la calificación sea mayor a 7.0

**Ejecución:**
```bash
behave features/operacion_grinch.feature
```

**Escenario Gherkin:**
```gherkin
Feature: Operacion Grinch

  Scenario: Validar Mi pobre angelito
    Given usuario ingresa a "https://www.imdb.com"
    When usuario llena "search_input" campo con "mi pobre angelito"
    And usuario clica en "search_button"
    And usuario clica en primera pelicula de la lista
    Then director debe ser "Chris Columbus"
    And calificacion debe ser mayor a "7.0"
```

### 2. Login SauceDemo (login.feature)

**Objetivo**: Validar el proceso de login en SauceDemo

**Pasos del test:**
1. Navega a la página de login de SauceDemo
2. Ingresa credenciales válidas (standard_user/secret_sauce)
3. Valida redirección a la página de inventario

**Ejecución:**
```bash
behave features/login.feature
```

**Escenario Gherkin:**
```gherkin
Feature: Login to SauceDemo

  Scenario: Successful login
    Given the user is on the SauceDemo login page
    When they enter valid credentials
    Then they should be redirected to the inventory page
```

