from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponseBadRequest
import json
from .static.python.clasif_cartas import Prueba_6
from .static.python.senalamiento_autodirigido import Prueba_2
from .static.python.ordenamiento import Prueba_3
from .static.python.cartas import Prueba_10
from .static.python.refranes import Prueba_11
from .static.python.memoria_visoespacial import Prueba_14

from PROCEEDING.models import Proceeding
from BANFE.models import *

# Create your views here.

prueba_senalamiento = Prueba_2()
prueba_ordenamiento = Prueba_3()
prueba_clasif_cartas = Prueba_6()
prueba_cartas = Prueba_10()
prueba_refranes = Prueba_11()
prueba_memoria = Prueba_14()


# Variables de control lógico
terminar = 0
    
def inicio(request):
    return render(request, "principal/home-image.html")  

def about(request):
    return render(request, "principal/footer_links/about.html")  

def contact(request):
    return render(request, "principal/footer_links/contact.html")  

def under_construction(request):
    return render(request, 'principal/under_construction.html')

def pruebas(request):
    id_proceeding = request.GET.get('pid')
    return render(request,"principal/pruebas.html",{"id_proceeding":id_proceeding})

def filter_proceedings(request):
    # Obtener los parámetros de búsqueda
    pid = request.GET.get('pid', None)
    gender = request.GET.get('gender', None)
    scholarship = request.GET.get('scholarship', None)

    print(scholarship)

    # Iniciar con todos los objetos Expedientes
    proceedings = Proceeding.objects.filter(user=request.user)
    
    # Filtrar por id si está presente
    if pid:
        proc_id = int(pid)
        proceeding = get_object_or_404(Proceeding, id=proc_id, user=request.user)
        
        # Convertir el QuerySet a una lista de diccionarios
        proceeding = [{'id': proceeding.id, 'name': proceeding.name+" "+proceeding.first_last_name+" "+proceeding.second_last_name, 'dateBirth': proceeding.dateNac}]
    else:
        proceeding = None
    # Filtrar por género si está presente
    if gender:
        proceedings = proceedings.filter(gender=gender)

    # Filtrar por escolaridad si está presente
    if scholarship:
        print(scholarship)
        proceedings = proceedings.filter(scholarship=scholarship)

    # Convertir el QuerySet a una lista de diccionarios
    proceedings = [{'id': item.id, 'name': item.name+" "+item.first_last_name+" "+item.second_last_name, 'dateBirth': item.dateNac} for item in proceedings]
    print(proceedings)

    return JsonResponse({'proceedings':proceedings, 'proceeding':proceeding})

def render_prueba_template(request, template_name, prueba):
    pid = request.GET.get('pid')
    if pid is not None:
        try:
            proc_id = int(pid)
            proceedings = Proceeding.objects.filter(user=request.user)
            if proc_id > 0:
                proceeding = get_object_or_404(Proceeding, id=proc_id, user=request.user)
                return render(request, template_name, {"proceedings": proceedings, "pid": proceeding.id, "dateBirth": proceeding.dateNac, "prueba":prueba})
            else:
                return render(request, template_name, {"proceedings": proceedings, "pid": proc_id, "prueba": prueba})
        except ValueError:
            return HttpResponseBadRequest("El valor de pid no es válido")
    else:
        return HttpResponseBadRequest("El valor de pid no está presente en la solicitud")


# Función para crear una instancia de BANFE y asociarla con una instancia de Cortex si existe
def create_banfe_instance(pid, prueba):
    # Buscar una instancia de Cortex con el nombre dado
    cortex_instance = Cortex.objects.filter(name=prueba).first()

    # Crear una instancia de BANFE con el PID proporcionado
    proceeding_instance = Proceeding.objects.get(id=pid)
    banfe_instance = BANFE.objects.create(proceeding=proceeding_instance)

    # Si se encuentra una instancia de Cortex, asociarla con la instancia de BANFE
    if cortex_instance:
        banfe_instance.area.add(cortex_instance)
    
    # Devolver la instancia de BANFE creada
    return banfe_instance

