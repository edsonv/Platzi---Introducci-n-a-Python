import threading
import time


def process_request(request_id):
    print(f"Procesando solicitud {request_id}")
    time.sleep(3)
    print(f"Solicitud {request_id} completada ")


threads = []

for i in range(3):
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    # Asegura que el programa espere a que cada hilo termine
    thread.join()

print("Todas las solicitudes fueron completadas")
