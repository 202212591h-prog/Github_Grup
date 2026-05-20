# ==============================================================================
# SISTEMA GERENCIAL DE CLASIFICACIÓN DE RIESGO CREDITICIO (GITHUB_GRUP)
# ==============================================================================

def evaluar_cliente(nombre, ingresos, historial, deudas):
    print(f"\n--- EVALUANDO SOLICITUD DE: {nombre} ---")
    print(f"Ingresos: ${ingresos} | Historial: {historial} | Deudas actuales: ${deudas}")
    
    # 1. REGRESIÓN LOGÍSTICA (Clasificación Binaria: Apto / No Apto)
    if ingresos > 2500 and historial == "Bueno":
        reg_logistica = "APTO"
    else:
        reg_logistica = "NO APTO"
    
    # 2. ÁRBOLES DE DECISIÓN (Clasificación por Ramas Categóricas)
    if deudas > (ingresos * 0.5):
        arbol_decision = "Riesgo Alto (Endeudamiento elevado)"
    elif historial == "Regular":
        arbol_decision = "Riesgo Medio (Monitorear comportamiento)"
    else:
        arbol_decision = "Riesgo Bajo (Perfil estable)"
        
    # 3. RANDOM FOREST (Combinación de árboles para decidir el monto máximo)
    # Simula votaciones de árboles: estabilidad laborar, edad, patrimonio
    if reg_logistica == "APTO" and arbol_decision == "Riesgo Bajo":
        monto_maximo = ingresos * 10
        random_forest = f"APROBADO (Monto sugerido: ${monto_maximo})"
    elif reg_logistica == "APTO" and arbol_decision == "Riesgo Medio":
        monto_maximo = ingresos * 5
        random_forest = f"APROBADO CON RESTRICCIÓN (Monto sugerido: ${monto_maximo})"
    else:
        random_forest = "RECHAZADO POR EL COMITÉ DE ÁRBOLES"

    # 4. K-VECINOS MÁS CERCANOS (KNN - Clasificación por similitud con otros clientes)
    # Busca clientes "vecinos" con comportamientos similares
    if historial == "Malo":
        knn_clasificacion = "Clasificado en grupo: 'Clientes Morosos Históricos'"
    else:
        knn_clasificacion = "Clasificado en grupo: 'Clientes Premium / Pagadores'"

    # 5. MÁQUINA DE VECTORES DE SOPORTE (SVM - Separación en hiperplanos)
    # Separa matemáticamente si requiere aval/garantía o no
    if deudas > 5000:
        svm_hiperplano = "REQUIERE AVAL (Fuera del margen seguro)"
    else:
        svm_hiperplano = "SIN AVAL (Dentro del margen seguro)"

    # 6. NAIVE BAYES (Clasificación Probabilística para Prioridad de Atención)
    # Evalúa la probabilidad de urgencia según el tipo de préstamo
    prioridad_probabilistica = "ALTA PRIORIDAD (Crédito Hipotecario/Empresarial)" if ingresos > 5000 else "PRIORIDAD ESTÁNDAR"

    # MOSTRAR RESULTADOS EN CONSOLA PARA GERENCIA
    print(f"[1. Regresión Logística] Estado Inicial: {reg_logistica}")
    print(f"[2. Árbol de Decisión]   Análisis de Perfil: {arbol_decision}")
    print(f"[3. Random Forest]       Decisión Final del Sistema: {random_forest}")
    print(f"[4. KNN (Vecinos)]       Segmentación de Grupo: {knn_clasificacion}")
    print(f"[5. SVM (Vectores)]      Garantía Requerida: {svm_hiperplano}")
    print(f"[6. Naive Bayes]         Flujo de Atención: {prioridad_probabilistica}")


# ==============================================================================
# EJECUCIÓN DE PRUEBA (SIMULACIÓN GERENCIAL)
# ==============================================================================
# Cliente 1: Perfil ideal
evaluar_cliente(nombre="Juan Pérez", ingresos=4500, historial="Bueno", deudas=1000)

# Cliente 2: Perfil de riesgo alto
evaluar_cliente(nombre="María López", ingresos=2000, historial="Malo", deudas=1800)