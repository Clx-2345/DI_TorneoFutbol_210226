# ⚽ Torneo de Fútbol - FINAL

Sistema completo de gestión de torneos de fútbol con generación de informes avanzados.

**Autor:** Samuel Polanco Martínez  
**Versión:** 1.0.0 (Final)  
**Fecha:** Febrero 2026

---

## 📋 Características

### Gestión de Torneo
- ✅ **Equipos:** Crear y gestionar equipos con emblemas
- ✅ **Participantes:** Registrar jugadores y árbitros
- ✅ **Calendario:** Programar partidos por eliminatorias
- ✅ **Partido en Vivo:** Seguimiento en tiempo real con reloj
- ✅ **Eventos:** Registrar goles, tarjetas, cambios
- ✅ **Resultados:** Actualizar goles y estadísticas
- ✅ **Clasificación:** Ver eliminatorias, goleadores y tarjetas

### 📊 Generación de Informes (NUEVO - Tarea 5)
- ✅ **3 Informes específicos del torneo**
  - **Equipos y Jugadores:** Listado con estadísticas por equipo
  - **Partidos y Resultados:** Calendario completo con resultados
  - **Clasificación y Eliminatorias:** Tabla de clasificación con estadísticas
- ✅ **Ventana integrada** en la aplicación principal (Menú > Informes)
- ✅ **Parámetros dinámicos:** Filtros por equipo y eliminatoria
- ✅ **Exportación a PDF** profesional con Jasper Reports
- ✅ **14 Informes de ejemplo** adicionales
- ✅ **Logos e imágenes** personalizadas

---

## 🚀 Instalación

### Requisitos
- Python 3.8+
- PySide6
- pyreportjasper
- **Java 11+ (JDK 21 recomendado)** - ⚠️ Nota: Java 8 NO es compatible

### Instalación de Dependencias

```bash
pip install PySide6 pyreportjasper
```

### Configurar Java (IMPORTANTE)
**La aplicación configura Java automáticamente,** pero si encuentras errores:

1. **Verificar versión de Java:**
   ```bash
   java -version
   ```
   Debe mostrar Java 11 o superior (ej: "21.0.5")

2. **Si tienes Java 8**, configura Java automáticamente:
   ```powershell
   .\scripts\configurar_java.ps1
   ```

3. **Para más detalles**, consulta: [INFORMES_CONFIGURACION.md](INFORMES_CONFIGURACION.md)

### Ejecutar la Aplicación

```bash
python main.py
```

---

## 📁 Estructura del Proyecto

```
TorneoFutbolFinal/
├── main.py                          # Punto de entrada principal
├── torneoFutbol_sqlite.db           # Base de datos SQLite
├── ARQUITECTURA.md                  # Documentación de arquitectura
├── controllers/
│   ├── main_controller.py           # Controlador principal
│   ├── crearinforme.py              # Generación de informes
│   ├── geninformes_logica.py        # Lógica de informes
│   └── libs/jdbc/                   # Driver JDBC SQLite
├── models/                          # Modelos de datos (CRUD)
├── views/                           # Vistas de la interfaz
├── resources/                       # Estilos y recursos
├── informes/                        # Plantillas Jasper Reports
│   ├── *.jrxml                      # Plantillas de informes
│   └── pdf/                         # PDFs generados
├── informesSQLite/                  # Informes SQLite
│   ├── *.jrxml
│   └── pdf/
└── scripts/
    └── check_db.py                  # Verificación de BD
```

Ver [ARQUITECTURA.md](ARQUITECTURA.md) para documentación completa.

---

## 🎯 Uso de la Aplicación

### Aplicación Principal

1. **Crear equipos** → Gestión de Equipos
2. **Registrar participantes** → Gestión de Participantes
3. **Programar partidos** → Gestión del Calendario
4. **Seguir partido en vivo** → Vista de Partido en Vivo
5. **Actualizar resultados** → Actualización de Resultados
6. **Ver estadísticas** → Clasificación y Eliminatorias
7. **Generar informes** → Generador de Informes (nuevo)

### 📊 Generador de Informes

#### Opción 1: Desde la aplicación principal (RECOMENDADO)
- Menú superior > **"Informes"** > **"Generar Informes..."**

#### Opción 2: Ejecución independiente
```bash
python controllers/geninformes_logica.py
```

#### Informes del Torneo (NUEVO):

1. **📋 Informe Equipos y Jugadores** (`Informe_1_Equipos_Jugadores.jrxml`)
   - Listado completo de equipos con sus jugadores
   - Estadísticas por jugador: posición, goles, tarjetas
   - Totales por equipo: goles, tarjetas amarillas y rojas
   - **Parámetro:** Filtrar por nombre de equipo (opcional)
   
