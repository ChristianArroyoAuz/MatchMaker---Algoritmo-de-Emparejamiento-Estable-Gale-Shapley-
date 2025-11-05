# 💕 MatchMaker - Algoritmo de Emparejamiento Estable (Gale-Shapley)

## 🎯 **Repositorio: Stable-Matching-Algorithm**

**Descripción del Repositorio:**
*"Implementación del famoso algoritmo Gale-Shapley para emparejamiento estable entre dos conjuntos. Perfecto para sistemas de matching en residencias médicas, admisiones universitarias y aplicaciones de citas. ¡Garantía matemática de estabilidad!"*

---

## 📋 **Resumen del Proyecto - Algoritmo de Emparejamiento Estable**

### 🎯 **Propósito General**
Implementación del algoritmo **Gale-Shapley** que resuelve el problema del emparejamiento estable entre dos conjuntos de entidades con preferencias mutuas, garantizando que no existan parejas que prefieran estar juntas antes que con sus asignaciones actuales.

## 🏥 **Contexto del Caso de Uso**

### **Escenario Principal: Hospitales ↔ Estudiantes de Medicina**
- **Hospitales**: Atlanta, Boston, Chicago, Detroit, El Paso
- **Estudiantes**: Val, Wayne, Xavier, Yolanda, Zeus
- **Aplicación real**: Sistema de residencias médicas (NRMP)

## 🧮 **El Algoritmo Gale-Shapley**

### **📖 Fundamentos Matemáticos**
- **Garantía**: Siempre encuentra un emparejamiento estable
- **Optimalidad**: Mejor posible para el grupo que propone
- **Complejidad**: O(n²) donde n es el número de participantes
- **Estabilidad**: No existen "bloqueos" en el emparejamiento final

### **🔄 Proceso Iterativo**
```python
while existan hospitales sin emparejar:
    1. Hospital sin emparejar hace propuesta a su siguiente estudiante preferido
    2. Estudiante evalúa la propuesta:
       - Si está libre: acepta
       - Si está emparejado: compara con su actual pareja
       - Elige la mejor opción según sus preferencias
```

## 🎨 **Características de Implementación**

### **🏗️ Arquitectura de Clases**
```python
class Emparejamiento_Estable:
    def mejor_opcion(self, elemento_entidad)
    def propuesta_de(self, elemento_entidad)
    def propuesta_a(self, elemento_entidad)
    def prospecto(self, elemento_entidad)
    def sin_emparejar(self)
    def liberar(self)
```

### **🎭 Entidades con Preferencias**
- **Cada hospital** tiene ranking de estudiantes preferidos
- **Cada estudiante** tiene ranking de hospitales preferidos
- **Preferencias** son listas ordenadas de mayor a menor preferencia

## 🔄 **Flujo del Algoritmo**

### **1. 📋 Inicialización**
```python
# Creación de objetos para hospitales y estudiantes
hospital = {}
estudiante = {}
# Asignación de listas de preferencias
```

### **2. 💌 Proceso de Propuestas**
- Hospitales libres proponen a su siguiente opción preferida
- Estudiantes evalúan propuestas comparando con emparejamiento actual
- Decisiones basadas en ranking de preferencias

### **3. ✅ Finalización**
- Todos los hospitales están emparejados
- Emparejamiento resultante es estable
- Resultados mostrados en formato claro

## 🎯 **Características Avanzadas**

### **⏱️ Visualización en Tiempo Real**
- **Sleeps estratégicos**: Para seguir el proceso paso a paso
- **Mensajes descriptivos**: Explicación de cada decisión
- **Transparencia completa**: Se ve toda la lógica de matching

### **🔄 Múltiples Configuraciones**
```python
# Ejemplo 0: Hospitales proponen a estudiantes
# Ejemplo 1: Mismo conjunto, diferente orden
# Ejemplo 2: Estudiantes proponen a hospitales (rol inverso)
```

## 💡 **Aplicaciones en el Mundo Real**

### **🏥 Sistemas de Salud**
- **Residencias médicas**: Matching entre hospitales y médicos graduados
- **Programas de especialización**: Asignación de plazas de formación

### **🎓 Educación Superior**
- **Admisiones universitarias**: Matching estudiantes-programas
- **Intercambios estudiantiles**: Asignación de destinos

### **💼 Recursos Humanos**
- **Placement de empleados**: Matching empresas-candidatos
- **Programas de rotación**: Asignación de departamentos

### **💝 Aplicaciones Sociales**
- **Sistemas de citas**: Matching basado en preferencias mutuas
- **Plataformas de networking**: Conexiones profesionales

## 📊 **Resultados y Estabilidad**

### **✅ Garantías del Algoritmo**
- **Emparejamiento estable**: No existen parejas que se prefieran mutuamente sobre sus asignaciones actuales
- **Optimalidad para proponentes**: Los hospitales obtienen su mejor emparejamiento posible
- **Terminación finita**: Siempre converge a una solución

### **🎭 Ejemplo de Output**
```
            Resultado de Emparejamiento

        (   Atlanta         ,   Wayne      )
        (   Boston          ,   Yolanda    )
        (   Chicago         ,   Zeus       )
        (   Detroit         ,   Val        )
        (   El Paso         ,   Xavier     )
```

## 🛠️ **Tecnologías Utilizadas**

| Tecnología | Propósito |
|------------|-----------|
| **Python 3** | Lenguaje de implementación |
| **Time.sleep()** | Visualización paso a paso |
| **Programación Orientada a Objetos** | Modelado de entidades |

## 🌟 **Valor Educativo**

### **🎓 Para Estudiantes de:**
- **Ciencias de la Computación**: Algoritmos y estructuras de datos
- **Matemáticas**: Teoría de juegos y optimización
- **Economía**: Mecanismos de mercado y matching
- **Investigación Operativa**: Problemas de asignación

### **💡 Conceptos Enseñados:**
- ✅ Algoritmos greedy
- ✅ Estabilidad en matching
- ✅ Optimalidad de Pareto
- ✅ Complejidad algorítmica
- ✅ Diseño de mecanismos

---

**¡El algoritmo que revolucionó los sistemas de matching y ganó el Premio Nobel de Economía 2012!** 🏆

*¿Listo para resolver problemas de emparejamiento en tu próximo proyecto? ¡Esta implementación es tu punto de partida!* 🚀

## 🚀 **Cómo Ejecutar**

```bash
python Python_Emparejamiento_Estable.py
```

**¡Experimenta la magia de las matemáticas creando emparejamientos perfectamente estables!** 💫
