from BANFE.models import *
# Importar el módulo math para utilizar el símbolo de infinito
import math

class Details_BANFE:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship  

    def get_data(self):
        labyrinths = Labyrinths_Handler(self.banfe_id, self.age, self.schoolarship)
        data_labyrinths = labyrinths.get_data()
        coded_labyrinths = labyrinths.get_data_coded()

        if data_labyrinths is "DoesNotExist":
            encoded_labyrinths = natural_labyrinths = {
                'cross': '',
                'caught': '',
                'time': ''
            }
        else:
            natural_labyrinths = {
                'cross': data_labyrinths['cross'],
                'caught': data_labyrinths['caught'],
                'time': data_labyrinths['time']
            }

            encoded_labyrinths = {
                'cross': coded_labyrinths['encoded_cross'],
                'caught': coded_labyrinths['encoded_caught'],
                'time': coded_labyrinths['encoded_time']
            }

        signaling = Signaling_Handler(self.banfe_id, self.age, self.schoolarship)
        data_signaling = signaling.get_data()
        coded_signaling = signaling.get_data_coded()   

        if data_signaling is "DoesNotExist":
            natural_signaling = {
                'successes': '',
                'perseverations': '',
                'time': ''
            }

            encoded_signaling = {
                'perseverations': '',
                'time': ''
            }
        else:
            natural_signaling = {
                'successes': data_signaling['successes'],
                'perseverations': data_signaling['perseverations'],
                'time': data_signaling['time']
            }

            encoded_signaling = {
                'perseverations': coded_signaling['encoded_perseverations'],
                'time': coded_signaling['encoded_time']
            }

        ordering = Ordering_Handler(self.banfe_id, self.age, self.schoolarship)
        data_ordering = ordering.get_data()
        coded_ordering = ordering.get_data_coded()   

        if data_ordering is "DoesNotExist":
            encoded_ordering = natural_ordering = {
                'essays_first_list': '',
                'essays_second_list': '',
                'essays_third_list': ''
            }
        else:
            if data_ordering['essays_third_list'] is None:
                data_ordering['essays_third_list'] = ''
                coded_ordering['encoded_essays_third_list'] = ''


            natural_ordering = {
                'essays_first_list': data_ordering['essays_first_list'],
                'essays_second_list': data_ordering['essays_second_list'],
                'essays_third_list': data_ordering['essays_third_list']
            }

            encoded_ordering = {
                'essays_first_list': coded_ordering['encoded_essays_first_list'],
                'essays_second_list': coded_ordering['encoded_essays_second_list'],
                'essays_third_list': coded_ordering['encoded_essays_third_list']
            }

        substraction = Substraction_Handler(self.banfe_id, self.age, self.schoolarship)
        data_substraction = substraction.get_data()
        coded_substraction = substraction.get_data_coded()   

        if data_substraction is "DoesNotExist":
            natural_substraction = {
                'successes_a': '',
                'time_a': '',
                'successes_b': '',
                'time_b': ''
            }

            encoded_substraction = {
                'time_a': '',
                'time_b': ''
            }
        else:
            if int(data_substraction['time_b'] ) == -1:
                print("RESTA: ",data_substraction['successes_b'], "tipo: ", type(int(data_substraction['time_b'] )))
                data_substraction['successes_b'] = ''
                data_substraction['time_b'] = ''

                coded_substraction['encoded_time_b'] = ''


            natural_substraction = {
                'successes_a': data_substraction['successes_a'],
                'time_a': data_substraction['time_a'],
                'successes_b': data_substraction['successes_b'],
                'time_b': data_substraction['time_b']
            }

            encoded_substraction = {
                'time_a': coded_substraction['encoded_time_a'],
                'time_b': coded_substraction['encoded_time_b'],
            }        

        addition = Addition_Handler(self.banfe_id, self.age, self.schoolarship)
        data_addition = addition.get_data()
        coded_addition = addition.get_data_coded()   

        if data_addition is "DoesNotExist":
            natural_addition = {
                'successes': '',
                'time': ''
            }

            encoded_addition = {
                'time': ''
            }
        else:
            natural_addition = {
                'successes': data_addition['successes'],
                'time': data_addition['time']
            }

            encoded_addition = {
                'time': coded_addition['encoded_time']
            }

        cards_sorting = Card_Sorting_Handler(self.banfe_id, self.age, self.schoolarship)
        data_cards = cards_sorting.get_data()
        coded_cards = cards_sorting.get_data_coded()   

        if data_cards is "DoesNotExist":
            natural_cards = {
                'successes': '',
                'perseverations': '',
                'deferred_perseverations': '',
                'maintenance_error': '',
                'time': ''  
            }

            encoded_cards = {
                'perseverations': '',
                'deferred_perseverations': '',
                'maintenance_error': '',
                'time': ''  
            }
        else:
            natural_cards = {
                'successes': data_cards['successes'],
                'perseverations': data_cards['perseverations'],
                'deferred_perseverations': data_cards['deferred_perseverations'],
                'maintenance_error': data_cards['maintenance_error'],
                'time': data_cards['time']  
            }

            encoded_cards = {
                'perseverations': coded_cards['encoded_perseverations'],
                'deferred_perseverations': coded_cards['encoded_deferred_perseverations'],
                'maintenance_error': coded_cards['encoded_maintenance_error'],
                'time': coded_cards['encoded_time']  
            }

        semantic = Semantic_Classification_Handler(self.banfe_id, self.age, self.schoolarship)
        data_semantic = semantic.get_data()
        coded_semantic = semantic.get_data_coded()   

        if data_semantic is "DoesNotExist":
            encoded_semantics = natural_semantics = {
                'abstract_categories': '',
                'total_categories': '',
                'total_average': '',
                'total_score': ''  
            }

        else:
            if self.age < 7:
                data_semantic['abstract_categories'] = ''
                coded_semantic['encoded_abstract_categories'] = ''

            natural_semantics = {
                'abstract_categories': data_semantic['abstract_categories'],
                'total_categories': data_semantic['total_categories'],
                'total_average': data_semantic['total_average'],
                'total_score': data_semantic['total_score']  
            }

            encoded_semantics = {
                'abstract_categories': coded_semantic['encoded_abstract_categories'],
                'total_categories': coded_semantic['encoded_total_categories'],
                'total_average': coded_semantic['encoded_total_average'],
                'total_score': coded_semantic['encoded_total_score']  
            }


        stroop_a = Stroop_A_Handler(self.banfe_id, self.age, self.schoolarship)
        data_stroop_a = stroop_a.get_data()
        coded_stroop_a = stroop_a.get_data_coded()   

        if data_stroop_a is "DoesNotExist":
            natural_stroop_a = {
                'successes': '',
                'stroop_errors': '',
                'time': ''
            }

            encoded_stroop_a = {
                'stroop_errors': '',
                'time': ''  
            }
        else:
            natural_stroop_a = {
                'successes': data_stroop_a['successes'],
                'stroop_errors': data_stroop_a['stroop_errors'],
                'time': data_stroop_a['time']
            }

            encoded_stroop_a = {
                'stroop_errors': coded_stroop_a['encoded_stroop_errors'],
                'time': coded_stroop_a['encoded_time']
            }  

        verbal_fluency = Verbal_Fluency_Handler(self.banfe_id, self.age, self.schoolarship)
        data_verbal_fluency = verbal_fluency.get_data()
        coded_verbal_fluency = verbal_fluency.get_data_coded()   

        if data_verbal_fluency is "DoesNotExist":
            encoded_fluency = natural_fluency = {
                'successes': '',
                'perseverations': ''
            }

        else:
            natural_fluency = {
                'successes': data_verbal_fluency['successes'],
                'perseverations': data_verbal_fluency['perseverations']
            }

            encoded_fluency = {
                'successes': coded_verbal_fluency['encoded_successes'],
                'perseverations': coded_verbal_fluency['encoded_perseverations']
            }  


        cards_game = Cards_Game_Handler(self.banfe_id, self.age, self.schoolarship)
        data_game = cards_game.get_data()
        print("JUEGO DE CARTAS: ",data_game)
        coded_game = cards_game.get_data_coded()   

        if data_game is "DoesNotExist":
            encoded_game = natural_game = {
                'percentage_risk_cards': '',
                'total_score': ''
            }

        else:
            natural_game = {
                'percentage_risk_cards': data_game['percentage_risk_cards'],
                'total_score': data_game['total_score']
            }

            encoded_game = {
                'percentage_risk_cards': coded_game['encoded_percentage_risk_cards'],
                'total_score': coded_game['encoded_total_score']
            }  


        sayings = Sayings_Handler(self.banfe_id, self.age, self.schoolarship)
        data_sayings = sayings.get_data()
        coded_sayings = sayings.get_data_coded()   

        if data_sayings is "DoesNotExist":
            natural_sayings = {
                'successes': '',
                'time': ''
            }

            encoded_sayings = {
                'time': ''  
            }
        else:
            natural_sayings = {
                'successes': data_sayings['successes'],
                'time': data_sayings['time']
            }

            encoded_sayings = {
                'time': coded_sayings['encoded_time']
            }   

        towers = Towers_Hanoi_Handler(self.banfe_id, self.age, self.schoolarship)
        data_towers = towers.get_data()
        coded_towers = towers.get_data_coded()   

        if data_towers is "DoesNotExist":
            encoded_towers = natural_towers = {
                'movements_first': '',
                'time_first': '',
                'movements_second': '',
                'time_second': ''
            }

        else:
            if int(data_towers['time_second'] ) == -1:
                data_towers['movements_second'] = ''
                data_towers['time_second'] = ''

                coded_towers['encoded_movements_second'] = ''
                coded_towers['encoded_time_second'] = ''


            natural_towers = {
                'movements_first': data_towers['movements_first'],
                'time_first': data_towers['time_first'],
                'movements_second': data_towers['movements_second'],
                'time_second': data_towers['time_second']
            }

            encoded_towers = {
                'movements_first': coded_towers['encoded_movements_first'],
                'time_first': coded_towers['encoded_time_first'],
                'movements_second': coded_towers['encoded_movements_second'],
                'time_second': coded_towers['encoded_time_second']
            }        


        metamemory = Metamemory_Handler(self.banfe_id, self.age, self.schoolarship)
        data_metamemory = metamemory.get_data()
        print("METAMEMORIA: ",data_metamemory)
        coded_metamemory = metamemory.get_data_coded()   

        if data_metamemory is "DoesNotExist":
            encoded_metamemory = natural_metamemory = {
                'positive_errors': '',
                'negative_errors': ''
            }

        else:
            natural_metamemory = {
                'positive_errors': data_metamemory['positive_errors'],
                'negative_errors': data_metamemory['negative_errors']
            }

            encoded_metamemory = {
                'positive_errors': coded_metamemory['encoded_positive_errors'],
                'negative_errors': coded_metamemory['encoded_negative_errors']
            }  


        memory = Visuospatial_Memory_Handler(self.banfe_id, self.age, self.schoolarship)
        data_memory = memory.get_data()
        coded_memory = memory.get_data_coded()   

        if data_memory is "DoesNotExist":
            natural_memory = {
                'maximum_sequence': '',
                'perseverations': '',
                'order_errors': ''
            }

            encoded_memory = {
                'perseverations': '',
                'order_errors': ''
            }
        else:
            natural_memory = {
                'maximum_sequence': data_memory['maximum_sequence'],
                'perseverations': data_memory['perseverations'],
                'order_errors': data_memory['order_errors']
            }

            encoded_memory = {
                'perseverations': coded_memory['encoded_perseverations'],
                'order_errors': coded_memory['encoded_order_errors']
            }   

        stroop_b = Stroop_B_Handler(self.banfe_id, self.age, self.schoolarship)
        data_stroop_b = stroop_b.get_data()
        coded_stroop_b = stroop_b.get_data_coded()   

        if data_stroop_b is "DoesNotExist":
            natural_stroop_b = {
                'successes': '',
                'stroop_errors': '',
                'time': ''
            }

            encoded_stroop_b = {
                'stroop_errors': '',
                'time': ''  
            }
        else:
            natural_stroop_b = {
                'successes': data_stroop_b['successes'],
                'stroop_errors': data_stroop_b['stroop_errors'],
                'time': data_stroop_b['time']
            }

            encoded_stroop_b = {
                'stroop_errors': coded_stroop_b['encoded_stroop_errors'],
                'time': coded_stroop_b['encoded_time']
            }                

        return {
            'natural_labyrinths': natural_labyrinths,
            'encoded_labyrinths': encoded_labyrinths,
            'natural_signaling': natural_signaling,
            'encoded_signaling': encoded_signaling,
            'natural_ordering': natural_ordering,
            'encoded_ordering': encoded_ordering,          
            'natural_substraction': natural_substraction,
            'encoded_substraction': encoded_substraction,    
            'natural_addition': natural_addition,
            'encoded_addition': encoded_addition,       
            'natural_cards': natural_cards,
            'encoded_cards': encoded_cards,       
            'natural_semantic': natural_semantics,
            'encoded_semantic': encoded_semantics,   
            'natural_stroopA': natural_stroop_a,
            'encoded_stroopA': encoded_stroop_a,       
            'natural_fluency': natural_fluency,
            'encoded_fluency': encoded_fluency,       
            'natural_game': natural_game,
            'encoded_game': encoded_game,  
            'natural_sayings': natural_sayings,
            'encoded_sayings': encoded_sayings,       
            'natural_towers': natural_towers,
            'encoded_towers': encoded_towers,         
            'natural_metamemory': natural_metamemory,
            'encoded_metamemory': encoded_metamemory,       
            'natural_memory': natural_memory,
            'encoded_memory': encoded_memory,      
            'natural_stroopB': natural_stroop_b,
            'encoded_stroopB': encoded_stroop_b                                                                              
        }

class Result:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship

        self.points_battery = 0
    
    def show_scores(self):
        banfe = BANFE.objects.get(id=self.banfe_id)
        cortex_names = [cortex.name for cortex in banfe.area.all()]
        print("BANFE_RESULT: ",banfe)
        print(cortex_names)

        if "Prefrontal Anterior" in cortex_names and "Orbitomedial" in cortex_names and "Dorsolateral" in cortex_names:
            orbitomedial = Orbitomedial(self.banfe_id, self.age, self.schoolarship)
            data_orbitomedial = orbitomedial.calculate_points()

            anterior_prefrontal = Anterior_Prefrontal(self.banfe_id, self.age, self.schoolarship)
            data_prefrontal = anterior_prefrontal.calculate_points()
                
            dorsolateral = Dorsolateral(self.banfe_id, self.age, self.schoolarship)
            data_dorsolateral = dorsolateral.calculate_points()

            self.add_points(data_orbitomedial['orbitomedial'])
            self.add_points(data_prefrontal['prefrontal_anterior'])
            self.add_points(data_dorsolateral['dorsolateral'])
                
            full_battery = Full_Battery(self.banfe_id, self.age, self.schoolarship)

            return {
                'banfe_id': self.banfe_id,
                'natural_orbitomedial': data_orbitomedial['orbitomedial'],
                'encoded_orbitomedial': data_orbitomedial['encoded_orbitomedial'],
                'diagnosis_orbitomedial': self.get_diagnosis(data_orbitomedial['encoded_orbitomedial']),
                'natural_prefrontal': data_prefrontal['prefrontal_anterior'],
                'encoded_prefrontal': data_prefrontal['encoded_prefrontal_anterior'],
                'diagnosis_prefrontal': self.get_diagnosis(data_prefrontal['encoded_prefrontal_anterior']),
                'natural_dorsolateral': data_dorsolateral['dorsolateral'],
                'work_memory': data_dorsolateral['work_memory'],
                'executive_functions': data_dorsolateral['executive_functions'],
                'encoded_dorsolateral': data_dorsolateral['encoded_dorsolateral'],
                'diagnosis_dorsolateral': self.get_diagnosis(data_dorsolateral['encoded_dorsolateral']),
                'natural_total': self.points_battery,
                'encoded_total': full_battery.get_data_coded(self.points_battery),
                'diagnosis_total': self.get_diagnosis(full_battery.get_data_coded(self.points_battery))                      
            }
        
        elif "Prefrontal Anterior" in cortex_names and "Orbitomedial" in cortex_names:
            anterior_prefrontal = Anterior_Prefrontal(self.banfe_id, self.age, self.schoolarship)
            data_prefrontal = anterior_prefrontal.calculate_points()

            orbitomedial = Orbitomedial(self.banfe_id, self.age, self.schoolarship)
            data_orbitomedial = orbitomedial.calculate_points()        
                            
            return {
                'banfe_id': self.banfe_id,
                'natural_orbitomedial': data_orbitomedial['orbitomedial'],
                'encoded_orbitomedial': data_orbitomedial['encoded_orbitomedial'],
                'diagnosis_orbitomedial': self.get_diagnosis(data_orbitomedial['encoded_orbitomedial']),
                'natural_prefrontal': data_prefrontal['prefrontal_anterior'],
                'encoded_prefrontal': data_prefrontal['encoded_prefrontal_anterior'],
                'diagnosis_prefrontal': self.get_diagnosis(data_prefrontal['encoded_prefrontal_anterior']),
                'natural_dorsolateral': '',
                'work_memory': '',
                'executive_functions': '',
                'encoded_dorsolateral': '',
                'diagnosis_dorsolateral': "NO APLICADA",
                'natural_total': '',
                'encoded_total': '',
                'diagnosis_total': "NO APLICADA"                      
            }    
        elif "Prefrontal Anterior" in cortex_names and "Dorsolateral" in cortex_names:
            anterior_prefrontal = Anterior_Prefrontal(self.banfe_id, self.age, self.schoolarship)
            data_prefrontal = anterior_prefrontal.calculate_points()

            dorsolateral = Dorsolateral(self.banfe_id, self.age, self.schoolarship)
            data_dorsolateral = dorsolateral.calculate_points()

            return {           
                'banfe_id': self.banfe_id,
                'natural_orbitomedial': '',
                'encoded_orbitomedial': '',
                'diagnosis_orbitomedial': "NO APLICADA",
                'natural_prefrontal': data_prefrontal['prefrontal_anterior'],
                'encoded_prefrontal': data_prefrontal['encoded_prefrontal_anterior'],
                'diagnosis_prefrontal': self.get_diagnosis(data_prefrontal['encoded_prefrontal_anterior']),
                'natural_dorsolateral': data_dorsolateral['dorsolateral'],
                'work_memory': data_dorsolateral['work_memory'],
                'executive_functions': data_dorsolateral['executive_functions'],
                'encoded_dorsolateral': data_dorsolateral['encoded_dorsolateral'],
                'diagnosis_dorsolateral': self.get_diagnosis(data_dorsolateral['encoded_dorsolateral']),
                'natural_total': '',
                'encoded_total': '',
                'diagnosis_total': "NO APLICADA"                     
            }                    
        elif "Orbitomedial" in cortex_names and "Dorsolateral" in cortex_names:
            orbitomedial = Orbitomedial(self.banfe_id, self.age, self.schoolarship)   
            data_orbitomedial = orbitomedial.calculate_points()   
                        
            dorsolateral = Dorsolateral(self.banfe_id, self.age, self.schoolarship)
            data_dorsolateral = dorsolateral.calculate_points()

            return {        
                'banfe_id': self.banfe_id,
                'natural_orbitomedial': data_orbitomedial['orbitomedial'],
                'encoded_orbitomedial': data_orbitomedial['encoded_orbitomedial'],
                'diagnosis_orbitomedial': self.get_diagnosis(data_orbitomedial['encoded_orbitomedial']),
                'natural_prefrontal': '',
                'encoded_prefrontal': '',
                'diagnosis_prefrontal': "NO APLICADA" ,
                'natural_dorsolateral': data_dorsolateral['dorsolateral'],
                'work_memory': data_dorsolateral['work_memory'],
                'executive_functions': data_dorsolateral['executive_functions'],                
                'encoded_dorsolateral': data_dorsolateral['encoded_dorsolateral'],
                'diagnosis_dorsolateral': self.get_diagnosis(data_dorsolateral['encoded_dorsolateral']),
                'natural_total': '',
                'encoded_total': '',
                'diagnosis_total': "NO APLICADA"                        
            }
        elif "Prefrontal Anterior" in cortex_names:
            anterior_prefrontal = Anterior_Prefrontal(self.banfe_id, self.age, self.schoolarship)
            data_prefrontal = anterior_prefrontal.calculate_points()
                        
            return {    
                'banfe_id': self.banfe_id,         
                'natural_orbitomedial': '',
                'encoded_orbitomedial': '',
                'diagnosis_orbitomedial': "NO APLICADA",
                'natural_prefrontal': data_prefrontal['prefrontal_anterior'],
                'encoded_prefrontal': data_prefrontal['encoded_prefrontal_anterior'],
                'diagnosis_prefrontal': self.get_diagnosis(data_prefrontal['encoded_prefrontal_anterior']),
                'natural_dorsolateral': '',
                'work_memory': '',
                'executive_functions': '',
                'encoded_dorsolateral': '',
                'diagnosis_dorsolateral': "NO APLICADA",
                'natural_total': '',
                'encoded_total': '',
                'diagnosis_total': "NO APLICADA"                     
            }        
        elif "Orbitomedial" in cortex_names:
            orbitomedial = Orbitomedial(self.banfe_id, self.age, self.schoolarship)
            data_orbitomedial = orbitomedial.calculate_points()   

            return {     
                'banfe_id': self.banfe_id,       
                'natural_orbitomedial': data_orbitomedial['orbitomedial'],
                'encoded_orbitomedial': data_orbitomedial['encoded_orbitomedial'],
                'diagnosis_orbitomedial': self.get_diagnosis(data_orbitomedial['encoded_orbitomedial']),
                'natural_prefrontal': '',
                'encoded_prefrontal': '',
                'diagnosis_prefrontal': "NO APLICADA",
                'natural_dorsolateral': '',
                'work_memory': '',
                'executive_functions': '',
                'encoded_dorsolateral': '',
                'diagnosis_dorsolateral': "NO APLICADA",
                'natural_total': '',
                'encoded_total': '',
                'diagnosis_total': "NO APLICADA"                      
            }
        elif "Dorsolateral" in cortex_names:
            dorsolateral = Dorsolateral(self.banfe_id, self.age, self.schoolarship)
            data_dorsolateral = dorsolateral.calculate_points()

            return {    
                'banfe_id': self.banfe_id,        
                'natural_orbitomedial': '',
                'encoded_orbitomedial': '',
                'diagnosis_orbitomedial': "NO APLICADA",
                'natural_prefrontal': '',
                'encoded_prefrontal': '',
                'diagnosis_prefrontal': "NO APLICADA",
                'natural_dorsolateral': data_dorsolateral['dorsolateral'],
                'work_memory': data_dorsolateral['work_memory'],
                'executive_functions': data_dorsolateral['executive_functions'],                
                'encoded_dorsolateral': data_dorsolateral['encoded_dorsolateral'],
                'diagnosis_dorsolateral': self.get_diagnosis(data_dorsolateral['encoded_dorsolateral']),
                'natural_total': '',
                'encoded_total': '',
                'diagnosis_total': "NO APLICADA"                      
            }            

    def add_points(self, points):
        if points != None:
            self.points_battery += int(points)

    def get_diagnosis(self, total_points):
        if total_points == None:
            return -1
        if total_points >= 116:
            return "NORMAL ALTO"
        elif total_points >= 85 and total_points <= 115:
            return "NORMAL" 
        elif total_points <= 84 and total_points >= 70:
            return "ALTERACIÓN MODERADA"
        elif total_points <= 69:
            return "ALTERACIÓN SEVERA"