2. **⚽ Informe Partidos y Resultados** (`Informe_2_Partidos_Resultados.jrxml`)
   - Calendario completo de partidos
   - Información: equipos, árbitro, fecha, hora, lugar
   - Resultados de partidos jugados
   - Partidos pendientes resaltados
   - Resumen: total de partidos y goles
   - **Parámetro:** Filtrar por eliminatoria (opcional)
   
3. **🏆 Informe Clasificación y Eliminatorias** (`Informe_3_Clasificacion_Eliminatorias.jrxml`)
   - Tabla de clasificación completa
   - Victorias, empates, derrotas por equipo
   - Goles a favor, en contra y diferencia
   - Puntos calculados (V=3, E=1, D=0)
   - Primeros 3 lugares destacados
   - Estadísticas globales del torneo
   - **Parámetro:** Filtrar por eliminatoria (opcional)

#### Informes de Ejemplo (14 adicionales):

4. **Informe_3_5_ClientesCiudad.jrxml**: Listado básico
5. **Informe_4_1_1_1_parametro_texto.jrxml**: Con parámetro de texto
6. **Informe_4_1_1_filtrado_datos.jrxml**: Con filtro por ciudad
7. **Informe_4_1_1_ordenar_datos.jrxml**: Ordenamiento personalizado
8. **Informe_4_2_1_recontarytotalizar.jrxml**: Con totales
9. **Informe_4_3_1_Agrupamiento.jrxml**: Con agrupación
10. **Informe_4_4_Subtotal.jrxml**: Con subtotales
11. **Informe_4_5_1_InformePrincipal.jrxml**: Con subinformes
12. **Informe_4_7_1_Graficos.jrxml**: Con gráficos

> **Nota:** Los informes de ejemplo (4-12) usan datos de prueba. Los informes 1-3 están diseñados específicamente para el torneo de fútbol.

#### Pasos para generar un informe:

1. **Acceder al generador:**
   - Desde menú: **Informes > Generar Informes...**
   - O ejecutar: `python controllers/geninformes_logica.py`

2. **Configurar rutas** (se configuran automáticamente si se abre desde menú):
   - **Ruta de entrada**: Carpeta con plantillas .jrxml
     - Por defecto: `C:/TorneoFutbolFinal/informesSQLite`
   - **Ruta de salida**: Carpeta para PDFs
     - Por defecto: `C:/TorneoFutbolFinal/informesSQLite/pdf`
   - Presiona **Enter** en "Ruta de entrada" para cargar ficheros

3. **Seleccionar informe:**
   - Elige del desplegable uno de los **3 informes del torneo**:
     - `Informe_1_Equipos_Jugadores.jrxml`
     - `Informe_2_Partidos_Resultados.jrxml`
     - `Informe_3_Clasificacion_Eliminatorias.jrxml`
   - O alguno de los 14 informes de ejemplo

4. **Generar:**
   - Clic en **"Generar Informe"**
   - Si solicita parámetros:
     - **Informe 1:** Nombre de equipo (deja vacío para todos)
     - **Informes 2 y 3:** Eliminatoria (vacío, Octavos, Cuartos, Semifinal, Final)
   - El PDF se guardará automáticamente en `informesSQLite/pdf/`

5. **Ver resultado:**
   - Abre la carpeta `informesSQLite/pdf/`
   - Verás el PDF: `Informe_1_Equipos_Jugadores.pdf` (por ejemplo)

### Verificar Base de Datos

```bash
python scripts/check_db.py
```

---

## 📊 Informes Disponibles

### Informes del Torneo de Fútbol

Los siguientes 3 informes están diseñados específicamente para los datos del torneo:

1. **Informe_1_Equipos_Jugadores.jrxml**
   - Consulta: `equipos` + `participantes` (jugadores)
   - Parámetro: `EQUIPO_FILTRO` (nombre del equipo o vacío para todos)
   - Contenido:
     - Equipos en orden alfabético
     - Jugadores por equipo con posición, goles, tarjetas
     - Totales acumulados por equipo
     - Número de jugadores por equipo

2. **Informe_2_Partidos_Resultados.jrxml**
   - Consulta: `partidos` + `equipos` + `participantes` (árbitros)
   - Parámetro: `ELIMINATORIA_FILTRO` (Octavos/Cuartos/Semifinal/Final o vacío)
   - Contenido:
     - Partidos agrupados por eliminatoria
     - Fecha, hora, lugar, árbitro
     - Resultados de partidos jugados
     - Partidos pendientes resaltados en naranja
     - Estadísticas: total de partidos y goles

