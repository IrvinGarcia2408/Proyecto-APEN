from django.forms.models import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Country, State, Municipality, Proceeding


# Create your views here.

# Vista para mostrar la lista de procedimientos
def show_proceedings(request):
    return render(request, "proceedings/list-proceedings.html")

# Vista para obtener la lista de procedimientos
def list_proceedings(request):
    # Filtrar los procedimientos del usuario actual
    proceedings = Proceeding.objects.filter(user=request.user)
    
    # Convertir los objetos Proceeding en diccionarios
    proceedings_data = [model_to_dict(proceeding) for proceeding in proceedings]
    
    # Crear el diccionario de datos a ser enviado como respuesta JSON
    data = {'proceedings': proceedings_data}
    
    # Devolver la respuesta JSON
    return JsonResponse(data)


# Vista para crear un Proceeding
def create_proceeding(request):
    # Verificar si la solicitud es de tipo GET
    if request.method == 'GET':
        # Obtener la lista de países para mostrar en el formulario
        countries = [{'id': country.id, 'nombre': country.name} for country in Country.objects.all()]
        # Renderizar el formulario de creación de procedimiento con la lista de países
        return render(request, "proceedings/create-proceeding.html", {'countries': countries})  
    else:
        try:
            #   Creo la instancia del modelo Proceeding
            proceeding = Proceeding()

            # Asignar los valores del formulario a los campos del procedimiento
            proceeding.name = request.POST.get('name')
            proceeding.first_last_name = request.POST.get('first_last_name')
            proceeding.second_last_name = request.POST.get('second_last_name')
            proceeding.dateEval = request.POST.get('dateEval')
            proceeding.dateNac = request.POST.get('dateNac')
            proceeding.country =  Country.objects.get(id=request.POST.get('country'))
            
            # Verificar si se proporcionó un estado en el formulario
            if request.POST.get('state'):
                proceeding.state =  State.objects.get(id=request.POST.get('state'))
            else:
                proceeding.state = None


            # Verificar si se proporcionó un municipio en el formulario
            if request.POST.get('municipality'):
                proceeding.municipality =  Municipality.objects.get(id=request.POST.get('municipality'))
            else:
                proceeding.municipality = None


            proceeding.language = request.POST.get('language')
            proceeding.indigenous_language = request.POST.get('indigenous_language')

            # Verificar si se habla otro idioma además del indígena
            if request.POST.get('talk_other_language') == 'Si':
                proceeding.talk_other_language = True
                proceeding.other_languages = request.POST.get('other_languages')
            else:
                proceeding.talk_other_language = False
                proceeding.other_languages = None

            proceeding.gender =  request.POST.get('gender')
            proceeding.scholarship = request.POST.get('scholarship')
            proceeding.years_study = request.POST.get('years_study')
            proceeding.laterality = request.POST.get('laterality')
            proceeding.occupation = request.POST.get('occupation')
            proceeding.instrument =  request.POST.get('instrument')

            # Verificar si se proporcionó el tiempo de uso del instrumento musical
            if request.POST.get('time_instrument'):
                proceeding.time_instrument = request.POST.get('time_instrument')
            else:
                proceeding.time_instrument = None

            proceeding.hobbies =  request.POST.get('hobbies')
        
            # Verificar si se proporcionó el tiempo dedicado a los pasatiempos
            if request.POST.get('time_hobbies'):
                proceeding.time_hobbies = request.POST.get('time_hobbies')
            else:
                proceeding.time_hobbies = None

            proceeding.civil_status = request.POST.get('civil_status')
            proceeding.religion = request.POST.get('religion')
            proceeding.mother_scholarship = request.POST.get('mother_scholarship')
            proceeding.father_scholarship = request.POST.get('father_scholarship')
            proceeding.referred_by = request.POST.get('referred_by')
            proceeding.phone_number =  request.POST.get('phone_number')
            proceeding.reason_consultation =  request.POST.get('reason_consultation')
            proceeding.alert_status =  request.POST.get('alert_status')
            proceeding.medicine = request.POST.get('medicine')
            proceeding.other_exams = request.POST.get('other_exams')

            # Verificar si se proporcionó un historial médico
            if len(request.POST.get('medical_history').lstrip()):
                proceeding.medical_history = request.POST.get('medical_history').lstrip()
            else:
                proceeding.medical_history = None

            # Verificar si el paciente tiene hipertensión y, en ese caso, asignar el tiempo de diagnóstico
            if request.POST.get('hyperthension') == 'Si':
                proceeding.hyperthension = True
                proceeding.time_hyperthension = request.POST.get('time_hyperthension')
            else:
                proceeding.hyperthension = False
                proceeding.time_hyperthension = None

            # Verificar si el paciente tiene enfermedades pulmonares y, en ese caso, asignar el tiempo de diagnóstico
            if request.POST.get('pulmonary_diseases') == 'Si':
                proceeding.pulmonary_diseases = True
                proceeding.time_pulmonary_diseases = request.POST.get('time_pulmonary_diseases')
            else:
                proceeding.pulmonary_diseases = False
                proceeding.time_pulmonary_diseases = None

            # Verificar si el paciente es alcohólico y, en ese caso, asignar el tiempo de diagnóstico
            if request.POST.get('alcoholism') == 'Si':
                proceeding.alcoholism = True
                proceeding.time_alcoholism = request.POST.get('time_alcoholism')
            else:
                proceeding.alcoholism = False
                proceeding.time_alcoholism = None

            # Verificar si el paciente consume drogas y, en ese caso, asignar el tiempo de consumo
            if request.POST.get('drugs') == 'Si':
                proceeding.drugs = True
                proceeding.time_drugs = request.POST.get('time_drugs')
            else:
                proceeding.drugs = False
                proceeding.time_drugs = None

            # Verificar si el paciente presenta disminución de los sentidos y, en ese caso, asignar el tiempo de diagnóstico
            if request.POST.get('decrease_senses') == 'Si':
                proceeding.decrease_senses = True
                proceeding.time_decrease_senses = request.POST.get('time_decrease_senses')
            else:
                proceeding.decrease_senses = False
                proceeding.time_decrease_senses = None

            # Verificar si el paciente ha sufrido traumatismo craneoencefálico y, en ese caso, asignar el tiempo de diagnóstico
            if request.POST.get('craniocerebral_trauma') == 'Si':
                proceeding.craniocerebral_trauma = True
                proceeding.time_craniocerebral_trauma = request.POST.get('time_craniocerebral_trauma')
            else:
                proceeding.craniocerebral_trauma = False
                proceeding.time_craniocerebral_trauma = None

            # Verificar si el paciente tiene diabetes y, en ese caso, asignar el tiempo de diagnóstico
            if request.POST.get('diabetes') == 'Si':
                proceeding.diabetes = True
                proceeding.time_diabetes = request.POST.get('time_diabetes')
            else:
                proceeding.diabetes = False
                proceeding.time_diabetes = None

            # Verificar si el paciente tiene hipotiroidismo y, en ese caso, asignar el tiempo de diagnóstico
            if request.POST.get('hypothyroidism') == 'Si':
                proceeding.hypothyroidism = True
                proceeding.time_hypothyroidism = request.POST.get('time_hypothyroidism')
            else:
                proceeding.hypothyroidism = False
                proceeding.time_hypothyroidism = None

            # Verificar si el paciente ha sufrido accidentes cerebrovasculares y, en ese caso, asignar el tiempo de diagnóstico
            if request.POST.get('strokes') == 'Si':
                proceeding.strokes = True
                proceeding.time_strokes = request.POST.get('time_strokes')
            else:
                proceeding.strokes = False
                proceeding.time_strokes = None

            # Verificar si el paciente tiene otras enfermedades y, en ese caso, asignar los detalles
            if request.POST.get('others_diseases') == 'Si':
                proceeding.others_diseases = True
                proceeding.details_others_diseases = request.POST.get('details_others_diseases')
            else:
                proceeding.others_diseases = False
                proceeding.details_others_diseases = None             

            # Asignar el usuario actual al procedimiento
            proceeding.user = request.user

            # Guardar el procedimiento en la base de datos
            proceeding.save()

            # Redirigir a la vista de mostrar procedimientos
            return redirect('show_proceedings')
        except:
            # En caso de error, recuperar la lista de países y renderizar nuevamente el formulario con un mensaje de error
            countries= [{'id': country.id, 'nombre': country.name} for country in Country.objects.all()]
            return render(request, "proceedings/create-proceeding.html", {'countries': countries, 'error': 'Los datos ingresados son inválidos' })  

