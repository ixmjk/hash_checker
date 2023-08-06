# Hash Checker Python Script

**hash_checker** is a lightweight and efficient Python script designed to verify the integrity of files using cryptographic hash functions. It leverages the [hashlib](https://docs.python.org/3/library/hashlib.html) library from [the Python standard library](https://docs.python.org/3/library/index.html) to compute hash values, ensuring that files have not been tampered with or corrupted.

## Features

- Calculate hash values for files/strings using different hash algorithms.
- Supports various hash algorithms provided by the `hashlib` library.

## Installation

1. Make sure you have [Python](https://www.python.org/downloads/) installed on your system.

2. Clone this repository or download the script directly.

   ```
   git clone https://github.com/ixmjk/hash_checker.git
   ```

3. Open a terminal/command prompt and navigate to the project directory.

   ```
   cd hash_checker
   ```

4. Run the script by executing the following command:
   
   ```
   python hash_checker.py
   ```

## Usage

After running the script, simply drag and drop any file you want to the terminal window and hit enter:

```
Drag and drop the file: D:\Pictures\image.png
```
In the next menu, select a hash algorithm and hit enter to get the hash value of the file.
```
--------------------------------------------------
File Name: image.png
File Size: 50.73 KB
File Path: D:\Pictures\image.png

sha256: db0d6ce23f8df41babeb581b340d43e3daaa7d53e14179f9781fe146e4a5ed57
--------------------------------------------------

0. Main Menu
1. blake2b
2. blake2s
3. md4
4. md5
5. md5-sha1
6. mdc2
7. ripemd160
8. sha1
9. sha224
10. sha256
11. sha384
12. sha3_224
13. sha3_256
14. sha3_384
15. sha3_512
16. sha512
17. sha512_224
18. sha512_256
19. shake_128
20. shake_256
21. sm3
22. whirlpool

> 4
9d5a59b531165a703d776d6ae79a7152

Press any key to continue...
```

You can also check the hash of any string:
```
Drag and drop the file: 1234567890
```
```
--------------------------------------------------
Input String: 1234567890
Lenght: 10

sha256: c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646
--------------------------------------------------

0. Main Menu
1. blake2b
2. blake2s
3. md4
4. md5
5. md5-sha1
6. mdc2
7. ripemd160
8. sha1
9. sha224
10. sha256
11. sha384
12. sha3_224
13. sha3_256
14. sha3_384
15. sha3_512
16. sha512
17. sha512_224
18. sha512_256
19. shake_128
20. shake_256
21. sm3
22. whirlpool

> 4
e807f1fcf82d132f9bb018ca6738a19f

Press any key to continue...
```

## Supported Hash Algorithms

To see a list of available hash algorithms, run the following command in your terminal:
```
python -c "import hashlib; aa = sorted(list(hashlib.algorithms_available)); [print(a) for a in aa]"
```
