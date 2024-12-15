import heapq
from collections import Counter, defaultdict

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freqs):

    heap = [HuffmanNode(char, freq) for char, freq in freqs.items()]
    heapq.heapify(heap)
    

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(root):
    codes = {}

    def traverse(node, code):
        if node is not None:
            if node.char is not None: 
                codes[node.char] = code
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

    traverse(root, "")
    return codes


def huffman_encode(text):
    frequencies = Counter(text)
    root = build_huffman_tree(frequencies)
    codes = build_huffman_codes(root)
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, codes


def huffman_decode(encoded_text, codes):
    reversed_codes = {code: char for char, code in codes.items()}
    

    decoded_text = []
    buffer = ""
    for bit in encoded_text:
        buffer += bit
        if buffer in reversed_codes:
            decoded_text.append(reversed_codes[buffer])
            buffer = ""

    return "".join(decoded_text)
