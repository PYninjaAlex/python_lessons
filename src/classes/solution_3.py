def is_free(table: list) -> bool:
    for i in table:
        for j in i:
            if j == "#":
                return True
    return False
 
 
print(is_free(['x x o', 'x x x', 'o o #']))      
    