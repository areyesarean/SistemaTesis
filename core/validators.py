from django.core.validators import *

CI_LENGTH_VALIDATORS = MinLengthValidator(11, message='El carné debe contener 11 caracteres')
CI_ONLY_DIGITS_VALIDATOR = RegexValidator('^[0-9]{11}$', message='Carné incorrecto')
CI_VALIDATORS = [CI_ONLY_DIGITS_VALIDATOR, CI_LENGTH_VALIDATORS]

EDAD_MIN_VALUE_VALIDATOR = MinValueValidator(18, message='La edad no puede ser menor a 18 años')
EDAD_MAX_VALUE_VALIDATOR = MaxValueValidator(80, message='La edad no puede ser superior a 80 años')
EDAD_VALIDATORS = [EDAD_MAX_VALUE_VALIDATOR, EDAD_MIN_VALUE_VALIDATOR]
