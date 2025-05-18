#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):  # Verificamos que sea una cadena
        return 0

    roman_dict = {  # Diccionario que asigna los números romanos a sus valores
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    length = len(roman_string)

    # Iteramos a través de la cadena
    for i in range(length):
        current_value = roman_dict[roman_string[i]]
        # Valor actual del símbolo
        if i + 1 < length:
            # Si no estamos en el último símbolo
            next_value = roman_dict[roman_string[i + 1]]
            # Valor del siguiente símbolo
            if current_value < next_value:
                # Si el valor actual es menor que el siguiente
                total -= current_value
                # Restamos el valor actual
            else:
                total += current_value
                # Si no, sumamos el valor actual
        else:
            total += current_value
            # Para el último símbolo, siempre lo sumamos

    return total