# Vista devuelve la lista de estados
def get_states(request):
    # Obtiene el ID del país de los parámetros de la solicitud GET
    country_id = request.GET.get('country')
    
    # Filtra los estados que pertenecen al país con el ID proporcionado
    states = State.objects.filter(country__id=country_id)
    
    # Convierte los objetos de estado filtrados en una lista de diccionarios JSON
    # Cada diccionario contiene las claves "id" y "name" para el ID y el nombre del estado respectivamente
    states_data = [{"id": state.pk, "name": state.name} for state in states]
    
    # Devuelve la lista JSON como respuesta a la solicitud
    # La opción safe=False se utiliza porque estamos devolviendo una lista JSON en lugar de un solo objeto JSON
    return JsonResponse(states_data, safe=False)

# Vista devuelve la lista de municipios
def get_municipalities(request):
    # Obtiene el ID del estado de los parámetros de la solicitud GET
    state_id = request.GET.get('state')
    
    # Filtra los municipios que pertenecen al estado con el ID proporcionado
    municipalities = Municipality.objects.filter(state__id=state_id)
    
    # Convierte los objetos de municipio filtrados en una lista de diccionarios JSON
    # Cada diccionario contiene las claves "id" y "name" para el ID y el nombre del municipio respectivamente
    municipalities_data = [{"id": municipality.id, "name": municipality.name} for municipality in municipalities]
    
    # Devuelve la lista JSON como respuesta a la solicitud
    # La opción safe=False se utiliza porque estamos devolviendo una lista JSON en lugar de un solo objeto JSON
    return JsonResponse(municipalities_data, safe=False)

