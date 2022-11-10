def circumfrance_circle(radius):
    final_circumfrance = 2 * 3.14 * int(radius)
    print("The circumfrance of a circle with your choosen radius of " + str(radius) +
          " meters is " + str(final_circumfrance) + " meters in circumfrance.")


circumfrance_circle(int(input("What is the radius of your desired circle?: ")))
