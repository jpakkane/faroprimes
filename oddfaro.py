#!/usr/bin/env python3

import sys, os, re


def num_unique(numarray):
    s = set(numarray)
    return len(s)

class PrimeThingy:
    def __init__(self):
        self.primelist = []
        self.primeset = set()

    def load(self, fname):
        for line in open(fname, 'r'):
            _, number, _ = line.split(',')
            number = number.strip()
            self.primelist.append(number)
            self.primeset.add(number)
        self.largest = int(self.primelist[-1])

    def full_faro(self):
        for num in self.primelist:
            #if len(num) < 3:
            #    continue
            if len(num) % 2 == 0:
                continue
            faro_in = self.test_faro_in(num)
            faro_out = self.test_faro_out(num)

            if faro_in:
                if faro_out:
                    print('Faro both:', faro_in, faro_out, )
                else:
                    print('Faro in:', faro_in)
            elif faro_out:
                print('Faro out:', faro_out)

    def test_faro_in(self, num):
        if len(num) < 2:
            return [num]
        seq = [num]
        current_num = num
        splitpoint = len(num)//2 + 1
        if num == '110017':
            pass
        while True:
            left = current_num[:splitpoint]
            right = current_num[splitpoint:]
            assert len(left) == len(right) + 1
            shuffled_arr = []
            for i in range(len(right)):
                shuffled_arr.append(left[i])
                shuffled_arr.append(right[i])
            shuffled_arr.append(left[-1])
            shuffled = ''.join(shuffled_arr)
            if shuffled not in self.primeset:
                return []
            if shuffled == num:
                break
            seq.append(shuffled)
            current_num = shuffled
        return seq

    def test_faro_out(self, num):
        if len(num) == 1:
            return [num]
        if len(num) == 2:
            swapped = num[1] + num[0]
            if swapped in self.primeset:
                return [num, swapped]
            return []
        seq = [num]
        current_num = num
        midpoint = len(num)//2
        while True:
            left = current_num[:midpoint]
            right = current_num[midpoint:]
            assert len(left) + 1 == len(right)
            if right[0] == '0':
                return []
            shuffled_arr = []
            for i in range(len(left)):
                shuffled_arr.append(right[i])
                shuffled_arr.append(left[i])
            shuffled_arr.append(right[-1])
            shuffled = ''.join(shuffled_arr)
            if shuffled not in self.primeset:
                return []
            if shuffled == num:
                break
            seq.append(shuffled)
            current_num = shuffled
        return seq

if __name__ == '__main__':
    pt = PrimeThingy()
    pt.load('P-1000000.txt')

    print('Results for primes with an odd number of digits')
    pt.full_faro()

