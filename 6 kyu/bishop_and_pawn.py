def bishop_and_pawn(bishop, pawn):
    if abs(int(bishop[1])-int(pawn[1]))==abs(ord(bishop[0])-ord(pawn[0])):
        return True
    return False