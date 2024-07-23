import csv
from decimal import Decimal
from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.db.models import Count
from django.template.loader import get_template
from weasyprint import HTML
from django.views.decorators.csrf import csrf_exempt
from BANFE.models import *
from PROCEEDING.models import Proceeding
from .static.python.results_test import Result, Details_BANFE

# Auxiliar Functions

def calculate_age(dateNac):
    """
    Calcula la edad dado una fecha de nacimiento.

    Args:
    - dateNac (date): Fecha de nacimiento.

    Returns:
    - int: Edad calculada.
    """
    today = date.today()
    age = today.year - dateNac.year - ((today.month, today.day) < (dateNac.month, dateNac.day))
    return int(age)

def get_proceeding_name(proceeding):
    """
    Obtiene el nombre completo de un Proceeding.

    Args:
    - proceeding (Proceeding): Objeto Proceeding.

    Returns:
    - str: Nombre completo del Proceeding.
    """
    return f"{proceeding.name} {proceeding.first_last_name} {proceeding.second_last_name}"

def convert_decimal_to_float(data):
    """
    Convierte decimales en un diccionario dado en floats.

    Args:
    - data (dict): Datos que pueden contener decimales.

    Returns:
    - dict: Datos convertidos con decimales a floats.
    """
    if isinstance(data, dict):
        return {k: convert_decimal_to_float(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_decimal_to_float(i) for i in data]
    elif isinstance(data, Decimal):
        return float(data)
    else:
        return data

# Create your views here.
def show_tests(request):
    return render(request, "list_banfe.html")

def list_tests(request):
    """
    Lista todos los tests asociados a Proceedings del usuario actual.

    Returns:
    - JsonResponse: Datos JSON con los tests asociados.
    """

    # Obtener los Proceedings que tienen al menos un BANFE asociado
    proceedings = Proceeding.objects.annotate(num_banfes=Count('banfe')).filter(num_banfes__gt=0, user=request.user)
    
    # Crear una lista para almacenar los datos de los Proceeding y sus BANFE asociados
    data = []

    # Iterar sobre cada Proceeding
    for proceeding in proceedings:
        banfe_results = get_banfe_results(proceeding)
        tests_data = create_tests_data(proceeding, banfe_results)
        data.append(tests_data)

    return JsonResponse(data, safe=False)

def get_banfe_results(proceeding):
    """
    Obtiene los resultados de todos los BANFEs asociados a un Proceeding.

    Args:
    - proceeding (Proceeding): Objeto Proceeding.

    Returns:
    - list: Lista de resultados de los BANFEs.
    """
    banfes = BANFE.objects.filter(proceeding=proceeding)
    banfe_results = []

    for banfe in banfes:
        result = Result(banfe.id, calculate_age(proceeding.dateNac), proceeding.years_study)
        banfe_results.append(result.show_scores())

    return banfe_results


def create_tests_data(proceeding, banfe_results):
    """
    Crea un diccionario con los datos de un Proceeding y sus BANFEs asociados.

    Args:
    - proceeding (Proceeding): Objeto Proceeding.
    - banfe_results (list): Lista de resultados de los BANFEs.

    Returns:
    - dict: Datos del Proceeding y sus BANFEs asociados.
    """
    return {
        'proceeding_name': get_proceeding_name(proceeding),
        'banfe_results': banfe_results
    }

def details_banfe(request):
    """
    Muestra los detalles de un BANFE específico.

    Returns:
    - HttpResponse: Respuesta con los detalles del BANFE.
    """
    banfe_id = request.GET.get('banfe', None)
    banfe = get_banfe(banfe_id)
    proceeding = Proceeding.objects.filter(banfe__id=banfe_id).first()

    result = Result(banfe.id, calculate_age(proceeding.dateNac), proceeding.years_study)
    banfe_results = result.show_scores()

    details = Details_BANFE(banfe.id, calculate_age(proceeding.dateNac), proceeding.years_study)

    banfe_test_result = {
        "test": banfe.id,
        'proceeding_name': get_proceeding_name(proceeding),
        'proceeding_age': calculate_age(proceeding.dateNac),
        'date_evaluation': proceeding.dateEval.isoformat(),
        'data_banfe': details.get_data(),
        'scores': banfe_results
    }

    # Convertir Decimals a floats
    banfe_test_result = convert_decimal_to_float(banfe_test_result)

    # Guardar datos en la sesión
    request.session['banfe_test_result'] = banfe_test_result

    return render(request, "details_banfe.html", banfe_test_result)

def export_table_pdf(request):
    """
    Exporta los datos almacenados en la sesión como un archivo PDF.

    Returns:
    - HttpResponse: Respuesta con el archivo PDF generado.
    """
    # Obtener los datos desde la sesión
    banfe_test_result = request.session.get('banfe_test_result')
    if not banfe_test_result:
        raise Http404("No data found in session.")
    
    # Obtener el objeto BANFE asociado al resultado para verificar permisos si es necesario
    banfe = get_object_or_404(BANFE, id=banfe_test_result['test'])

    # Obtener el Proceeding asociado al BANFE para verificar permisos si es necesario
    proceeding = Proceeding.objects.filter(banfe__id=banfe.id).first()
    if not proceeding or proceeding.user != request.user:
        raise Http404("Proceeding not found or you do not have permission to access it.")

    # Cargar el template HTML con los datos incluidos
    template = get_template('banfe_sheet.html')
    html_string = template.render(banfe_test_result)

    # Crear el PDF
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    # Crear una respuesta HTTP con el tipo de contenido PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="hoja_resumen.pdf"'

    return response

@csrf_exempt
def export_selected_tests_csv(request):
    print("Inicio de exportación CSV")
    
    if request.method == 'POST':
        print("Solicitud POST recibida")
        
        test_ids = request.POST.getlist('test_ids[]')
        if not test_ids:
            print("No se proporcionaron IDs de pruebas")
            return HttpResponse(status=400)

        print(f"IDs de pruebas seleccionadas: {test_ids}")
        
        # Crear la respuesta Http para el CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="selected_tests.csv"'

        writer = csv.writer(response)
        # Escribir encabezados del CSV
        writer.writerow(['No. Expediente','Nombre del participante', 'Laberintos (Atravesar)', 'Juego de cartas (Porcentaje de cartas de riesgo)', 'Juego de cartas (Puntuación total)', 'Stroop A (Errores stroop)', 'Stroop A (Tiempo)', 'Stroop A (Aciertos)', 'Stroop B (Errores stroop)', 'Stroop B (Tiempo)', 'Stroop B (Aciertos)', 'Clasificación de cartas (Errores de mantenimiento)', 'Total orbitomedial', 'Clasificación semántica (Número de categorías astractas)', 'Selección de refranes (Tiempo)', 'Selección de refranes (Aciertos)', 'Metamemoria (Errores negativos)', 'Metamemoria (Errores positivos)', 'Total Prefrontal', 'Señalamiento autodirigido (Persevaraciones)', 'Señalamiento autodirigido (Tiempo)', 'Señalamiento autodirigido (Aciertos)', 'Resta A (Tiempo)', 'Resta A (Aciertos)', 'Resta B (Tiempo)', 'Resta B (Aciertos)', 'Suma (Tiempo)', 'Suma (Aciertos)', 'Ordenamiento alfabético (Ensayo 1)', 'Ordenamiento alfabético (Ensayo 2)', 'Ordenamiento alfabético (Ensayo 3)', 'Memoria visoespacial (Secuencia máxima)', 'Memoria visoespacial (Perseveraciones)', 'Memoria visoespacial (Errores de orden)', 'Subtotal Memoria de trabajo', 'Laberintos (Planeación [sin salida])', 'Laberintos (Tiempo)', 'Clasificación de cartas (Aciertos)', 'Clasificación de cartas (Perseveraciones)', 'Clasificación de cartas (Perseveraciones diferidas)', 'Clasificación de cartas (Tiempo)', 'Clasificación semántica (Total de categorías)', 'Clasificación semántica (Promedio total animales)', 'Clasificación semántica (Puntaje total)', 'Fluidez verbal (Aciertos)', 'Fluidez verbal (Perseveraciones)', 'Torre de Hanoi 3 discos (Movimientos)', 'Torre de Hanoi 3 discos (Tiempo)', 'Torre de Hanoi 4 discos (Movimientos)', 'Torre de Hanoi 4 discos (Tiempo)', 'Subtotal Funciones ejecutivas', 'Total Dorsolateral', 'Total Batería'])
        
        # Iterar sobre los IDs de las pruebas seleccionadas
        for banfe_id in test_ids:
            print(f"Procesando prueba con ID: {banfe_id}")
            banfe_details = get_data_banfe(banfe_id)
            print(f"Detalles de la prueba {banfe_id}: {banfe_details}")

            areas = {
                'orbitomedial': ['encoded_orbitomedial', 'diagnosis_orbitomedial'],
                'prefrontal': ['encoded_prefrontal', 'diagnosis_prefrontal'],
                'dorsolateral': ['encoded_dorsolateral', 'diagnosis_dorsolateral']
            }

            # Verificar qué áreas están aplicadas
            applied_areas = {area: all(banfe_details['scores'][key] != 'NO APLICADA' for key in keys) for area, keys in areas.items()}

            # Verificar si todas las áreas aplicadas son las tres principales
            all_applied_areas = all(applied_areas.values())

            full_row =  [
                banfe_details['test'], 
                banfe_details['proceeding_name'], 
                banfe_details['data_banfe']['encoded_labyrinths']['cross'] if applied_areas['orbitomedial'] else 'NA',
                banfe_details['data_banfe']['encoded_game']['percentage_risk_cards'] if applied_areas['orbitomedial'] else 'NA',
                banfe_details['data_banfe']['encoded_game']['total_score'] if applied_areas['orbitomedial'] else 'NA',
                banfe_details['data_banfe']['encoded_stroopA']['stroop_errors'] if applied_areas['orbitomedial'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['encoded_stroopA']['time'] if applied_areas['orbitomedial'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['natural_stroopA']['successes'] if applied_areas['orbitomedial'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['encoded_stroopB']['stroop_errors'] if applied_areas['orbitomedial'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['encoded_stroopB']['time'] if applied_areas['orbitomedial'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['natural_stroopB']['successes'] if applied_areas['orbitomedial'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['encoded_cards']['maintenance_error'] if applied_areas['orbitomedial'] else 'NA',
                banfe_details['scores']['encoded_orbitomedial'] if applied_areas['orbitomedial'] else 'NA',
                banfe_details['data_banfe']['encoded_semantic']['abstract_categories'] if applied_areas['prefrontal'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['encoded_sayings']['time'] if applied_areas['prefrontal'] and banfe_details['proceeding_age'] >= 10 else 'NA',
                banfe_details['data_banfe']['natural_sayings']['successes'] if applied_areas['prefrontal']  and banfe_details['proceeding_age'] >= 10 else 'NA',
                banfe_details['data_banfe']['encoded_metamemory']['positive_errors'] if applied_areas['prefrontal'] else 'NA',
                banfe_details['data_banfe']['encoded_metamemory']['negative_errors'] if applied_areas['prefrontal'] else 'NA',
                banfe_details['scores']['encoded_prefrontal'] if applied_areas['prefrontal'] else 'NA',
                banfe_details['data_banfe']['encoded_signaling']['perseverations'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_signaling']['time'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['natural_signaling']['successes'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_substraction']['time_a'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['natural_substraction']['successes_a'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['encoded_substraction']['time_b'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 10 else 'NA',
                banfe_details['data_banfe']['natural_substraction']['successes_b'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 10 else 'NA',
                banfe_details['data_banfe']['encoded_addition']['time'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['natural_addition']['successes'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['encoded_ordering']['essays_first_list'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['encoded_ordering']['essays_second_list'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['encoded_ordering']['essays_third_list'] if applied_areas['dorsolateral'] and (banfe_details['proceeding_age'] >= 10 and (banfe_details['proceeding_age'] <= 30 or (banfe_details['proceeding_age'] >= 31 and banfe_details['proceeding_age'] <= 55 and banfe_details['proceeding_study'] > 3 and banfe_details['proceeding_study'] < 10))) else 'NA',
                banfe_details['data_banfe']['natural_memory']['maximum_sequence'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['encoded_memory']['perseverations'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['data_banfe']['encoded_memory']['order_errors'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 8 else 'NA',
                banfe_details['scores']['work_memory'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_labyrinths']['caught'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_labyrinths']['time'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['natural_cards']['successes'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_cards']['perseverations'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_cards']['deferred_perseverations'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_cards']['time'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_semantic']['total_categories'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_semantic']['total_average'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_semantic']['total_score'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_fluency']['successes'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_fluency']['perseverations'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_towers']['movements_first'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_towers']['time_first'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['data_banfe']['encoded_towers']['movements_second'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 10 else 'NA',
                banfe_details['data_banfe']['encoded_towers']['time_second'] if applied_areas['dorsolateral'] and banfe_details['proceeding_age'] >= 10 else 'NA',
                banfe_details['scores']['executive_functions'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['scores']['encoded_dorsolateral'] if applied_areas['dorsolateral'] else 'NA',
                banfe_details['scores']['encoded_total'] if all_applied_areas else 'NA'                
            ]
        
            writer.writerow(full_row)
        print("Exportación de CSV completada")
        return response

    else:
        return HttpResponse(status=405)  # Método no permitido



# Funciones para obtener datos
def get_banfe(banfe_id):
    """
    Obtiene un objeto BANFE por su ID.

    Args:
    - banfe_id (int): ID del BANFE.

    Returns:
    - BANFE: Objeto BANFE.
    """
    return get_object_or_404(BANFE, id=banfe_id)

def get_data_banfe(banfe_id):
    """
    Obtiene los datos detallados de un BANFE específico.

    Args:
    - banfe_id (int): ID del BANFE.

    Returns:
    - dict: Diccionario con los detalles del BANFE.
    """
    banfe = get_banfe(banfe_id)
    proceeding = Proceeding.objects.filter(banfe__id=banfe_id).first()
    result = Result(banfe.id, calculate_age(proceeding.dateNac), proceeding.years_study)
    banfe_results = result.show_scores()
    details = Details_BANFE(banfe.id, calculate_age(proceeding.dateNac), proceeding.years_study)

    banfe_test_result = {
        "test": banfe.id,
        'proceeding_name': get_proceeding_name(proceeding),
        'proceeding_age': calculate_age(proceeding.dateNac),
        'proceeding_study': proceeding.years_study,
        'date_evaluation': proceeding.dateEval.isoformat(),
        'data_banfe': details.get_data(),
        'scores': banfe_results
    }

    banfe_test_result = convert_decimal_to_float(banfe_test_result)
    return banfe_test_result


