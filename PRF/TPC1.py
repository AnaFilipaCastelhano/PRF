# funções para fazer isto, documentado e com os nomes todos certos:
# join two lists of strings based on the index
# find top N element(s) in list ( o N vai ser definido pelo utilizador)
# encontrar o maior elemento de uma lista


names1 = ["a", "b", "c", "d", "e", "f"]
names2 = ["g", "h", "i", "j", "k", "l"]


def join_lists(list1, list2):
    new_list = []  # this creats a empty list, so the pars can be added
    for element1, element2 in zip(list1,
                                  list2):  # for cicle iterates for both lists at the same time, and will append the
        # par of elements as a tuple, on the new list
        new_list.append((element1, element2))
    return new_list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30]


def find_highest_number(list):
    container = list[
        0]  # this creates a variable where the highest number should be stored, and it is initialized with the 1st
    # element of the list
    for number in list:  # for cicle will iterate for all elements on the list
        if number > container:  # for every element on the list if function tests is it is greater than the number on
            # the container
            container = number  # if the number we are analysing turns out to be greater, it is used to replace the
            # value on the container
    return container


# this function will find the top elements on a certain list, the number of elements to find will be given by the user
def find_top_n_elements(n, list):
    # since we already have a function to find the highest element of a specific list, we will use that, to find the
    # highest, to add it to a new list and at the same time we will remove it from the list where we
    # are working
    highest = find_highest_number(list)
    new_list = [highest]
    list.remove(highest)
    # we will continue doing these 3 operations, until we have found all the elements we need, i.e., everything we
    # find the highest on the list, we will append to the new list, and remove it from the initial one and continue
    # doing this, until the len of the new list equals the n given by the user
    while len(new_list) < n:
        highest = find_highest_number(list)
        new_list.append(highest)
        list.remove(highest)
    # the new list will have the elements on decreasing order, therefore, on the final step we will sort the list
    return sorted(new_list)


print(find_top_n_elements(10, numbers))