3. **Informe_3_Clasificacion_Eliminatorias.jrxml**
   - Consulta: `equipos` + `partidos` (cálculo de puntos)
   - Parámetro: `ELIMINATORIA_FILTRO` (opcional)
   - Contenido:
     - Clasificación ordenada por puntos
     - Victorias, empates, derrotas
     - Goles a favor, en contra, diferencia
     - Primeros 3 lugares destacados con borde dorado
     - Estadísticas globales del torneo

### Informes de Ejemplo

Los siguientes 14 informes son plantillas de ejemplo con datos de prueba:

4. **Informe_3_5_ClientesCiudad.jrxml**: Listado básico
5. **Informe_4_1_1_1_parametro_texto.jrxml**: Con parámetro de texto
6. **Informe_4_1_1_filtrado_datos.jrxml**: Con filtro por ciudad
7. **Informe_4_1_1_ordenar_datos.jrxml**: Ordenamiento personalizado
8. **Informe_4_2_1_recontarytotalizar.jrxml**: Con totales
9. **Informe_4_2_2y3_recontarytotalizar_con_encabypie_numlin.jrxml**: Con encabezados
10. **Informe_4_3_1_Agrupamiento.jrxml**: Con agrupación
11. **Informe_4_3_2_AgrupamientoComplejo.jrxml**: Agrupación compleja
12. **Informe_4_4_Subtotal.jrxml**: Con subtotales
13. **Informe_4_5_1_InformePrincipal.jrxml**: Con subinformes
14. **Informe_4_5_2_Subinformeemails.jrxml**: Subinforme de emails
15. **Informe_4_5_3_SubinformeTfnos.jrxml**: Subinforme de teléfonos
16. **Informe_4_7_1_Graficos.jrxml**: Con gráficos

> **Nota:** Los informes de ejemplo (4-16) son de `EjemploTema7` y usan datos de prueba (clientes, ciudades). Para usarlos con datos del torneo, abre los .jrxml en Jaspersoft Studio y modifica las consultas SQL para apuntar a las tablas del torneo (equipos, participantes, partidos).

---

## 🛠️ Crear Informes Personalizados

### 1. Instalar Jaspersoft Studio
- Descarga gratuita: https://community.jaspersoft.com/project/jaspersoft-studio

### 2. Conectar a la Base de Datos
- **Tipo**: SQLite
- **Driver**: `sqlite-jdbc-3.51.0.0.jar` (incluido en `controllers/libs/jdbc/`)
- **URL**: `jdbc:sqlite:c:/ruta/TorneoFutbolFinal/torneoFutbol_sqlite.db`

### 3. Tablas Disponibles
- **Equipos**: Información de equipos
- **Partidos**: Partidos jugados
- **Participantes**: Equipos en cada partido
- **EstadisticasPartido**: Estadísticas por partido
- **EventosPartido**: Eventos (goles, tarjetas, etc.)

### 4. Guardar y Usar
- Guarda el archivo .jrxml en `informesSQLite/`
- Añade configuración en `controllers/geninformes_logica.py` si hay parámetros

---

## 🔧 Solución de Problemas

### Error: "No se pudo generar el informe"
- ✅ Verifica Java: `java -version`
- ✅ Comprueba que el .jrxml existe
- ✅ Verifica datos: `python scripts/check_db.py`

### Error: "JDBC driver not found"
- ✅ Verifica: `controllers/libs/jdbc/sqlite-jdbc-3.51.0.0.jar`
- ✅ Descarga: https://github.com/xerial/sqlite-jdbc/releases

### El informe sale vacío
- ✅ Verifica SQL en el .jrxml apunta a tablas correctas
- ✅ Comprueba que hay datos: `python scripts/check_db.py`
- ✅ Revisa nombres de campos en el Dataset

### Error de módulo
```bash
pip install PySide6 pyreportjasper
```

---

## 📚 Documentación

- [ARQUITECTURA.md](ARQUITECTURA.md): Arquitectura detallada del proyecto
- [Informe Tecnico.pdf](Informe%20Tecnico.pdf): Documentación técnica
- [Manual de usuario.pdf](Manual%20de%20usuario.pdf): Guía de usuario

---

## 👨‍💻 Tecnologías

- **Python 3.x**: Lenguaje principal
- **PySide6 (Qt)**: Framework de interfaz gráfica
- **SQLite**: Base de datos embebida
- **pyreportjasper**: Generación de informes PDF
- **Jasper Reports**: Motor de plantillas de informes

---

## 📝 Licencia

Proyecto educativo del Instituto - Desarrollo de Interfaces

---

**¿Necesitas ayuda?** Consulta [ARQUITECTURA.md](ARQUITECTURA.md) o ejecuta `python scripts/check_db.py`

