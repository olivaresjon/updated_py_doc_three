def area(L, W):
    surface_area = L * W
    print("The surface area of the rectangular shaped house is " +
          str(surface_area) + " square meters.")


final_surface_area = area(int(input("Enter a legth in meters: ")), int(
    input("Enter a width in meters: ")))
