def linear_search(linear_arr, search_number):
    for i in range(len(linear_arr)):
      if linear_arr[i] == search_number:
        return i

if __name__ == "__main__":
    linear_arr = [5,22,87,1,3]
    search_number = 1
    print("search index :", linear_search(linear_arr, search_number))