def maxmin_ladder(input_list):
    row_lengths = [len(row) for row in input_list]

    longest_row_length = max(row_lengths)
    longest_row_idx = row_lengths.index(longest_row_length)
    shortest_row_length = min(row_lengths)
    shortest_row_idx = row_lengths.index(shortest_row_length)

    second_longest_row_length = shortest_row_length - 1
    second_longest_row_idx = None
    for i in range(len(row_lengths)):
        if row_lengths[i] > second_longest_row_length and i != longest_row_idx:
            second_longest_row_idx = i
            second_longest_row_length = row_lengths[i]

    second_shortest_row_length = longest_row_length + 1
    second_shortest_row_idx = None
    for i in range(len(row_lengths)):
        if row_lengths[i] < second_shortest_row_length and i != shortest_row_idx:
            second_shortest_row_idx = i
            second_shortest_row_length = row_lengths[i]

    if second_longest_row_idx < second_shortest_row_idx:
        result = [input_list[second_longest_row_idx], input_list[second_shortest_row_idx]]
        print("The indices are ",second_longest_row_idx, "for second longest row and ",second_shortest_row_idx," for second shortest row")
    else:
        result = [input_list[second_shortest_row_idx], input_list[second_longest_row_idx]]
        print("The indices are ",second_longest_row_idx, "for second longest row and ",second_shortest_row_idx," for second shortest row")
    
    return result