# Vista para la prueba 'pruebas_cof'
def pruebas_cof(request):
    if request.method == 'POST':
        # Si la solicitud es POST, obtener los datos del cuerpo de la solicitud JSON
        data = json.loads(request.body)

        # Crear una instancia de BANFE y asociarla con una instancia de Cortex si corresponde
        banfe_instance = create_banfe_instance(data.get('pid'), data.get('prueba'))
        
        # Devolver una respuesta JSON indicando que la prueba se creó exitosamente
        return JsonResponse({'status': 'BANFE-2 Created Successfully', 'banfe_id': banfe_instance.id})
    else:
        # Si la solicitud no es POST, obtener el parámetro 'prueba' de la solicitud GET
        prueba = request.GET.get('prueba')

        # Renderizar la plantilla con el parámetro 'prueba'
        return render_prueba_template(request, "principal/pruebas_cof.html", prueba)

# Vistas similares para las pruebas 'pruebas_cpfdl', 'pruebas_cpfa' y 'pruebas_todas'
# La lógica es la misma, solo cambia el nombre de la prueba y la plantilla renderizada

def pruebas_cpfdl(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        banfe_instance = create_banfe_instance(data.get('pid'), data.get('prueba'))
        # Devolver una respuesta JSON indicando que la prueba se creó exitosamente
        return JsonResponse({'status': 'BANFE-2 Created Successfully', 'banfe_id': banfe_instance.id})
    else:
        prueba = request.GET.get('prueba')
        return render_prueba_template(request, "principal/pruebas_cpfdl.html", prueba)

def pruebas_cpfa(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        print("MANOS A LA OBRA: ",data.get('prueba'))
        print("RECIBIMOS: ",data)
        banfe_instance = create_banfe_instance(data.get('pid'), data.get('prueba'))

        # Devolver una respuesta JSON indicando que la prueba se creó exitosamente
        return JsonResponse({'status': 'BANFE-2 Created Successfully', 'banfe_id': banfe_instance.id})
    else:
        prueba = request.GET.get('prueba')
        return render_prueba_template(request, "principal/pruebas_cpfa.html", prueba)

def pruebas_todas(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data.get('prueba'))
        if data.get('prueba') == 'allTests':
            name_cortex = ['Prefrontal Anterior', 'Orbitomedial', 'Dorsolateral']
            print(name_cortex)
        elif data.get('prueba') == 'copfaTests':
            name_cortex = ['Prefrontal Anterior', 'Orbitomedial']
            print(name_cortex)
        elif data.get('prueba') == 'cofdoTests':            
            name_cortex = ['Orbitomedial', 'Dorsolateral']
            print(name_cortex)
        else:
            name_cortex = ['Prefrontal Anterior', 'Dorsolateral']
            print(name_cortex)

        # Buscar instancias de Cortex con los nombres dados
        cortex_instances = Cortex.objects.filter(name__in=name_cortex)
        print(cortex_instances)

        # Crear una instancia de BANFE y asociarla con las instancias de Cortex encontradas
        proceeding_instance = Proceeding.objects.get(id=data.get('pid'))
        banfe_instance = BANFE.objects.create(proceeding=proceeding_instance)

        for cortex_instance in cortex_instances:
            banfe_instance.area.add(cortex_instance)

        # Devolver una respuesta JSON indicando que la prueba se creó exitosamente
        return JsonResponse({'status': 'BANFE-2 Created Successfully', 'banfe_id': banfe_instance.id})

    else:    
        prueba = request.GET.get('prueba')
        return render_prueba_template(request, "principal/pruebas_todas.html", prueba)

def laberintos_control(request):
    if request.method == 'POST':
        # Obtener los datos de la solicitud
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')
        print(results)

        # Crear una instancia del modelo Labytrinths
        labyrinth = Labyrinths(
            touch = results[0],
            cross = results[1],
            caught = results[2],
            time = results[3],
            banfe_test_id = data.get('banfe')
        )

        # Guardar la instancia en la base de datos
        labyrinth.save()

        print(labyrinth)

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)
        
        resultados = {
            "num_prueba": 1,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista":lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe
        }

    return render(request, "banfe-2/otras-pruebas/laberintos.html", resultados)


def senalamiento_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)

        # Crear una instancia del modelo Signaling
        signaling = Signaling(
            successes = results[0],
            perseverations = results[1],
            omissions = results[2],
            time = results[3],
            banfe_test_id = data.get('banfe')
        )

        # Guardar la instancia en la base de datos
        signaling.save()

        print(signaling)

        prueba_senalamiento.limpiar_variables()

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)
        
        resultados = {
            "aciertos": prueba_senalamiento.aciertos,
            "perseveraciones": prueba_senalamiento.perseveraciones,
            "omisiones": prueba_senalamiento.calcular_omisiones(),
            "terminar": prueba_senalamiento.terminar,
            "num_prueba": 2,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista": lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe
        }


    return render(request, "banfe-2/senalamiento-autodirigido/senalamiento-control.html", resultados)

