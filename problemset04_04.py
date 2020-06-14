def asterix_triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print (' ' * ( i + 2 ) + '*' * ( t * 2 + 2 ))
        return asterix_triangle( i - 1, t + 1 )

asterix_triangle(5)