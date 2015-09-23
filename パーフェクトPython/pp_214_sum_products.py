#!/usr/bin/env python


def sum_products(filename):
    with open(filename) as f:
        results = {}
        for line in f:
            parts = line.split(",")
            title = parts[0]
            try:
                results[title] = results.get(title, 0) + parts[1]
            except:
                print('error')
    return results


def print_result(results):
    for key, value in results.items():
        print(key, value)

print_result(sum_products('./pp_213_行の分割.csv'))
