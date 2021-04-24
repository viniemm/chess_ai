import pygame
import copy
import sys, os
import math


def legal(a1, a2, current_pos) -> bool:
    dif = a2 - a1
    flag = True
    p1 = current_pos[a1]
    p2 = current_pos[a2]

    try:
        if p1.id[0] == p2.id[0]:
            flag = False
    except TypeError:
        pass

    # Pawn
    if p1.id[1:] == "pawn":
        if p1.moved is False:
            i = [8, 16]
            mx = 16
        else:
            i = [8]
            mx = 8
        if p2.empty is True:
            if abs(dif) > mx:
                flag = False
            if p1.id[0] == "b" and dif not in i:
                flag = False
            if p1.id[0] == "w" and -dif not in i:
                flag = False
        else:
            flag = False
            if p1.id[0] == "b" and dif in [7, 9]:
                flag = True
            if p1.id[0] == "w" and -dif in [7, 9]:
                flag = True

    # Horse
    if p1.id[1:] == "horse":
        horse_set = [-17, -15, -10, -6, 6, 10, 15, 17]
        if dif not in horse_set:
            flag = False

    # Rook
    if p1.id[1:] == "rook":
        rook_set1 = []
        rook_set2 = []
        for pos in range(0, 64):
            if (pos - a1) % 8 == 0:
                rook_set1.append(pos)
            if pos in range((a1//8)*8, ((a1//8)+1)*8):
                rook_set2.append(pos)

        # for x in rook_set1:
        #     if current_pos[x].id[0] == p1.id[0]:
        #         rook_set1.remove()

        rook_set = rook_set1 + rook_set2
        print(rook_set, a2)
        if a2 not in rook_set:
            flag = False

    # Bishop
    if p1.id[1:] == "bishop":
        bish_set = []
        for pos in range(0, 64):
            if (pos - a1) % 9 == 0 or (pos - a1) % 7 == 0:
                bish_set.append(pos)
        print(bish_set, a2)
        if a2 not in bish_set:
            flag = False

    # Queen
    if p1.id[1:] == "queen":
        queen_set = []
        for pos in range(0, 64):
            if (pos - a1) % 8 == 0 or pos in range((a1//8)*8, ((a1//8)+1)*8) or (pos - a1) % 9 == 0 or (pos - a1) % 7 == 0:
                queen_set.append(pos)
        print(queen_set, a2)
        if a2 not in queen_set:
            flag = False


    if flag:
        p1.moved = True
    return flag
