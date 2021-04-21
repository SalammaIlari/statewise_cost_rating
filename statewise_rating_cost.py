import csv

Tamilnadu_list = []
Maharashtra_list = []
Karnataka_list = []

india_list =[]

hotel_code_list = []
cost_list =[]
rating_list = []

state_input = input("What is the state:")
cost_or_rating_input = input("Cost or Rating:")
operation = input("Operation:")

with open('hotels.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
        india_list.append(row)
        if row[2] == 'Tamilnadu':
            Tamilnadu_list.append(row)
        elif row[2] == 'Maharashtra' :
            Maharashtra_list.append(row)
        elif row[2] == 'Karnataka' :
            Karnataka_list.append(row)

    if state_input == 'Tamilnadu':
        for data in Tamilnadu_list :
            hotel_code_list.append(data[1])
            cost_list.append(int(data[3]))
            rating_list.append(float(data[4]))
        if cost_or_rating_input == 'cost':
            if operation == 'cheapest':
                min_value = min(cost_list)
                code_hotel_value = hotel_code_list[cost_list.index(min_value)]
                print('Hotel with cheapest price in {} is {} with price {}'.format(state_input, code_hotel_value,min_value))
            elif operation == 'highest':
                max_value = max(cost_list)
                code_hotel_value = hotel_code_list[cost_list.index(max_value)]
                print('Hotel with highest price in {} is {} with price {}'.format(state_input, code_hotel_value,max_value))
            elif operation == 'average':
                cost_list_sorted = sorted(cost_list)
                avg_value = cost_list_sorted[int(len(cost_list) / 2)]
                code_hotel_value = hotel_code_list[cost_list.index(avg_value)]
                print('Hotel with average price in {} is {} with price {}'.format(state_input, code_hotel_value,avg_value))

            else:
                print('enter correct operation')
        elif cost_or_rating_input == 'rating':
            if operation == 'cheapest':
                min_value = min(rating_list)
                code_hotel_value = hotel_code_list[rating_list.index(min_value)]
                print('Hotel with cheapest rating  in {} is {} with rating  {}'.format(state_input, code_hotel_value,min_value))
            elif operation == 'highest':
                max_value = max(rating_list)
                code_hotel_value = hotel_code_list[rating_list.index(max_value)]
                print('Hotel with highest rating  in {} is {} with rating  {}'.format(state_input, code_hotel_value,max_value))
            elif operation == 'average':
                rating_list_sorted = sorted(rating_list)
                avg_value = rating_list_sorted[int(len(rating_list) / 2)]
                code_hotel_value = hotel_code_list[rating_list.index(avg_value)]
                print('Hotel with average rating  in {} is {} with rating  {}'.format(state_input, code_hotel_value,avg_value))
            else:
                print('enter correct operation')
    elif state_input == 'Maharashtra':
        for data in Maharashtra_list :
            hotel_code_list.append(data[1])
            cost_list.append(int(data[3]))
            rating_list.append(float(data[4]))
        if cost_or_rating_input == 'cost':
            if operation == 'cheapest':
                min_value = min(cost_list)
                code_hotel_value = hotel_code_list[cost_list.index(min_value)]
                print('Hotel with cheapest price in {} is {} with price {}'.format(state_input, code_hotel_value,
                                                                                min_value))
            elif operation == 'highest':
                max_value = max(cost_list)
                code_hotel_value = hotel_code_list[cost_list.index(max_value)]
                print('Hotel with highest price in {} is {} with price {}'.format(state_input, code_hotel_value,
                                                                                  max_value))
            elif operation == 'average':
                cost_list_sorted = sorted(cost_list)
                avg_value = cost_list_sorted[int(len(cost_list) / 2)]
                code_hotel_value = hotel_code_list[cost_list.index(avg_value)]
                print('Average rating of Hotel in Maharashtra is {}'.format(avg_value))

            else:
                print('enter correct operation')
        elif cost_or_rating_input == 'rating':
            if operation == 'cheapest':
                min_value = min(rating_list)
                code_hotel_value = hotel_code_list[rating_list.index(min_value)]
                print('Hotel with cheapest rating  in {} is {} with rating  {}'.format(state_input, code_hotel_value,min_value))
            elif operation == 'highest':
                max_value = max(rating_list)
                code_hotel_value = hotel_code_list[rating_list.index(max_value)]
                print('Hotel with highest rating  in {} is {} with rating  {}'.format(state_input, code_hotel_value,max_value))
            elif operation == 'average':
                rating_list_sorted = sorted(rating_list)
                avg_value = rating_list_sorted[int(len(rating_list) / 2)]
                code_hotel_value = hotel_code_list[rating_list.index(avg_value)]
                print('Average rating of Hotel in Maharashtra is {}'.format(avg_value))
            else:
                print('enter correct operation')
    elif state_input == 'Karnataka':
        for data in Karnataka_list :
            hotel_code_list.append(data[1])
            cost_list.append(int(data[3]))
            rating_list.append(float(data[4]))
        if cost_or_rating_input == 'cost':
            if operation == 'cheapest':
                min_value = min(cost_list)
                code_hotel_value = hotel_code_list[cost_list.index(min_value)]
                print('Hotel with cheapest price in {} is {} with price {}'.format(state_input, code_hotel_value,min_value))
            elif operation == 'highest':
                max_value = max(cost_list)
                code_hotel_value = hotel_code_list[cost_list.index(max_value)]
                print('Hotel with highest price in {} is {} with price {}'.format(state_input, code_hotel_value,max_value))
            elif operation == 'average':
                cost_list_sorted = sorted(cost_list)
                avg_value = cost_list_sorted[int(len(cost_list) / 2)]
                code_hotel_value = hotel_code_list[cost_list.index(avg_value)]
                print('Hotel with average price in {} is {} with price {}'.format(state_input, code_hotel_value,avg_value))

            else:
                print('enter correct operation')
        elif cost_or_rating_input == 'rating':
            if operation == 'cheapest':
                min_value = min(rating_list)
                code_hotel_value = hotel_code_list[rating_list.index(min_value)]
                print('Hotel with cheapest rating  in {} is {} with rating  {}'.format(state_input, code_hotel_value,min_value))
            elif operation == 'highest':
                max_value = max(rating_list)
                code_hotel_value = hotel_code_list[rating_list.index(max_value)]
                print('Hotel with highest rating  in {} is {} with rating  {}'.format(state_input, code_hotel_value,max_value))
            elif operation == 'average':
                rating_list_sorted = sorted(rating_list)
                avg_value = rating_list_sorted[int(len(rating_list) / 2)]
                code_hotel_value = hotel_code_list[rating_list.index(avg_value)]
                print('Hotel with average rating  in {} is {} with rating  {}'.format(state_input, code_hotel_value,avg_value))
            else:
                print('enter correct operation')
    elif state_input == 'India':
        state_list = []
        for data in range(1,len(india_list)) :
            hotel_code_list.append(india_list[data][1])
            state_list.append(india_list[data][2])
            cost_list.append(int(india_list[data][3]))
            rating_list.append(float(india_list[data][4]))

        if cost_or_rating_input == 'cost':
            if operation == 'cheapest':
                min_value = min(cost_list)
                code_hotel_value = hotel_code_list[cost_list.index(min_value)]
                state_name = state_list[cost_list.index(min_value)]
                print('Hotel with cheapest price in {} is {} with price {}'.format(state_name, code_hotel_value,min_value))
            elif operation == 'highest':
                max_value = max(cost_list)
                code_hotel_value = hotel_code_list[cost_list.index(max_value)]
                state_name = state_list[cost_list.index(max_value)]
                print('Hotel with highest price in {} is {} with price {}'.format(state_name, code_hotel_value,max_value))
            elif operation == 'average':
                cost_list_sorted = sorted(cost_list)
                avg_value = cost_list_sorted[int(len(cost_list) / 2)]
                code_hotel_value = hotel_code_list[cost_list.index(avg_value)]
                state_name = state_list[cost_list.index(avg_value)]
                print('Hotel with average price in {} is {} with price {}'.format(state_name, code_hotel_value,avg_value))

            else:
                print('enter correct operation')
        elif cost_or_rating_input == 'rating':
            if operation == 'cheapest':
                min_value = min(rating_list)
                code_hotel_value = hotel_code_list[rating_list.index(min_value)]
                state_name = state_list[rating_list.index(min_value)]
                print('Hotel with cheapest rating  in {} is {} with rating  {}'.format(state_name, code_hotel_value,min_value))
            elif operation == 'highest':
                max_value = max(rating_list)
                code_hotel_value = hotel_code_list[rating_list.index(max_value)]
                state_name = state_list[rating_list.index(max_value)]
                print('Hotel with highest rating  in {} is {} with rating  {}'.format(state_name, code_hotel_value,max_value))
            elif operation == 'average':
                rating_list_sorted = sorted(rating_list)
                avg_value = rating_list_sorted[int(len(rating_list) / 2)]
                code_hotel_value = hotel_code_list[rating_list.index(avg_value)]
                state_name = state_list[rating_list.index(avg_value)]
                print('Hotel with average rating  in {} is {} with rating  {}'.format(state_name, code_hotel_value,avg_value))
            else:
                print('enter correct operation')

    else:
        print("enter valid state ")
