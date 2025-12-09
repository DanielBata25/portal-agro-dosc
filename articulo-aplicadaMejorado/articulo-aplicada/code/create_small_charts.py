#!/usr/bin/env python3
"""
Script to create smaller, compact charts to replace the wide graphics
Focus on pie charts and compact bar charts for better layout
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Wedge
import pandas as pd

# Set style for better appearance
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Create figure with smaller dimensions for compact charts
def create_pie_chart_comparison():
    """Create pie charts for architectural comparison"""
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))
    
    # Legacy vs Modern comparison
    legacy_data = [60, 40]
    legacy_labels = ['Mantenimiento\\n(Legacy)', 'Desarrollo\\n(Nuevo)']
    colors1 = ['#ff7f7f', '#7fbf7f']
    
    ax1.pie(legacy_data, labels=legacy_labels, colors=colors1, autopct='%1.1f%%', 
            startangle=90, textprops={'fontsize': 8})
    ax1.set_title('Tiempo en Sistemas Legacy', fontsize=10, fontweight='bold')
    
    # Modern system time distribution
    modern_data = [20, 80]
    modern_labels = ['Mantenimiento\\n(Moderno)', 'Desarrollo\\n(Nuevo)']
    colors2 = ['#ffb366', '#66ff66']
    
    ax2.pie(modern_data, labels=modern_labels, colors=colors2, autopct='%1.1f%%', 
            startangle=90, textprops={'fontsize': 8})
    ax2.set_title('Tiempo en Arquitecturas Modernas', fontsize=10, fontweight='bold')
    
    # DevOps practices impact
    devops_data = [40, 35, 25]
    devops_labels = ['TDD\\n(40%)', 'CI/CD\\n(35%)', 'Refactorización\\n(25%)']
    colors3 = ['#66b3ff', '#99ff99', '#ffcc99']
    
    ax3.pie(devops_data, labels=devops_labels, colors=colors3, autopct='%1.1f%%', 
            startangle=90, textprops={'fontsize': 8})
    ax3.set_title('Impacto de Prácticas DevSecOps', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('graphics/comparacion_arquitecturas_circular.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_metrics_evolution():
    """Create compact metrics evolution chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # Test coverage evolution
    months = ['Mes 1', 'Mes 2', 'Mes 3', 'Mes 4', 'Mes 5', 'Mes 6']
    coverage = [45, 58, 67, 75, 82, 85]
    
    ax1.plot(months, coverage, marker='o', linewidth=2.5, markersize=6, color='#2E86AB')
    ax1.fill_between(months, coverage, alpha=0.3, color='#2E86AB')
    ax1.set_title('Evolución de Cobertura de Pruebas', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Cobertura (%)', fontsize=9)
    ax1.tick_params(axis='x', rotation=45, labelsize=8)
    ax1.tick_params(axis='y', labelsize=8)
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=80, color='red', linestyle='--', alpha=0.7, label='Meta 80%')
    ax1.legend(fontsize=8)
    
    # Defect density reduction
    complexity = [12, 10, 8, 6, 4, 3]
    defects = [2.5, 1.8, 1.2, 0.8, 0.4, 0.1]
    
    ax2_twin = ax2.twinx()
    
    line1 = ax2.plot(months, complexity, marker='s', color='#A23B72', linewidth=2.5, 
                     markersize=6, label='Complejidad Ciclomática')
    line2 = ax2_twin.plot(months, defects, marker='^', color='#F18F01', linewidth=2.5, 
                          markersize=6, label='Densidad de Defectos')
    
    ax2.set_title('Reducción de Complejidad y Defectos', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Complejidad', color='#A23B72', fontsize=9)
    ax2_twin.set_ylabel('Defectos por KLOC', color='#F18F01', fontsize=9)
    ax2.tick_params(axis='x', rotation=45, labelsize=8)
    ax2.tick_params(axis='y', labelsize=8)
    ax2_twin.tick_params(axis='y', labelsize=8)
    
    # Combine legends
    lines1, labels1 = ax2.get_legend_handles_labels()
    lines2, labels2 = ax2_twin.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=8)
    
    plt.tight_layout()
    plt.savefig('graphics/evolucion_metricas_compacta.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_dora_metrics():
    """Create compact DORA metrics visualization"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))
    
    # Lead Time comparison
    methods = ['Manual', 'CI/CD\\nAutomatizado']
    lead_times = [24, 4]  # hours
    
    bars1 = ax1.bar(methods, lead_times, color=['#ff6b6b', '#4ecdc4'], alpha=0.8)
    ax1.set_title('Lead Time (Horas)', fontsize=10, fontweight='bold')
    ax1.set_ylabel('Horas', fontsize=9)
    for i, v in enumerate(lead_times):
        ax1.text(i, v + 0.5, str(v), ha='center', va='bottom', fontweight='bold')
    
    # Deployment Frequency
    freq_labels = ['Semanal', 'Mensual', 'Trimestral']
    freq_values = [70, 25, 5]
    
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    ax2.pie(freq_values, labels=freq_labels, colors=colors, autopct='%1.1f%%', 
            startangle=90, textprops={'fontsize': 8})
    ax2.set_title('Frecuencia de Despliegue\\n(Equipos Elite)', fontsize=10, fontweight='bold')
    
    # MTTR (Mean Time to Recovery)
    mttr_data = ['Antes', 'Después']
    mttr_values = [120, 15]  # minutes
    
    bars3 = ax3.bar(mttr_data, mttr_values, color=['#ff6b6b', '#4ecdc4'], alpha=0.8)
    ax3.set_title('MTTR (Minutos)', fontsize=10, fontweight='bold')
    ax3.set_ylabel('Minutos', fontsize=9)
    for i, v in enumerate(mttr_values):
        ax3.text(i, v + 3, str(v), ha='center', va='bottom', fontweight='bold')
    
    # Change Failure Rate
    failure_labels = ['Antes', 'Después']
    failure_values = [25, 5]  # percentage
    
    bars4 = ax4.bar(failure_labels, failure_values, color=['#ff6b6b', '#4ecdc4'], alpha=0.8)
    ax4.set_title('Tasa de Fallos (%)', fontsize=10, fontweight='bold')
    ax4.set_ylabel('Porcentaje', fontsize=9)
    for i, v in enumerate(failure_values):
        ax4.text(i, v + 0.5, str(v), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('graphics/metricas_dora_compacta.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_roi_analysis():
    """Create compact ROI and benefits analysis"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # ROI over time
    months = np.arange(1, 25)
    roi_cumulative = np.concatenate([
        np.linspace(-100, -50, 6),  # Investment phase
        np.linspace(-50, 0, 6),     # Break-even phase  
        np.linspace(0, 250, 12)     # Profit phase
    ])
    
    ax1.plot(months, roi_cumulative, linewidth=3, color='#2E8B57')
    ax1.fill_between(months, roi_cumulative, alpha=0.3, color='#2E8B57')
    ax1.set_title('ROI Proyectado (24 meses)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('ROI Acumulado (%)', fontsize=9)
    ax1.set_xlabel('Meses', fontsize=9)
    ax1.axhline(y=0, color='red', linestyle='--', alpha=0.7, label='Break-even')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=8)
    
    # Cost-benefit breakdown
    categories = ['Inversión\\nInicial', 'Mantenimiento\\nReducido', 'Nuevas\\nFunciones']
    values = [100, -40, 60]  # Relative values
    colors = ['#ff7f7f', '#7fbf7f', '#7f7fff']
    
    bars = ax2.bar(categories, values, color=colors, alpha=0.8)
    ax2.set_title('Análisis Costo-Beneficio', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Impacto Relativo (%)', fontsize=9)
    ax2.axhline(y=0, color='black', linestyle='-', alpha=0.5)
    
    for i, v in enumerate(values):
        if v > 0:
            ax2.text(i, v + 2, f'+{v}%', ha='center', va='bottom', fontweight='bold')
        else:
            ax2.text(i, v - 2, f'{v}%', ha='center', va='top', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('graphics/roi_beneficios_compacto.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_success_factors():
    """Create compact success factors visualization"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # Success factors importance
    factors = ['Cobertura\\nPruebas', 'Experiencia\\nEquipo', 'Complejidad\\nDominio', 'Gasto\\nProyecto']
    weights = [4.2, 3.8, 2.5, 1.2]
    
    bars = ax1.barh(factors, weights, color=['#ff6b6b', '#4ecdc4', '#45b7d1', '#f9ca24'])
    ax1.set_title('Factores Predictivos de Éxito\\n(Peso OR)', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Importancia (Peso OR)', fontsize=9)
    
    for i, v in enumerate(weights):
        ax1.text(v + 0.05, i, f'{v}', va='center', fontweight='bold')
    
    # Implementation phases
    phases = ['Planificación', 'Cimientos', 'Desarrollo', 'Pruebas', 'Implementación']
    effort = [15, 25, 35, 15, 10]
    
    colors = plt.cm.Set3(np.linspace(0, 1, len(phases)))
    wedges, texts, autotexts = ax2.pie(effort, labels=phases, colors=colors, 
                                       autopct='%1.1f%%', startangle=90,
                                       textprops={'fontsize': 8})
    ax2.set_title('Distribución de Esfuerzo\\npor Fase', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('graphics/factores_exito_compacto.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_devops_correlation():
    """Create compact DevOps correlation chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # DevOps maturity vs quality
    maturity_levels = ['Básico', 'Intermedio', 'Avanzado', 'Élite']
    quality_scores = [45, 65, 80, 95]
    team_satisfaction = [50, 70, 85, 92]
    
    x = np.arange(len(maturity_levels))
    width = 0.35
    
    bars1 = ax1.bar(x - width/2, quality_scores, width, label='Calidad del Software', 
                    color='#4ecdc4', alpha=0.8)
    bars2 = ax1.bar(x + width/2, team_satisfaction, width, label='Satisfacción del Equipo', 
                    color='#ff6b6b', alpha=0.8)
    
    ax1.set_title('Correlación DevOps vs Resultados', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Puntuación (%)', fontsize=9)
    ax1.set_xlabel('Nivel de Madurez DevOps', fontsize=9)
    ax1.set_xticks(x)
    ax1.set_xticklabels(maturity_levels)
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3)
    
    # Practice adoption impact
    practices = ['TDD', 'CI/CD', 'Code\\nReview', 'Automatización\\nSeguridad']
    impact_scores = [85, 90, 75, 80]
    
    bars = ax2.bar(practices, impact_scores, color=['#a8e6cf', '#dcedc8', '#f8bbd9', '#e1bee7'], alpha=0.8)
    ax2.set_title('Impacto de Prácticas DevSecOps', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Mejora en Calidad (%)', fontsize=9)
    ax2.tick_params(axis='x', rotation=45, labelsize=8)
    
    for i, v in enumerate(impact_scores):
        ax2.text(i, v + 1, f'{v}%', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('graphics/correlacion_devops_compacta.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    print("Creating compact circular and chart replacements...")
    
    create_pie_chart_comparison()
    print("Created architectural comparison charts")
    
    create_metrics_evolution()
    print("Created metrics evolution chart")
    
    create_dora_metrics()
    print("Created DORA metrics chart")
    
    create_roi_analysis()
    print("Created ROI analysis chart")
    
    create_success_factors()
    print("Created success factors chart")
    
    create_devops_correlation()
    print("Created DevOps correlation chart")
    
    print("\nAll compact charts created successfully!")