def senalamiento(request):    
    prueba_senalamiento.limpiar_variables()
    return render(request, "banfe-2/senalamiento-autodirigido/senalamiento.html")

def seleccionar_figura(request, figura):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            figura = data.get('data')
            prueba_senalamiento.seleccionar(figura)        
            return JsonResponse({'status':'Take Card'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def terminar_prueba(request, fin):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            fin = data.get('data')
            prueba_senalamiento.apagar(fin)    
            return JsonResponse({'status':'Take Card'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def ordenamiento_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)

        if len(results) > 8:
            # Crear una instancia del modelo Ordering
            ordering = Ordering(
                essays_first_list = results[0],
                order_errors_first = results[1],
                perseverations_first = results[2],
                intrusions_first = results[3],
                essays_second_list = results[4],
                order_errors_second = results[5],
                perseverations_second = results[6],
                intrusions_second = results[7],
                essays_third_list = results[8],
                order_errors_third = results[9],
                perseverations_third = results[10],
                intrusions_third = results[11],
                banfe_test_id = data.get('banfe')
            )
            
        else:
            # Crear una instancia del modelo Ordering
            ordering = Ordering(
                essays_first_list = results[0],
                order_errors_first = results[1],
                perseverations_first = results[2],
                intrusions_first = results[3],
                essays_second_list = results[4],
                order_errors_second = results[5],
                perseverations_second = results[6],
                intrusions_second = results[7],
                essays_third_list = None,
                order_errors_third = None,
                perseverations_third = None,
                intrusions_third = None,
                banfe_test_id = data.get('banfe')
            )
            

        # Guardar la instancia en la base de datos
        ordering.save()

        print(ordering)
        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)

        if prueba_ordenamiento.reiniciar == 1:
            prueba_ordenamiento.limpiar_ordenamiento()


        resultados = {
            "num_ensayo_1": prueba_ordenamiento.num_ensayo[0],
            "error_orden_1": prueba_ordenamiento.error_orden[0],
            "perseveraciones_1": prueba_ordenamiento.perseveraciones[0],
            "intrusiones_1": prueba_ordenamiento.intrusiones[0],
            "num_ensayo_2": prueba_ordenamiento.num_ensayo[1],
            "error_orden_2": prueba_ordenamiento.error_orden[1],
            "perseveraciones_2": prueba_ordenamiento.perseveraciones[1],
            "intrusiones_2": prueba_ordenamiento.intrusiones[1],
            "num_ensayo_3": prueba_ordenamiento.num_ensayo[2],
            "error_orden_3": prueba_ordenamiento.error_orden[2],
            "perseveraciones_3": prueba_ordenamiento.perseveraciones[2],
            "intrusiones_3": prueba_ordenamiento.intrusiones[2],
            "result_ensayo": prueba_ordenamiento.estado,
            "num_prueba": 3,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista": lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe
        }

        print(lista)

    return render(request, "banfe-2/otras-pruebas/ordenamiento.html", resultados)

def leer_palabra(request,palabra):
    crawler = ['',0,0]
    i = 0
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            for x in data['data']:
                crawler[i] = x
                i += 1
            prueba_ordenamiento.comparar_palabra(crawler[0],int(crawler[1]),int(crawler[2]))
            return JsonResponse({'status':'Take Card'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')    

def comprobar_ordenamiento(request,lista):
    data = {'message': "Success", 'estado': prueba_ordenamiento.comprobar_ensayo(lista)}
    print("dekdnendnkendken: ", data)
    return JsonResponse(data)    

def reiniciar_ordenamiento(request, reiniciar):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            prueba_ordenamiento.reiniciar = data.get('data')  
            return JsonResponse({'status':'Take Card'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def resta_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)


        if len(results) > 3:
            # Crear una instancia del modelo Subtraction
            substraction = Substraction(
                successes_a = results[0],
                mistakes_a = results[1],
                time_a = results[2],
                successes_b = results[3],
                mistakes_b = results[4],
                time_b = results[5],
                banfe_test_id = data.get('banfe')
            )
        else:
            # Crear una instancia del modelo Subtraction
            substraction = Substraction(
                successes_a = results[0],
                mistakes_a = results[1],
                time_a = results[2],
                successes_b = None,
                mistakes_b = None,
                time_b = None,
                banfe_test_id = data.get('banfe')
            )


        # Guardar la instancia en la base de datos
        substraction.save()

        print(substraction)

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)
        
        resultados = {
            "num_prueba": 4,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista":lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe
        }
    return render(request, "banfe-2/otras-pruebas/resta.html", resultados)

def suma_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)

        # Crear una instancia del modelo Addition
        addition = Addition(
            successes = results[0],
            mistakes = results[1],
            time = results[2],
            banfe_test_id = data.get('banfe')
        )

        # Guardar la instancia en la base de datos
        addition.save()

        print(addition)

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)
        
        resultados = {
            "num_prueba": 5,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista":lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe
        }
    return render(request, "banfe-2/otras-pruebas/suma.html", resultados)

def clasif_cartas_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)

        # Crear una instancia del modelo Card_Sorting
        card_sorting = Card_Sorting(
            successes = results[0],
            mistakes = results[1],
            perseverations = results[2],
            deferred_perseverations = results[3],
            maintenance_error = results[4],
            time = results[5],
            banfe_test_id = data.get('banfe')
        )

        # Guardar la instancia en la base de datos
        card_sorting.save()

        print(card_sorting)

        prueba_clasif_cartas.limpiar_prueba()

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)
        
        resultados = {
            "aciertos": prueba_clasif_cartas.aciertos,
            "errores": prueba_clasif_cartas.errores,
            "perseveraciones": prueba_clasif_cartas.perseveraciones,
            "error_mantenimiento": prueba_clasif_cartas.err_mant,
            "persev_diferidas": prueba_clasif_cartas.pers_dif,
            "num_prueba": 6,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista": lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe        
    }
    return render(request, "banfe-2/clasif-cartas/clasif-cartas-control.html", resultados)

