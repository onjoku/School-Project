def captures(chessboard, positionOfRook):
    # Get dimension n of board
    n = len(chessboard)
    # Initialize total captures to 0
    total_captures = 0

    # Get row and col of rook
    rook_row = positionOfRook[0]
    rook_col = positionOfRook[1]

    # Loop to check for Captured
    found = False
    row = rook_row

    #while the top border is not reached and no opponent
    #pieces are found
    while row >= 0 and found is False:

        #if the piece at row, rook's col is an opponent
        if chessboard[row][rook_col] != "":

            # Opponent piece found
            found = True

            #Increment total captures
            total_captures = total_captures + 1

            # Move to the next row above
            row = row - 1

            #Loop to check below the rook for captures
            found = False
            row = rook_row

            #while the bottom border is not reached and no opponent
            #pieces are found
            while row < n and found is False:
                if chessboard[row][rook_col] != "":
                    #Opponent piece found
                    found = True

                    #Increment total cptures
                    total_captures = total_captures + 1

                    # Move to the next row below
                    row = row + 1

                    # Loop to check left of the rook for captures
                    found = False
                    col = rook_col

                    #While the left border is n ot reach and no opponent
                    #piece are found
                    while col >= 0 and found is False:
                        if chessboard[rook_row][col] != "":

                            #Opponents piece found
                            found = True

                            #Increment total Captures
                            total_captures = total_captures + 1

                            # Move to the next column on the left
                            col = col -1

                            #Loop to check the right of the rook for captures
                            found = False
                            col = rook_col

                            #While the right border is not reached and no opponent
                            #pieces are found
                            while col < n and found is False:
                                if chessboard[rook_row][col] != "":

                                    #Opponent piece found
                                    found = True

                                    #Increment total captures
                                    total_captures = total_captures + 1

                                    # Move to the next column on the right
                                    col = col + 1

                                    return total_captures
