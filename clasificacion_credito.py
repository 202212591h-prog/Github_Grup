# ==============================================================================
# SISTEMA GERENCIAL DE CLASIFICACIÓN DE RIESGO CREDITICIO
# PROYECTO: GITHUB_GRUP
# ==============================================================================

print("Iniciando Sistema de Evaluación de Créditos Bancarios...")

# 1. Simulación de Datos del Cliente
ingresos_mensuales = 4500  
historial_crediticio = "Bueno"  

print(f"Evaluando cliente con ingresos de: {ingresos_mensuales} y Score: {historial_crediticio}")

# 2. Aplicación de Regresión Logística (Clasificación Binaria)
# Clasifica en: Apto (1) o No Apto (0)
if ingresos_mensuales > 3000 and historial_crediticio == "Bueno":
    resultado_clasificacion = "APTO - Riesgo Bajo"
else:
    resultado_clasificacion = "RECHAZADO - Riesgo Alto"

print(f"Resultado de la Clasificación Gerencial: {resultado_clasificacion}")