def clasif_cartas(request):    
    prueba_clasif_cartas.limpiar_prueba()
    return render(request, "banfe-2/clasif-cartas/clasif-cartas.html")

def tomar_carta(request, carta):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            carta = data.get('data')
            prueba_clasif_cartas.asignar_valores(carta)
            return JsonResponse({'status':'Take Card'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
    

def colocar_carta(request, posicion):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            posicion = data.get('data')
            prueba_clasif_cartas.evaluar_respuesta(posicion)            
            return JsonResponse({'status':'Take Card'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
    
def mensaje_incorrecto(request,error,posicion):
    if prueba_clasif_cartas.incorrecto:
        data = {'message': "Success", 'error': 1}
    else:
        data = {'message': "Success", 'error': 0}
    return JsonResponse(data)

def semanticas_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)

        # Crear una instancia del modelo Semantic_Classification
        semantic_classification = Semantic_Classification(
            specific_categories = results[0],
            functional_categories = results[1],
            abstract_categories = results[2],
            total_categories = results[3],
            total_average = results[4],
            total_score = results[5],
            banfe_test_id = data.get('banfe')
        )

        # Guardar la instancia en la base de datos
        semantic_classification.save()

        print(semantic_classification)        
        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)
        
        resultados = {
            "num_prueba": 7,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista":lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe
        }

    return render(request, "banfe-2/clasif-semanticas/clasif-semanticas-control.html", resultados)

def semanticas(request):    
    return render(request, "banfe-2/clasif-semanticas/clasif-semanticas.html")

def stroopA_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)

        # Crear una instancia del modelo Stroop_A
        stroop_a = Stroop_A(
        
            successes = results[0],
            stroop_errors = results[1],
            non_stroop_errors = results[2],
            time = results[3],
            banfe_test_id = data.get('banfe')
        )

        # Guardar la instancia en la base de datos
        stroop_a.save()

        print(stroop_a)  

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)
        
        resultados = {
            "num_prueba": 8,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista":lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe
        }

    return render(request, "banfe-2/stroopA/stroopA-control.html", resultados)

