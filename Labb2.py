def aritmetisk_summa(a_1, d, n):
    return (n * (2 * a_1 + (n - 1) * d)) // 2

def geometrisk_summa(a_1, r, n):
    if r == 1:
        return a_1 * n
    else:
        return a_1 * (1 - r**n) // (1 - r)

def menu():
    print("[1] Räkna ut en aritmetisk summa")
    print("[2] Räkna ut en geometrisk summa")
    print("[3] Jämför din aritmetiska och geometriska summa")
    print("[0] Lämna programmet")

while True:
    menu()
    option = int(input("Välj ett alternativ: "))

    if option == 1:
        try:
            a_1_aritmetisk = float(input("Välj ett startvärde: "))
            d_aritmetisk = float(input("Välj en differens: "))
            n_aritmetisk = int(input("Välj antalet element (i både din aritmetiska och geometriska summa): "))
            summa_aritmetisk = aritmetisk_summa(a_1_aritmetisk, d_aritmetisk, n_aritmetisk)
            print(f"Din aritmetiska summa blir: {summa_aritmetisk}")
        except ValueError:
            print("Felaktig inmatning. Ange giltiga numeriska värden.")
        
    elif option == 2:
        try:
            a_1_geometrisk = float(input("Välj ett startvärde: "))
            r_geometrisk = float(input("Välj en kvot: "))
            n_geometrisk = n_aritmetisk
            summa_geometrisk = geometrisk_summa(a_1_geometrisk, r_geometrisk, n_geometrisk)
            print(f"Din geometriska summa blir: {summa_geometrisk}")
        except ValueError:
            print("Felaktig inmatning. Ange giltiga numeriska värden.")
        
    elif option == 3:
        if 'summa_aritmetisk' not in locals() or 'summa_geometrisk' not in locals():
            print("Var snäll och skapa både en aritmetisk och geometrisk summa först")
        elif summa_geometrisk < summa_aritmetisk:
            print(f"Din aritmetiska summa är större än din geometriska summa")
        elif summa_geometrisk == summa_aritmetisk:
            print(f"Din aritmetiska och geometriska summa är lika stora")
        else:
            print("Din geometriska summa är större än din aritmetiska summa")
        
    elif option == 0:
        print("Tack för att du använde programmet")
        break
    else:
        print("Felaktig inmatning. Välj ett giltigt alternativ (0-3).")