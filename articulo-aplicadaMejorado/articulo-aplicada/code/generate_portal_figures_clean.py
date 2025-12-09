#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Graficas para Portal Agro-comercial del Huila
Genera graficas especificas basadas en el contenido del articulo aplicado
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams
import os

# Configuracion global para mejorar la calidad de las graficas
plt.style.use('default')
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 10
rcParams['axes.labelsize'] = 11
rcParams['axes.titlesize'] = 12
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9
rcParams['legend.fontsize'] = 9
rcParams['figure.titlesize'] = 13
rcParams['savefig.dpi'] = 300
rcParams['savefig.bbox'] = 'tight'
rcParams['savefig.pad_inches'] = 0.1

# Crear directorio de graficas si no existe
graphics_dir = 'graphics'
os.makedirs(graphics_dir, exist_ok=True)

def generar_comparacion_legacy_moderno():
    """Genera grafica comparando tiempo invertido en sistemas legacy vs modernos"""
    
    categorias = ['Sistemas Legacy', 'Sistemas Modernos']
    tiempo_desarrollo = [60, 20]  # Porcentaje de tiempo
    tiempo_mantenimiento = [30, 10]
    tiempo_nuevas_funciones = [10, 70]
    
    x = np.arange(len(categorias))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars1 = ax.bar(x - width, tiempo_desarrollo, width, label='Correccion de Fallos', color='#C73E1D')
    bars2 = ax.bar(x, tiempo_mantenimiento, width, label='Mantenimiento', color='#F18F01')
    bars3 = ax.bar(x + width, tiempo_nuevas_funciones, width, label='Nuevas Funcionalidades', color='#2E86AB')
    
    ax.set_xlabel('Tipo de Sistema')
    ax.set_ylabel('Porcentaje de Tiempo (%)')
    ax.set_title('Distribucion del Tiempo de Desarrollo: Legacy vs Moderno\n(Portal Agro-comercial del Huila)')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()
    
    # Anadir valores en las barras
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{height}%', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/comparacion_legacy_moderno.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/comparacion_legacy_moderno.png', format='png')
    plt.close()
    print("Generada: comparacion_legacy_moderno.pdf/png")

def generar_factores_exito():
    """Genera grafica de factores predictivos de exito en refactorizacion"""
    
    factores = ['Cobertura de\nPruebas', 'Experiencia\ndel Equipo', 'Complejidad\ndel Dominio', 'Presupuesto/\nTamano']
    pesos = [4.2, 3.8, 2.5, 1.2]
    colores = ['#C73E1D', '#F18F01', '#2E86AB', '#A23B72']
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    bars = ax.bar(factores, pesos, color=colores)
    ax.set_ylabel('Peso Predictivo (Odds Ratio)')
    ax.set_title('Factores Predictivos de Exito en Proyectos de Refactorizacion\n(Portal Agro-comercial del Huila)')
    ax.set_ylim(0, 5)
    
    # Anadir valores en las barras
    for bar, peso in zip(bars, pesos):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{peso}', ha='center', va='bottom', fontweight='bold')
    
    # Anadir lineas de referencia
    ax.axhline(y=4, color='red', linestyle='--', alpha=0.7, label='Critico (>=4.0)')
    ax.axhline(y=3, color='orange', linestyle='--', alpha=0.7, label='Alto (>=3.0)')
    ax.axhline(y=2, color='yellow', linestyle='--', alpha=0.7, label='Medio (>=2.0)')
    
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/factores_exito.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/factores_exito.png', format='png')
    plt.close()
    print("Generada: factores_exito.pdf/png")

def generar_evolucion_metricas_portal():
    """Genera grafica de evolucion temporal de metricas del Portal"""
    
    meses = ['Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    cobertura_pruebas = [34, 45, 58, 68, 75, 82, 87]  # % de cobertura
    defectos_produccion = [15, 12, 9, 7, 5, 3, 2]    # defectos por mes
    velocidad_equipo = [20, 25, 30, 35, 40, 45, 50]  # story points
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Grafica 1: Cobertura de Pruebas
    ax1.plot(meses, cobertura_pruebas, 'o-', color='#2E86AB', linewidth=3, markersize=8)
    ax1.fill_between(meses, cobertura_pruebas, alpha=0.3, color='#2E86AB')
    ax1.set_ylabel('Cobertura de Pruebas (%)')
    ax1.set_title('Evolucion de Metricas de Calidad del Portal Agro-comercial del Huila')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 100)
    
    # Anadir linea de meta
    ax1.axhline(y=80, color='red', linestyle='--', alpha=0.7, label='Meta (>80%)')
    ax1.legend()
    
    # Grafica 2: Defectos y Velocidad
    ax2_twin = ax2.twinx()
    
    line1 = ax2.plot(meses, defectos_produccion, 's-', color='#C73E1D', linewidth=3, markersize=8, label='Defectos en Produccion')
    line2 = ax2_twin.plot(meses, velocidad_equipo, '^-', color='#F18F01', linewidth=3, markersize=8, label='Velocidad del Equipo (SP)')
    
    ax2.set_xlabel('Mes (2024)')
    ax2.set_ylabel('Defectos por Mes', color='#C73E1D')
    ax2_twin.set_ylabel('Velocidad del Equipo (Story Points)', color='#F18F01')
    ax2.set_title('Defectos en Produccion vs Velocidad del Equipo')
    
    # Combinar leyendas
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax2.legend(lines, labels, loc='upper right')
    
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/evolucion_metricas_portal.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/evolucion_metricas_portal.png', format='png')
    plt.close()
    print("Generada: evolucion_metricas_portal.pdf/png")