# Vista para actualizar la información del Proceeding
def update_proceeding(request, proceeding_id):
    # Obtiene la instancia del procedimiento a actualizar
    proceeding = Proceeding.objects.get(id=proceeding_id, user=request.user)
    
    if request.method == 'GET':
        # Obtiene todos los países para mostrar en el formulario de actualización
        countries = [{'id': country.id, 'name': country.name} for country in Country.objects.all()]
        
        # Renderiza el formulario de actualización con los datos del procedimiento y la lista de países
        return render(request, "proceedings/update-proceeding.html", {'proceeding': proceeding, 'countries': countries})
    else:
        try:
            # Actualiza los campos del procedimiento con los datos enviados en la solicitud POST
            proceeding.name = request.POST.get('name')
            proceeding.first_last_name = request.POST.get('first_last_name')
            proceeding.second_last_name = request.POST.get('second_last_name')
            proceeding.dateEval = request.POST.get('dateEval')
            proceeding.dateNac = request.POST.get('dateNac')
            proceeding.country = Country.objects.get(id=request.POST.get('country'))
        
            if request.POST.get('state'):
                proceeding.state = State.objects.get(id=request.POST.get('state'))
            else:
                proceeding.state = None

            if request.POST.get('municipality'):
                proceeding.municipality = Municipality.objects.get(id=request.POST.get('municipality'))
            else:
                proceeding.municipality = None

            proceeding.language = request.POST.get('language')
            proceeding.indigenous_language = request.POST.get('indigenous_language')
        
            # Actualiza el campo de idiomas adicionales si es necesario
            if request.POST.get('talk_other_language') == 'Si':
                proceeding.talk_other_language = True
                proceeding.other_languages = request.POST.get('other_languages')
            else:
                proceeding.talk_other_language = False
                proceeding.other_languages = None

            proceeding.gender = request.POST.get('gender')
            proceeding.scholarship = request.POST.get('scholarship')
            proceeding.years_study = request.POST.get('years_study')
            proceeding.laterality = request.POST.get('laterality')
            proceeding.occupation = request.POST.get('occupation')
            proceeding.instrument = request.POST.get('instrument')

            proceeding.time_instrument = request.POST.get('time_instrument') if request.POST.get('time_instrument') else None
            proceeding.hobbies = request.POST.get('hobbies')
            proceeding.time_hobbies = request.POST.get('time_hobbies') if request.POST.get('time_hobbies') else None
            proceeding.civil_status = request.POST.get('civil_status')
            proceeding.religion = request.POST.get('religion')
            proceeding.mother_scholarship = request.POST.get('mother_scholarship')
            proceeding.father_scholarship = request.POST.get('father_scholarship')
            proceeding.referred_by = request.POST.get('referred_by')
            proceeding.phone_number = request.POST.get('phone_number')
            proceeding.reason_consultation = request.POST.get('reason_consultation')
            proceeding.alert_status = request.POST.get('alert_status')
            proceeding.medicine = request.POST.get('medicine')
            proceeding.other_exams = request.POST.get('other_exams')
            proceeding.medical_history = request.POST.get('medical_history').lstrip() if len(request.POST.get('medical_history').lstrip()) else None

            proceeding.hyperthension = True if request.POST.get('hyperthension') == 'Si' else False
            proceeding.time_hyperthension = request.POST.get('time_hyperthension') if request.POST.get('hyperthension') == 'Si' else None

            proceeding.pulmonary_diseases = True if request.POST.get('pulmonary_diseases') == 'Si' else False
            proceeding.time_pulmonary_diseases = request.POST.get('time_pulmonary_diseases') if request.POST.get('pulmonary_diseases') == 'Si' else None

            proceeding.alcoholism = True if request.POST.get('alcoholism') == 'Si' else False
            proceeding.time_alcoholism = request.POST.get('time_alcoholism') if request.POST.get('alcoholism') == 'Si' else None

            proceeding.drugs = True if request.POST.get('drugs') == 'Si' else False
            proceeding.time_drugs = request.POST.get('time_drugs') if request.POST.get('drugs') == 'Si' else None

            proceeding.decrease_senses = True if request.POST.get('decrease_senses') == 'Si' else False
            proceeding.time_decrease_senses = request.POST.get('time_decrease_senses') if request.POST.get('decrease_senses') == 'Si' else None

            proceeding.craniocerebral_trauma = True if request.POST.get('craniocerebral_trauma') == 'Si' else False
            proceeding.time_craniocerebral_trauma = request.POST.get('time_craniocerebral_trauma') if request.POST.get('craniocerebral_trauma') == 'Si' else None

            proceeding.diabetes = True if request.POST.get('diabetes') == 'Si' else False
            proceeding.time_diabetes = request.POST.get('time_diabetes') if request.POST.get('diabetes') == 'Si' else None

            proceeding.hypothyroidism = True if request.POST.get('hypothyroidism') == 'Si' else False
            proceeding.time_hypothyroidism = request.POST.get('time_hypothyroidism') if request.POST.get('hypothyroidism') == 'Si' else None

            proceeding.strokes = True if request.POST.get('strokes') == 'Si' else False
            proceeding.time_strokes = request.POST.get('time_strokes') if request.POST.get('strokes') == 'Si' else None

            proceeding.others_diseases = True if request.POST.get('others_diseases') == 'Si' else False
            proceeding.details_others_diseases = request.POST.get('details_others_diseases') if request.POST.get('others_diseases') == 'Si' else None             

            # Asigna el usuario actual al procedimiento
            proceeding.user = request.user
        
            # Guarda los cambios en el procedimiento y redirige a la vista de visualización de procedimientos
            proceeding.save()
            return redirect('show_proceedings')
        except:
            # Si ocurre algún error, vuelve a renderizar el formulario de actualización con los datos del procedimiento y la lista de países
            countries = [{'id': country.id, 'name': country.name} for country in Country.objects.all()]
            return render(request, "proceedings/update-proceeding.html", {'proceeding': proceeding, 'countries': countries})

# Vista para eliminar el Proceeding
def delete_proceeding(request):
    context = {}

    # Verifica si se proporciona un ID de procedimiento en la solicitud GET
    if "pid" in request.GET:
        pid = request.GET["pid"]
        # Obtiene el procedimiento correspondiente o muestra un error 404 si no se encuentra
        proceeding = get_object_or_404(Proceeding, id=pid)
        context["proceeding"] = proceeding

        # Verifica si se proporciona una acción en la solicitud GET
        if "action" in request.GET:
            # Elimina el procedimiento si la acción es 'delete'
            if request.GET["action"] == "delete":
                proceeding.delete()
                context["status"] = f"{proceeding.name} {proceeding.first_last_name} {proceeding.second_last_name} eliminado satisfactoriamente!!!"

    # Renderiza la plantilla 'delete-proceeding.html' con el contexto proporcionado
    return render(request, "proceedings/delete-proceeding.html", context)