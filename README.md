# Huffman Coding Compression Tool

## Overview

This repository hosts a Python-based command-line tool for Huffman Coding, a classic algorithm used for lossless data compression. The project demonstrates the implementation of Huffman coding to encode and decode text files, showcasing how this algorithm can reduce file size while maintaining the original data's integrity. This tool is ideal for educational purposes, offering insights into data structures, algorithms, and the principles of computer architecture and performance optimization.

## Features

-   **Text File Compression**: Compresses any text file using Huffman coding, reducing file size efficiently.
-   **Text File Decompression**: Restores the original text file from the compressed format without any loss of data.
-   **Command-Line Interface**: Easy-to-use CLI for encoding and decoding operations.
-   **Efficiency Analysis**: Ideal for studying the efficiency of data compression algorithms.

## Installation

To use the Huffman Coding Compression Tool, follow these steps:

1.  Clone the repository:
    
    ```
    git clone https://github.com/stevobain/HuffmanCodingProject.git
    ``` 
    
3.  Navigate to the project directory:
    
    ```
    cd HuffmanCodingProject
    ``` 
    

## Usage

To compress and decompress files using the Huffman Coding Compression Tool, use the following commands:

-   **To Encode (Compress) a File:**
    
    ```
    python sbHuffmanScript.py encode [input file path] [output file path]
    ``` 
    
    Example:
    
    ```
    python sbHuffmanScript.py encode sample.txt encoded.txt
    ``` 
    
-   **To Decode (Decompress) a File:**
    
    ```
    python sbHuffmanScript.py decode [input file path] [output file path]
    ``` 
    
    Example:
    
    ```
    python sbHuffmanScript.py decode encoded.txt decoded.txt
    ```
