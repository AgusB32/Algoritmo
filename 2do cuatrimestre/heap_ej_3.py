from heap import HeapMin

class Operation:
    def __init__(self, in_charge, description, time, priority, stormtroopers=None):
        self.in_charge = in_charge
        self.description = description
        self.time = time
        self.priority = priority
        self.stormtroopers = stormtroopers

    def __str__(self):
        troopers = f", Stormtroopers: {self.stormtroopers}" if self.stormtroopers else ""
        return f"Encargado: {self.in_charge}, Descripción: {self.description}, Hora: {self.time}, Prioridad: {self.priority}{troopers}"

# Inicializamos la cola de prioridad usando HeapMin
priority_queue = HeapMin()

# Función para agregar operaciones a la cola de prioridad
def add_operation(in_charge, description, time, priority, stormtroopers=None):
    operation = Operation(in_charge, description, time, priority, stormtroopers)
    priority_queue.arrive(operation, priority)

# Función para atender operaciones
def attend_operation():
    if priority_queue.elements:
        operation = priority_queue.atention()[1]
        print(f"Atendiendo operación: {operation}")
        return operation
    else:
        print("No hay más operaciones en la cola.")
        return None

# c. Cargamos al menos 10 operaciones (2 de nivel 3, 4 de nivel 2, 4 de nivel 1)
add_operation("Líder Supremo Snoke", "Revisión del sistema de armas", "10:00", 3)
add_operation("Kylo Ren", "Revisión del sable láser", "10:30", 3)

add_operation("Capitán Phasma", "Entrenamiento de Stormtroopers", "11:00", 2, 50)
add_operation("Capitán Phasma", "Inspección de seguridad", "11:30", 2)
add_operation("General Hux", "Mantenimiento del escudo", "12:00", 1)
add_operation("General Hux", "Revisión del sistema de energía", "12:30", 1)
add_operation("General Hux", "Revisión de los TIE Fighters", "13:00", 1)
add_operation("Capitán Phasma", "Inspección de naves de transporte", "13:30", 2)
add_operation("General Hux", "Revisión de los androides", "14:00", 1)

# e. Atender las operaciones
print("\nAtendiendo operaciones:")
for i in range(5):
    attend_operation()

# f. Luego de atender la quinta operación, agregar operación solicitada por Capitán Phasma
print("\nAgregando operación de Capitán Phasma (Revisión de intrusos en el hangar B7):")
add_operation("Capitán Phasma", "Revisión de intrusos en el hangar B7", "14:30", 2, 25)

# Atender la siguiente operación
attend_operation()

# g. Luego de atender la sexta operación, agregar operación solicitada por el Líder Supremo Snoke
print("\nAgregando operación de Líder Supremo Snoke (Destrucción del planeta Takodana):")
add_operation("Líder Supremo Snoke", "Destrucción del planeta Takodana", "15:00", 3)

# Atender las operaciones restantes
while priority_queue.elements:
    attend_operation()