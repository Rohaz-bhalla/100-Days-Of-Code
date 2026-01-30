def chai_generate(flavour = "chocolate"):
    """Return the flavour of chai"""
    chai = "ginger"
    return flavour

print(chai_generate.__doc__)
print(chai_generate,__name__)

help(len)

def generate_bill(chai = 0, samosa = 0):
    """
    Docstring for generate_bill
    calculate the bill for samosa and chai
    
    :param chai: Number of chai cups(10rs per cup)
    :param samosa: number of samosa(15rs per piece)
    :return:(total amount, thank_you msg as string)
    """
    total = chai*10 + samosa*15
    return total, "Thank you from Rohaz"