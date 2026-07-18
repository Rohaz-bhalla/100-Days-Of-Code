class Avengers:
    def __init__(self, name, level, gender):
        self.name = name
        self.level = level
        self.gender = gender

    @classmethod
    def from_dict(cls, avengers_data):
        # Use the keys that actually exist in your dictionary!
        return cls(
            avengers_data["name"],
            avengers_data["level"],
            avengers_data["gender"]
        )

    @classmethod
    def from_string(cls, abilities):
        # The string must have 3 parts separated by '-'
        name, level, gender = abilities.split("-")
        return cls(name, level, gender)
    
class AgentUtils:
    @staticmethod
    def is_valid_ability(name):
        return name in ("Iron_man", "Captain_america")
    
# 1. Testing Static Method
print(f"Is Iron Man valid? {AgentUtils.is_valid_ability('Iron_man')}")

# 2. Testing from_dict (Fixed Keys)
player1 = Avengers.from_dict({
    "name": "Iron_man", "level": 3, "gender": "male"
})

# 3. Testing from_string (Fixed Data)
player2 = Avengers.from_string("Thor-High-Male")

# 4. Testing standard constructor
player3 = Avengers("Falcon", "Mid", "Male")

print(player1.__dict__)
print(player2.__dict__)
print(player3.__dict__)