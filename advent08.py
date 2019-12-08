with open('advent08.txt') as image_file:
    image_string = image_file.readline().strip()
layers = []
width = 25
height = 6

for layer_index in range(int(len(image_string)/(width*height))): # for each layer 
    layer_beginning = layer_index*width*height
    layer_end = layer_beginning + width*height - 1
    layer = image_string[layer_beginning:layer_end + 1]
    layers.append(layer)
    


min_zeroes = float("inf")
min_zeroes_layer = []
for layer in layers:
    zero_count = 0
    for character in layer:
        if character == '0':
            zero_count += 1
    if zero_count < min_zeroes:
        min_zeroes = zero_count
        min_zeroes_layer= layer

one_count = 0
two_count = 0
for character in min_zeroes_layer:
    if character == '1':
        one_count += 1
    elif character == '2':
        two_count += 1
print(one_count * two_count)

decoded_layer = []
for i in range(width*height):
    curr_layer = 0
    while layers[curr_layer][i] == '2':
        curr_layer += 1
    decoded_layer.append(layers[curr_layer][i])
for i in range(height):
    layer = decoded_layer[i*width:(i+1)*width]
    outstring = ''
    for character in layer:
        if character == '0':
            outstring += ' '
        else:
            outstring += u"\u2588"
    print(outstring)