class Orbitomedial:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship

        self.coded_points = 0
        self.points_orbitomedial = {
            "tabla B-1": {
                (0, 0): 25, 1: 31, 2: 36, 3: 42, 4: 47, 5: 53, 6: 59, 7: 64, 8: 70, 9: 75, 10: 81, 11: 86, 12: 92, 13: 97, 14: 103, 15: 109, 16: 114, 17: 120, 18: 125, 19: 131, 20: 136 
            },
            "tabla B-2": {
                (0, 160): 44, 161: 45, 162: 47, 163: 49, 164: 50, 165: 52, 166: 54, 167: 55, 168: 57, 169: 59, 170: 61, 171: 62, 172: 64, 173: 66, 174: 67, 175: 69, 176: 71, 177: 72, 178: 74, 179: 76, 180: 78, 181: 79, 182: 81, 183: 83, 184: 84, 185: 86, 186: 88, 187: 89, 188: 91, 189: 93, 190: 95, 191: 96, 192: 98, 193: 100, 194: 101, 195: 103, 196: 105, 197: 106, 198: 108, 199: 110, 200: 112, 201: 113, 202: 115, 203: 117, 204: 118, 205: 120, 206: 122, 207: 123, 208: 125, 209: 127, 210: 129, (211, math.inf): 130
            },
            "tabla B-3": {
                (0, 157): 43, 158: 44, 159: 46, 160: 47, 161: 49, 162: 50, 163: 52, 164: 53, 165: 55, 166: 56, 167: 58, 168: 59, 169: 61, 170: 62, 171: 64, 172: 65, 173: 67, 174: 68, 175: 70, 176: 71, 177: 73, 178: 74, 179: 76, 180: 77, 181: 79, 182: 81, 183: 82, 184: 84, 185: 85, 186: 87, 187: 88, 188: 90, 189: 91, 190: 93, 191: 94, 192: 96, 193: 97, 194: 99, 195: 100, 196: 102, 197: 103, 198: 105, 199: 106, 200: 108, 201: 109, 202: 111, 203: 112, 204: 114, 205: 115, 206: 117, 207: 118, 208: 120, 209: 122, 210: 123, 211: 125, 212: 126, 213: 128, 214: 129, (215, math.inf): 131
            },
            "tabla B-4": {
                (0, 176): 44, 177: 47, 178: 50, 179: 52, 180: 55, 181: 58, 182: 61, 183: 63, 184: 66, 185: 69, 186: 72, 187: 74, 188: 77, 189: 80, 190: 83, 191: 85, 192: 88, 193: 91, 194: 94, 195: 96, 196: 99, 197: 102, 198: 105, 199: 107, 200: 110, 201: 113, 202: 116, 203: 118, 204: 121, 205: 124, 206: 127, 207: 129, 208: 132 
            },
            "tabla B-5": {
                (0, 183): 46, 184: 50, 185: 54, 186: 58, 187: 62, 188: 65, 189: 69, 190: 73, 191: 77, 192: 81, 193: 85, 194: 89, 195: 93, 196: 97, 197: 100, 198: 104, 199: 108, 200: 112, 201: 116, 202: 117, 203: 124, 204: 128, (205, math.inf): 132
            },
            "tabla B-6": {
                (0, 160): 45, 161: 46, 162: 48, 163: 50, 164: 52, 165: 54, 166: 56, 167: 58, 168: 60, 169: 62, 170: 64, 171: 66, 172: 67, 173: 69, 174: 71, 175: 73, 176: 75, 177: 77, 178: 79, 179: 81, 180: 83, 181: 85, 182: 87, 183: 88, 184: 90, 185: 92, 186: 94, 187: 96, 188: 98, 189: 100, 190: 102, 191: 104, 192: 106, 193: 108, 194: 109, 195: 111, 196: 113, 197: 115, 198: 117, 199: 119, 200: 121, 201: 123, 202: 125, 203: 127, 204: 129, (205, math.inf): 130
            },    
            "tabla B-7": {
                (0, 177): 45, 178: 48, 179: 51, 180: 54, 181: 57, 182: 60, 183: 63, 184: 66, 185: 69, 186: 72, 187: 75, 188: 78, 189: 80, 190: 83, 191: 86, 192: 89, 193: 92, 194: 95, 195: 98, 196: 101, 197: 104, 198: 107, 199: 110, 200: 113, 201: 116, 202: 119, 203: 122, 204: 125, 205: 128, (206, math.inf): 131
            },          
            "tabla B-8": {
                (0, 150): 30, 151: 31, 152: 33, 153: 35, 154: 36, 155: 38, 156: 39, 157: 41, 158: 42, 159: 44, 160: 45, 161: 47, 162: 48, 163: 50, 164: 51, 165: 53, 166: 54, 167: 56, 168: 57, 169: 59, 170: 61, 171: 62, 172: 64, 173: 65, 174: 67, 175: 68, 176: 70, 177: 71, 178: 73, 179: 74, 180: 76, 181: 77, 182: 79, 183: 80, 184: 82, 185: 84, 186: 85, 187: 87, 188: 88, 189: 90, 190: 91, 191: 93, 192: 94, 193: 96, 194: 97, 195: 99, 196: 100, 197: 102, 198: 103, 199: 105, 200: 106, 201: 108, 202: 110, 203: 111, 204: 112, 205: 114, 206: 116, 207: 117, (208, math.inf): 119
            },
            "tabla B-9": {
                (0, 179): 43, 180: 46, 181: 49, 182: 52, 183: 55, 184: 58, 185: 61, 186: 64, 187: 67, 188: 70, 189: 73, 190: 76, 191: 79, 192: 82, 193: 85, 194: 88, 195: 91, 196: 94, 197: 97, 198: 100, 199: 103, 200: 106, 201: 109, 202: 112, 203: 115, 204: 118, 205: 121, 206: 124, 207: 127, (208, math.inf): 130
            },
            "tabla B-10": {
                (0, 161): 44, 162: 46, 163: 47, 164: 49, 165: 51, 166: 53, 167: 54, 168: 56, 169: 58, 170: 60, 171: 61, 172: 63, 173: 65, 174: 67, 175: 68, 176: 70, 177: 72, 178: 74, 179: 75, 180: 77, 181: 79, 182: 80, 183: 82, 184: 84, 185: 86, 186: 87, 187: 89, 188: 91, 189: 93, 190: 94, 191: 96, 192: 98, 193: 100, 194: 101, 195: 103, 196: 105, 197: 107, 198: 108, 199: 110, 200: 112, 201: 114, 202: 115, 203: 117, 204: 119, 205: 121, 206: 122, 207: 124, 208: 126, 209: 128, 210: 129, (211, math.inf): 131
            },
            "tabla B-11": {
                (0, 175): 47, 176: 50, 177: 54, 178: 57, 179: 60, 180: 64, 181: 67, 182: 71, 183: 74, 184: 78, 185: 81, 186: 84, 187: 88, 188: 91, 189: 95, 190: 98, 191: 102, 192: 105, 193: 108, 194: 112, 195: 115, 196: 119, 197: 122, 198: 126, 199: 129, (200, math.inf): 132
            }                                                                          
        }   

    def define_table(self):
        if self.age > 5 and self.age < 8:
            return "tabla B-1"
        elif self.age > 7 and self.age < 10:
            return "tabla B-2"
        elif self.age > 9 and self.age < 12:
            return "tabla B-3"
        elif self.age > 11 and self.age < 14:
            return "tabla B-4"
        elif self.age > 13 and self.age < 16:
            return "tabla B-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla B-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla B-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla B-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla B-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla B-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla B-11"           

    def add_points(self, points):
        print(points)
        if points != None:
            self.coded_points += int(points)
    
    def calculate_points(self):
        labyrinths = Labyrinths_Handler(self.banfe_id, self.age, self.schoolarship)
        coded_labyrinths = labyrinths.get_data_coded()

        if coded_labyrinths is not "DoesNotEncoded":
            self.add_points(coded_labyrinths['encoded_cross'])

        cards_game = Cards_Game_Handler(self.banfe_id, self.age, self.schoolarship)
        coded_game = cards_game.get_data_coded()

        if coded_game is not "DoesNotEncoded":
            self.add_points(coded_game['encoded_percentage_risk_cards'])
            self.add_points(coded_game['encoded_total_score'])

        stroop_a = Stroop_A_Handler(self.banfe_id, self.age, self.schoolarship)
        data_stroop_a = stroop_a.get_data()
        
        if data_stroop_a is not "DoesNotExist":
            coded_stroop_a = stroop_a.get_data_coded()
            self.add_points(coded_stroop_a['encoded_stroop_errors'])
            self.add_points(coded_stroop_a['encoded_time'])
            self.add_points(data_stroop_a['successes'])

        stroop_b = Stroop_B_Handler(self.banfe_id, self.age, self.schoolarship)
        data_stroop_b = stroop_b.get_data()
        
        if data_stroop_b is not "DoesNotExist":
            coded_stroop_b = stroop_b.get_data_coded()
            self.add_points(coded_stroop_b['encoded_stroop_errors'])
            self.add_points(coded_stroop_b['encoded_time'])
            self.add_points(data_stroop_b['successes'])

        cards = Card_Sorting_Handler(self.banfe_id, self.age, self.schoolarship)
        coded_cards = cards.get_data_coded()

        if coded_cards is not "DoesNotEncoded":
            self.add_points(coded_cards['encoded_maintenance_error'])

        return {
            'orbitomedial': self.coded_points,
            'encoded_orbitomedial': self.get_data_coded(self.coded_points)
        }        

    def get_data_coded(self, natural_points):
        print("TABLA: ",self.define_table())
        points = self.points_orbitomedial.get(self.define_table())
        print("POINTS: ",points)

        if points is not None:
            for rank, coded_value in points.items():
                if isinstance(rank, tuple):
                    start, end = rank
                    if natural_points >= start and natural_points <= end:
                        print(rank)
                        return coded_value
                else:
                    if rank == natural_points:
                        return coded_value
        return 0         

class Anterior_Prefrontal:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship

        self.coded_points = 0
        self.points_anterior_prefrontal = {
            "tabla B-1": {
                0: 46, 1: 53, 2: 60, 3: 67, 4: 75, 5: 82, 6: 89, 7: 96, 8: 103, 9: 110, 10: 117, 11: 125, (12, math.inf): 132 
            },
            "tabla B-2": {
                0: 47, 1: 52, 2: 57, 3: 62, 4: 67, 5: 72, 6: 77, 7: 82, 8: 87, 9: 92, 10: 97, 11: 102, 12: 107, 13: 112, 14: 117, 15: 122, 16: 127, (17, math.inf): 132
            },
            "tabla B-3": {
                (0, 10): 41, 11: 48, 12: 56, 13: 63, 14: 70, 15: 78, 16: 85, 17: 92, 18: 99, 19: 107, 20: 114, 21: 121, 22: 129, (23, math.inf): 136
            },
            "tabla B-4": {
                (0, 9): 44, 10: 50, 11: 57, 12: 63, 13: 70, 14: 76, 15: 83, 16: 89, 17: 96, 18: 102, 19: 109, 20: 115, 21: 122, 22: 128, (23, math.inf): 135
            },
            "tabla B-5": {
                (0, 9): 40, 10: 46, 11: 52, 12: 58, 13: 64, 14: 70, 15: 76, 16: 82, 17: 88, 18: 94, 19: 100, 20: 106, 21: 112, 22: 118, 23: 124, 24: 130, (25, math.inf): 136
            },
            "tabla B-6": {
                (0, 9): 42, 10: 48, 11: 53, 12: 58, 13: 64, 14: 69, 15: 74, 16: 80, 17: 85, 18: 90, 19: 96, 20: 101, 21: 106, 22: 112, 23: 117, 24: 123, 25: 128, (26, math.inf): 133
            },    
            "tabla B-7": {
                (0, 9): 42, 10: 47, 11: 52, 12: 58, 13: 63, 14: 68, 15: 74, 16: 79, 17: 85, 18: 90, 19: 95, 20: 101, 21: 106, 22: 111, 23: 117, 24: 122, 25: 127, (26, math.inf): 133
            },          
            "tabla B-8": {
                (0, 9): 40, 10: 46, 11: 52, 12: 58, 13: 64, 14: 70, 15: 76, 16: 82, 17: 88, 18: 94, 19: 100, 20: 106, 21: 112, 22: 118, 23: 124, 24: 130, (25, math.inf): 136
            },
            "tabla B-9": {
                (0, 9): 29, 10: 35, 11: 42, 12: 49, 13: 56, 14: 63, 15: 70, 16: 76, 17: 83, 18: 90, 19: 97, 20: 104, 21: 111, 22: 118, 23: 124, (24, math.inf): 131
            },
            "tabla B-10": {
                (0, 11): 45, 12: 51, 13: 58, 14: 64, 15: 71, 16: 77, 17: 84, 18: 90, 19: 97, 20: 103, 21: 110, 22: 116, 23: 123, (24, math.inf): 130
            },
            "tabla B-11": {
                (0, 11): 48, 12: 55, 13: 61, 14: 67, 15: 73, 16: 80, 17: 86, 18: 92, 19: 98, 20: 105, 21: 111, 22: 117, 23: 123, (24, math.inf): 130
            }                                                                          
        }   

    def define_table(self):
        if self.age > 5 and self.age < 8:
            return "tabla B-1"
        elif self.age > 7 and self.age < 10:
            return "tabla B-2"
        elif self.age > 9 and self.age < 12:
            return "tabla B-3"
        elif self.age > 11 and self.age < 14:
            return "tabla B-4"
        elif self.age > 13 and self.age < 16:
            return "tabla B-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla B-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla B-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla B-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla B-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla B-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla B-11"           
   
    def add_points(self, points):
        if points != None:
            self.coded_points += int(points)
       
    def calculate_points(self):
        semantics = Semantic_Classification_Handler(self.banfe_id, self.age, self.schoolarship)
        coded_semantics = semantics.get_data_coded()

        if coded_semantics is not "DoesNotEncoded":
            self.add_points(coded_semantics['encoded_abstract_categories'])

        sayings = Sayings_Handler(self.banfe_id, self.age, self.schoolarship)
        data_sayings = sayings.get_data()

        if data_sayings is not "DoesNotExist":
            coded_sayings = sayings.get_data_coded()            
            self.add_points(coded_sayings['encoded_time'])
            self.add_points(data_sayings['successes'])

        metamemory = Metamemory_Handler(self.banfe_id, self.age, self.schoolarship)
        coded_metamemory = metamemory.get_data_coded()

        if coded_metamemory is not "DoesNotEncoded":
            self.add_points(coded_metamemory['encoded_negative_errors'])
            self.add_points(coded_metamemory['encoded_positive_errors'])

        return {
            'prefrontal_anterior': self.coded_points,
            'encoded_prefrontal_anterior': self.get_data_coded(self.coded_points)
        }      

    def get_data_coded(self, natural_points):
        points = self.points_anterior_prefrontal.get(self.define_table())

        if points is not None:
            for rank, coded_value in points.items():
                if isinstance(rank, tuple):
                    start, end = rank
                    if natural_points >= start and natural_points <= end:
                        print(rank)
                        return coded_value
                else:
                    if rank == natural_points:
                        return coded_value
        return 0         
     
