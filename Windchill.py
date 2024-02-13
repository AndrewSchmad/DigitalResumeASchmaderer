def main():
    print("    ", end="")
    for i in range (-40, 51, 10):
        print(f"{i:7d}", end="")
    print("")
    for wind in range (5, 55, 5):
        print(f"{wind:3d}", end="")
        wind_pow = wind **0.16
        for temp in range(-40, 51, 10):
            chill = 35.74 + 0.6215*temp - 35.75*wind_pow +0.42 *temp * wind_pow
            print(f"{chill:7.1f}", end="")
        print("")
main()