import re


def group(barcode):
    bar_code_group = '00'
    digits = re.findall(r'\d', barcode)

    if digits:
        bar_code_group = ''.join(digits)

    return bar_code_group


valid_barcode = r'^(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)$'
valid_pattern = re.compile(valid_barcode)

total_barcodes = int(input())

for _ in range(total_barcodes):
    barcode = input()

    match = re.search(valid_pattern, barcode)

    if match:
        current_barcode = match.group(2)
        barcode_group = group(current_barcode)
        print(f'Product group: {barcode_group}')
    else:
        print('Invalid barcode')