class Dorsolateral:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship

        self.coded_points = 0
        self.work_memory = 0
        self.executive_functions = 0

        self.points_dorsolateral = {
            "tabla B-1": {
                (0, 40): 43, 41: 44, 42: 45, 43: 46, 44: 47, 45: 48, 46: 49, 47: 50, 48: 50, 49: 51, 50: 52, 51: 53, 52: 54, 53: 55, 54: 56, 55: 57, 56: 58, 57: 59, 58: 60, 59: 61, 60: 62, 61: 63, 62: 64, 63: 65, 64: 66, 65: 67, 66: 67, 67: 68, 68: 69, 69: 70, 70: 71, 71: 72, 72: 73, 73: 74, 74: 75, 75: 76, 76: 77, 77: 78, 78: 79, 79: 80, 80: 81, 81: 82, 82: 83, 83: 83, 84: 84, 85: 85, 86: 86, 87: 87, 88: 88, 89: 89, 90: 90, 91: 91, 92: 92, 93: 93, 94: 94, 95: 95, 96: 96, 97: 97, 98: 98, 99: 99, 100: 100, 101: 100, 102: 101, 103: 102, 104: 103, 105: 104, 106: 105, 107: 106, 108: 107, 109: 108, 110: 109, 111: 110, 112: 111, 113: 112, 114: 113, 115: 114, 116: 115, 117: 116, 118: 116, 119: 117, 120: 118, 121: 119, 122: 120, 123: 121, 124: 122, 125: 123, 126: 124, 127: 125, 128: 126, 129: 127, 130: 128, 131: 129, 132: 130, 133: 131, 134: 132, 135: 132, 136: 133, 137: 134, (138, math.inf): 135
            },
            "tabla B-2": {
                (0, 64): 45, 65: 46, 66: 46, 67: 47, 68: 47, 69: 48, 70: 49, 71: 49, 72: 50, 73: 51, 74: 51, 75: 52, 76: 52, 77: 53, 78: 54, 79: 54, 80: 55, 81: 55, 82: 56, 83: 57, 84: 57, 85: 58, 86: 59, 87: 59, 88: 60, 89: 60, 90: 61, 91: 62, 92: 62, 93: 63, 94: 64, 95: 64, 96: 65, 97: 65, 98: 66, 99: 67, 100: 67, 101: 68, 102: 69, 103: 69, 104: 70, 105: 70, 106: 71, 107: 72, 108: 72, 109: 73, 110: 74, 111: 74, 112: 75, 113: 75, 114: 76, 115: 77, 116: 77, 117: 78, 118: 79, 119: 79, 120: 80, 121: 80, 122: 81, 123: 82, 124: 82, 125: 83, 126: 83, 127: 84, 128: 85, 129: 85, 130: 86, 131: 87, 132: 87, 133: 88, 134: 88, 135: 89, 136: 90, 137: 90, 138: 91, 139: 92, 140: 92, 141: 93, 142: 93, 143: 94, 144: 95, 145: 95, 146: 96, 147: 97, 148: 97, 149: 98, 150: 98, 151: 99, 152: 100, 153: 100, 154: 101, 155: 102, 156: 102, 157: 103, 158: 103, 159: 104, 160: 105, 161: 105, 162: 106, 163: 106, 164: 107, 165: 108, 166: 108, 167: 108, 168: 108, 169: 108, 170: 108, 171: 108, 172: 108, 173: 108, 174: 108, 175: 108, 176: 108, 177: 108, 178: 108, 179: 108, 180: 108, 181: 108, 182: 108, 183: 108, 184: 120, 185: 120, 186: 121, 187: 121, 188: 122, 189: 123, 190: 123, 191: 124, 192: 125, 193: 125, 194: 126, 195: 126, 196: 127, 197: 128, 198: 128, 199: 129, 200: 130, (201, math.inf): 130 
            },
            "tabla B-3": {
                (0, 131): 45, 132: 46, 133: 47, 134: 48, 135: 49, 136: 50, 137: 50, 138: 51, 139: 52, 140: 53, 141: 54, 142: 55, 143: 56, 144: 56, 145: 57, 146: 58, 147: 59, 148: 60, 149: 61, 150: 62, 151: 62, 152: 63, 153: 64, 154: 65, 155: 66, 156: 67, 157: 68, 158: 68, 159: 69, 160: 70, 161: 71, 162: 72, 163: 73, 164: 74, 165: 74, 166: 75, 167: 76, 168: 77, 169: 78, 170: 79, 171: 80, 172: 80, 173: 81, 174: 82, 175: 83, 176: 84, 177: 85, 178: 86, 179: 86, 180: 87, 181: 88, 182: 89, 183: 90, 184: 91, 185: 92, 186: 92, 187: 93, 188: 94, 189: 95, 190: 96, 191: 97, 192: 98, 193: 98, 194: 99, 195: 100, 196: 101, 197: 102, 198: 103, 199: 104, 200: 104, 201: 105, 202: 106, 203: 107, 204: 108, 205: 109, 206: 110, 207: 110, 208: 111, 209: 112, 210: 113, 211: 114, 212: 115, 213: 116, 214: 116, 215: 117, 216: 118, 217: 119, 218: 120, 219: 121, 220: 122, 221: 122, 223: 124, 224: 125, 225: 126, 226: 127, 227: 128, 228: 129, 229: 129, (230, math.inf): 130
            },
            "tabla B-4": {
                (0, 134): 45, 135: 46, 136: 47, 137: 47, 138: 48, 139: 49, 140: 50, 141: 51, 142: 52, 143: 53, 144: 53, 145: 54, 146: 55, 147: 56, 148: 57, 149: 58, 150: 59, 151: 60, 152: 60, 153: 1, 154: 62, 155: 63, 156: 64, 157: 65, 158: 66, 159: 66, 160: 67, 161: 68, 162: 69, 163: 70, 164: 71, 165: 72, 166: 72, 167: 73, 168: 74, 169: 75, 170: 76, 171: 77, 172: 78, 173: 79, 174: 79, 175: 80, 176: 81, 177: 82, 178: 83, 179: 84, 180: 85, 181: 85, 182: 86, 183: 87, 184: 88, 185: 89, 186: 90, 187: 91, 188: 92, 189: 92, 190: 93, 191: 94, 192: 95, 193: 96, 194: 97, 195: 98, 196: 98, 197: 99, 198: 100, 199: 101, 200: 102, 201: 103, 202: 104, 203: 105, 204: 105, 205: 106, 206: 107, 207: 108, 208: 109, 209: 110, 210: 111, 211: 111, 212: 112, 213: 113, 214: 114, 215: 115, 216: 116, 217: 117, 218: 118, 219: 118, 220: 119, 221: 120, 222: 121, 223: 122, 224: 123, 225: 124, 226: 124, 227: 125, 228: 126, 229: 127, 230: 128, 231: 129, (232, math.inf): 130
            },
            "tabla B-5": {
                (0, 152): 44, 153: 45, 154: 46, 155: 47, 156: 48, 157: 49, 158: 50, 159: 51, 160: 53, 161: 54, 162: 55, 163: 56, 164: 57, 165: 58, 166: 59, 167: 60, 168: 61, 169: 62, 170: 63, 171: 64, 172: 65, 173: 66, 174: 68, 175: 69, 176: 70, 177: 71, 178: 72, 179: 73, 180: 74, 181: 75, 182: 76, 183: 77, 184: 78, 185: 79, 186: 80, 187: 82, 188: 83, 189: 84, 190: 85, 191: 86, 192: 87, 193: 88, 194: 89, 195: 90, 196: 91, 197: 92, 198: 93, 199: 94, 200: 96, 201: 97, 202: 98, 203: 99, 204: 100, 205: 101, 206: 102, 207: 103, 208: 104, 209: 105, 210: 106, 211: 107, 212: 108, 213: 110, 214: 111, 215: 112, 216: 113, 217: 114, 218: 115, 219: 116, 220: 117, 221: 118, 222: 119, 223: 120, 224: 121, 225: 122, 226: 124, 227: 125, 228: 126, 229: 127, 230: 128, 231: 129, (232, math.inf): 130            
            },
            "tabla B-6": {
                (0, 95): 45, 91: 46, 92: 46, 93: 47, 94: 47, 95: 48, 96: 48, 97: 49, 98: 49, 99: 50, 100: 50, 101: 51, 102: 52, 103: 52, 104: 53, 105: 53, 106: 54, 107: 54, 108: 55, 109: 55, 110: 56, 111: 56, 112: 57, 113: 57, 114: 58, 115: 59, 116: 59, 117: 60, 118: 60, 119: 61, 120: 61, 121: 62, 122: 62, 123: 63, 124: 63, 125: 64, 126: 65, 127: 65, 128: 66, 129: 66, 130: 67, 131: 67, 132: 68, 133: 68, 134: 69, 135: 69, 136: 70, 137: 70, 138: 71, 139: 72, 140: 72, 141: 73, 142: 73, 143: 74, 144: 74, 145: 75, 146: 75, 147: 76, 148: 76, 149: 77, 150: 78, 151: 78, 152: 79, 153: 79, 154: 80, 155: 80, 156: 81, 157: 81, 158: 82, 159: 82, 160: 83, 161: 83, 162: 84, 163: 85, 164: 85, 165: 86, 166: 86, 167: 87, 168: 87, 169: 88, 170: 88, 171: 89, 172: 89, 173: 90, 174: 91, 175: 91, 176: 92, 177: 92, 178: 93, 179: 93, 180: 94, 181: 94, 182: 95, 183: 95, 184: 96, 185: 96, 186: 97, 187: 98, 188: 98, 189: 99, 190: 99, 191: 100, 192: 100, 193: 101, 194: 101, 195: 102, 196: 102, 197: 103, 198: 104, 199: 104, 200: 105, 201: 105, 202: 106, 203: 106, 204: 107, 205: 107, 206: 108, 207: 108, 208: 109, 209: 109, 210: 110, 211: 111, 212: 111, 213: 112, 214: 112, 215: 113, 216: 113, 217: 114, 218: 114, 219: 115, 220: 115, 221: 116, 222: 117, 223: 117, 224: 118, 225: 118, 226: 119, 227: 119, 228: 120, 229: 120, 230: 121, 231: 121, 232: 122, 233: 122, 234: 123, 235: 124, 236: 124, 237: 125, 238: 125, 239: 126, 240: 126, 241: 127, 242: 127, 243: 128, 244: 128, 245: 129, 246: 130, (247, math.inf): 130 
            },    
            "tabla B-7": {
                (0, 151): 45, 152: 46, 153: 47, 154: 47, 155: 48, 156: 49, 157: 50, 158: 51, 159: 51, 160: 52, 161: 53, 162: 54, 163: 54, 164: 55, 165: 56, 166: 57, 167: 58, 168: 58, 169: 59, 170: 60, 171: 61, 172: 61, 173: 62, 174: 63, 175: 64, 176: 65, 177: 65, 178: 66, 179: 67, 180: 68, 181: 68, 182: 69, 183: 70, 184: 71, 185: 72, 186: 72, 187: 73, 188: 74, 189: 75, 190: 75, 191: 76, 192: 77, 193: 78, 194: 79, 195: 79, 196: 80, 197: 81, 198: 82, 199: 82, 200: 83, 201: 84, 202: 85, 203: 85, 204: 86, 205: 87, 206: 88, 207: 89, 208: 89, 209: 90, 210: 91, 211: 92, 212: 92, 213: 93, 214: 94, 215: 95, 216: 96, 217: 96, 218: 97, 219: 98, 220: 99, 221: 99, 222: 100, 223: 101, 224: 102, 225: 103, 226: 103, 227: 104, 228: 105, 229: 106, 230: 106, 231: 107, 232: 108, 233: 109, 234: 110, 235: 110, 236: 111, 237: 112, 238: 113, 239: 113, 240: 114, 241: 115, 242: 116, 243: 117, 244: 117, 245: 118, 246: 119, 247: 120, 248: 120, 249: 121, 250: 122, 251: 123, 252: 124, 253: 124, 254: 125, 255: 126, 256: 127, 257: 127, 258: 128, 259: 129, (260, math.inf): 130
            },          
            "tabla B-8": {
                (0, 95): 39, 96: 39, 97: 40, 98: 41, 99: 41, 100: 42, 101: 43, 102: 43, 103: 44, 104: 45, 105: 45, 106: 46, 107: 47, 108: 47, 109: 48, 110: 48, 111: 49, 112: 50, 113: 50, 114: 51, 115: 52, 116: 52, 117: 53, 118: 54, 119: 54, 120: 55, 121: 56, 122: 56, 123: 57, 124: 57, 125: 58, 126: 59, 127: 59, 128: 60, 129: 61, 130: 61, 131: 62, 132: 63, 133: 63, 134: 64, 135: 64, 136: 65, 137: 66, 138: 66, 139: 67, 140: 68, 141: 68, 142: 69, 143: 70, 144: 70, 145: 71, 146: 72, 147: 72, 148: 73, 149: 73, 150: 74, 151: 75, 152: 75, 153: 76, 154: 77, 155: 77, 156: 78, 157: 79, 158: 79, 159: 80, 160: 81, 161: 81, 162: 82, 163: 82, 164: 83, 165: 84, 166: 84, 167: 85, 168: 86, 169: 86, 170: 87, 171: 88, 172: 88, 173: 89, 174: 90, 175: 90, 176: 91, 177: 91, 178: 92, 179: 93, 180: 93, 181: 94, 182: 95, 183: 95, 184: 96, 185: 97, 186: 97, 187: 98, 188: 99, 189: 99, 190: 100, 191: 10, 192: 101, 193: 102, 194: 102, 195: 103, 196: 104, 197: 104, 198: 105, 199: 106, 200: 106, 201: 107, 202: 107, 203: 108, 204: 109, 205: 109, 206: 110, 207: 111, 208: 111, 209: 112, 210: 113, 211: 113, 212: 114, 213: 115, 214: 115, 215: 116, 216: 116, 217: 117, 218: 118, 219: 118, 220: 119, 221: 120, 222: 120, 223: 121, 224: 122, 225: 122, 226: 123, 227: 124, 228: 124, 229: 125, 230: 125, 231: 126, 232: 127, 233: 127, 234: 128, 235: 129, 236: 129, (237, math.inf): 130
            },
            "tabla B-9": {
                (0, 136): 45, 137: 46, 138: 46, 139: 47, 140: 48, 141: 49, 142: 50, 143: 50, 144: 51, 145: 52, 146: 53, 147: 54, 148: 54, 149: 55, 150: 56, 151: 57, 152: 58, 153: 58, 154: 59, 155: 60, 156: 61, 157: 62, 158: 62, 159: 63, 160: 64, 161: 65, 162: 66, 163: 66, 164: 67, 165: 68, 166: 69, 167: 70, 168: 70, 169: 71, 170: 72, 171: 73, 172: 74, 173: 74, 174: 75, 175: 76, 176: 77, 177: 78, 178: 78, 179: 79, 180: 80, 181: 81, 182: 82, 183: 82, 184: 83, 185: 84, 186: 85, 187: 86, 188: 86, 189: 87, 190: 88, 191: 89, 192: 90, 193: 90, 194: 91, 195: 92, 196: 93, 197: 94, 198: 94, 199: 95, 200: 96, 201: 97, 202: 98, 203: 98, 204: 99, 205: 100, 206: 101, 207: 102, 208: 102, 209: 103, 210: 104, 211: 105, 212: 106, 213: 106, 214: 107, 215: 108, 216: 109, 217: 110, 218: 110, 219: 111, 220: 112, 221: 113, 222: 114, 223: 114, 224: 115, 225: 116, 226: 117, 227: 118, 228: 118, 229: 119, 230: 120, 231: 121, 232: 122, 233: 122, 234: 123, 235: 124, 236: 125, 237: 126, 238: 126, 239: 127, 240: 128, 241: 129, 242: 130, (243, math.inf): 130 
            },
            "tabla B-10": {
                (0, 140): 40, 141: 41, 142: 42, 143: 44, 144: 45, 145: 46, 146: 47, 147: 48, 148: 49, 149: 51, 150: 52, 151: 53, 152: 54, 153: 55, 154: 56, 155: 58, 156: 59, 157: 60, 158: 61, 159: 62, 160: 63, 161: 65, 162: 66, 163: 67, 164: 68, 165: 69, 166: 70, 167: 71, 168: 73, 169: 74, 170: 75, 171: 76, 172: 77, 173: 78, 174: 80, 175: 81, 176: 82, 177: 83, 178: 84, 179: 85, 180: 87, 181: 88, 182: 89, 183: 90, 184: 91, 185: 92, 186: 94, 187: 95, 188: 96, 189: 97, 190: 98, 191: 99, 192: 101, 193: 102, 194: 103, 195: 104, 196: 105, 197: 106, 198: 108, 199: 109, 200: 110, 201: 111, 202: 112, 203: 113, 204: 115, 205: 116, 206: 117, 207: 118, 208: 119, 209: 120, 210: 121, 211: 123, 212: 124, 213: 125, 214: 126, 215: 127, 216: 128, (217, math.inf): 130
            },
            "tabla B-11": {
                (0, 126): 45, 127: 46, 128: 47, 129: 48, 130: 49, 131: 50, 132: 51, 133: 52, 134: 53, 135: 54, 136: 55, 137: 56, 138: 57, 139: 58, 140: 59, 141: 60, 142: 61, 143: 62, 144: 63, 145: 64, 146: 65, 147: 66, 148: 67, 149: 68, 150: 69, 151: 70, 152: 70, 153: 71, 154: 72, 155: 73, 156: 74, 157: 75, 158: 76, 159: 77, 160: 78, 161: 79, 162: 80, 163: 81, 164: 82, 165: 83, 166: 84, 167: 85, 168: 86, 169: 87, 170: 88, 171: 89, 172: 90, 173: 91, 174: 92, 175: 93, 176: 94, 177: 95, 178: 96, 179: 97, 180: 98, 181: 99, 182: 100, 183: 101, 184: 102, 185: 103, 186: 104, 187: 105, 188: 106, 189: 107, 190: 107, 191: 108, 192: 109, 193: 110, 194: 111, 195: 112, 196: 113, 197: 114, 198: 115, 199: 116, 200: 117, 201: 118, 202: 119, 203: 120, 204: 121, 205: 122, 206: 123, 207: 124, 208: 125, 209: 126, 210: 127, 211: 128, 212: 129, (213, math.inf): 130 
            }                                                                          
        }   

    def define_table(self):
        if self.age > 5 and self.age < 8:
            return "tabla B-1"
        elif self.age > 7 and self.age < 10:
            return "tabla B-2"
        elif self.age > 9 and self.age < 12:
            return "tabla B-3"
        elif self.age > 11 and self.age < 14:
            return "tabla B-4"
        elif self.age > 13 and self.age < 16:
            return "tabla B-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla B-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla B-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla B-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla B-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla B-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla B-11"           

    def add_points(self, subarea, points):
        print("Points: ", points)
        if int(points) != -1:
            self.coded_points += int(points)

            if subarea is "Work Memory":
                self.work_memory += int(points)
                print("WORK MEMORY: ", self.work_memory)
            elif subarea is "Executive Functions":
                self.executive_functions += int(points)
                print("EXECUTIVE FUNCTIONS: ", self.executive_functions)
               
    def calculate_points(self):
        # Dorsolateral: Memoria de trabajo
        signaling = Signaling_Handler(self.banfe_id, self.age, self.schoolarship)
        data_signaling = signaling.get_data()

        if data_signaling is not "DoesNotExist":
            coded_signaling = signaling.get_data_coded()
            self.add_points("Work Memory", coded_signaling['encoded_perseverations'])
            self.add_points("Work Memory", coded_signaling['encoded_time'])
            self.add_points("Work Memory", data_signaling['successes'])
        
            
        substraction = Substraction_Handler(self.banfe_id, self.age, self.schoolarship)
        data_substraction = substraction.get_data()

        if data_substraction is not "DoesNotExist":
            coded_substraction = substraction.get_data_coded()            
            self.add_points("Work Memory", coded_substraction['encoded_time_a'])
            self.add_points("Work Memory", data_substraction['successes_a'])
            self.add_points("Work Memory", coded_substraction['encoded_time_b'])
            self.add_points("Work Memory", data_substraction['successes_b'])

        addition = Addition_Handler(self.banfe_id, self.age, self.schoolarship)
        data_addition = addition.get_data()

        if data_addition is not "DoesNotExist":
            coded_addition = addition.get_data_coded()
            self.add_points("Work Memory", coded_addition['encoded_time'])
            self.add_points("Work Memory", data_addition['successes'])
        
        ordering = Ordering_Handler(self.banfe_id, self.age, self.schoolarship)
        coded_ordering = ordering.get_data_coded()

        if coded_ordering is not "DoesNotEncoded":
            self.add_points("Work Memory", coded_ordering['encoded_essays_first_list'])
            self.add_points("Work Memory", coded_ordering['encoded_essays_second_list'])
            self.add_points("Work Memory", coded_ordering['encoded_essays_third_list'])


        print("WORK MEMORY VA EN: ", self.work_memory)
        
        visuospatial_memory = Visuospatial_Memory_Handler(self.banfe_id, self.age, self.schoolarship)
        data_memory = visuospatial_memory.get_data()

        if data_memory is not "DoesNotExist":
            coded_memory = visuospatial_memory.get_data_coded()            
            self.add_points("Work Memory", data_memory['maximum_sequence'])
            self.add_points("Work Memory", coded_memory['encoded_perseverations'])
            self.add_points("Work Memory", coded_memory['encoded_order_errors'])

        print("MEMORIA DE TRABAJO: ",self.work_memory)
        # Dorsolateral: Funciones ejecutivas
        labyrinths = Labyrinths_Handler(self.banfe_id, self.age, self.schoolarship)
        coded_labyrinths = labyrinths.get_data_coded()

        if coded_labyrinths is not "DoesNotEncoded":
            self.add_points("Executive Functions", coded_labyrinths['encoded_caught'])
            self.add_points("Executive Functions", coded_labyrinths['encoded_time'])

            print("EXECUTIVE FUNCTIONS: ", self.executive_functions)
        
        cards_sorting = Card_Sorting_Handler(self.banfe_id, self.age, self.schoolarship)
        data_cards = cards_sorting.get_data()

        if data_cards is not "DoesNotExist":
            coded_cards = cards_sorting.get_data_coded()
            self.add_points("Executive Functions", data_cards['successes'])
            self.add_points("Executive Functions", coded_cards['encoded_perseverations'])
            self.add_points("Executive Functions", coded_cards['encoded_deferred_perseverations'])
            self.add_points("Executive Functions", coded_cards['encoded_time'])

            print("EXECUTIVE FUNCTIONS: ", self.executive_functions)

        semantics = Semantic_Classification_Handler(self.banfe_id, self.age, self.schoolarship)
        coded_semantics = semantics.get_data_coded()

        if coded_semantics is not "DoesNotEncoded":
            self.add_points("Executive Functions", coded_semantics['encoded_total_categories'])
            self.add_points("Executive Functions", coded_semantics['encoded_total_average'])
            self.add_points("Executive Functions", coded_semantics['encoded_total_score'])  

            print("EXECUTIVE FUNCTIONS: ", self.executive_functions)      

        verbal_fluency = Verbal_Fluency_Handler(self.banfe_id, self.age, self.schoolarship)
        coded_fluency = verbal_fluency.get_data_coded()

        if coded_fluency is not "DoesNotEncoded":
            self.add_points("Executive Functions", coded_fluency['encoded_successes'])
            self.add_points("Executive Functions", coded_fluency['encoded_perseverations']) 

            print("EXECUTIVE FUNCTIONS: ", self.executive_functions)        

        towers_hanoi = Towers_Hanoi_Handler(self.banfe_id, self.age, self.schoolarship)
        coded_towers = towers_hanoi.get_data_coded()
        print(coded_towers)
        if coded_towers is not "DoesNotEncoded":
            self.add_points("Executive Functions", coded_towers['encoded_movements_first'])
            self.add_points("Executive Functions", coded_towers['encoded_time_first'])  
            self.add_points("Executive Functions", coded_towers['encoded_movements_second'])
            self.add_points("Executive Functions", coded_towers['encoded_time_second'])                       
        
            print("FUNCIONES EJECUTIVAS: ",self.executive_functions)
        
        print("EXECUTIVE FUNCTIONS: ", self.executive_functions)
        return {
            'dorsolateral': self.coded_points,
            'work_memory': self.work_memory,
            'executive_functions': self.executive_functions,
            'encoded_dorsolateral': self.get_data_coded(self.coded_points)
        }
        
    def get_data_coded(self, natural_points):
        points = self.points_dorsolateral.get(self.define_table())

        if points is not None:
            for rank, coded_value in points.items():
                if isinstance(rank, tuple):
                    start, end = rank
                    if natural_points >= start and natural_points <= end:
                        print(rank)
                        return coded_value
                else:
                    if rank == natural_points:
                        return coded_value
        return 0         

