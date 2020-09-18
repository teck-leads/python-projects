# Define custom filters

def evenFilter(sequence):
    sequenceEvn = []
    for num in sequence:
        if num % 2 == 0:
                sequenceEvn.append(num)
    
    return sequenceEvn
    
    # Complete the definition of evenFilter below
