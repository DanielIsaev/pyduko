#!/usr/bin/python3

def sudoku(rows):
    
    flag = True
    for row in rows:                                                # validate each row.
        if len(row) != len(set(row)):
            flag = False
            return flag 
    
    coloums = [[row[i] for row in rows] for i in range(9)]          # extract the vertical coloums. 

    for coloum in coloums:                  
        if len(coloum) != len(set(coloum)):
            flag = False
            return flag                      

    def blocks(start, stop):                                        # extract the 3x3 blocks. 
        nonlocal flag
        block = [row[i] for i in range(start, stop) for row in rows[start:stop]]
        if len(block) != len(set(block)):
            flag = False
            return flag
                                    
    slices = [i for i in range(0,9,3)]                            
    for idx, slice in enumerate(slices):                            # iterate over blocks(),
        if not blocks(slice, slices[idx+1]):                        # with proper indexes.
            return flag                      
            break
    
    return flag                                                     # input is valid.                                
                                              
                                
if __name__ == '__main__':

    # Proof of concept 
    
    print(sudoku(                                                   # ->> Ture. 
        [
            (2, 9, 5, 7, 4, 3, 8, 6, 1),
            (4, 3, 1, 8, 6, 5, 9, 2, 7),
            (8, 7, 6, 1, 9, 2, 5, 4, 3),
            (3, 8, 7, 4, 5, 9, 2, 1, 6),
            (6, 1, 2, 3, 8, 7, 4, 9, 5),
            (5, 4, 9, 2, 1, 6, 7, 3, 8),
            (7, 6, 3, 5, 2, 4, 1, 8, 9),
            (9, 2, 8, 6, 7, 1, 3, 5, 4),
            (1, 5, 4, 9, 3, 8, 6, 7, 2),
        ]
        )  
    )


    