class Full_Battery:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship
 
        self.points_battery = {
            "tabla B-1": {
                (0, 57): 45, 58: 46, 59: 47, 60: 48, 61: 49, 62: 49, 63: 50, 64: 51, 65: 52, 66: 53, 67: 54, 68: 54, 69: 55, 70: 56, 71: 57, 72: 58, 73: 59, 74: 60, 75: 60, 76: 61, 77: 62, 78: 63, 79: 64, 80: 65, 81: 66, 82: 66, 83: 67, 84: 68, 85: 69, 86: 70, 87: 71, 88: 72, 89: 72, 90: 73, 91: 74, 92: 75, 93: 76, 94: 77, 95: 77, 96: 78, 97: 79, 98: 80, 99: 81, 100: 82, 101: 83, 102: 83, 103: 84, 104: 85, 105: 86, 106: 87, 107: 88, 108: 89, 109: 89, 110: 90, 111: 91, 112: 92, 113: 93, 114: 94, 115: 95, 116: 95, 117: 96, 118: 97, 119: 98, 120: 99, 121: 100, 122: 100, 123: 101, 124: 102, 125: 103, 126: 104, 127: 105, 128: 106, 129: 106, 130: 107, 131: 108, 132: 109, 133: 110, 134: 111, 135: 112, 136: 112, 137: 113, 138: 114, 139: 115, 140: 116, 141: 117, 142: 118, 143: 118, 144: 119, 145: 120, 146: 121, 147: 122, 148: 123, 149: 123, 150: 124, 151: 125, 152: 126, 153: 127, 154: 128, 155: 129, 156: 129, 157: 130, 158: 131, 159: 132, (160, math.inf): 133
            },
            "tabla B-2": {
                (0, 246): 44, 247: 44, 248: 45, 249: 45, 250: 46, 251: 46, 252: 47, 253: 47, 254: 48, 255: 48, 256: 49, 257: 49, 258: 50, 259: 50, 260: 51, 261: 51, 262: 52, 263: 53, 264: 53, 265: 54, 266: 54, 267: 55, 268: 55, 269: 56, 270: 56, 271: 57, 272: 57, 273: 58, 274: 58, 275: 59, 276: 59, 277: 60, 278: 60, 279: 61, 280: 61, 281: 62, 282: 62, 283: 63, 284: 63, 285: 64, 286: 64, 287: 65, 288: 65, 289: 66, 290: 66, 291: 67, 292: 67, 293: 68, 294: 69, 295: 69, 296: 70, 297: 70, 298: 71, 299: 71, 300: 72, 301: 72, 302: 73, 303: 73, 304: 74, 305: 74, 306: 75, 307: 75, 308: 76, 309: 76, 310: 77, 311: 77, 312: 78, 313: 78, 314: 79, 315: 79, 316: 80, 317: 80, 318: 81, 319: 81, 320: 82, 321: 82, 322: 83, 323: 83, 324: 84, 325: 84, 326: 85, 327: 86, 328: 86, 329: 87, 330: 87, 331: 88, 332: 88, 333: 89, 334: 89, 335: 90, 336: 90, 337: 91, 338: 91, 339: 92, 340: 92, 341: 93, 342: 93, 343: 94, 344: 94, 345: 95, 346: 95, 347: 96, 348: 96, 349: 97, 350: 97, 351: 98, 352: 98, 353: 99, 354: 99, 355: 100, 356: 100, 357: 101, 358: 101, 359: 102, 360: 103, 361: 103, 362: 104, 363: 104, 364: 105, 365: 105, 366: 106, 367: 106, 368: 107, 369: 107, 370: 108, 371: 108, 372: 109, 373: 109, 374: 110, 375: 110, 376: 111, 377: 111, 378: 112, 379: 112, 380: 113, 381: 113, 382: 114, 383: 114, 384: 115, 385: 115, 386: 116, 387: 116, 388: 117, 389: 117, 390: 118, 391: 118, 392: 119, 393: 120, 394: 120, 395: 121, 396: 121, 397: 122, 398: 122, 399: 123, 400: 123, 401: 124, 402: 124, 403: 125, 404: 125, 405: 126, 406: 126, 407: 127, 408: 127, 409: 128, 410: 128, 411: 129, 412: 129, 413: 130, (414, math.inf): 130 
            },
            "tabla B-3": {
                (0, 316): 45, 317: 45, 318: 46, 319: 46, 320: 47, 321: 48, 322: 48, 323: 49, 324: 49, 325: 50, 326: 51, 327: 51, 328: 52, 329: 52, 330: 53, 331: 54, 332: 54, 333: 55, 334: 55, 335: 56, 336: 57, 337: 57, 338: 58, 339: 59, 340: 59, 341: 60, 342: 60, 343: 61, 344: 62, 345: 62, 346: 63, 347: 63, 348: 64, 349: 65, 350: 65, 351: 66, 352: 66, 353: 67, 354: 68, 355: 68, 356: 69, 357: 69, 358: 70, 359: 71, 360: 71, 361: 72, 362: 72, 363: 73, 364: 74, 365: 74, 366: 75, 367: 75, 368: 76, 369: 77, 370: 77, 371: 78, 372: 78, 373: 79, 374: 80, 375: 80, 376: 81, 377: 82, 378: 82, 379: 83, 380: 83, 381: 84, 382: 85, 383: 85, 384: 86, 385: 86, 386: 87, 387: 88, 388: 88, 389: 89, 390: 89, 391: 90, 392: 91, 393: 91, 394: 92, 395: 92, 396: 93, 397: 94, 398: 94, 399: 95, 400: 95, 401: 96, 402: 97, 403: 97, 404: 98, 405: 98, 406: 99, 407: 100, 408: 100, 409: 101, 410: 101, 411: 102, 412: 103, 413: 103, 414: 104, 415: 105, 416: 105, 417: 106, 418: 106, 419: 107, 420: 108, 421: 108, 422: 109, 423: 109, 424: 110, 425: 111, 426: 111, 427: 112, 428: 112, 429: 113, 430: 114, 431: 114, 432: 115, 433: 115, 434: 116, 435: 117, 436: 117, 437: 118, 438: 118, 439: 119, 440: 120, 441: 120, 442: 121, 443: 121, 444: 122, 445: 123, 446: 124, 447: 124, 448: 124, 449: 125, 450: 126, 451: 126, 452: 127, 453: 128, 454: 128, 455: 129, 456: 129, (457, math.inf): 130 
            },
            "tabla B-4": {
                (0, 338): 45, 339: 46, 340: 46, 341: 47, 342: 48, 343: 49, 344: 49, 345: 50, 346: 51, 347: 52, 348: 52, 349: 53, 350: 54, 351: 55, 352: 55, 353: 55, 354: 57, 355: 58, 356: 58, 357: 59, 358: 60, 359: 61, 360: 61, 361: 62, 362: 63, 363: 64, 364: 64, 365: 65, 366: 66, 367: 67, 368: 67, 369: 68, 370: 69, 371: 70, 372: 70, 373: 71, 374: 72, 375: 73, 376: 73, 377: 74, 378: 75, 379: 76, 380: 76, 381: 77, 382: 78, 383: 79, 384: 79, 385: 80, 386: 81, 387: 82, 388: 82, 389: 83, 390: 84, 391: 85, 392: 85, 393: 86, 394: 87, 395: 88, 396: 88, 397: 89, 398: 90, 399: 91, 400: 91, 401: 92, 402: 93, 403: 94, 404: 94, 405: 95, 406: 96, 407: 97, 408: 97, 409: 98, 410: 99, 411: 100, 412: 100, 413: 101, 414: 102, 415: 103, 416: 103, 417: 104, 418: 105, 419: 106, 420: 106, 421: 107, 422: 108, 423: 109, 424: 109, 425: 110, 426: 111, 427: 112, 428: 112, 429: 113, 430: 114, 431: 115, 432: 115, 433: 116, 434: 117, 435: 118, 436: 118, 437: 119, 438: 120, 439: 121, 440: 121, 441: 122, 442: 123, 443: 124, 444: 124, 445: 125, 446: 126, 447: 127, 448: 127, 449: 128, 450: 129, 451: 130, (452, math.inf): 130
            },
            "tabla B-5": {
                (0, 355): 45, 356: 45, 357: 46, 358: 47, 359: 48, 360: 49, 361: 50, 362: 50, 363: 51, 364: 52, 365: 53, 366: 54, 367: 55, 368: 56, 369: 56, 370: 57, 371: 58, 372: 59, 373: 60, 374: 61, 375: 61, 376: 62, 377: 63, 378: 64, 379: 65, 380: 66, 381: 67, 382: 67, 383: 68, 384: 69, 385: 70, 386: 71, 387: 72, 388: 72, 389: 73, 390: 74, 391: 75, 392: 76, 393: 77, 394: 78, 395: 78, 396: 79, 397: 80, 398: 81, 399: 82, 400: 83, 401: 83, 402: 84, 403: 85, 404: 86, 405: 87, 406: 88, 407: 89, 408: 89, 409: 90, 410: 91, 411: 92, 412: 93, 413: 94, 414: 94, 415: 95, 416: 96, 417: 97, 418: 98, 419: 99, 420: 99, 421: 100, 422: 101, 423: 102, 424: 103, 425: 104, 426: 105, 427: 105, 428: 106, 429: 107, 430: 108, 431: 109, 432: 110, 433: 110, 434: 111, 435: 112, 436: 113, 437: 114, 438: 115, 439: 116, 440: 116, 441: 116, 442: 118, 443: 119, 444: 120, 445: 121, 446: 121, 447: 122, 448: 123, 449: 124, 450: 125, 451: 126, 452: 127, 453: 127, 454: 128, 455: 129, (456, math.inf): 130                   
            },
            "tabla B-6": {
                (0, 280): 45, 281: 45, 282: 46, 283: 46, 284: 47, 285: 47, 286: 48, 287: 48, 288: 49, 289: 49, 290: 49, 291: 50, 292: 50, 293: 51, 294: 51, 295: 52, 296: 52, 297: 53, 298: 53, 299: 54, 300: 54, 301: 55, 302: 55, 303: 55, 304: 56, 305: 56, 306: 57, 307: 57, 308: 58, 309: 58, 310: 59, 311: 59, 312: 60, 313: 60, 314: 60, 315: 61, 316: 61, 317: 62, 318: 62, 319: 63, 320: 63, 321: 64, 322: 64, 323: 65, 324: 65, 325: 66, 326: 66, 327: 66, 328: 67, 329: 67, 330: 68, 331: 68, 332: 69, 333: 69, 334: 70, 335: 70, 336: 71, 337: 71, 338: 71, 339: 72, 340: 72, 341: 73, 342: 73, 343: 74, 344: 74, 345: 75, 346: 75, 347: 76, 348: 76, 349: 77, 350: 77, 351: 77, 352: 78, 353: 78, 354: 79, 355: 79, 356: 80, 357: 80, 358: 81, 359: 84, 360: 82, 361: 82, 362: 82, 363: 83, 364: 83, 365: 84, 366: 84, 367: 85, 368: 85, 369: 86, 370: 86, 371: 87, 372: 87, 373: 88, 374: 88, 375: 88, 376: 89, 377: 89, 378: 90, 379: 90, 380: 91, 381: 91, 382: 92, 383: 92, 384: 93, 385: 93, 386: 83, 387: 94, 388: 94, 389: 95, 390: 95, 391: 96, 392: 96, 393: 97, 394: 97, 395: 98, 396: 98, 397: 99, 398: 99, 399: 99, 400: 100, 401: 100, 402: 101, 403: 101, 404: 102, 405: 102, 406: 103, 407: 103, 408: 104, 409: 104, 410: 105, 411: 105, 412: 105,  413: 106, 414: 106, 415: 107, 416: 107, 417: 108, 418: 108, 419: 109, 420: 109, 421: 110, 422: 110, 423: 110, 424: 111, 425: 111, 426: 112, 427: 113, 428: 113, 429: 113, 430: 114, 431: 114, 432: 115, 433: 115, 434: 116, 435: 116, 436: 116, 437: 117, 438: 117, 439: 118, 440: 118, 441: 119, 442: 119, 443: 120, 444: 120, 445: 121, 446: 121, 447: 121, 448: 122, 449: 122, 450: 123, 451: 123, 452: 124, 453: 124, 454: 125, 455: 125, 456: 126, 457: 126, 458: 127, 459: 127, 460: 127, 461: 128, 462: 128, 463: 129, 464: 129, 465: 130, (466, math.inf): 130  
            },    
            "tabla B-7": {
                (0, 346): 45, 347: 45, 348: 46, 349: 46, 350: 47, 351: 48, 352: 48, 353: 49, 354: 49, 355: 50, 356: 51, 357: 51, 358: 52, 359: 52, 360: 53, 361: 54, 362: 54, 363: 55, 364: 55, 365: 56, 366: 57, 367: 57, 368: 58, 369: 58, 370: 59, 371: 60, 372: 60, 373: 61, 374: 61, 375: 62, 376: 63, 377: 63, 378: 64, 379: 64, 380: 65, 381: 66, 382: 66, 383: 67, 384: 67, 385: 68, 386: 69, 387: 69, 388: 70, 389: 70, 390: 71, 391: 72, 393: 73, 394: 73, 395: 74, 396: 75, 397: 75, 398: 76, 399: 76, 400: 77, 401: 78, 402: 78, 403: 79, 404: 79, 405: 80, 406: 81, 407: 81, 408: 82, 409: 82, 410: 83, 411: 84, 412: 84, 413: 85, 414: 85, 415: 86, 416: 87, 417: 87, 418: 88, 419: 88, 420: 89, 421: 90, 422: 90, 423: 91, 424: 91, 425: 92, 426: 93, 427: 93, 428: 94, 429: 95, 430: 95, 431: 96, 432: 96, 433: 97, 434: 98, 435: 98, 436: 99, 437: 99, 438: 100, 439: 101, 440: 101, 441: 102, 442: 102, 443: 103, 444: 104, 445: 104, 446: 105, 447: 105, 448: 106, 449: 107, 450: 107, 451: 108, 452: 108, 453: 109, 454: 110, 455: 110, 456: 111, 457: 111, 458: 112, 459: 113, 460: 113, 461: 114, 462: 114, 463: 115, 464: 116, 465: 116, 466: 117, 467: 117, 468: 118, 469: 119, 470: 119, 471: 120, 472: 120, 473: 121, 474: 122, 475: 122, 476: 123, 477: 123, 478: 124, 479: 125, 480: 125, 481: 126, 482: 126, 483: 127, 484: 128, 485: 128, 486: 129, 487: 129, (488, math.inf): 130
            },          
            "tabla B-8": {
                (0, 295): 44, 296: 45, 297: 45, 298: 46, 299: 47, 300: 47, 301: 48, 302: 48, 303: 49, 304: 49, 305: 50, 306: 50, 307: 51, 308: 51, 309: 52, 310: 52, 311: 53, 312: 53, 313: 54, 314: 54, 315: 55, 316: 55, 317: 56, 318: 56, 319: 57, 320: 57, 321: 58, 322: 58, 323: 59, 324: 59, 325: 60, 326: 60, 327: 61, 328: 61, 329: 62, 330: 62, 331: 63, 332: 63, 333: 64, 334: 64, 335: 65, 336: 65, 337: 66, 338: 66, 339: 67, 340: 67, 341: 68, 342: 68, 343: 69, 344: 69, 345: 70, 346: 70, 347: 71, 348: 71, 349: 72, 350: 72, 351: 73, 352: 73, 353: 74, 354: 74, 355: 75, 356: 75, 357: 76, 358: 76, 359: 77, 360: 77, 361: 78, 362: 78, 363: 79, 364: 79, 365: 80, 366: 80, 367: 81, 368: 81, 369: 82, 370: 82, 371: 83, 372: 83, 373: 84, 374: 84, 375: 85, 376: 85, 377: 86, 378: 86, 379: 87, 380: 87, 381: 88, 382: 88, 383: 89, 384: 89, 385: 90, 386: 90, 387: 91, 388: 91, 389: 92, 390: 92, 391: 93, 392: 93, 393: 94, 394: 94, 395: 95, 396: 95, 397: 96, 398: 97, 399: 97, 400: 98, 401: 98, 402: 99, 403: 99, 404: 100, 405: 100, 406: 101, 407: 101, 408: 102, 409: 102, 410: 103, 411: 103, 412: 104, 413: 104, 414: 105, 415: 105, 416: 106, 417: 106, 418: 107, 419: 107, 420: 108, 421: 108, 422: 109, 423: 109, 424: 110, 425: 110, 426: 111, 427: 111, 428: 112, 429: 112, 430: 113, 431: 113, 432: 114, 433: 114, 434: 115, 435: 115, 436: 116, 437: 116, 438: 117, 439: 117, 440: 118, 441: 118, 442: 119, 443: 119, 444: 120, 445: 120, 446: 120, 447: 121, 448: 122, 449: 122, 450: 123, 451: 123, 452: 124, 453: 124, 454: 125, 455: 125, 456: 126, 457: 126, 458: 127, 459: 127, 460: 128, 461: 128, 462: 129, 463: 129, 464: 130, (465, math.inf): 130  
            },
            "tabla B-9": {
                (0, 347): 45, 348: 45, 349: 46, 350: 47, 351: 47, 352: 48, 353: 49, 354: 50, 355: 50, 356: 51, 357: 52, 358: 53, 359: 53, 360: 54, 361: 55, 362: 56, 363: 56, 364: 57, 365: 58, 366: 59, 367: 59, 368: 60, 369: 61, 370: 62, 371: 62, 372: 63, 373: 64, 374: 65, 375: 65, 376: 66, 377: 67, 378: 67, 379: 68, 380: 69, 381: 70, 382: 70, 383: 71, 384: 72, 385: 73, 386: 73, 387: 74, 388: 75, 389: 76, 390: 76, 391: 77, 392: 78, 393: 79, 394: 79, 395: 80, 396: 81, 397: 82, 398: 82, 399: 83, 400: 84, 401: 84, 402: 85, 403: 86, 404: 87, 405: 87, 406: 88, 407: 89, 408: 90, 409: 90, 410: 91, 411: 92, 412: 93, 413: 93, 414: 94, 415: 95, 416: 96, 417: 96, 418: 97, 419: 98, 420: 99, 421: 99, 422: 100, 423: 101, 424: 101, 425: 102, 426: 103, 427: 104, 428: 104, 429: 105, 430: 106, 431: 107, 432: 107, 433: 108, 434: 109, 435: 110, 436: 110, 437: 111, 438: 112, 439: 113, 440: 113, 441: 114, 442: 115, 443: 116, 444: 116, 445: 117, 446: 118, 447: 118, 448: 119, 449: 120, 450: 121, 451: 121, 452: 122, 453: 123, 454: 124, 455: 124, 456: 125, 457: 126, 458: 127, 459: 127, 460: 128, 461: 129, 462: 130, (463, math.inf): 130
            },
            "tabla B-10": {
                (0, 335): 45, 336: 45, 337: 46, 338: 47, 339: 48, 340: 49, 341: 49, 342: 50, 343: 51, 344: 52, 345: 53, 346: 53, 347: 54, 348: 55, 349: 56, 350: 57, 351: 57, 352: 58, 353: 59, 354: 60, 355: 61, 356: 61, 357: 62, 358: 63, 359: 64, 360: 65, 361: 65, 362: 66, 363: 67, 364: 68, 365: 69, 366: 69, 367: 70, 368: 71, 369: 72, 370: 73, 371: 73, 372: 74, 373: 75, 374: 76, 375: 77, 376: 77, 377: 78, 378: 79, 379: 80, 380: 81, 381: 81, 382: 82, 383: 83, 384: 84, 385: 85, 386: 85, 387: 86, 388: 87, 389: 88, 390: 89, 391: 89, 392: 90, 393: 91, 394: 92, 395: 93, 396: 93, 397: 94, 398: 95, 399: 96, 400: 97, 401: 97, 402: 98, 403: 99, 404: 100, 405: 101, 406: 102, 407: 102, 408: 103, 409: 104, 410: 105, 411: 106, 412: 106, 413: 107, 414: 108, 415: 109, 416: 110, 417: 110, 418: 111, 419: 112, 420: 113, 421: 114, 422: 114, 423: 115, 424: 116, 425: 117, 426: 118, 427: 118, 428: 119, 429: 120, 430: 121, 431: 122, 432: 122, 433: 123, 434: 124, 435: 125, 436: 126, 437: 126, 438: 127, 439: 128, 440: 129, (441, math.inf): 130
            },
            "tabla B-11": {
                (0, 332): 45, 333: 46, 334: 47, 335: 48, 336: 48, 337: 49, 338: 50, 339: 51, 340: 52, 341: 53, 342: 54, 343: 55, 344: 56, 345: 57, 346: 58, 347: 59, 348: 59, 349: 60, 350: 61, 351: 62, 352: 63, 353: 64, 354: 65, 355: 66, 356: 67, 357: 68, 358: 69, 359: 70, 360: 71, 361: 71, 362: 72, 363: 73, 364: 74, 365: 75, 366: 76, 367: 77, 368: 78, 369: 79, 370: 80, 371: 81, 372: 82, 373: 82, 374: 83, 375: 84, 376: 85, 377: 86, 378: 87, 379: 88, 380: 89, 381: 90, 382: 91, 383: 92, 384: 93, 385: 94, 386: 94, 387: 95, 388: 96, 389: 97, 390: 98, 391: 99, 392: 100, 393: 101, 394: 102, 395: 103, 396: 104, 397: 105, 398: 105, 399: 106, 400: 107, 401: 108, 402: 109, 403: 110, 404: 111, 405: 112, 406: 113, 407: 114, 408: 115, 409: 116, 410: 117, 411: 117, 412: 118, 413: 119, 414: 120, 415: 121, 416: 122, 417: 123, 418: 124, 419: 125, 420: 126, 421: 127, 422: 128, 423: 128, 424: 129, (425, math.inf): 130
            }                                                                          
        }   

    def define_table(self):
        if self.age > 5 and self.age < 8:
            return "tabla B-1"
        elif self.age > 7 and self.age < 10:
            return "tabla B-2"
        elif self.age > 9 and self.age < 12:
            return "tabla B-3"
        elif self.age > 11 and self.age < 14:
            return "tabla B-4"
        elif self.age > 13 and self.age < 16:
            return "tabla B-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla B-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla B-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla B-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla B-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla B-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla B-11"           

    def get_data_coded(self, natural_points):
        points = self.points_battery.get(self.define_table())

        print("Bateria: ", natural_points)
        print("Tabla: ", points)

        if points is not None:
            for rank, coded_value in points.items():
                if isinstance(rank, tuple):
                    start, end = rank
                    if natural_points >= start and natural_points <= end:
                        print(rank)
                        return coded_value
                else:
                    if rank == natural_points:
                        return coded_value
        return 0         