def stroopA(request):    
    return render(request, "banfe-2/stroopA/stroopA.html")

def fluidez_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)

        # Crear una instancia del modelo Verbal_Fluency
        verbal_fluency = Verbal_Fluency(
            successes = results[0],
            perseverations = results[1],
            intrusions = results[2],
            banfe_test_id = data.get('banfe')
        )

        # Guardar la instancia en la base de datos
        verbal_fluency.save()

        print(verbal_fluency)  

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)
        
        resultados = {
            "num_prueba": 9,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista":lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe
        }

    return render(request, "banfe-2/otras-pruebas/fluidez-verbal.html", resultados)

def cartas_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)

        # Crear una instancia del modelo Cards_Game
        cards_game = Cards_Game(
            total_score = results[0],
            percentage_risk_cards=results[1].replace('%', ''),  # Eliminar el carácter '%'
            first_question = results[2],
            second_question = results[3],
            third_question = results[4],
            fourth_question = results[5],
            banfe_test_id = data.get('banfe')
        )

        # Guardar la instancia en la base de datos
        cards_game.save()

        print(cards_game)  

        prueba_cartas.limpiar_cartas()

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)

        resultados = {
            "carta_1": prueba_cartas.cartas[0],
            "carta_2": prueba_cartas.cartas[1],
            "carta_3": prueba_cartas.cartas[2],
            "carta_4": prueba_cartas.cartas[3],
            "carta_5": prueba_cartas.cartas[4],
            "punto_1": prueba_cartas.cartas[0],
            "punto_2": prueba_cartas.cartas[1]*2,
            "punto_3": prueba_cartas.cartas[2]*3,
            "punto_4": prueba_cartas.cartas[3]*4,
            "punto_5": prueba_cartas.cartas[4]*5,
            "castigop_1": prueba_cartas.castigos[0],
            "castigop_2": prueba_cartas.castigos[1],
            "castigop_3": prueba_cartas.castigos[2],
            "castigop_4": prueba_cartas.castigos[3],
            "castigop_5": prueba_cartas.castigos[4],
            "castigo_1": prueba_cartas.castigos[0]*2,
            "castigo_2": prueba_cartas.castigos[1]*3,
            "castigo_3": prueba_cartas.castigos[2]*5,
            "castigo_4": prueba_cartas.castigos[3]*8,
            "castigo_5": prueba_cartas.castigos[4]*12,
            "cartas_puntos": prueba_cartas.cartas_puntos,
            "cartas_castigos": prueba_cartas.cartas_castigos,
            "total_puntos": prueba_cartas.total_puntos,
            "total_castigos": prueba_cartas.total_castigos,
            "puntuacion": prueba_cartas.puntuacion,
            "porcentaje": prueba_cartas.porcentaje,
            "fin_cartas": prueba_cartas.terminar,
            "num_prueba": 10,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista": lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe   
        }
    
    return render(request, "banfe-2/juego-cartas/cartas-control.html", resultados)

