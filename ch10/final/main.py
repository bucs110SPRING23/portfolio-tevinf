from iss import ISS 
from weather import Weather

# results = [region, country, precip, uv, temp]
def main(): 
    weather = Weather(query = ISS.get_data)
    results = weather.get() 
    results[4] = weather.convert_to_F(results[4])
    print(f'The ISS is currently above {results[0]}, {results[1]}. The rain coverage is {results[2]}. The UV index is {results[3]}. The temperature feels like {results[4]} degrees Fahrenheit.')
    
    ## UMBRELLA ##

    if results[2] >= 0.2: 
        print("People below the ISS should bring an umbrella!")
    elif results[2] < 0.2: 
        print("If you are below the ISS, you do not need an umbrella today.")

    ## SUNSCREEN ## 

    if results[3] >= 5:
        print("If you are below the ISS, you need sunscreen today!")
    elif results[3] < 5: 
        print("If you are below the ISS, you don't need sunscreen today.")

    ## JACKET ##

    if results[4] <= 18 and results[4] > 3:
        print("People below the ISS need a jacket today!")
    elif results[4] > 18:
        print("People below the ISS don't need a jacket today.")
    else:
        print("People below the ISS need a coat!!!")


main()