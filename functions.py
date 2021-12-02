
ProductList = {}
def Open_file():
###Opens the file###
    with open("Your_list.csv") as file:
        for row in file:
            if not row:
                continue
            else:
                product_name, values = row.split(',')
                ProductList[product_name] = values


def macro(product_name, gram):
###Calculates the nutritional values and returns result###
    kcal_value = protein_value = carb_value = fat_value = 0

    if product_name in ProductList:
        (kcal, protein, carb, fat) = ProductList[product_name].split(':')
        #calculating the nutritional values
        kcal_value += gram / 100 * int(kcal)
        protein_value += gram / 100 * int(protein)
        carb_value += gram / 100 * int(carb)
        fat_value += gram / 100 * int(fat)
        outcome = "Your product provided you with %d kcal, "\
           "%d protein, %d carbs oraz %d fat."\
           % (kcal_value, protein_value, carb_value, fat_value)
    else:
        outcome = "Sorry, the product you tried to look for is not in the dataset: %s, but you can add it! :)"% (product_name)
    return outcome











