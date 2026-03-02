# -*- coding: utf-8 -*-
"""
═════════════════════════════════════════════════════════════════════════════
GESTOR DE GENERACIÓN DE INFORMES CON JASPER REPORTS - TORNEO DE FÚTBOL
═════════════════════════════════════════════════════════════════════════════

Módulo para procesar ficheros JRXML y generar informes en PDF.
Utiliza pyreportjasper como intermediario con Jasper Reports.

Bases de datos soportadas:
  - PostgreSQL
  - MySQL  
  - SQLite (vía JDBC)
  - XML (fuentes de datos XML)
  - JSON (fuentes de datos JSON)

Validaciones implementadas:
  ✓ Validación de ficheros JRXML (existencia y extensión)
  ✓ Validación de directorios de salida (creación automática)
  ✓ Validación de parámetros (tipo dict)
  ✓ Manejo de errores con mensajes descriptivos
"""

import os

# Configuración de rutas
# base_path apunta al directorio raíz del proyecto (un nivel arriba de controllers/)

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))



def _validar_fichero_entrada(ruta_fichero):
    """
    Valida que el fichero JRXML existe y es accesible.
    
    Args:
        ruta_fichero (str): Ruta absoluta del fichero JRXML
        
    Returns:
        bool: True si el fichero es válido
        
    Raises:
        FileNotFoundError: Si el fichero no existe
        ValueError: Si la ruta es inválida o no es JRXML
    """
    if not isinstance(ruta_fichero, str) or not ruta_fichero.strip():
        raise ValueError("❌ La ruta del fichero no puede estar vacía")
    
    if not ruta_fichero.lower().endswith('.jrxml'):
        raise ValueError(f"❌ El fichero debe tener extensión .jrxml\n   Recibido: {ruta_fichero}")
    
    if not os.path.exists(ruta_fichero):
        raise FileNotFoundError(f"❌ El fichero JRXML no existe:\n   {ruta_fichero}")
    
    if not os.path.isfile(ruta_fichero):
        raise ValueError(f"❌ La ruta no es un fichero:\n   {ruta_fichero}")
    
    return True


def _garantizar_directorio_salida(ruta_salida):
    """
    Crea el directorio de salida si no existe.
    
    Args:
        ruta_salida (str): Ruta donde se guardarán los PDFs
        
    Returns:
        bool: True si el directorio existe o fue creado correctamente
        
    Raises:
        OSError: Si no se puede crear el directorio
        ValueError: Si la ruta no es un directorio válido
    """
    if not os.path.exists(ruta_salida):
        try:
            os.makedirs(ruta_salida, exist_ok=True)
            print(f"📁 Directorio de salida creado: {ruta_salida}")
        except OSError as e:
            raise OSError(f"❌ No se pudo crear el directorio de salida:\n   {ruta_salida}\n   Error: {e}")
    
    if not os.path.isdir(ruta_salida):
        raise ValueError(f"❌ La ruta de salida no es un directorio: {ruta_salida}")
    
    return True


def compiling():
    """
    Compila un fichero JRXML en formato .jasper (compilado).
    
    Útil cuando no usas JasperSoft Studio.
    Genera un fichero .jasper compilado que se procesa más rápido.
    """
    input_file = os.path.join(base_path, 'informes', 'Agrupamiento.jrxml')
    
    try:
        import pyreportjasper
        _validar_fichero_entrada(input_file)
        jasper = pyreportjasper.PyReportJasper()
        jasper.config(input_file)
        jasper.compile()
        print(f"✅ Compilación exitosa: {input_file}")
    except Exception as e:
        print(f"❌ Error en compilación: {e}")
        raise


def processing():
    """
    Procesa un informe JRXML y genera PDFs y RTF.
    
    Genera el informe de Agrupamiento en múltiples formatos.
    Sin parámetros ni filtros, solo datos de ejemplo.
    """
    input_file = os.path.join(base_path, 'informes', 'Agrupamiento.jrxml')
    output = os.path.join(base_path, 'informes', 'pdf')
    
    try:
        import pyreportjasper
        _validar_fichero_entrada(input_file)
        _garantizar_directorio_salida(output)
        
        jasper = pyreportjasper.PyReportJasper()
        jasper.process(
            input_file,
            output_file=output,
            format_list=["pdf", "rtf"]
        )
        print(f"✅ Procesamiento exitoso.")
        print(f"   Ficheros generados en: {output}")
    except Exception as e:
        print(f"❌ Error en procesamiento: {e}")
        raise


