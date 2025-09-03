def calculate_sales():
    months = 11

    crops = {
        'tomato':    [(4.8, 10), 7, 6],
        'potato':    [(16, 10), 20, months + 1],
        'cabbage':   [(16, 14), 24, months + 1],
        'sunflower': [(16, 0.7), 200, 10],
        'sugarcane': [(16, 45), 4000, 14]
    }

    total_sales = 0
    chemical_free_sales = 0

    for crop, data in crops.items():
        # Handle both 3 or 4 element scenarios
        if len(data) == 4:
            (land, yield_per_acre), price, conversion_time, _ = data
        elif len(data) == 3:
            (land, yield_per_acre), price, conversion_time = data
        else:
            print(f"Invalid data structure for {crop}: {data}")

        total_yield = land * yield_per_acre

        if crop == 'sugarcane':
            sales = total_yield * (price / 1000)
        else:
            sales = total_yield * 1000 * price

        total_sales += sales

        if conversion_time <= months:
            chemical_free_sales += sales

    print(f"a. Total sales: ₹{total_sales:,.2f}")
    print(f"b. Chemical-free sales at {months} months: ₹{chemical_free_sales:,.2f}")

calculate_sales()