class Labyrinths_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship
      
        self.points_cross = {
            "tabla A-1": {
                (0, 3): 5,  (4, 4): 4,  (5, 6): 3,  (7, 9): 2,  (10, math.inf): 1
            },
            "tabla A-2": {
                (0, 1): 5,  (2, 2): 4,  (3, 4): 3,  (5, 6): 2,  (7, math.inf): 1
            },
            "tabla A-3": {
                (0, 0): 5,  (1, 1): 4,  (2, 2): 3,  (3, 3): 2,  (4, math.inf): 1
            },
            "tabla A-4": {
                (0, 0): 5,  (1, 1): 3,  (2, 2): 2,  (3, math.inf): 1
            },
            "tabla A-5": {
                (0, 0): 5,  (1, 1): 4,  (2, 2): 2,  (3, math.inf): 1
            },
            "tabla A-6": {
                (0, 0): 3,  (1, math.inf): 1
            },    
            "tabla A-7": {
                (0, 0): 4,  (1, 1): 2,  (2, math.inf): 1
            },          
            "tabla A-8": {
                (0, 0): 5,  (1, 1): 4,  (2, 2): 3,  (3, 3): 2,  (4, math.inf): 1 
            },
            "tabla A-9": {
                (0, 0): 4,  (1, 1): 2,  (2, math.inf): 1
            },
            "tabla A-10": {
                (0, 0): 5,  (1, 1): 4,  (2, 2): 3,  (3, 4): 2,  (5, math.inf): 1 
            },
            "tabla A-11": {
                (0, 0): 5,  (1, 1): 4,  (2, 2): 3,  (3, 4): 2,  (5, math.inf): 1 
            }                                                                          
        }    
        self.points_caught = {
            "tabla A-1": {
                (0, 6): 5,  (7, 7): 4,  (8, 10): 3,  (11, 14): 2,  (15, math.inf): 1
            },
            "tabla A-2": {
                (0, 5): 5,  (6, 6): 4,  (7, 10): 3,  (11, 14): 2,  (15, math.inf): 1
            },
            "tabla A-3": {
                (0, 2): 5,  (3, 4): 3,  (5, 6): 2,  (7, math.inf): 1
            },
            "tabla A-4": {
                (0, 1): 5,  (2, 3): 3,  (4, 4): 2,  (5, math.inf): 1
            },
            "tabla A-5": {
                (0, 1): 5,  (2, 2): 4,  (3, 4): 3,  (5, 6): 2,  (7, math.inf): 1
            },
            "tabla A-6": {
                (0, 2): 5,  (3, 3): 4,  (4, 7): 3,  (8, 10): 2,  (11, math.inf): 1
            },    
            "tabla A-7": {
                (0, 1): 5,  (2, 2): 4,  (3, 3): 3,  (4, 4): 2,  (5, math.inf): 1
            },          
            "tabla A-8": {
                (0, 1): 5,  (2, 2): 4,  (3, 4): 3,  (5, 7): 2,  (8, math.inf): 1 
            },
            "tabla A-9": {
                (0, 0): 5,  (1, 1): 4,  (2, 3): 3,  (4, 4): 2,  (5, math.inf): 1 
            },
            "tabla A-10": {
                (0, 1): 5,  (2, 2): 4,  (3, 5): 3,  (6, 8): 2,  (9, math.inf): 1 
            },
            "tabla A-11": {
                (0, 1): 5,  (2, 2): 4,  (3, 5): 3,  (6, 8): 2,  (9, math.inf): 1 
            }                                                                      
        }    
        self.points_time = {
            "tabla A-1": {
                (1, 56): 5,  (57, 63): 4,  (64, 84): 3,  (85, 105): 2,  (106, math.inf): 1
            },
            "tabla A-2": {
                (1, 53): 5,  (54, 62): 4,  (63, 88): 3,  (89, 115): 2,  (116, math.inf): 1
            },
            "tabla A-3": {
                (1, 44): 5,  (45, 48): 4,  (49, 61): 3,  (62, 73): 2,  (74, math.inf): 1
            },
            "tabla A-4": {
                (1, 35): 5,  (36, 41): 4,  (42, 59): 3,  (60, 77): 2,  (78, math.inf): 1
            },
            "tabla A-5": {
                (1, 29): 5,  (30, 31): 4,  (32, 37): 3,  (38, 43): 2,  (44, math.inf): 1
            },
            "tabla A-6": {
                (1, 48): 5,  (49, 57): 4,  (58, 87): 3,  (88, 117): 2,  (118, math.inf): 1
            },    
            "tabla A-7": {
                (1, 27): 5,  (28, 31): 4,  (32, 43): 3,  (44, 55): 2,  (56, math.inf): 1
            },          
            "tabla A-8": {
                (1, 50): 5,  (51, 59): 4,  (60, 87): 3,  (88, 114): 2,  (115, math.inf): 1 
            },
            "tabla A-9": {
                (1, 38): 5,  (39, 45): 4,  (46, 64): 3,  (65, 83): 2,  (84, math.inf): 1 
            },
            "tabla A-10": {
                (1, 48): 5,  (49, 61): 4,  (62, 100): 3, (101, 139): 2,  (140, math.inf): 1 
            },
            "tabla A-11": {
                (1, 48): 5,  (49, 61): 4,  (62, 100): 3, (101, 139): 2,  (140, math.inf): 1 
            }                                                                      
        }    

    def define_table(self):
        if self.age > 5 and self.age < 8:
            return "tabla A-1"
        elif self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"           

    def get_data(self):
        try:
            labyrinths = Labyrinths.objects.get(banfe_test_id = self.banfe_id)
            return {
                'touch': labyrinths.touch,
                'cross': labyrinths.cross,
                'caught': labyrinths.caught,
                'time': labyrinths.time
            }

        except Labyrinths.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Labyrinths
        data_labyrinths = self.get_data()

        if data_labyrinths is not "DoesNotExist":
            return {
                'encoded_cross': self.encode_cross(data_labyrinths['cross']),
                'encoded_caught': self.encode_caught(data_labyrinths['caught']),
                'encoded_time': self.encode_time(data_labyrinths['time'])
            }
        else:
            return "DoesNotEncoded"

    def encode_cross(self,cross): 
        points = self.points_cross.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= cross <= rank[1]:
                    return coded_value
        return default_value                       

    def encode_caught(self,caught):     
        points = self.points_caught.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= caught <= rank[1]:
                    return coded_value
        return default_value
       
    def encode_time(self,time):
        points = self.points_time.get(self.define_table())
        
        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= time <= rank[1]:
                    return coded_value
        return default_value  

class Signaling_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship

        self.points_perseverations = {
            "tabla A-1": {
                (0, 3): 5,  (4, 4): 4,  (5, 8): 3,  (9, 11): 2,  (12, math.inf): 1
            },
            "tabla A-2": {
                (0, 2): 5,  (3, 3): 4,  (4, 6): 3,  (7, 9): 2,  (10, math.inf): 1
            },
            "tabla A-3": {
                (0, 1): 5,  (2, 2): 4,  (3, 3): 3,  (4, 4): 2,  (5, math.inf): 1
            },
            "tabla A-4": {
                (0, 2): 5,  (3, 3): 4,  (4, 5): 3,  (6, 7): 2,  (8, math.inf): 1
            },
            "tabla A-5": {
                (0, 2): 5,  (3, 3): 4,  (4, 5): 3,  (6, 8): 2,  (9, math.inf): 1
            },
            "tabla A-6": {
                (0, 2): 5,  (3, 3): 4,  (4, 4): 3,  (5, 6): 2,  (7, math.inf): 1
            },    
            "tabla A-7": {
                (0, 1): 5,  (2, 2): 4,  (3, 5): 3,  (6, 7): 2,  (8, math.inf): 1
            },          
            "tabla A-8": {
                (0, 2): 5,  (3, 3): 4,  (4, 6): 3,  (7, 9): 2,  (10, math.inf): 1 
            },
            "tabla A-9": {
                (0, 2): 5,  (3, 3): 4,  (4, 5): 3,  (6, 7): 2,  (8, math.inf): 1 
            },
            "tabla A-10": {
                (0, 4): 5,  (5, 5): 4,  (6, 8): 3, (9, 11): 2,  (12, math.inf): 1 
            },
            "tabla A-11": {
                (0, 3): 5,  (4, 5): 4,  (6, 8): 3, (9, 12): 2,  (13, math.inf): 1 
            }                                                                      
        }           
        self.points_time = {
            "tabla A-1": {
                (1, 110): 5,  (111, 132): 4,  (133, 196): 3,  (197, 261): 2,  (262, math.inf): 1
            },
            "tabla A-2": {
                (1, 93): 5,  (94, 110): 4,  (111, 161): 3,  (162, 212): 2,  (213, math.inf): 1
            },
            "tabla A-3": {
                (1, 92): 5,  (93, 106): 4,  (107, 148): 3,  (149, 190): 2,  (191, math.inf): 1
            },
            "tabla A-4": {
                (1, 84): 5,  (85, 100): 4,  (101, 148): 3,  (149, 196): 2,  (197, math.inf): 1
            },
            "tabla A-5": {
                (1, 69): 5,  (70, 82): 4,  (83, 122): 3,  (123, 162): 2,  (163, math.inf): 1
            },
            "tabla A-6": {
                (1, 75): 5,  (76, 92): 4,  (93, 148): 3,  (149, 204): 2,  (205, math.inf): 1
            },    
            "tabla A-7": {
                (1, 67): 5,  (68, 81): 4,  (82, 124): 3,  (125, 167): 2,  (168, math.inf): 1
            },          
            "tabla A-8": {
                (1, 77): 5,  (78, 92): 4,  (93, 138): 3,  (139, 184): 2,  (185, math.inf): 1 
            },
            "tabla A-9": {
                (1, 85): 5,  (86, 101): 4,  (102, 149): 3,  (150, 198): 2,  (199, math.inf): 1 
            },
            "tabla A-10": {
                (1, 86): 5,  (87, 104): 4,  (105, 160): 3, (161, 216): 2,  (217, math.inf): 1 
            },
            "tabla A-11": {
                (1, 72): 5,  (73, 86): 4,  (87, 128): 3, (129, 170): 2,  (171, math.inf): 1 
            }                                                                      
        }   

    def define_table(self):
        if self.age > 5 and self.age < 8:
            return "tabla A-1"
        elif self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"  

    def get_data(self):
        try:
            signaling = Signaling.objects.get(banfe_test_id = self.banfe_id)
            return {
                'successes': signaling.successes,
                'perseverations': signaling.perseverations,
                'omissions': signaling.omissions,
                'time': signaling.time
            }

        except Signaling.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Signaling
        data_signaling = self.get_data()

        if data_signaling is not "DoesNotExist":
            encoded_perseverations = self.encode_perseverations(data_signaling.get('perseverations'))
            encoded_time = self.encode_time(data_signaling.get('time'))
            return {
                'encoded_perseverations': encoded_perseverations,
                'encoded_time': encoded_time
            }            
        else:
            return "DoesNotEncoded"

    def encode_perseverations(self,perseverations):
        points = self.points_perseverations.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia
        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= perseverations <= rank[1]:
                    return coded_value
        return default_value                   


    def encode_time(self,time):
        points = self.points_time.get(self.define_table())
        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia
        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= time <= rank[1]:
                    return coded_value
        return default_value                

class Ordering_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship

        self.points_essays_first_list = {
            "tabla A-2": {
                (0, 0): 0, (1, 1): 5,  (2, 2): 4,  (3, 3): 2,  (4, 5): 1
            },
            "tabla A-3": {
                (0, 0): 0, (1, 1): 5,  (2, 2): 4,  (3, 3): 2,  (4, 5): 1
            },
            "tabla A-4": {
                (0, 0): 0, (1, 1): 5,  (2, 2): 3,  (3, 3): 2,  (4, 5): 1
            },
            "tabla A-5": {
                (0, 0): 0, (1, 1): 5,  (2, 2): 3,  (3, 5): 1
            },
            "tabla A-6": {
                (0, 0): 0, (1, 1): 5,  (2, 2): 4,  (3, 3): 3,  (4, 5): 2
            },    
            "tabla A-7": {
                (0, 0): 0, (1, 1): 5,  (2, 2): 3,  (3, 3): 2,  (4, 5): 1
            },          
            "tabla A-8": {
                (0, 0): 0, (1, 1): 5,  (2, 2): 4,  (3, 3): 3,  (4, 4): 2,  (5, 5): 1 
            },
            "tabla A-9": {
                (0, 0): 0, (1, 1): 4,  (2, 2): 3,  (3, 5): 1 
            },
            "tabla A-10": {
                (0, 0): 0, (1, 1): 5,  (2, 3): 3, (4, 4): 2,  (5, 5): 1 
            },
            "tabla A-11": {
                (0, 0): 0, (1, 2): 5, (3, 3): 3,  (4, 5): 2 
            }                                                                      
        }   
        self.points_essays_second_list = {
            "tabla A-2": {
                (0, 0): 0, (1, 2): 5,  (3, 3): 4,  (4, 4): 3,  (5, 5): 2
            },
            "tabla A-3": {
                (0, 0): 0, (1, 2): 5,  (3, 3): 4,  (4, 4): 2,  (5, 5): 1
            },
            "tabla A-4": {
                (0, 0): 0, (1, 2): 5,  (3, 3): 4,  (4, 4): 3,  (5, 5): 1
            },
            "tabla A-5": {
                (0, 0): 0, (1, 2): 5,  (3, 3): 4,  (4, 4): 2,  (5, 5): 1
            },
            "tabla A-6": {
                (0, 0): 0, (1, 3): 5,  (4, 4): 4,  (5, 5): 3
            },    
            "tabla A-7": {
                (0, 0): 0, (1, 2): 5,  (3, 3): 4,  (4, 4): 3,  (5, 5): 2
            },          
            "tabla A-8": {
                (0, 0): 0, (1, 2): 5,  (3, 3): 4,  (4, 5): 3 
            },
            "tabla A-9": {
                (0, 0): 0, (1, 2): 5,  (3, 3): 4,  (4, 4): 3, (5, 5): 2 
            },
            "tabla A-10": {
                (0, 0): 0, (1, 2): 5,  (3, 3): 4,  (4, 4): 3,  (5, 5): 2 
            },
            "tabla A-11": {
                (0, 0): 0, (1, 3): 5, (4, 5): 3 
            }                                                                      
        }  
        self.points_essays_third_list = {
            "tabla A-3": {
                (0, 0): 0, (1, 3): 5,  (4, 4): 4,  (5, 5): 3
            },
            "tabla A-4": {
                (0, 0): 0, (1, 2): 5,  (3, 3): 3,  (4, 4): 2,  (5, 5): 1
            },
            "tabla A-5": {
                (0, 0): 0, (1, 2): 5,  (3, 3): 4,  (4, 4): 3,  (5, 5): 2
            },
            "tabla A-6": {
                (0, 0): 0, (1, 3): 5,  (4, 4): 4,  (5, 5): 2
            },    
            "tabla A-7": {
                (0, 0): 0, (1, 3): 5,  (4, 5): 3
            },           
            "tabla A-9": {
                (0, 0): 0, (1, 2): 5,  (3, 3): 4,  (4, 5): 3 
            },
            "tabla A-10": {
                (0, 0): 0, (1, 3): 5,  (4, 4): 4,  (5, 5): 3 
            },
            "tabla A-11": {
                (0, 0): 0, (1, 3): 5,  (4, 5): 4 
            }                                                                      
        }  

    def define_table(self):
        if self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"  

    def get_data(self):
        try:
            ordering = Ordering.objects.get(banfe_test_id = self.banfe_id)
            return {
                'essays_first_list': ordering.essays_first_list,
                'essays_second_list': ordering.essays_second_list,
                'essays_third_list': ordering.essays_third_list
            }

        except Ordering.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Ordering
        data_ordering = self.get_data()

        if data_ordering is not "DoesNotExist":
            
            encoded_essays_third_list = -1
            if data_ordering['essays_third_list'] is not None:
                print("ordering: ", data_ordering['essays_third_list'])
                encoded_essays_third_list = self.encode_essays_third_list(data_ordering['essays_third_list'])
                print("encode: ", encoded_essays_third_list)
            
            return {
                'encoded_essays_first_list': self.encode_essays_first_list(data_ordering['essays_first_list']),
                'encoded_essays_second_list': self.encode_essays_second_list(data_ordering['essays_second_list']),
                'encoded_essays_third_list': encoded_essays_third_list,
            }
        else:
            return "DoesNotEncoded"

    def encode_essays_first_list(self,essays_first_list):
        points = self.points_essays_first_list.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= essays_first_list <= rank[1]:
                    return coded_value
        return default_value                               

    def encode_essays_second_list(self,essays_second_list):
        points = self.points_essays_second_list.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= essays_second_list <= rank[1]:
                    return coded_value
        return default_value                              

    def encode_essays_third_list(self,essays_third_list):
        points = self.points_essays_third_list.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia


        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= essays_third_list <= rank[1]:
                    return coded_value
        return default_value                        

