examples_delete_livraria_invalid_values = [
    ("123", 400),
    ("123.to_i", 400),
    ("123.to_f", 400),
    ("None", 400),
    ("Null", 400),
    ("number_negative", 400),
    ("boolean_true", 400),
    ("boolean_false", 400),
    ("256.characters_type_string", 400),
    ("256.characters_type_numbers", 400),
]