def cartas(request):    
    prueba_cartas.limpiar_cartas()
    return render(request, "banfe-2/juego-cartas/cartas.html")

def escoger_carta(request, carta):
    crawler = [0,0]
    i = 0
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            for x in data['data']:
                crawler[i] = x
                i += 1
            prueba_cartas.anotar_carta(int(crawler[0]),int(crawler[1]))
            return JsonResponse({'status':'Take Card'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')    

def terminar_cartas(request, fin):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            fin = data.get('data')
            prueba_cartas.apagar(fin)    
            return JsonResponse({'status':'Take Card'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def refranes_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)

        # Crear una instancia del modelo Sayings
        sayings = Sayings(
            successes = results[0],
            time = results[1],
            banfe_test_id = data.get('banfe')
        )

        # Guardar la instancia en la base de datos
        sayings.save()

        print(sayings)  

        prueba_refranes.limpiar_refranes()

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)

        
        resultados = {
            "refran_p1": prueba_refranes.puntos_ganados[0],
            "refran_p2": prueba_refranes.puntos_ganados[1],
            "refran_p3": prueba_refranes.puntos_ganados[2],
            "refran_p4": prueba_refranes.puntos_ganados[3],
            "refran_p5": prueba_refranes.puntos_ganados[4],
            "aciertos_refranes": prueba_refranes.aciertos,
            "terminar_refran": prueba_refranes.fin,
            "num_prueba": 11,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista": lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe                   
        }
        
    return render(request, "banfe-2/refranes/refranes-control.html", resultados)

def refranes(request):    
    prueba_refranes.limpiar_refranes()
    return render(request, "banfe-2/refranes/refranes.html")

def calificar_respuesta(request,opcion):
    crawler = [0,'']
    i = 0
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            for x in data['data']:
                crawler[i] = x
                i += 1
            prueba_refranes.evaluar_respuesta(crawler[0],crawler[1])
            return JsonResponse({'status':'Take Card'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')    
    
def terminar_refranes(request, terminar):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            terminar = data.get('data')
            prueba_refranes.fin = terminar 
            return JsonResponse({'status':'Take Card'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')


def torres_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)
        print("TAMAÑO: ",len(results))

        if len(results) > 5:
            # Crear una instancia del modelo Towers_Hanoi
            towers_hanoi = Towers_Hanoi(
                movements_first = results[0],
                time_first = results[1],
                type_1_error_first = results[2],
                type_2_error_first = results[3],
                total_error_first = results[4],
                movements_second = results[5],
                time_second = results[6],
                type_1_error_second = results[7],
                type_2_error_second = results[8],
                total_error_second = results[9],
                banfe_test_id = data.get('banfe')
            )
        else:
            # Crear una instancia del modelo Towers_Hanoi
            towers_hanoi = Towers_Hanoi(
                movements_first = results[0],
                time_first = results[1],
                type_1_error_first = results[2],
                type_2_error_first = results[3],
                total_error_first = results[4],
                movements_second = None,
                time_second = None,
                type_1_error_second = None,
                type_2_error_second = None,
                total_error_second = None,
                banfe_test_id = data.get('banfe')
            )            

        # Guardar la instancia en la base de datos
        towers_hanoi.save()

        print(towers_hanoi)  

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)
        
        resultados = {
            "num_prueba": 12,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista":lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe
        }

    return render(request, "banfe-2/otras-pruebas/torres-hanoi.html", resultados)

def metamemoria_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)

        # Crear una instancia del modelo Metamemory
        metamemory = Metamemory(
            intrusions = results[0],
            perseverations = results[1],
            positive_errors = results[2],
            negative_errors = results[3],
            total_errors = results[4],                       
            banfe_test_id = data.get('banfe')
        )

        # Guardar la instancia en la base de datos
        metamemory.save()

        print(metamemory)  

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)
        
        resultados = {
            "num_prueba": 13,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista":lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe
        }

    return render(request, "banfe-2/otras-pruebas/metamemoria.html", resultados)

def memoria_control(request):
    # Recuperar el estado de test_started de la sesión
    test_started = request.session.get('test_started', False)

    print("SI LLEGO AL SERVIDOR")
    if request.method == 'POST':
        print("SOY POST")
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)

        # Crear una instancia del modelo Visuospatial_Memory
        visuospatial_memory = Visuospatial_Memory(
            order_errors = results[0],
            substitution_errors = results[1],
            perseverations = results[2],
            maximum_sequence = results[3],                       
            banfe_test_id = data.get('banfe')
        )

        # Guardar la instancia en la base de datos
        visuospatial_memory.save()

        print(visuospatial_memory)  

        prueba_memoria.limpiar_variables()

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)

        if not test_started:
            prueba_memoria.limpiar_variables()
            # Establecer test_started a True en la sesión
            request.session['test_started'] = True
        
        resultados = {
            "secuencia": prueba_memoria.secuencia_maxima(),
            "perseveraciones": prueba_memoria.perseveraciones,
            "err_sust": prueba_memoria.sustituciones,
            "err_ord": prueba_memoria.error_orden,
            "memoria_fin": prueba_memoria.fin,
            "num_prueba": 14,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista": lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe                 
        }

    return render(request, "banfe-2/memoria-visoespacial/memoria-control.html", resultados)