class Substraction_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship

        self.points_time_a = {
            "tabla A-2": {
                (1, 103): 5, (104, 118): 4, (119, 162): 3, (163, 206): 2, (207, math.inf): 1 
            },
            "tabla A-3": {
                (1, 66): 5, (67, 77): 4, (78, 111): 3, (112, 145): 2, (146, math.inf): 1 
            },
            "tabla A-4": {
                (1, 47): 5, (48, 53): 4, (54, 69): 3, (70, 85): 2, (86, math.inf): 1 
            },
            "tabla A-5": {
                (1, 44): 5, (45, 55): 4, (56, 86): 3, (87, 116): 2, (117, math.inf): 1 
            },
            "tabla A-6": {
                (1, 69): 5, (70, 87): 4, (88, 142): 3, (143, 197): 2, (198, math.inf): 1 
            },    
            "tabla A-7": {
                (1, 40): 5, (41, 48): 4, (49, 73): 3, (74, 97): 2, (98, math.inf): 1 
            },          
            "tabla A-8": {
                (1, 70): 5, (71, 86): 4, (87, 134): 3, (135, 183): 2, (184, math.inf): 1 
            },
            "tabla A-9": {
                (1, 45): 5, (46, 54): 4, (55, 81): 3, (82, 108): 2, (109, math.inf): 1
            },
            "tabla A-10": {
                (1, 44): 5, (45, 49): 4, (50, 63): 3, (64, 77): 2, (78, math.inf): 1
            },
            "tabla A-11": {
                (1, 44): 5, (45, 49): 4, (50, 63): 3, (64, 77): 2, (78, math.inf): 1
            }                                                                      
        }   
        self.points_time_b = {
            "tabla A-3": {
                (1, 138): 5, (139, 157): 4,  (158, 214): 3,  (215, 271): 2, (272, math.inf): 1 
            },
            "tabla A-4": {
                (1, 86): 5, (87, 97): 4,  (98, 129): 3,  (130, 161): 2, (162, math.inf): 1
            },
            "tabla A-5": {
                (1, 90): 5, (91, 104): 4,  (105, 145): 3,  (146, 187): 2, (188, math.inf): 1
            },
            "tabla A-6": {
                (1, 113): 5, (114, 139): 4,  (140, 214): 3,  (215, 290): 2, (291, math.inf): 1
            },    
            "tabla A-7": {
                (1, 86): 5, (87, 105): 4,  (106, 161): 3,  (162, 217): 2, (218, math.inf): 1
            },          
            "tabla A-8": {
                (1, 134): 5, (135, 163): 4,  (164, 247): 3, (248, math.inf): 2 
            },
            "tabla A-9": {
                (1, 95): 5, (96, 111): 4,  (112, 159): 3,  (160, 207): 2, (208, math.inf): 1
            },
            "tabla A-10": {
                (1, 109): 5, (110, 131): 4,  (132, 199): 3,  (200, 266): 2, (267, math.inf): 1
            },
            "tabla A-11": {
                (1, 99): 5, (100, 121): 4,  (122, 189): 3,  (190, 257): 2, (258, math.inf): 1
            }                                                                      
        }  

    def define_table(self):
        if self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"  

    def get_data(self):
        try:
            substraction = Substraction.objects.get(banfe_test_id = self.banfe_id)
            
            if substraction.successes_b is None and substraction.time_b is None:
                successes_b = -1
                time_b = -1
            else:
                successes_b = substraction.successes_b
                time_b = substraction.time_b               

            return {
                'successes_a': substraction.successes_a,
                'time_a': substraction.time_a,
                'successes_b': successes_b,
                'time_b': time_b
            }

        except Substraction.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Substraction
        data_substraction = self.get_data()
        encoded_time_b = -1

        print("substraction es: ", data_substraction)

        if data_substraction is not "DoesNotExist":
            if data_substraction['time_b'] != -1:
                encoded_time_b = self.encode_time_b(data_substraction['time_b'])
        
            return {
                'encoded_time_a': self.encode_time_a(data_substraction['time_a']),
                'encoded_time_b': encoded_time_b            
            }
        else:
            return "DoesNotEncoded"

    def encode_time_a(self,time_a):
        points = self.points_time_a.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= time_a <= rank[1]:
                    return coded_value
        return default_value                   

    def encode_time_b(self,time_b):
        points = self.points_time_b.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= time_b <= rank[1]:
                    return coded_value
        return default_value                   

class Addition_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship

        self.points_time = {
            "tabla A-2": {
                (1, 96): 5, (97, 108): 4, (109, 146): 3, (147, 183): 2, (184, math.inf): 1 
            },
            "tabla A-3": {
                (1, 71): 5, (72, 80): 4, (81, 106): 3, (107, 132): 2, (133, math.inf): 1 
            },
            "tabla A-4": {
                (1, 56): 5, (57, 64): 4, (65, 89): 3, (90, 114): 2, (115, math.inf): 1 
            },
            "tabla A-5": {
                (1, 43): 5, (44, 46): 4, (47, 57): 3, (58, 68): 2, (69, math.inf): 1 
            },
            "tabla A-6": {
                (1, 73): 5, (74, 89): 4, (90, 136): 3, (137, 183): 2, (184, math.inf): 1 
            },    
            "tabla A-7": {
                (1, 45): 5, (46, 54): 4, (55, 81): 3, (82, 107): 2, (108, math.inf): 1 
            },          
            "tabla A-8": {
                (1, 67): 5, (68, 77): 4, (78, 107): 3, (108, 137): 2, (138, math.inf): 1 
            },
            "tabla A-9": {
                (1, 47): 5, (48, 52): 4, (53, 66): 3, (67, 80): 2, (81, math.inf): 1
            },
            "tabla A-10": {
                (1, 58): 5, (59, 64): 4, (65, 82): 3, (83, 100): 2, (101, math.inf): 1
            },
            "tabla A-11": {
                (1, 58): 5, (59, 64): 4, (65, 82): 3, (83, 100): 2, (101, math.inf): 1
            }                                                                      
        }   

    def define_table(self):
        if self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"  

    def get_data(self):
        try:
            addition = Addition.objects.get(banfe_test_id = self.banfe_id)
            return {
                'successes': addition.successes,
                'time': addition.time
            }

        except Addition.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Addition
        data_addition = self.get_data()

        if data_addition is not "DoesNotExist":
            return {
                'encoded_time': self.encode_time(data_addition['time']),      
            }
        else:
            return "DoesNotEncoded"

    def encode_time(self,time):
        points = self.points_time.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= time <= rank[1]:
                    return coded_value
        return default_value       

class Card_Sorting_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship
        
        self.points_perserverations = {
            "tabla A-1": {
                (0, 9): 5, (10, 10): 4, (11, 15): 3, (16, 20): 2, (21, math.inf): 1
            },
            "tabla A-2": {
                (0, 7): 5, (8, 9): 4, (10, 13): 3, (14, 17): 2, (18, math.inf): 1 
            },
            "tabla A-3": {
                (0, 5): 5, (6, 7): 4, (8, 11): 3, (12, 16): 2, (17, math.inf): 1 
            },
            "tabla A-4": {
                (0, 3): 5, (4, 4): 4, (5, 6): 3, (7, 8): 2, (9, math.inf): 1 
            },
            "tabla A-5": {
                (0, 3): 5, (4, 4): 4, (5, 6): 3, (7, 8): 2, (9, math.inf): 1 
            },
            "tabla A-6": {
                (0, 7): 5, (8, 9): 4, (10, 14): 3, (15, 20): 2, (21, math.inf): 1 
            },    
            "tabla A-7": {
                (0, 3): 5, (4, 5): 4, (6, 9): 3, (10, 14): 2, (15, math.inf): 1 
            },          
            "tabla A-8": {
                (0, 7): 5, (8, 9): 4, (10, 15): 3, (16, 21): 2, (22, math.inf): 1 
            },
            "tabla A-9": {
                (0, 6): 5, (7, 8): 4, (9, 13): 3, (14, 19): 2, (20, math.inf): 1
            },
            "tabla A-10": {
                (0, 10): 5, (11, 12): 4, (13, 20): 3, (21, 28): 2, (29, math.inf): 1
            },
            "tabla A-11": {
                (0, 7): 5, (8, 9): 4, (10, 16): 3, (17, 23): 2, (24, math.inf): 1
            }                                                                      
        }    
        self.points_deferred_perseverations = {
            "tabla A-1": {
                (0, 8): 5, (9, 9): 4, (10, 12): 3, (13, 16): 2, (17, math.inf): 1
            },
            "tabla A-2": {
                (0, 5): 5, (6, 6): 4, (7, 8): 3, (9, 11): 2, (12, math.inf): 1 
            },
            "tabla A-3": {
                (0, 6): 5, (7, 7): 4, (8, 11): 3, (12, 14): 2, (15, math.inf): 1 
            },
            "tabla A-4": {
                (0, 5): 5, (6, 6): 4, (7, 9): 3, (10, 13): 2, (14, math.inf): 1 
            },
            "tabla A-5": {
                (0, 5): 5, (6, 6): 4, (7, 9): 3, (10, 12): 2, (13, math.inf): 1 
            },
            "tabla A-6": {
                (0, 6): 5, (7, 8): 4, (9, 11): 3, (12, 15): 2, (16, math.inf): 1 
            },    
            "tabla A-7": {
                (0, 3): 5, (4, 4): 4, (5, 7): 3, (8, 11): 2, (12, math.inf): 1 
            },          
            "tabla A-8": {
                (0, 6): 5, (7, 8): 4, (9, 12): 3, (13, 16): 2, (17, math.inf): 1 
            },
            "tabla A-9": {
                (0, 5): 5, (6, 6): 4, (7, 11): 3, (12, 16): 2, (17, math.inf): 1
            },
            "tabla A-10": {
                (0, 6): 5, (7, 8): 4, (9, 14): 3, (15, 21): 2, (22, math.inf): 1
            },
            "tabla A-11": {
                (0, 6): 5, (7, 7): 4, (8, 12): 3, (13, 16): 2, (17, math.inf): 1
            }                                                                      
        }  
        self.points_maintenance_error = {
            "tabla A-1": {
                (0, 3): 5, (4, 4): 4, (5, 6): 3, (7, 9): 2, (10, math.inf): 1
            },
            "tabla A-2": {
                (0, 4): 5, (5, 6): 4, (7, 9): 3, (10, 12): 2, (13, math.inf): 1 
            },
            "tabla A-3": {
                (0, 2): 5, (3, 4): 4, (5, 7): 3, (8, 11): 2, (12, math.inf): 1 
            },
            "tabla A-4": {
                (0, 1): 5, (2, 2): 4, (3, 3): 3, (4, 5): 2, (6, math.inf): 1 
            },
            "tabla A-5": {
                (0, 1): 5, (2, 2): 4, (3, 3): 3, (4, 5): 2, (6, math.inf): 1 
            },
            "tabla A-6": {
                (0, 0): 5, (1, 1): 4, (2, 2): 3, (3, 3): 2, (4, math.inf): 1 
            },    
            "tabla A-7": {
                (0, 0): 3, (1, 1): 2, (2, math.inf): 1 
            },          
            "tabla A-8": {
                (0, 0): 5, (1, 1): 4, (2, 2): 2, (3, math.inf): 1 
            },
            "tabla A-9": {
                (0, 0): 5, (1, 1): 4, (2, 2): 2, (3, math.inf): 1
            },
            "tabla A-10": {
                (0, 0): 5, (1, 1): 3, (2, 2): 2, (3, math.inf): 1
            },
            "tabla A-11": {
                (0, 0): 5, (1, 1): 4, (2, 2): 3, (3, 4): 2, (5, math.inf): 1
            }                                                                      
        }  
        self.points_time = {
            "tabla A-1": {
                (1, 424): 5, (425, 464): 4, (465, 582): 3, (583, 600): 2
            },
            "tabla A-2": {
                (1, 358): 5, (359, 391): 4, (392, 490): 3, (491, 588): 2, (589, math.inf): 1 
            },
            "tabla A-3": {
                (1, 392): 5, (393, 434): 4, (435, 560): 3, (561, 687): 2, (688, math.inf): 1 
            },
            "tabla A-4": {
                (1, 341): 5, (342, 379): 4, (380, 493): 3, (494, 606): 2, (607, math.inf): 1 
            },
            "tabla A-5": {
                (1, 270): 5, (271, 296): 4, (297, 375): 3, (376, 453): 2, (454, math.inf): 1 
            },
            "tabla A-6": {
                (1, 474): 5, (475, 513): 4, (514, 636): 3, (637, 759): 2, (760, math.inf): 1 
            },    
            "tabla A-7": {
                (1, 336): 5, (337, 371): 4, (372, 473): 3, (474, 546): 2, (547, math.inf): 1 
            },          
            "tabla A-8": {
                (1, 416): 5, (417, 470): 4, (471, 632): 3, (633, 794): 2, (795, math.inf): 1 
            },
            "tabla A-9": {
                (1, 367): 5, (368, 406): 4, (407, 520): 3, (521, 600): 2
            },
            "tabla A-10": {
                (1, 309): 5, (310, 331): 4, (332, 400): 3, (401, 468): 2, (469, math.inf): 1
            },
            "tabla A-11": {
                (1, 391): 5, (392, 439): 4, (440, 585): 3, (586, 731): 2, (732, math.inf): 1
            }                                                                      
        }   

    def define_table(self):
        if self.age > 5 and self.age < 8:
            return "tabla A-1"
        elif self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"  
        
    def get_data(self):
        try:
            card_sorting = Card_Sorting.objects.get(banfe_test_id = self.banfe_id)
            return {
                'successes': card_sorting.successes,
                'perseverations': card_sorting.perseverations,
                'deferred_perseverations': card_sorting.deferred_perseverations,
                'maintenance_error': card_sorting.maintenance_error,
                'time': card_sorting.time
            }

        except Card_Sorting.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Card Sorting
        data_card_sorting = self.get_data()

        if data_card_sorting is not "DoesNotExist":
            return {
                'encoded_perseverations': self.encode_perseverations(data_card_sorting['perseverations']),     
                'encoded_deferred_perseverations': self.encode_deferred_perseverations(data_card_sorting['deferred_perseverations']),     
                'encoded_maintenance_error': self.encode_maintenance_error(data_card_sorting['maintenance_error']),     
                'encoded_time': self.encode_time(data_card_sorting['time']),      
            }
        else: 
            return "DoesNotEncoded"

    def encode_perseverations(self,perseverations):
        points = self.points_perserverations.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= perseverations <= rank[1]:
                    return coded_value
        return default_value                        

    def encode_deferred_perseverations(self,deferred_perseverations):
        points = self.points_deferred_perseverations.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= deferred_perseverations <= rank[1]:
                    return coded_value
        return default_value                

    def encode_maintenance_error(self,maintenance_error):
        points = self.points_maintenance_error.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= maintenance_error <= rank[1]:
                    return coded_value
        return default_value                        

    def encode_time(self,time):
        points = self.points_time.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= time <= rank[1]:
                    return coded_value
        return default_value                        

class Semantic_Classification_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship 
        
        self.points_abstract_categories = {
            "tabla A-2": {
                (0, 0): 2, (1, 1): 3, (2, 2): 4, (3, math.inf): 5
            },
            "tabla A-3": {
                (0, 1): 2, (2, 2): 3, (3, 3): 4, (4, math.inf): 5
            },
            "tabla A-4": {
                (0, 0): 1, (1, 2): 2, (3, 3): 3, (4, 4): 4, (5, math.inf): 5 
            },
            "tabla A-5": {
                (0, 0): 1, (1, 2): 2, (3, 4): 3, (5, 5): 4, (6, math.inf): 5 
            },
            "tabla A-6": {
                (0, 0): 2, (1, 2): 3, (3, 3): 4, (4, math.inf): 5
            },    
            "tabla A-7": {
                (0, 0): 1, (1, 2): 2, (3, 5): 3, (6, 6): 4, (7, math.inf): 5  
            },          
            "tabla A-8": {
                (0, 2): 3, (3, 3): 4, (4, math.inf): 5
            },
            "tabla A-9": {
                (0, 2): 2, (3, 4): 3, (5, 5): 4, (6, math.inf): 5
            },
            "tabla A-10": {
                (0, 2): 2, (3, 4): 3, (5, 5): 4, (6, math.inf): 5
            },
            "tabla A-11": {
                (0, 0): 0, (1, 1): 2, (2, 3): 3, (4, 4): 4, (5, math.inf): 1
            }                                                                      
        }  
        self.points_total_categories = {
            "tabla A-1": {
                (0, 1): 1, (2, 4): 2, (5, 6): 3, (7, 7): 4, (8, math.inf): 5
            },
            "tabla A-2": {
                (0, 3): 1, (4, 4): 2, (5, 6): 3, (7, 7): 4, (8, math.inf): 5 
            },
            "tabla A-3": {
                (0, 3): 1, (4, 4): 2, (5, 6): 3, (7, 7): 4, (8, math.inf): 5  
            },
            "tabla A-4": {
                (0, 2): 1, (3, 4): 2, (5, 6): 3, (7, 7): 4, (8, math.inf): 5   
            },
            "tabla A-5": {
                (0, 3): 1, (4, 5): 2, (6, 6): 3, (7, 7): 4, (8, math.inf): 5  
            },
            "tabla A-6": {
                (0, 2): 1, (3, 4): 2, (5, 6): 3, (7, 7): 4, (8, math.inf): 5 
            },    
            "tabla A-7": {
                (0, 4): 1, (5, 5): 2, (6, 8): 3, (9, 9): 4, (10, math.inf): 5  
            },          
            "tabla A-8": {
                (0, 2): 1, (3, 4): 2, (5, 6): 3, (7, 7): 4, (8, math.inf): 5  
            },
            "tabla A-9": {
                (0, 2): 1, (3, 5): 2, (6, 8): 3, (9, 9): 4, (10, math.inf): 5  
            },
            "tabla A-10": {
                (0, 0): 1, (1, 3): 2, (4, 6): 3, (7, 7): 4, (8, math.inf): 5  
            },
            "tabla A-11": {
                (0, 0): 1, (1, 2): 2, (3, 4): 3, (5, math.inf): 5  
            }                                                                      
        }  
        self.points_total_average = {
            "tabla A-1": {
                (0, 1): 2, (2, 3): 3, (4, math.inf): 5
            },
            "tabla A-2": {
                (0, 1): 1, (2, 2): 2, (3, 3): 3, (4, 4): 4, (5, math.inf): 5 
            },
            "tabla A-3": {
                (0, 2): 1, (3, 3): 2, (4, 5): 3, (6, math.inf): 5 
            },
            "tabla A-4": {
                (0, 2): 1, (3, 4): 2, (5, 5): 3, (6, 6): 4, (7, math.inf): 5 
            },
            "tabla A-5": {
                (0, 2): 1, (3, 4): 2, (5, 5): 3, (6, 6): 4, (7, math.inf): 5 
            },
            "tabla A-6": {
                (0, 1): 1, (2, 3): 2, (4, 5): 3, (6, 6): 4, (7, math.inf): 5  
            },    
            "tabla A-7": {
                (0, 0): 1, (1, 3): 2, (4, 5): 3, (6, 6): 4, (7, math.inf): 5  
            },          
            "tabla A-8": {
                (0, 2): 1, (3, 4): 2, (5, 5): 3, (6, 6): 4, (7, math.inf): 5
            },
            "tabla A-9": {
                (0, 2): 1, (3, 4): 2, (5, 5): 3, (6, 6): 4, (7, math.inf): 5
            },
            "tabla A-10": {
                (0, 1): 1, (2, 3): 2, (4, 5): 3, (6, 6): 4, (7, math.inf): 5
            },
            "tabla A-11": {
                (0, 2): 1, (3, 4): 2, (5, 5): 3, (6, 6): 4, (7, math.inf): 5
            }                                                                      
        }  
        self.points_total_score = {
            "tabla A-1": {
                (0, 0): 1, (1, 4): 2, (5, 9): 3, (10, 10): 4, (11, math.inf): 5
            },
            "tabla A-2": {
                (0, 4): 1, (5, 8): 2, (9, 12): 3, (13, 13): 4, (14, math.inf): 5 
            },
            "tabla A-3": {
                (0, 7): 1, (8, 11): 2, (12, 15): 3, (16, 16): 4, (17, math.inf): 5  
            },
            "tabla A-4": {
                (0, 6): 1, (7, 11): 2, (12, 16): 3, (17, 18): 4, (19, math.inf): 5  
            },
            "tabla A-5": {
                (0, 8): 1, (9, 13): 2, (14, 18): 3, (19, 19): 4, (20, math.inf): 5   
            },
            "tabla A-6": {
                (0, 3): 1, (4, 9): 2, (10, 15): 3, (16, 17): 4, (18, math.inf): 5    
            },    
            "tabla A-7": {
                (0, 10): 1, (11, 16): 2, (17, 22): 3, (23, 24): 4, (25, math.inf): 5     
            },          
            "tabla A-8": {
                (0, 2): 1, (3, 7): 2, (8, 13): 3, (14, 15): 4, (16, math.inf): 5     
            },
            "tabla A-9": {
                (0, 9): 1, (10, 15): 2, (16, 21): 3, (22, 23): 4, (24, math.inf): 5  
            },
            "tabla A-10": {
                (0, 4): 1, (5, 11): 2, (12, 19): 3, (20, 21): 4, (22, math.inf): 5  
            },
            "tabla A-11": {
                (0, 4): 1, (5, 11): 2, (12, 19): 3, (20, 21): 4, (22, math.inf): 5  
            }                                                                      
        }   
            
    def define_table(self):
        if self.age > 5 and self.age < 8:
            return "tabla A-1"
        elif self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"  
        
    def get_data(self):
        try:
            semantic_classification = Semantic_Classification.objects.get(banfe_test_id = self.banfe_id)
            return {
                'abstract_categories': semantic_classification.abstract_categories,
                'total_categories': semantic_classification.total_categories,
                'total_average': semantic_classification.total_average,
                'total_score': semantic_classification.total_score
            }

        except Semantic_Classification.DoesNotExist:           
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Card Sorting
        data_semantic_classification = self.get_data()
        
        if data_semantic_classification is not "DoesNotExist":
            return {
                'encoded_abstract_categories': self.encode_abstract_categories(data_semantic_classification['abstract_categories']),     
                'encoded_total_categories': self.encode_total_categories(data_semantic_classification['total_categories']),     
                'encoded_total_average': self.encode_total_average(data_semantic_classification['total_average']),     
                'encoded_total_score': self.encode_total_score(data_semantic_classification['total_score']),      
            }
        else:
            return "DoesNotEncoded"

    def encode_abstract_categories(self,abstract_categories):
        points = self.points_abstract_categories.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= abstract_categories <= rank[1]:
                    return coded_value
        return default_value               
    
    def encode_total_categories(self,total_categories):
        points = self.points_total_categories.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= total_categories <= rank[1]:
                    return coded_value
        return default_value                       

    def encode_total_average(self,total_average):
        points = self.points_total_average.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= total_average <= rank[1]:
                    return coded_value
        return default_value               

    def encode_total_score(self,total_score):
        points = self.points_total_score.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= total_score <= rank[1]:
                    return coded_value
        return default_value                       