def generar_pipeline_devsecops():
    """Genera diagrama del pipeline DevSecOps implementado"""
    
    etapas = ['Commit', 'Aceptacion', 'Produccion']
    tiempos = [15, 45, 30]  # minutos promedio
    colores = ['#2E86AB', '#F18F01', '#C73E1D']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Grafica 1: Tiempo por etapa
    bars = ax1.bar(etapas, tiempos, color=colores)
    ax1.set_ylabel('Tiempo Promedio (minutos)')
    ax1.set_title('Pipeline DevSecOps del Portal\nTiempo por Etapa')
    
    for bar, tiempo in zip(bars, tiempos):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{tiempo} min', ha='center', va='bottom', fontweight='bold')
    
    # Grafica 2: Tasa de exito por etapa
    tasas_exito = [95, 88, 99]  # porcentaje de exito
    bars2 = ax2.bar(etapas, tasas_exito, color=colores)
    ax2.set_ylabel('Tasa de Exito (%)')
    ax2.set_title('Pipeline DevSecOps del Portal\nTasa de Exito por Etapa')
    ax2.set_ylim(80, 100)
    
    for bar, tasa in zip(bars2, tasas_exito):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{tasa}%', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/pipeline_devsecops.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/pipeline_devsecops.png', format='png')
    plt.close()
    print("Generada: pipeline_devsecops.pdf/png")

def generar_comparacion_arquitecturas():
    """Genera comparacion entre estrategias de modernizacion"""
    
    criterios = ['Riesgo', 'Tiempo', 'Calidad', 'Costo', 'Mantenibilidad']
    refactorizacion = [9, 7, 8, 6, 9]  # Puntuacion 1-10
    reescritura = [3, 9, 6, 4, 5]
    
    x = np.arange(len(criterios))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    bars1 = ax.bar(x - width/2, refactorizacion, width, label='Refactorizacion Incremental', 
                   color='#2E86AB', alpha=0.8)
    bars2 = ax.bar(x + width/2, reescritura, width, label='Reescritura Completa', 
                   color='#C73E1D', alpha=0.8)
    
    ax.set_xlabel('Criterios de Evaluacion')
    ax.set_ylabel('Puntuacion (1-10)')
    ax.set_title('Comparacion de Estrategias de Modernizacion\n(Portal Agro-comercial del Huila)')
    ax.set_xticks(x)
    ax.set_xticklabels(criterios)
    ax.legend()
    ax.set_ylim(0, 10)
    
    # Anadir valores en las barras
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/comparacion_arquitecturas.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/comparacion_arquitecturas.png', format='png')
    plt.close()
    print("Generada: comparacion_arquitecturas.pdf/png")

def generar_roi_beneficios():
    """Genera grafica de ROI y beneficios proyectados"""
    
    categorias = ['Reduccion\nCostos Mantenimiento', 'Aumento\nVelocidad Desarrollo', 'Reduccion\nDefectos', 'Mejora\nCalidad Codigo']
    valores_actuales = [0, 0, 0, 0]
    valores_proyectados = [40, 300, 85, 75]  # Porcentajes de mejora
    
    x = np.arange(len(categorias))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    bars1 = ax.bar(x - width/2, valores_actuales, width, label='Estado Actual', color='lightgray')
    bars2 = ax.bar(x + width/2, valores_proyectados, width, label='Beneficios Proyectados', color='#2E86AB')
    
    ax.set_xlabel('Metricas de Impacto')
    ax.set_ylabel('Mejora (%)')
    ax.set_title('ROI y Beneficios Proyectados del Portal Agro-comercial del Huila')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()
    
    # Anadir valores en las barras
    for bar, valor in zip(bars2, valores_proyectados):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 5,
                f'+{valor}%', ha='center', va='bottom', fontweight='bold')
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/roi_beneficios.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/roi_beneficios.png', format='png')
    plt.close()
    print("Generada: roi_beneficios.pdf/png")

def main():
    """Funcion principal para generar todas las graficas del Portal"""
    print("Generando graficas especificas del Portal Agro-comercial del Huila...")
    print("=" * 60)
    
    try:
        generar_comparacion_legacy_moderno()
        generar_factores_exito()
        generar_evolucion_metricas_portal()
        generar_pipeline_devsecops()
        generar_comparacion_arquitecturas()
        generar_roi_beneficios()
        
        print("=" * 60)
        print("Todas las graficas del Portal fueron generadas exitosamente!")
        print("\nArchivos generados:")
        print("Graficas PDF (para LaTeX): graphics/")
        print("Graficas PNG (para vista previa): graphics/")
        
        print("\nGraficas especificas del Portal:")
        print("1. comparacion_legacy_moderno - Tiempo en sistemas legacy vs modernos")
        print("2. factores_exito - Factores predictivos de exito")
        print("3. evolucion_metricas_portal - Evolucion de metricas de calidad")
        print("4. pipeline_devsecops - Pipeline DevSecOps implementado")
        print("5. comparacion_arquitecturas - Comparacion de estrategias")
        print("6. roi_beneficios - ROI y beneficios proyectados")
        
    except Exception as e:
        print(f"Error al generar graficas: {e}")
        raise

if __name__ == "__main__":
    main()