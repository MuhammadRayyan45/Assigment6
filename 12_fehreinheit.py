class TeamperatureConverter:

    @staticmethod
    def  celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
print(TeamperatureConverter.celsius_to_fahrenheit(20))    