class Stroop_A_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship
        
        self.point_stroop_errors = {
            "tabla A-2": {
                (0, 2): 5, (3, 3): 4, (4, 5): 3, (6, 7): 2, (8, math.inf): 1
            },
            "tabla A-3": {
                (0, 1): 5, (2, 2): 4, (3, 4): 3, (5, 5): 2, (6, math.inf): 1   
            },
            "tabla A-4": {
                (0, 0): 5, (1, 1): 3, (2, 2): 2, (3, math.inf): 1     
            },
            "tabla A-5": {
                (0, 0): 5, (1, 1): 3, (2, 2): 2, (3, math.inf): 1        
            },
            "tabla A-6": {
                (0, 1): 5, (2, 2): 4, (3, 5): 3, (6, 8): 2, (9, math.inf): 1   
            },    
            "tabla A-7": {
                (0, 0): 5, (1, 1): 3, (2, 2): 2, (3, math.inf): 1  
            },          
            "tabla A-8": {
                (0, 1): 5, (2, 2): 4, (3, 4): 3, (5, 6): 2, (7 , math.inf): 1  
            },
            "tabla A-9": {
                (0, 0): 5, (1, 1): 4, (2, 2): 2, (3, math.inf): 1    
            },
            "tabla A-10": {
                (0, 2): 5, (3, 3): 4, (4, 6): 3, (7, 9): 2, (10 , math.inf): 1  
            },
            "tabla A-11": {
                (0, 2): 5, (3, 3): 4, (4, 5): 3, (6, 7): 2, (8 , math.inf): 1  
            }                                                                      
        }  
        self.points_time = {
            "tabla A-2": {
                (1, 147): 5, (148, 159): 4, (160, 197): 3, (198, 235): 2, (236, math.inf): 1 
            },
            "tabla A-3": {
                (1, 112): 5, (113, 123): 4, (124, 156): 3, (157, 189): 2, (190, math.inf): 1
            },
            "tabla A-4": {
                (1, 93): 5, (94, 100): 4, (101, 121): 3, (122, 142): 2, (143, math.inf): 1
            },
            "tabla A-5": {
                (1, 80): 5, (81, 85): 4, (86, 99): 3, (100, 113): 2, (114, math.inf): 1
            },
            "tabla A-6": {
                (1, 90): 5, (91, 101): 4, (102, 137): 3, (138, 173): 2, (174, math.inf): 1
            },    
            "tabla A-7": {
                (1, 78): 5, (79, 84): 4, (85, 103): 3, (104, 122): 2, (123, math.inf): 1
            },          
            "tabla A-8": {
                (1, 92): 5, (93, 101): 4, (102, 129): 3, (130, 158): 2, (159, math.inf): 1
            },
            "tabla A-9": {
                (1, 86): 5, (87, 95): 4, (96, 124): 3, (125, 152): 2, (153, math.inf): 1
            },
            "tabla A-10": {
                (1, 97): 5, (98, 107): 4, (108, 135): 3, (136, 164): 2, (165, math.inf): 1
            },
            "tabla A-11": {
                (1, 112): 5, (113, 129): 4, (130, 180): 3, (181, 230): 2, (231, math.inf): 1
            }                                                                      
        }  

    def define_table(self):
        if self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"  
        
    def get_data(self):
        try:
            stroop_a = Stroop_A.objects.get(banfe_test_id = self.banfe_id)
            return {
                'successes': stroop_a.successes,
                'stroop_errors': stroop_a.stroop_errors,
                'time': stroop_a.time
            }

        except Stroop_A.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Stroop_A
        data_stroop_a = self.get_data()
        print("stroop_a: ", data_stroop_a)

        if data_stroop_a is not "DoesNotExist":
            return {
                'encoded_stroop_errors': self.encoded_stroop_errors(data_stroop_a['stroop_errors']),     
                'encoded_time': self.encoded_time(data_stroop_a['time']),          
            }
        else:
            return "DoesNotEncoded"

    
    def encoded_stroop_errors(self,stroop_errors):
        print("stroop_a ", stroop_errors)
        points = self.point_stroop_errors.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= stroop_errors <= rank[1]:
                    return coded_value
        return default_value       

    def encoded_time(self,time):
        points = self.points_time.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= time <= rank[1]:
                    return coded_value
        return default_value       

class Verbal_Fluency_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship
        
        self.points_successes = {
            "tabla A-1": {
                (0, 1): 1, (2, 4): 2, (5, 7): 3, (8, 9): 4, (10, math.inf): 5
            },
            "tabla A-2": {
                (0, 5): 1, (6, 8): 2, (9, 12): 3, (13, 13): 4, (14, math.inf): 5
            },
            "tabla A-3": {
                (0, 5): 1, (6, 9): 2, (10, 13): 3, (14, 14): 4, (15, math.inf): 5
            },
            "tabla A-4": {
                (0, 8): 1, (9, 12): 2, (13, 16): 3, (17, 18): 4, (19, math.inf): 5
            },
            "tabla A-5": {
                (0, 7): 1, (8, 12): 2, (13, 17): 3, (18, 18): 4, (19, math.inf): 5
            },
            "tabla A-6": {
                (0, 3): 1, (4, 8): 2, (9, 12): 3, (13, 14): 4, (15, math.inf): 5
            },    
            "tabla A-7": {
                (0, 8): 1, (9, 15): 2, (16, 22): 3, (23, 24): 4, (25, math.inf): 5
            },          
            "tabla A-8": {
                (0, 2): 1, (3, 7): 2, (8, 13): 3, (14, 15): 4, (16, math.inf): 5
            },
            "tabla A-9": {
                (0, 6): 5, (7, 12): 4, (13, 18): 3, (19, 20): 2, (21, math.inf): 1    
            },
            "tabla A-10": {
                (0, 9): 5, (10, 15): 4, (16, 20): 3, (21, 21): 2, (22 , math.inf): 1  
            },
            "tabla A-11": {
                (0, 7): 5, (8, 13): 4, (14, 18): 3, (19, 20): 2, (21 , math.inf): 1 
            }                                                                      
        }  
        self.points_perseverations = {
            "tabla A-1": {
                (0, 0): 5, (1, 1): 4, (2, 2): 3, (3, 3): 2, (4, math.inf): 1
            },            
            "tabla A-2": {
                (0, 0): 4, (1, math.inf): 1 
            },
            "tabla A-3": {
                (0, 0): 5, (1, math.inf): 1 
            },
            "tabla A-4": {
                (0, 0): 5, (1, 1): 3, (2, 2): 2, (3, math.inf): 1
            },
            "tabla A-5": {
                (0, 0): 5, (1, 1): 2, (2, math.inf): 1
            },
            "tabla A-6": {
                (0, 0): 5, (1, 1): 4, (2, 2): 3, (3, 3): 2, (4, math.inf): 1
            },    
            "tabla A-7": {
                (0, 0): 5, (1, 2): 3, (3, 3): 2, (4, math.inf): 1
            },          
            "tabla A-8": {
                (0, 0): 5, (1, 1): 4, (2, 2): 3, (3, 3): 2, (4, math.inf): 1
            },
            "tabla A-9": {
                (0, 0): 5, (1, 1): 4, (2, 3): 3, (4, 4): 2, (5, math.inf): 1
            },
            "tabla A-10": {
                (0, 2): 5, (3, 4): 3, (5, 6): 2, (7, math.inf): 1
            },
            "tabla A-11": {
                (0, 1): 5, (2, 2): 4, (3, 3): 3, (4, 5): 2, (6, math.inf): 1
            }                                                                      
        }  

    def define_table(self):
        if self.age > 5 and self.age < 8:
            return "tabla A-1"
        elif self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"  
     
    def get_data(self):
        try:
            verbal_fluency = Verbal_Fluency.objects.get(banfe_test_id = self.banfe_id)
            return {
                'successes': verbal_fluency.successes,
                'perseverations': verbal_fluency.perseverations
            }

        except Verbal_Fluency.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Card Sorting
        data_verbal_fluency = self.get_data()

        if data_verbal_fluency is not "DoesNotExist":
            return {
                'encoded_successes': self.encoded_successes(data_verbal_fluency['successes']),     
                'encoded_perseverations': self.encoded_perseverations(data_verbal_fluency['perseverations']),          
            }
        else:
            return "DoesNotEncoded"

    def encoded_successes(self,successes):
        points = self.points_successes.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= successes <= rank[1]:
                    return coded_value
        return default_value         

    def encoded_perseverations(self,perseverations):
        points = self.points_perseverations.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= perseverations <= rank[1]:
                    return coded_value
        return default_value         

class Cards_Game_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship
        
        self.points_percentage_risk_cards = {
            "tabla A-1": {
                (0, 34): 5, (35, 37): 4, (38, 47): 3, (48, 57): 2, (58, math.inf): 1
            },
            "tabla A-2": {
                (0, 36): 5, (37, 39): 4, (40, 45): 3, (46, 52): 2, (53, math.inf): 1
            },
            "tabla A-3": {
                (0, 36): 5, (37, 38): 4, (39, 46): 3, (47, 54): 2, (55, math.inf): 1
            },
            "tabla A-4": {
                (0, 33): 5, (34, 37): 4, (38, 46): 3, (47, 55): 2, (56, math.inf): 1
            },
            "tabla A-5": {
                (0, 30): 5, (31, 33): 4, (34, 44): 3, (45, 54): 2, (55, math.inf): 1
            },
            "tabla A-6": {
                (0, 31): 5, (32, 36): 4, (37, 49): 3, (50, 63): 2, (64, math.inf): 1
            },    
            "tabla A-7": {
                (0, 0): 0, (1, 31): 5, (32, 35): 4, (36, 45): 3, (46, 55): 2, (56, math.inf): 1
            },          
            "tabla A-8": {
                (0, 32): 5, (33, 36): 4, (37, 47): 3, (48, 59): 2, (60, math.inf): 1
            },
            "tabla A-9": {
                (0, 33): 5, (34, 37): 4, (38, 48): 3, (49, 59): 2, (60, math.inf): 1  
            },
            "tabla A-10": {
                (0, 27): 5, (28, 33): 4, (34, 48): 3, (49, 64): 2, (65, math.inf): 1  
            },
            "tabla A-11": {
                (0, 0): 0, (1, 34): 5, (35, 38): 4, (39, 51): 3, (52, 64): 2, (65, math.inf): 1
            }                                                                      
        }  
        self.points_total_score = {
            "tabla A-1": {
                (0, 0): 1, (1, 9): 2, (10, 18): 3, (19, 21): 4, (22, math.inf): 5
            },            
            "tabla A-2": {
                (0, 8): 1, (9, 14): 2, (15, 20): 3, (21, 23): 4, (24, math.inf): 5 
            },
            "tabla A-3": {
                (0, 8): 1, (9, 15): 2, (16, 23): 3, (24, 25): 4, (26, math.inf): 5 
            },
            "tabla A-4": {
                (0, 11): 1, (12, 18): 2, (19, 26): 3, (27, 28): 4, (29, math.inf): 5 
            },
            "tabla A-5": {
                (0, 10): 1, (11, 20): 2, (21, 29): 3, (30, 32): 4, (33, math.inf): 5
            },
            "tabla A-6": {
                (0, 8): 2, (9, 24): 3, (25, 29): 4, (30, math.inf): 5
            },    
            "tabla A-7": {
                (0, 4): 1, (5, 18): 2, (19, 31): 3, (32, 36): 4, (37, math.inf): 5
            },          
            "tabla A-8": {
                (0, 8): 2, (9, 24): 3, (25, 29): 4, (30, math.inf): 5
            },
            "tabla A-9": {
                (0, 2): 1, (3, 15): 2, (16, 29): 3, (30, 33): 4, (34, math.inf): 5
            },
            "tabla A-10": {
                (0, 2): 1, (2, 16): 2, (17, 34): 3, (35, 40): 4, (41, math.inf): 5
            },
            "tabla A-11": {
                (0, 0): 0, (1, 7): 2, (8, 21): 3, (22, 25): 4, (26, 55): 5
            }                                                                      
        }  


    def define_table(self):
        if self.age > 5 and self.age < 8:
            return "tabla A-1"
        elif self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"  

    def get_data(self):
        try:
            cards_game = Cards_Game.objects.get(banfe_test_id = self.banfe_id)
            return {
                'percentage_risk_cards': cards_game.percentage_risk_cards,
                'total_score': cards_game.total_score,
            }

        except Cards_Game.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Card Sorting
        data_cards_game = self.get_data()

        if data_cards_game is not "DoesNotExist":
            return {
                'encoded_percentage_risk_cards': self.encoded_percentage_risk_cards(data_cards_game['percentage_risk_cards']),     
                'encoded_total_score': self.encoded_total_score(data_cards_game['total_score']),          
            }
        else:
            return "DoesNotEncoded"
    
    def encoded_percentage_risk_cards(self,percentage_risk_cards):
        points = self.points_percentage_risk_cards.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= percentage_risk_cards <= rank[1]:
                    return coded_value
        return default_value         

    def encoded_total_score(self,total_score):
        print("TABLA CARTAS: ",self.define_table())
        points = self.points_total_score.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= total_score <= rank[1]:
                    return coded_value
        return default_value         

class Sayings_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship
        
        self.points_time = {
            "tabla A-3": {
                (0, 0): 0, (1, 113): 5, (114, 130): 4, (131, 180): 3, (181, 230): 2, (231, math.inf): 1
            },
            "tabla A-4": {
                (0, 0): 0, (1, 110): 5, (111, 124): 4, (125, 166): 3, (167, 208): 2, (209, math.inf): 1
            },
            "tabla A-5": {
                (0, 0): 0, (1, 78): 5, (79, 88): 4, (89, 118): 3, (119, 148): 2, (149, math.inf): 1
            },
            "tabla A-6": {
                (0, 0): 0, (1, 101): 5, (102, 115): 4, (116, 154): 3, (155, 193): 2, (194, math.inf): 1
            },    
            "tabla A-7": {
                (0, 0): 0, (1, 84): 5, (85, 95): 4, (96, 128): 3, (129, 162): 2, (163, math.inf): 1
            },          
            "tabla A-8": {
                (0, 0): 0, (1, 128): 5, (129, 146): 4, (147, 201): 3, (202, 256): 2, (257, math.inf): 1
            },
            "tabla A-9": {
                (0, 0): 0, (1, 84): 5, (85, 95): 4, (96, 130): 3, (131, 165): 2, (166, math.inf): 1
            },
            "tabla A-10": {
                (0, 0): 0, (1, 73): 5, (74, 94): 4, (95, 157): 3, (158, 220): 2, (221, math.inf): 1
            },
            "tabla A-11": {
                (0, 0): 0, (1, 84): 5, (85, 100): 4, (101, 147): 3, (148, 195): 2, (196, math.inf): 1
            }                                                                      
        }  


    def define_table(self):
        if self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"  

    def get_data(self):
        try:
            sayings = Sayings.objects.get(banfe_test_id = self.banfe_id)
            return {
                'successes': sayings.successes,
                'time': sayings.time,
            }

        except Sayings.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Card Sorting
        data_sayings = self.get_data()

        if data_sayings is not "DoesNotExist":
            return {     
                'encoded_time': self.encoded_time(data_sayings['time']),          
            }   
        else:
            return "DoesNotEncoded"

    def encoded_time(self,time):
        points = self.points_time.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= time  <= rank[1]:
                    return coded_value
        return default_value         