def listing_parameters():
    """
    Lista los parámetros definidos en un informe JRXML.
    
    Útil para conocer qué parámetros debe proporcionar el usuario.
    Muestra el nombre, tipo y valor por defecto de cada parámetro.
    """
    input_file = os.path.join(base_path, 'informes', 'Listado_clientes_param_filtrado.jrxml')
    
    try:
        import pyreportjasper
        _validar_fichero_entrada(input_file)
        jasper = pyreportjasper.PyReportJasper()
        jasper.config(input_file=input_file)
        output = jasper.list_report_params()
        print(f"\n📋 Parámetros del informe:")
        print(f"   {input_file}")
        print(f"\n{output}")
    except Exception as e:
        print(f"❌ Error al listar parámetros: {e}")
        raise


def xml_to_pdf():
    """
    Convierte un informe JRXML con datos XML a PDF.
    
    Ejemplo de procesamiento donde la fuente de datos es un fichero XML.
    Demuestra cómo usar 'driver': 'xml' para cargar datos XML.
    """
    input_file = os.path.join(base_path, 'controllers', 'examples', 'CancelAck.jrxml')
    output = os.path.join(base_path, 'controllers', 'output', '_CancelAck')
    data_file = os.path.join(base_path, 'controllers', 'examples', 'CancelAck.xml')

    try:
        import pyreportjasper
        _validar_fichero_entrada(input_file)
        _garantizar_directorio_salida(os.path.dirname(output))
        
        jasper = pyreportjasper.PyReportJasper()
        jasper.process(
            input_file,
            output=output,
            format_list=["pdf"],
            parameters={},
            db_connection={
                'data_file': data_file,
                'driver': 'xml',
                'xml_xpath': '/CancelResponse/CancelResult/ID',
            },
            locale='pt_BR'
        )
        print(f"✅ Informe XML generado: {output}.pdf")
    except Exception as e:
        print(f"❌ Error en conversión XML: {e}")
        raise


def json_to_pdf():
    """
    Convierte un informe JRXML con datos JSON a PDF.
    
    Ejemplo de procesamiento donde la fuente de datos es un fichero JSON.
    Demuestra cómo usar 'driver': 'json' para cargar datos JSON.
    """
    input_file = os.path.join(base_path, 'controllers', 'examples', 'json.jrxml')
    output = os.path.join(base_path, 'controllers', 'output', '_Contacts')
    json_query = 'contacts.person'
    data_file = os.path.join(base_path, 'controllers', 'examples', 'contacts.json')

    try:
        import pyreportjasper
        _validar_fichero_entrada(input_file)
        _garantizar_directorio_salida(os.path.dirname(output))
        
        jasper = pyreportjasper.PyReportJasper()
        jasper.process(
            input_file,
            output=output,
            format_list=["pdf"],
            parameters={},
            db_connection={
                'data_file': data_file,
                'driver': 'json',
                'json_query': json_query,
            },
            locale='pt_BR'
        )
        print(f"✅ Informe JSON generado: {output}.pdf")
    except Exception as e:
        print(f"❌ Error en conversión JSON: {e}")
        raise


