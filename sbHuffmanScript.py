import argparse
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            frequency = {}
            for char in text:
                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1
            return frequency
    except FileNotFoundError:
        print("File not found.")
        return None

def build_tree(frequencies):
    priority_queue = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    return priority_queue[0]

def generate_codes(node, prefix="", code_table={}):
    if node is not None:
        if node.char is not None:
            code_table[node.char] = prefix
        generate_codes(node.left, prefix + "0", code_table)
        generate_codes(node.right, prefix + "1", code_table)
    return code_table

def write_header(output_file, frequencies):
    with open(output_file, 'wb') as file:
        file.write(str(frequencies).encode())
        file.write(b'\n')

def encode_text(text, code_table):
    encoded_text = ''.join([code_table[char] for char in text])
    return encoded_text

def write_compressed_data(output_file, encoded_text):
    with open(output_file, 'ab') as file:
        byte_array = bytearray()
        for i in range(0, len(encoded_text), 8):
            byte = encoded_text[i:i+8]
            byte_array.append(int(byte, 2))
        file.write(bytes(byte_array))

def read_header(input_file):
    with open(input_file, 'rb') as file:
        frequencies = eval(file.readline())
    return frequencies

def decode_text(encoded_text, root):
    decoded_text = ""
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root
    return decoded_text

def read_compressed_data(input_file):
    with open(input_file, 'rb') as file:
        file.readline()  # Skip the header line
        byte_data = file.read()
        encoded_text = ''.join([f'{byte:08b}' for byte in byte_data])
    return encoded_text

def encode_file(input_file, output_file):
    frequencies = calculate_frequencies(input_file)
    if frequencies is None:
        return
    root = build_tree(frequencies)
    code_table = generate_codes(root)
    write_header(output_file, frequencies)
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
        encoded_text = encode_text(text, code_table)
        write_compressed_data(output_file, encoded_text)

def decode_file(input_file, output_file):
    frequencies = read_header(input_file)
    root = build_tree(frequencies)
    compressed_data = read_compressed_data(input_file)
    decoded_text = decode_text(compressed_data, root)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(decoded_text)

def main():
    parser = argparse.ArgumentParser(description='Huffman Encoding/Decoding Tool')
    parser.add_argument('mode', choices=['encode', 'decode'], help='Mode: encode or decode')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output file path')
    args = parser.parse_args()

    if args.mode == 'encode':
        encode_file(args.input_file, args.output_file)
    elif args.mode == 'decode':
        decode_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()