class Towers_Hanoi_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship
        
        self.points_movements_first = {
            "tabla A-1": {
                (0, 6): 0, (7, 15): 5, (16, 17): 4, (18, 23): 3, (24, 29): 2, (30, math.inf): 1
            },            
            "tabla A-2": {
                (0, 6): 0, (7, 13): 5, (14, 15): 4, (16, 19): 3, (20, 23): 2, (24, math.inf): 1
            },
            "tabla A-3": {
                (0, 6): 0, (7, 12): 5, (13, 13): 4, (14, 17): 3, (18, 21): 2, (22, math.inf): 1
            },
            "tabla A-4": {
                (0, 6): 0, (7, 12): 5, (13, 13): 4, (14, 18): 3, (19, 22): 2, (23, math.inf): 1
            },
            "tabla A-5": {
                (0, 6): 0, (7, 9): 5, (10, 10): 4, (11, 14): 3, (15, 17): 2, (18, math.inf): 1
            },
            "tabla A-6": {
                (0, 6): 0, (7, 12): 5, (13, 14): 4, (15, 21): 3, (22, 28): 2, (29, math.inf): 1
            },    
            "tabla A-7": {
                (0, 6): 0, (7, 9): 5, (10, 11): 4, (12, 15): 3, (16, 19): 2, (20, math.inf): 1
            },          
            "tabla A-8": {
                (0, 6): 0, (7, 12): 5, (13, 14): 4, (15, 21): 3, (22, 27): 2, (28, math.inf): 1
            },
            "tabla A-9": {
                (0, 6): 0, (7, 10): 5, (11, 12): 4, (13, 16): 3, (17, 21): 2, (22, math.inf): 1
            },
            "tabla A-10": {
                (0, 6): 0, (7, 10): 5, (11, 11): 4, (12, 16): 3, (17, 20): 2, (21, math.inf): 1
            },
            "tabla A-11": {
                (0, 6): 0, (7, 9): 5, (10, 11): 4, (12, 16): 3, (17, 21): 2, (22, math.inf): 1
            }                                                                      
        }  
        self.points_time_first = {
            "tabla A-1": {
                (1, 130): 5, (131, 147): 4, (148, 200): 3, (201, 252): 2, (253, math.inf): 1
            },            
            "tabla A-2": {
                (1, 109): 5, (110, 128): 4, (129, 184): 3, (185, 241): 2, (242, math.inf): 1
            },            
            "tabla A-3": {
                (1, 80): 5, (81, 96): 4, (97, 143): 3, (144, 190): 2, (191, math.inf): 1
            },
            "tabla A-4": {
                (1, 55): 5, (56, 67): 4, (68, 103): 3, (104, 139): 2, (140, math.inf): 1
            },
            "tabla A-5": {
                (1, 29): 5, (30, 35): 4, (36, 53): 3, (54, 70): 2, (71, math.inf): 1
            },
            "tabla A-6": {
                (1, 73): 5, (74, 95): 4, (96, 164): 3, (165, 233): 2, (234, math.inf): 1
            },    
            "tabla A-7": {
                (1, 39): 5, (40, 51): 4, (52, 90): 3, (91, 128): 2, (129, math.inf): 1
            },          
            "tabla A-8": {
                (1, 69): 5, (70, 90): 4, (91, 152): 3, (153, 215): 2, (216, math.inf): 1
            },
            "tabla A-9": {
                (1, 49): 5, (50, 65): 4, (66, 112): 3, (113, 160): 2, (161, math.inf): 1
            },
            "tabla A-10": {
                (1, 64): 5, (65, 81): 4, (82, 130): 3, (131, 180): 2, (181, math.inf): 1
            },
            "tabla A-11": {
                (1, 45): 5, (46, 58): 4, (59, 97): 3, (98, 135): 2, (136, math.inf): 1
            }                                                                      
        }  
        self.points_movements_second = {
            "tabla A-3": {
                (0, 13): 0, (14, 27): 5, (28, 31): 4, (32, 43): 3, (44, 55): 2, (56, math.inf): 1
            },
            "tabla A-4": {
                (0, 13): 0, (14, 26): 5, (27, 29): 4, (30, 37): 3, (38, 46): 2, (47, math.inf): 1
            },
            "tabla A-5": {
                (0, 13): 0, (14, 27): 5, (28, 30): 4, (31, 40): 3, (41, 49): 2, (50, math.inf): 1
            },
            "tabla A-6": {
                (0, 13): 0, (14, 24): 5, (25, 27): 4, (28, 35): 3, (36, 42): 2, (43, math.inf): 1
            },    
            "tabla A-7": {
                (0, 13): 0, (14, 25): 5, (26, 28): 4, (29, 36): 3, (37, 44): 2, (45, math.inf): 1
            },          
            "tabla A-8": {
                (0, 13): 0, (14, 27): 5, (28, 32): 4, (33, 46): 3, (47, 60): 2, (61, math.inf): 1
            },
            "tabla A-9": {
                (0, 13): 0, (14, 27): 5, (28, 31): 4, (32, 43): 3, (44, 54): 2, (55, math.inf): 1
            },
            "tabla A-10": {
                (0, 13): 0, (14, 22): 5, (23, 24): 4, (25, 32): 3, (33, 40): 2, (41, math.inf): 1
            },
            "tabla A-11": {
                (0, 13): 0, (14, 20): 5, (21, 24): 4, (25, 35): 3, (36, 47): 2, (48, math.inf): 1
            }                                                                      
        }  
        self.points_time_second = {
            "tabla A-3": {
                (1, 120): 5, (121, 144): 4, (145, 216): 3, (217, 288): 2, (289, math.inf): 1
            },
            "tabla A-4": {
                (1, 84): 5, (85, 98): 4, (99, 143): 3, (144, 187): 2, (188, math.inf): 1
            },
            "tabla A-5": {
                (1, 104): 5, (105, 125): 4, (126, 186): 3, (187, 248): 2, (249, math.inf): 1
            },
            "tabla A-6": {
                (1, 98): 5, (99, 113): 4, (114, 160): 3, (161, 207): 2, (208, math.inf): 1
            },    
            "tabla A-7": {
                (1, 83): 5, (84, 102): 4, (103, 158): 3, (159, 214): 2, (215, math.inf): 1
            },          
            "tabla A-8": {
                (1, 118): 5, (119, 138): 4, (139, 200): 3, (201, 261): 2, (262, math.inf): 1
            },
            "tabla A-9": {
                (1, 82): 5, (83, 99): 4, (100, 150): 3, (151, 202): 2, (203, math.inf): 1
            },
            "tabla A-10": {
                (1, 122): 5, (123, 149): 4, (150, 231): 3, (232, 313): 2, (314, math.inf): 1
            },
            "tabla A-11": {
                (1, 98): 5, (99, 120): 4, (121, 187): 3, (188, 254): 2, (255, math.inf): 1
            }                                                                      
        }  

    def define_table(self):
        if self.age > 5 and self.age < 8:
            return "tabla A-1"
        elif self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"  
        
    def get_data(self):
        try:
            towers_hanoi = Towers_Hanoi.objects.get(banfe_test_id = self.banfe_id)

            if towers_hanoi.movements_second is None and towers_hanoi.time_second is None:
                movements_second = -1
                time_second = -1
                print("si fue none")
            else:
                movements_second = towers_hanoi.movements_second
                time_second = towers_hanoi.time_second
                print("no fue none")

            return {
                'movements_first': towers_hanoi.movements_first,
                'time_first': towers_hanoi.time_first,
                'movements_second': movements_second,
                'time_second': time_second
            }

        except Towers_Hanoi.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Card Sorting
        data_towers_hanoi = self.get_data()
        print("towers: ", data_towers_hanoi)

        if data_towers_hanoi is not "DoesNotExist":

            if int(data_towers_hanoi['movements_second']) != -1 and int(data_towers_hanoi['time_second']):
                encoded_movements_second = self.encoded_movements_second(data_towers_hanoi['movements_second'])
                encoded_time_second = self.encoded_time_second(data_towers_hanoi['time_second'])
            else:
                encoded_movements_second = -1
                encoded_time_second = -1

            return {     
                'encoded_movements_first': self.encoded_movements_first(data_towers_hanoi['movements_first']),
                'encoded_time_first': self.encoded_time_first(data_towers_hanoi['time_first']),
                'encoded_movements_second': encoded_movements_second,
                'encoded_time_second': encoded_time_second
            }
        else:
            return "DoesNotEncoded"
    
    def encoded_movements_first(self,movements_first):
        points = self.points_movements_first.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= movements_first <= rank[1]:
                    return coded_value
        return default_value         

    def encoded_time_first(self,time_first):
        points = self.points_time_first.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= time_first <= rank[1]:
                    return coded_value
        return default_value         

    def encoded_movements_second(self,movements_second):
        points = self.points_movements_second.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= movements_second <= rank[1]:
                    return coded_value
        return default_value         

    def encoded_time_second(self,time_second):
        points = self.points_time_second.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= time_second <= rank[1]:
                    return coded_value
        return default_value         

class Metamemory_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship

        self.points_positive_errors = {
            "tabla A-1": {
                (0, 4): 5, (5, 5): 4, (6, 8): 3, (9, 11): 2, (12, math.inf): 1
            },            
            "tabla A-2": {
                (0, 2): 5, (3, 3): 4, (4, 5): 3, (6, 7): 2, (8, math.inf): 1
            },
            "tabla A-3": {
                (0, 2): 5, (3, 3): 4, (4, 5): 3, (6, 8): 2, (9, math.inf): 1
            },
            "tabla A-4": {
                (0, 0): 5, (1, 2): 3, (3, 3): 2, (4, math.inf): 1
            },
            "tabla A-5": {
                (0, 1): 5, (2, 2): 4, (3, 3): 3, (4, 4): 2, (5, math.inf): 1
            },
            "tabla A-6": {
                (0, 1): 5, (2, 2): 4, (3, 3): 3, (4, 5): 2, (6, math.inf): 1
            },    
            "tabla A-7": {
                (0, 1): 5, (2, 3): 3, (4, 5): 2, (6, math.inf): 1
            },          
            "tabla A-8": {
                (0, 1): 5, (2, 2): 4, (3, 3): 3, (4, 5): 2, (6, math.inf): 1
            },
            "tabla A-9": {
                (0, 1): 5, (2, 2): 4, (3, 4): 3, (5, 6): 2, (7, math.inf): 1
            },
            "tabla A-10": {
                (0, 2): 5, (3, 3): 4, (4, 5): 3, (6, 7): 2, (8, math.inf): 1
            },
            "tabla A-11": {
                (0, 1): 5, (2, 2): 4, (3, 5): 3, (6, 8): 2, (9, math.inf): 1
            }                                                                      
        }  
        self.points_negative_errors = {
            "tabla A-1": {
                (0, 1): 5, (2, 2): 4, (3, 3): 3, (4, 5): 2, (6, math.inf): 1
            },            
            "tabla A-2": {
                (0, 1): 5, (2, 2): 4, (3, 3): 3, (4, 4): 2, (5, math.inf): 1
            },            
            "tabla A-3": {
                (0, 1): 5, (2, 2): 4, (3, 4): 3, (5, 5): 2, (6, math.inf): 1
            },
            "tabla A-4": {
                (0, 0): 5, (1, 2): 3, (3, 3): 2, (4, math.inf): 1
            },
            "tabla A-5": {
                (0, 1): 5, (2, 2): 4, (3, 3): 3, (4, 4): 2, (5, math.inf): 1
            },
            "tabla A-6": {
                (0, 4): 5, (5, 6): 4, (7, 13): 3, (14, 19): 2, (20, math.inf): 1
            },    
            "tabla A-7": {
                (0, 1): 5, (2, 2): 4, (3, 4): 3, (5, 5): 2, (6, math.inf): 1
            },          
            "tabla A-8": {
                (0, 2): 5, (3, 3): 4, (4, 5): 3, (6, 8): 2, (9, math.inf): 1
            },
            "tabla A-9": {
                (0, 1): 5, (2, 2): 4, (3, 4): 3, (5, 6): 2, (7, math.inf): 1
            },
            "tabla A-10": {
                (0, 1): 5, (2, 3): 3, (4, 5): 2, (6, math.inf): 1
            },
            "tabla A-11": {
                (0, 2): 5, (3, 3): 4, (4, 7): 3, (8, 9): 2, (10, math.inf): 1
            }                                                                      
        }  


    def define_table(self):
        if self.age > 5 and self.age < 8:
            return "tabla A-1"
        elif self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11"  
        
    def get_data(self):
        try:
            metamemory = Metamemory.objects.get(banfe_test_id = self.banfe_id)
            return {
                'positive_errors': metamemory.positive_errors,
                'negative_errors': metamemory.negative_errors
            }

        except Metamemory.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Card Sorting
        data_metamemory = self.get_data()

        if data_metamemory is not "DoesNotExist":
            return {     
                'encoded_positive_errors': self.encoded_positive_errors(data_metamemory['positive_errors']),
                'encoded_negative_errors': self.encoded_negative_errors(data_metamemory['negative_errors'])        
            }
        else:
            return "DoesNotEncoded"
        
    def encoded_positive_errors(self,positive_errors):
        points = self.points_positive_errors.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= positive_errors <= rank[1]:
                    return coded_value
        return default_value         

    def encoded_negative_errors(self,negative_errors):
        points = self.points_negative_errors.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= negative_errors <= rank[1]:
                    return coded_value
        return default_value         

class Visuospatial_Memory_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship

        self.points_perseverations = {         
            "tabla A-2": {
                (0, 0): 5, (1, 1): 4, (2, 2): 3, (3, 4): 2, (5, math.inf): 1
            },
            "tabla A-3": {
                (0, 0): 4, (1, math.inf): 1
            },
            "tabla A-4": {
                (0, 0): 5, (1, math.inf): 1
            },
            "tabla A-5": {
                (0, 0): 5, (1, math.inf): 1
            },
            "tabla A-6": {
                (0, 0): 4, (1, 1): 2, (2, math.inf): 1
            },    
            "tabla A-7": {
                (0, 0): 5, (1, 1): 2, (2, math.inf): 1
            },          
            "tabla A-8": {
                (0, 0): 4, (1, math.inf): 1
            },
            "tabla A-9": {
                (0, 0): 4, (1, math.inf): 1
            },
            "tabla A-10": {
                (0, 0): 4, (1, math.inf): 1
            },
            "tabla A-11": {
                (0, 0): 5, (1, 1): 3, (2, 3): 2, (4, 4): 1, (5, math.inf): 0
            }                                                                      
        }  
        self.points_order_errors = {     
            "tabla A-2": {
                (0, 3): 5, (4, 4): 4, (5, 7): 3, (8, 9): 2, (10, math.inf): 1
            },            
            "tabla A-3": {
                (0, 4): 5, (5, 5): 4, (6, 9): 3, (10, 12): 2, (13, math.inf): 1
            },
            "tabla A-4": {
                (0, 1): 5, (2, 3): 3, (4, 4): 2, (5, math.inf): 1
            },
            "tabla A-5": {
                (0, 1): 5, (2, 3): 3, (4, 4): 2, (5, math.inf): 1
            },
            "tabla A-6": {
                (0, 2): 5, (3, 4): 4, (5, 8): 3, (9, 11): 2, (12, math.inf): 1
            },    
            "tabla A-7": {
                (0, 0): 5, (1, 1): 4, (2, 4): 3, (5, 6): 2, (7, math.inf): 1
            },          
            "tabla A-8": {
                (0, 1): 5, (2, 2): 4, (3, 5): 3, (6, 7): 2, (8, math.inf): 1
            },
            "tabla A-9": {
                (0, 1): 5, (2, 2): 4, (3, 4): 3, (5, 6): 2, (7, math.inf): 1
            },
            "tabla A-10": {
                (0, 1): 5, (2, 2): 4, (3, 3): 3, (4, 4): 2, (5, math.inf): 1
            },
            "tabla A-11": {
                (0, 1): 5, (2, 2): 4, (3, 4): 3, (5, 7): 2, (8, 9): 1, (10, math.inf): 0
            }                                                                      
        }  


    def define_table(self):
        if self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11" 

    def get_data(self):
        try:
            visuospatial_memory = Visuospatial_Memory.objects.get(banfe_test_id = self.banfe_id)
            return {
                'maximum_sequence': visuospatial_memory.maximum_sequence,
                'perseverations': visuospatial_memory.perseverations,
                'order_errors': visuospatial_memory.order_errors
            }

        except Visuospatial_Memory.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Card Sorting
        data_visuospatial_memory = self.get_data()

        if data_visuospatial_memory is not "DoesNotExist":
            return {     
                'encoded_perseverations': self.encoded_perseverations(data_visuospatial_memory['perseverations']),
                'encoded_order_errors': self.encoded_order_errors(data_visuospatial_memory['order_errors'])        
            }
        else:
            return "DoesNotEncoded"

    def encoded_perseverations(self,perseverations):
        points = self.points_perseverations.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= perseverations <= rank[1]:
                    return coded_value
        return default_value         

    def encoded_order_errors(self,order_errors):
        points = self.points_order_errors.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= order_errors <= rank[1]:
                    return coded_value
        return default_value         

class Stroop_B_Handler:
    def __init__(self, banfe_id, age, schoolarship):
        self.banfe_id = banfe_id
        self.age = age
        self.schoolarship = schoolarship

        self.points_stroop_errors = {
            "tabla A-2": {
                (0, 3): 5, (4, 4): 4, (5, 7): 3, (8, 10): 2, (11, math.inf): 1
            },
            "tabla A-3": {
                (0, 1): 5, (2, 2): 4, (3, 3): 3, (4, 5): 2, (6, math.inf): 1   
            },
            "tabla A-4": {
                (0, 0): 5, (1, 1): 4, (2, 2): 3, (3, math.inf): 1     
            },
            "tabla A-5": {
                (0, 0): 4, (1, 1): 3, (2, 2): 2, (3, math.inf): 1        
            },
            "tabla A-6": {
                (0, 1): 5, (2, 2): 4, (3, 5): 3, (6, 7): 2, (8, math.inf): 1   
            },    
            "tabla A-7": {
                (0, 0): 4, (1, 1): 2, (2, math.inf): 1  
            },          
            "tabla A-8": {
                (0, 1): 5, (2, 3): 4, (4, 7): 3, (8, 11): 2, (12 , math.inf): 1  
            },
            "tabla A-9": {
                (0, 0): 5, (1, 1): 4, (2, 3): 3, (4, 4): 2, (5, math.inf): 1    
            },
            "tabla A-10": {
                (0, 1): 5, (2, 2): 4, (3, 4): 3, (5, 7): 2, (8 , math.inf): 1  
            },
            "tabla A-11": {
                (0, 1): 5, (2, 2): 4, (3, 4): 3, (5, 7): 2, (8 , math.inf): 1  
            }                                                                      
        }  
        self.points_time = {
            "tabla A-2": {
                (1, 121): 5, (122, 131): 4, (132, 158): 3, (159, 186): 2, (187, math.inf): 1 
            },
            "tabla A-3": {
                (1, 105): 5, (106, 112): 4, (113, 135): 3, (136, 158): 2, (159, math.inf): 1
            },
            "tabla A-4": {
                (1, 81): 5, (82, 87): 4, (88, 103): 3, (104, 119): 2, (120, math.inf): 1
            },
            "tabla A-5": {
                (1, 73): 5, (74, 78): 4, (79, 92): 3, (93, 107): 2, (108, math.inf): 1
            },
            "tabla A-6": {
                (1, 77): 5, (78, 86): 4, (87, 111): 3, (112, 137): 2, (138, math.inf): 1
            },    
            "tabla A-7": {
                (1, 70): 5, (71, 76): 4, (77, 93): 3, (94, 110): 2, (111, math.inf): 1
            },          
            "tabla A-8": {
                (1, 80): 5, (81, 87): 4, (88, 105): 3, (106, 124): 2, (125, math.inf): 1
            },
            "tabla A-9": {
                (1, 80): 5, (81, 88): 4, (89, 113): 3, (114, 137): 2, (138, math.inf): 1
            },
            "tabla A-10": {
                (1, 82): 5, (83, 91): 4, (92, 120): 3, (121, 148): 2, (149, math.inf): 1
            },
            "tabla A-11": {
                (1, 92): 5, (93, 101): 4, (102, 128): 3, (129, 155): 2, (156, math.inf): 1
            }                                                                      
        }  


    def define_table(self):
        if self.age > 7 and self.age < 10:
            return "tabla A-2"
        elif self.age > 9 and self.age < 12:
            return "tabla A-3"
        elif self.age > 11 and self.age < 14:
            return "tabla A-4"
        elif self.age > 13 and self.age < 16:
            return "tabla A-5"                                    
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-6"
        elif (self.age > 15 and self.age < 31) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-7"            
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-8"
        elif (self.age > 30 and self.age < 56) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-9"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 3 and self.schoolarship < 10):
            return "tabla A-10"
        elif (self.age > 55 and self.age < 66) and (self.schoolarship > 9 and self.schoolarship < 25):
            return "tabla A-11" 

    def get_data(self):
        try:
            stroop_b = Stroop_B.objects.get(banfe_test_id = self.banfe_id)
            return {
                'successes': stroop_b.successes,
                'stroop_errors': stroop_b.stroop_errors,
                'time': stroop_b.time
            }

        except Stroop_B.DoesNotExist:
            return "DoesNotExist"
    
    def get_data_coded(self):
        # Llamar al método para obtener los datos de Card Sorting
        data_stroop_b = self.get_data()

        if data_stroop_b != "DoesNotExist":
            return {
                'encoded_stroop_errors': self.encoded_stroop_errors(data_stroop_b['stroop_errors']),     
                'encoded_time': self.encoded_time(data_stroop_b['time']),          
            }
        else:
            return "DoesNotEncoded"
    
    def encoded_stroop_errors(self,stroop_errors):
        points = self.points_stroop_errors.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= stroop_errors <= rank[1]:
                    return coded_value
        return default_value         

    def encoded_time(self,time):
        points = self.points_time.get(self.define_table())

        default_value = -1  # Valor predeterminado para devolver si no hay coincidencia

        if points is not None:
            for rank, coded_value in points.items():
                if rank[0] <= time <= rank[1]:
                    return coded_value
        return default_value         
