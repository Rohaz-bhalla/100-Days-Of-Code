def pure_chai(cups):
    return cups * 10

total_chai = 10

def chai(n):
    if n == 0:
        return "all chai are poured...!"
    return chai(n-1)

print(chai(3))

chai_types = ["light", "dark", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai not in ["kadak", "ginger"], chai_types))
print(strong_chai)