def advanced_example_using_database(ficheroEntrada, ficheroSalida, parametros):
    """
    ═════════════════════════════════════════════════════════════════════════
    FUNCIÓN PRINCIPAL: Genera informe PDF desde JRXML usando BD SQLite
    ═════════════════════════════════════════════════════════════════════════
    
    Args:
        ficheroEntrada (str): Ruta ABSOLUTA del fichero JRXML a procesar
                              Ejemplo: 'C:/ruta/informes/Informe_4_1_1_1_parametro_texto.jrxml'
        
        ficheroSalida (str): Ruta ABSOLUTA del DIRECTORIO donde guardar el PDF
                             (SIN extensión, se añade automáticamente .pdf)
                             Ejemplo: 'C:/ruta/informes/pdf'
        
        parametros (dict): Diccionario con parámetros del informe
                          {nombreParametro: valor}
                          
                          Ejemplos:
                          - {'Comentario': 'Mi texto'}
                          - {'Ciudad': 'Madrid'}
                          - {'Titulo': 'Resumen de partidos'}
                          - {}  (informe sin parámetros)
    
    Returns:
        bool: True si la generación fue exitosa
    
    Raises:
        FileNotFoundError: El fichero JRXML no existe
        ValueError: Parámetros inválidos o rutas incorrectas
        Exception: Error en la generación del informe
    
    ═════════════════════════════════════════════════════════════════════════
    CONFIGURACIÓN DE BASE DE DATOS (SQLite vía JDBC)
    ═════════════════════════════════════════════════════════════════════════
    
    pyreportjasper NO soporta SQLite de forma nativa en db.get_connection().
    
    SOLUCIÓN: Usar 'generic' + 'jdbc_url' para pasar la conexión SQLite vía JDBC
    
    Requisitos:
    - Driver JDBC: sqlite-jdbc-3.51.0.0.jar en controllers/libs/jdbc/
    - Fichero BD: torneoFutbol_sqlite.db
    
    NOTAS SOBRE SQLite EN REPORTES JRXML:
    
    1. Funciones SQL incompatibles con MySQL:
       ❌ CURDATE(), NOW(), DATE_ADD(), DATE_SUB()  (manejo de fechas)
       ✅ Usar: date('now'), date('now', 'start of day')
    
    2. Tipado de datos ESTRICTO:
       SQLite es más permisivo que MySQL, pero los Datasets en JRXML
       necesitan indicar claramente el tipo:
       ✓ <field name="Cantidad" class="java.lang.Integer"/>
       ✓ <field name="Precio" class="java.lang.Float"/>
       ✓ <field name="Nombre" class="java.lang.String"/>
       ❌ NO dejar sin clase (class)
    
    3. Cast de tipos:
       SELECT CAST(monto AS NUMERIC) as Precio
       SELECT CAST(id AS INTEGER) as EquipoID
    
    ═════════════════════════════════════════════════════════════════════════
    """
    
    # ─────────────────────────────────────────────────────────────────────
    # 1. VALIDACIONES
    # ─────────────────────────────────────────────────────────────────────
    
    try:
        _validar_fichero_entrada(ficheroEntrada)
        # ✅ Validar solo el DIRECTORIO PADRE, no la ruta del fichero
        _garantizar_directorio_salida(os.path.dirname(ficheroSalida))
    except (FileNotFoundError, ValueError, OSError) as e:
        print(f"❌ Error en validación de rutas:")
        print(f"   {e}")
        raise
    
    if not isinstance(parametros, dict):
        raise ValueError(
            f"❌ Los parámetros deben ser un diccionario {{clave: valor}}\n"
            f"   Tipo recibido: {type(parametros)}\n"
            f"   Valor recibido: {parametros}"
        )
    
    # ─────────────────────────────────────────────────────────────────────
    # 2. CONVERSIÓN Y VALIDACIÓN DE RUTAS Y PARÁMETROS
    # ─────────────────────────────────────────────────────────────────────
    
    # ✅ IMPORTANTE: Convertir todas las rutas a strings absolutos
    # Evita problemas de bytes encoding en Windows con caracteres acentuados
    ficheroEntrada_str = str(ficheroEntrada)  # Asegurar string
    ficheroSalida_str = str(ficheroSalida)    # Asegurar string
    
    # ✅ Convertir \ a / (Java entiende mejor forward slashes)
    ficheroEntrada_str = ficheroEntrada_str.replace('\\', '/')
    ficheroSalida_str = ficheroSalida_str.replace('\\', '/')
    
    # ✅ Validar y limpiar parámetros: todos deben ser strings
    parametros_limpios = {}
    for clave, valor in parametros.items():
        if valor is None:
            print(f"⚠️  Parámetro '{clave}' es None, se ignora")
            continue
        # Convertir a string si es necesario (Integer, Float, etc.)
        parametros_limpios[clave] = str(valor)
    
    parametros = parametros_limpios  # Usar versión limpia
    
    # ─────────────────────────────────────────────────────────────────────
    # 3. CONFIGURACIÓN DE CONEXIÓN JDBC (SQLite)
    # ─────────────────────────────────────────────────────────────────────
    
    jdbc_dir = str(os.path.join(base_path, 'controllers', 'libs', 'jdbc', 'sqlite-jdbc-3.51.0.0.jar')).replace('\\', '/')
    jdbc_file = str(os.path.join(base_path, 'torneoFutbol_sqlite.db')).replace('\\', '/')
    
    con = {
        'driver': 'generic',
        'jdbc_driver': 'org.sqlite.JDBC',
        'jdbc_dir': jdbc_dir,
        'jdbc_url': f'jdbc:sqlite:{jdbc_file}',
    }
    
    # ─────────────────────────────────────────────────────────────────────
    # 4. GENERACIÓN DEL INFORME
    # ─────────────────────────────────────────────────────────────────────
    
    try:
        import pyreportjasper
        jasper = pyreportjasper.PyReportJasper()

        # --- DEBUG: imprimir tipos y valores antes de llamar a jasper.process() ---
        try:
            print("DEBUG: ficheroEntrada_str type:", type(ficheroEntrada_str), "repr:", repr(ficheroEntrada_str))
            print("DEBUG: ficheroSalida_str type:", type(ficheroSalida_str), "repr:", repr(ficheroSalida_str))
            print("DEBUG: parametros type:", type(parametros), "len:", len(parametros))
            for _k, _v in (parametros or {}).items():
                print(f"DEBUG: param {_k}: type={type(_v)} repr={repr(_v)}")
            print("DEBUG: db_connection type:", type(con))
            print("DEBUG: db_connection keys:", list(con.keys()))
            print("DEBUG: jdbc_dir:", repr(con.get('jdbc_dir')))
            print("DEBUG: jdbc_url:", repr(con.get('jdbc_url')))
        except Exception as _dbg_e:
            print("DEBUG: error printing debug info:", _dbg_e)

        try:
            jasper.process(
                ficheroEntrada_str,
                output_file=ficheroSalida_str,
                format_list=["pdf"],
                parameters=parametros,
                db_connection=con,
                locale='es_ES'
            )
        except Exception as e:
            import traceback
            print("DEBUG: Exception raised by jasper.process():", type(e).__name__, e)
            traceback.print_exc()
            raise
        
        # Éxito
        pdf_path = f"{ficheroSalida_str}.pdf"
        print(f"\n{'='*75}")
        print(f"✅ INFORME GENERADO EXITOSAMENTE")
        print(f"{'='*75}")
        print(f"📄 Fichero JRXML: {ficheroEntrada_str}")
        print(f"📁 Guardado en:   {pdf_path}")
        if parametros:
            print(f"🔧 Parámetros:    {parametros}")
        print(f"{'='*75}\n")
        return True
        
    except Exception as e:
        # Error
        print(f"\n{'='*75}")
        print(f"❌ ERROR EN GENERACIÓN DE INFORME")
        print(f"{'='*75}")
        print(f"📄 Fichero JRXML:    {ficheroEntrada_str}")
        print(f"📁 Directorio salida: {ficheroSalida_str}")
        print(f"🔧 Parámetros:        {parametros}")
        print(f"\n⚠️  DETALLES DEL ERROR:")
        print(f"{type(e).__name__}: {e}")
        print(f"\n💡 POSIBLES SOLUCIONES:")
        if "concatenate" in str(e):
            print(f"   • Error de encoding en rutas/parámetros")
            print(f"   • Verificar que no hay valores None en parámetros")
            print(f"   • Asegurar que el JRXML usa los parámetros correctamente")
        if "no such table" in str(e).lower():
            print(f"   • Verificar que la tabla existe en la BD torneoFutbol_sqlite.db")
            print(f"   • Ejecutar check_db.py para validar la BD")
        if not os.path.exists(ficheroEntrada_str):
            print(f"   • El fichero JRXML no existe: {ficheroEntrada_str}")
        print(f"{'='*75}\n")
        raise


if __name__ == "__main__":
    """
    Script de prueba. Este módulo generalmente se importa desde geninformes_logica.py
    
    Para probar manualmente, descomenta uno de estos ejemplos:
    """
    
    #EJEMPLO 1: Informe con parámetro de texto
    try:
        entrada = os.path.join(base_path, 'informesSQLite', 'Informe_4_1_1_1_parametro_texto.jrxml')
        salida = os.path.join(base_path, 'informesSQLite', 'pdfsalida')
        params = {'Comentario': 'Prueba de parámetro'}
        advanced_example_using_database(entrada, salida, params)
    except Exception as e:
        print(f"Fallo: {e}")
    
    # EJEMPLO 2: Informe sin parámetros
    # try:
    #     entrada = os.path.join(base_path, 'informesSQLite', 'Informe_3_5_ClientesCiudad.jrxml')
    #     salida = os.path.join(base_path, 'informesSQLite', 'pdfsalida')
    #     advanced_example_using_database(entrada, salida, {})
    # except Exception as e:
    #     print(f"Fallo: {e}")
    
    
