from django.db import models
from PROCEEDING.models import Proceeding

# Create your models here.
class Cortex(models.Model):
    name = models.CharField(max_length=50)

class BANFE(models.Model):
    area = models.ManyToManyField(Cortex)
    proceeding = models.ForeignKey(Proceeding, on_delete=models.CASCADE)

class Labyrinths(models.Model):
    touch = models.IntegerField()
    cross = models.IntegerField()
    caught = models.IntegerField()
    time = models.IntegerField()
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Signaling(models.Model):
    successes = models.IntegerField()
    perseverations = models.IntegerField()
    omissions = models.IntegerField()
    time = models.IntegerField()
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Ordering(models.Model):
    essays_first_list = models.IntegerField()
    order_errors_first = models.IntegerField()
    perseverations_first = models.IntegerField()
    intrusions_first = models.IntegerField()
    essays_second_list = models.IntegerField()
    order_errors_second = models.IntegerField()
    perseverations_second = models.IntegerField()
    intrusions_second = models.IntegerField()
    essays_third_list = models.IntegerField(null=True)
    order_errors_third = models.IntegerField(null=True)
    perseverations_third = models.IntegerField(null=True)
    intrusions_third = models.IntegerField(null=True)
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Substraction(models.Model):
    successes_a = models.IntegerField()
    mistakes_a = models.IntegerField()
    time_a = models.IntegerField()
    successes_b = models.IntegerField(null=True)
    mistakes_b = models.IntegerField(null=True)
    time_b = models.IntegerField(null=True)    
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Addition(models.Model):
    successes = models.IntegerField()
    mistakes = models.IntegerField()
    time = models.IntegerField()
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Card_Sorting(models.Model):
    successes = models.IntegerField()
    mistakes = models.IntegerField()
    perseverations = models.IntegerField()
    deferred_perseverations = models.IntegerField()
    maintenance_error = models.IntegerField()
    time = models.IntegerField()
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Semantic_Classification(models.Model): 
    specific_categories = models.IntegerField()
    specific_average = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    functional_categories = models.IntegerField()
    functional_average = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    abstract_categories = models.IntegerField()
    abstract_average = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    total_categories = models.IntegerField()
    total_average = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    total_score = models.IntegerField()
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Stroop_A(models.Model):
    successes = models.IntegerField()
    stroop_errors = models.IntegerField()
    non_stroop_errors = models.IntegerField()
    time = models.IntegerField()
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Verbal_Fluency(models.Model):
    successes = models.IntegerField()
    perseverations = models.IntegerField()
    intrusions = models.IntegerField()
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Cards_Game(models.Model):
    total_score = models.IntegerField()
    percentage_risk_cards = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    first_question = models.CharField(max_length=30)
    second_question = models.CharField(max_length=30)
    third_question = models.CharField(max_length=30)
    fourth_question = models.CharField(max_length=30)
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Sayings(models.Model):
    successes = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    time = models.IntegerField()
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Towers_Hanoi(models.Model): #
    movements_first = models.IntegerField()
    time_first = models.IntegerField()
    type_1_error_first = models.IntegerField()
    type_2_error_first = models.IntegerField()
    total_error_first = models.IntegerField()
    movements_second = models.IntegerField(null=True)
    time_second = models.IntegerField(null=True)
    type_1_error_second = models.IntegerField(null=True)
    type_2_error_second = models.IntegerField(null=True)
    total_error_second = models.IntegerField(null=True)
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Metamemory(models.Model):
    intrusions = models.IntegerField()
    perseverations = models.IntegerField()
    positive_errors = models.IntegerField()
    negative_errors = models.IntegerField()
    negative_errors = models.IntegerField()
    total_errors = models.IntegerField()
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Visuospatial_Memory(models.Model):
    order_errors = models.IntegerField()
    substitution_errors = models.IntegerField()
    perseverations = models.IntegerField()
    maximum_sequence = models.IntegerField()
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)

class Stroop_B(models.Model):
    successes = models.IntegerField()
    stroop_errors = models.IntegerField()
    non_stroop_errors = models.IntegerField()
    time = models.IntegerField()
    banfe_test = models.ForeignKey(BANFE, on_delete=models.CASCADE)
