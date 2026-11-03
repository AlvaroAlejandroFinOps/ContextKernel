# ContextKernel: Plano de Control de Contexto y Atención

**ContextKernel es un plano de control de contexto y atención para agentes de ingeniería de IA.** Actualizaciones de evidencia incremental, skills portables para Antigravity y Codex, arquitectura modular de paquetes y continuidad de sesión. Guía: [operación y migración v6](docs/specs/icontext-v6.md).
<!-- ICONTEXT-V6:RELEASE -->


**Idioma:** [English](README.md) | [Español](README_ES.md)

[![Standard](https://img.shields.io/badge/Standard-Enterprise%20Paper--Grade%20v6.1-2b2b2b?style=flat-square)](#)
[![Ecosystem](https://img.shields.io/badge/Ecosystem-Multi--AI%20%28Google%20%7C%20Claude%20%7C%20OpenAI%20%7C%20Cursor%29-34495e?style=flat-square)](#)
[![iContext Federation](https://img.shields.io/badge/iContext-Federated%20v6.1-1a1a1a?style=flat-square)](#)
[![iDirectory L0](https://img.shields.io/badge/L0-iDirectory%20v6.1-2b2b2b?style=flat-square)](#)
[![ThinkingSeed L1](https://img.shields.io/badge/L1-ThinkingSeed%20v6.1-34495e?style=flat-square)](#)
[![MetricsThinking L2](https://img.shields.io/badge/L2-MetricsThinking%20v6.1-4b5563?style=flat-square)](#)
[![iReadme L3](https://img.shields.io/badge/L3-iReadme%20v6.1-000000?style=flat-square)](#)
[![Engine](https://img.shields.io/badge/Engine-ContextKernel%20Core-1a1a1a?style=flat-square)](#)

---

## 1. Resumen Ejecutivo

Los sistemas de software empresarial modernos, las plataformas de datos en la nube y los agentes autónomos de IA enfrentan una severa fricción arquitectónica derivada de topologías desestructuradas, derivas no rastreadas de contratos y fronteras de contexto desalineadas. En ausencia de una gobernanza determinista, los equipos de alta velocidad acumulan deuda cognitiva, comprometiendo los tiempos de incorporación técnica y rompiendo la orquestación agéntica autónoma en clusters productivos.

ContextKernel coordina la sincronización, auditoría y fronteras de contexto mediante un monorepo modular unificado y un runtime versionado. Actualiza evidencia incremental, propaga fallos entre capas y entrega al agente anfitrión actual secciones aisladas de SeedMaster y documentación para redacción quirúrgica. No se han medido ahorros de TCO ni cumplimiento de SLA.

La arquitectura opera bajo un modelo de ingesta universal multi-IA, funcionando de manera homogénea en Google Antigravity, Anthropic Claude Code, OpenAI ChatGPT/Codex y Cursor IDE. Mediante sincronización dual de idiomas (Inglés/Español), formulación matemática en KaTeX, insignias sobrias de alto impacto y topologías simétricas en ASCII, ContextKernel entrega transparencia institucional tanto para líderes tecnológicos como para ingenieros principales.

---

## 2. Arquitectura y Topología del Sistema

El sistema implementa una separación arquitectónica estricta entre el Plano de Control de Ingesta, el Núcleo Analítico Autónomo y el Plano de Estado Sincronizado de Artefactos.

```
+---------------------------------------------------------------------------------------------------+
|                                  TOPOLOGÍA DEL MONOREPO CONTEXTKERNEL                             |
+---------------------------------------------------------------------------------------------------+
                                                  |
                 +--------------------------------+--------------------------------+
                 |                                                                 |
                 v                                                                 v
+----------------------------------+                              +----------------------------------+
|    PLANO DE CONTROL DE INGESTA   |                              |      PLANO DE DATOS Y ANALÍTICA  |
|  - Orquestadores Multi-IA        |                              |  - Motor de Alto Rendimiento Rust|
|  - Cápsulas de Contexto Aisladas |                              |  - Verificación Espectral FPIA   |
|  - Integridad por Topology Hash  |                              |  - Cumplimiento de Invariantes   |
+----------------------------------+                              +----------------------------------+
                 |                                                                 |
                 +--------------------------------+--------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                                PLANO DE ARTEFACTOS SINCRONIZADOS                                  |
|  - Artefactos Duales Enterprise Paper-Grade (README.md / README_ES.md con paridad phi = 1.0)     |
|  - Satélites Criptográficos (.context/tree.json & .context/icontext_bus.json)                     |
|  - SeedMasters Jerárquicos (Vector General Raíz y Seeds Modulares por Subpaquete)                 |
+---------------------------------------------------------------------------------------------------+
```

### Protocolo Federado de Control de Contexto (FCCP v6.1)

Este monorepo implementa formalmente el **Protocolo Federado de Control de Contexto v6.1**, orquestando **5 paquetes canónicos** bajo `packages/` para gobernanza agéntica autónoma y optimización atencional:

| Capa | Componente | Directorio de Paquete | Función Principal de Ingeniería | Estado |
| :--- | :--- | :--- | :--- | :--- |
| `CLI` | **ContextKernel CLI** | `packages/contextkernel-cli` | Interfaz de línea de comandos universal, runtime de orquestación, continuidad de sesión e instalador de skills multi-agente. | `ACTIVE (v6.1)` |
| `L0` | **iDirectory** | `packages/idirectory` | Gobierna la topología canónica all-lowercase, balizas semánticas (`.context.yaml`), satélite criptográfico (`tree.json`), presupuestos de tokens y aislamiento mediante cápsulas (<450 tokens). | `ACTIVE (v6.1)` |
| `L1` | **ThinkingSeed** | `packages/thinkingseed` | Preserva la memoria técnica y contratos simbólicos AST sin fuga de código fuente (Zero Source Code), auditado bajo validación estricta de 6 gates deterministas. | `ACTIVE (v6.1)` |
| `L2` | **MetricsThinking** | `packages/metricsthinking` | Calcula madurez por Ground Truth en 10 módulos canónicos, deriva semántica AST, eficiencia espectral FPIA ($S_{\text{spectral}}$, $PF_{\text{spectral}}$) y escaneo de seguridad Zero-Trust. | `ACTIVE (v6.1)` |
| `L3` | **iReadme** | `packages/ireadme` | Sincroniza documentación dual inglés/español bajo el estándar Enterprise Paper-Grade, garantizando paridad estructural $\Phi = 1.0$, formulación formal en KaTeX y cero fugas de ruta local. | `ACTIVE (v6.1)` |

La interoperabilidad entre estas herramientas se orquesta de manera no-bloqueante a través del **Bus Cognitivo Federado** (`./.context/icontext_bus.json`), garantizando continuidad atencional, cero deriva satelital y protección estricta contra alucinaciones en agentes autónomos.

---

## 3. Formulación Matemática y Motores Analíticos

La estabilidad arquitectónica y eficiencia computacional de ContextKernel están gobernadas por modelos matemáticos formales de optimización.

Sea $\mathcal{T}$ la topología rastreada del sistema de archivos, donde cada nodo $n_i \in \mathcal{T}$ posee un estado de activación $\alpha_i \in \{0, 1\}$ gobernado por balizas de contexto. El presupuesto atencional activo $\Omega(\mathcal{T})$ se formaliza como:

$$\Omega(\mathcal{T}) = \sum_{i=1}^{N} \alpha_i \cdot \tau(n_i)$$

donde $\tau(n_i)$ representa el peso estimado en tokens del artefacto $n_i$. El factor de potencia espectral FPIA $PF_{\text{spectral}}$ evalúa la eficiencia cognitiva:

$$PF_{\text{spectral}} = \frac{P_{\text{activo}}}{\sqrt{P_{\text{activo}}^2 + Q_{\text{muerto}}^2 + Q_{\text{duplicado}}^2 + D_{\text{estructural}}^2}}$$

La paridad estructural documental $\Phi$ entre las variantes de idioma se certifica deterministamente:

$$\Phi = \frac{1}{M} \sum_{m=1}^{M} \mathbb{I}(\text{Sección}_{m}^{\text{EN}} \equiv \text{Sección}_{m}^{\text{ES}}) = 1.0$$

La potencia espectral aparente $S_{\text{spectral}}$ cuantifica la entropía multidimensional del repositorio:

$$S_{\text{spectral}} = \sqrt{P^2 + (Q_{\text{muerto}} + Q_{\text{duplicado}})^2 + D^2}$$

---

## 4. Rendimiento Empírico y Benchmarks

<!-- ICONTEXT-V6:TELEMETRY:START -->
| Evidence / Evidencia | Recorded value / Valor registrado |
| :--- | :--- |
| Metrics score | 80.5 |
| Estimated spectral factor (auxiliary) | 0.9777 |
| Query latency p95 (ms) | 7.313400041311979 |
| Validity | Recorded evidence; verify freshness with icontext audit |
<!-- ICONTEXT-V6:TELEMETRY:END -->

La versión 6.1 consolida los 4 productos independientes en un único monorepo modular, erradicando árboles de runtime duplicados y eliminando la deriva de sincronización entre repositorios. Las mediciones de esta entrega se registran en `.context/benchmark_v6.json`; incluyen p50/p95 del motor y del proceso, lecturas de archivos y comparación con inventario completo. Los tokens son estimaciones explícitas. Las métricas de atención del modelo requieren sesiones observadas y no se deducen de FPAI.

---

## 5. Estructura del Repositorio y Artefactos

El repositorio sigue estrictamente la topología canónica normalizada en minúsculas (`all-lowercase`) y un workspace modular de paquetes:

```
ContextKernel/
├── .context/                          # Satélites de estado (tree.json, checkpoint.json, icontext_bus.json)
├── 01_seed/                           # SeedMaster General (seed-contextkernel-master.md)
├── config/                            # Políticas parametrizadas y configuración desacoplada
├── schemas/                           # Esquemas formales JSON Schema Draft-07
├── packages/                          # Módulos de alta ingeniería aislados
│   ├── contextkernel-cli/             # Entrypoint CLI universal, runtime e instalador de skills
│   ├── idirectory/                    # Capa L0: Plano de control topológico, balizas y satélite tree
│   ├── thinkingseed/                  # Capa L1: ADN arquitectónico simbólico y 6 gates deterministas
│   ├── metricsthinking/               # Capa L2: Auditor forense, motor espectral FPIA, backend Rust
│   └── ireadme/                       # Capa L3: Sintetizador documental bilingüe Paper-Grade
├── skills/                            # Bundles de skills para agentes (icontext, idir, seed, seed-master, metrics, readme)
├── pyproject.toml                     # Configuración del workspace raíz y dependencias unificadas
├── Contex.code-workspace              # Configuración multi-root de IDE
├── FWengine.py                        # Launcher de compatibilidad topológica (L0)
└── icontext.py                        # Launcher del CLI Maestro Universal (L0-L3)
```

---

## 6. Protocolo de Ejecución y Verificación

### Orden Canónico de Ejecución

ContextKernel establece un ciclo de vida determinista en 3 etapas: **(1) Inicializar Carpeta Vacía**, **(2) Actualizar y Sincronizar ContextKernel**, y **(3) Auditar y Verificar la Salud del Sistema**. Los comandos usan rutas absolutas para ejecución directa e inmediata desde cualquier directorio de trabajo:

```powershell
# ==============================================================================
# ETAPA 1: INICIALIZAR UNA CARPETA VACÍA (Andamiaje de un Nuevo Workspace)
# ==============================================================================
# Inicializa la topología canónica all-lowercase, balizas semánticas (.context.yaml),
# políticas de contexto y satélite criptográfico (.context/tree.json) en la carpeta destino:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextKernel\icontext.py" init "D:\Proyectos\MiProyectoDestino"
# O alternativamente mediante el motor topológico L0 directo:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextKernel\FWengine.py" init "D:\Proyectos\MiProyectoDestino"

# ==============================================================================
# ETAPA 2: ACTUALIZAR CONTEXTKERNEL (Reconciliación, Sincronización y Empaquetado)
# ==============================================================================
# 1. Reconciliar topología física, validar balizas y reconstruir satélite tree.json:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextKernel\FWengine.py" reconcile

# 2. Sincronizar todas las capas federadas (L0 iDirectory, L1 ThinkingSeed, L2 MetricsThinking, L3 iReadme):
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextKernel\icontext.py" sync --all

# 3. Simulación de sincronización para inspeccionar deltas pendientes sin mutar archivos:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextKernel\icontext.py" sync --dry-run --all

# 4. Generar cápsula quirúrgica de contexto (<450 tokens) para subagentes:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextKernel\icontext.py" pack packages/idirectory --tier 1a --json

# 5. Extraer seed modular quirúrgica para trabajo atencionalmente eficiente en un paquete:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextKernel\icontext.py" prepare seed --target packages/metricsthinking

# ==============================================================================
# ETAPA 3: AUDITAR Y VERIFICAR (Auditoría Forense, Diagnóstico y Suite de Pruebas)
# ==============================================================================
# 1. Inspeccionar el último estado registrado de todas las capas:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextKernel\icontext.py" status --all

# 2. Ejecutar auditoría forense profunda de evidencias en todos los componentes (M01-M10, AST drift, PII):
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextKernel\icontext.py" audit --all

# 3. Diagnosticar la salud del ecosistema, integridad del runtime y skills activas:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextKernel\icontext.py" doctor

# 4. Reparar automáticamente inconsistencias de capitalización y reinstalar skills dañadas:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextKernel\icontext.py" doctor --fix

# 5. Ejecutar suite integral de pruebas automatizadas (239+ pruebas unitarias y de integración):
python -m pytest "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextKernel\packages" --import-mode=importlib -v
```

`status` muestra el último estado registrado; `audit` verifica la evidencia actual. `reconcile` restaura los nombres canónicos en minúsculas cuando el motor detecta una diferencia de capitalización, sincroniza las balizas y reconstruye el satélite. `reconcile --check` informa la deriva sin modificar archivos.

---

## 7. Glosario de Dominio

- **Cápsula de Contexto**: Carga quirúrgica ultra-densa en formato JSON (<450 tokens) diseñada para subagentes, previniendo degradación atencional.
- **Topology Hash**: Huella criptográfica SHA-256 representativa de la estructura gobernada de directorios, asegurando cero derivas satelitales.
- **Bus Federado**: Vector de estado interoperable (`.context/icontext_bus.json`) que sincroniza las capas L0, L1, L2 y L3 de forma no-bloqueante.
- **Índice de Paridad ($\Phi$)**: Invariante estricto de coincidencia 1 a 1 entre los artefactos documentales en inglés y español.
- **SeedMasters Jerárquicos**: Sistema de vectores arquitectónicos en dos niveles: SeedMaster General en la raíz para fronteras del ecosistema, y SeedMasters Modulares por paquete para tareas quirúrgicas con ahorro de tokens.

---

## 8. Referencias Académicas y de Ingeniería

1. **Dean, J., & Ghemawat, S.** (2004). *MapReduce: Simplified Data Processing on Large Clusters*. Communications of the ACM.
2. **Gamma, E., et al.** (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
3. **Gravity HyperScale Thinking**. (2026). *ContextKernel: Universal Context & Attention Control Plane for AI Engineering Agents*.

```bibtex
@article{contextkernel2026architecture,
  title={ContextKernel: Universal Context & Attention Control Plane for AI Engineering Agents},
  author={Gravity HyperScale Thinking Systems Architecture Lab},
  year={2026},
  institution={Gravity HyperScale Thinking}
}
```
