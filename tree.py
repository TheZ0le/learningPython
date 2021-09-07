def main():
    center = 30
    base_tree = [1,3,5]
    height = max(3, int(input('Höhe des Baums: ')))
  
    for tree_parts in range(0, height//3):
        for base_width in base_tree:
            line = '*' * (base_width+tree_parts*2)
            print(line.center(center))
 
    for tree_parts in range(0, height%3):
        print('###'.center(center))
main()