def memoria(request):    
    prueba_memoria.limpiar_variables()
    return render(request, "banfe-2/memoria-visoespacial/memoria.html")

def escoger_figura(request, nom_figura):
    crawler = ['',0,0,'']
    i = 0
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            for x in data['data']:
                crawler[i] = x
                i += 1
            prueba_memoria.comparar(crawler[0],int(crawler[1]),int(crawler[2]))
            return JsonResponse({'status':'Take Card'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')    

def comprobar_memoria(request,error):
    for key in prueba_memoria.figuras_pers:
        prueba_memoria.figuras_pers[key] = 0

    if (prueba_memoria.aciertos == 4 and prueba_memoria.figura == 4) or (prueba_memoria.aciertos == 5 and prueba_memoria.figura == 5) or (prueba_memoria.aciertos == 6 and prueba_memoria.figura == 6) or (prueba_memoria.aciertos == 7 and prueba_memoria.figura == 7):
        data = {'message': "Success", 'error': 1}
        if(prueba_memoria.nivel != 4):
            prueba_memoria.aciertos = 0
    else:
        prueba_memoria.aciertos = 0
        data = {'message': "Success", 'error': 0}
    return JsonResponse(data)

def terminar_memoria(request, terminar):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            terminar = data.get('data')
            prueba_memoria.fin = terminar
            return JsonResponse({'status':'Take Card'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def stroopB_control(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data.get('pid')
        data.get('banfe')
        results = data.get('result')

        print(results)

        # Crear una instancia del modelo Stroop_B
        stroop_b = Stroop_B(
            successes = results[0],
            stroop_errors = results[1],
            non_stroop_errors = results[2],
            time = results[3],                       
            banfe_test_id = data.get('banfe')
        )

        # Guardar la instancia en la base de datos
        stroop_b.save()

        print(stroop_b)  

        return JsonResponse({'status': 'Test Created Successfully', 'banfe_id': data.get('banfe')})        
        
    else:
        pid = request.GET.get('pid')
        age = request.GET.get('edad')
        lista = json.loads(request.GET.get('lista'))
        test = request.GET.get('num_prueba')
        banfe = request.GET.get('banfe')
        print(banfe)
        
        resultados = {
            "num_prueba": 15,
            "proceeding": Proceeding.objects.get(id=int(pid)),
            "age": age,
            "lista":lista,
            "prueba_actual": test,
            "total_pruebas": len(lista),
            "longitud_barra": int(test)*100/(len(lista)),
            "banfe": banfe
        }
    return render(request, "banfe-2/stroopB/stroopB-control.html", resultados)

def stroopB(request):    
    return render(request, "banfe-2/stroopB/stroopB.html")

