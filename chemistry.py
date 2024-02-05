def get_valency(element):
    valencies = {'H':1,'O':2,'N':3,'Cl':1, 'Na':1, 'Ca':2,'Mg':2,'Fe':3}
    
    return valencies.get(element, 1)

def combine_elements(element1, element2):
    valency1 = get_valency(element`1)
    valency2 = get_valency(element2)
    
    
    compound = f'{element1}{valency2}{element2}{valency1}' if valency1 != 1 or valency2 != 1 else f"{element1}{element2}"
    
    return compound


element1 = input("Enter the symbol of the first element: ").capitalize()
element2 = input("Enter the symbol of the second element: ").capitalize()

chemical_equation = combine_elements(element1, element2)
print(f"The formed compund is: {chemical_equation}")
