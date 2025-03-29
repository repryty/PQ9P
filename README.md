# PQ9+

PQ9+ is a programming language designed for fun and obscurity. It allows you to create unique outputs through a few simple commands.

## Features

*   **Obscurity:** It emphasizes the fun of programming rather than practical purposes.
*   **Simplicity:** It consists of only four commands, making it easy to learn.
*   **Uniqueness:** It provides enjoyment through unexpected results.

## Commands

| Command | Description                                                                 |
| :------ | :-------------------------------------------------------------------------- |
| `P`     | Prints "안녕 난 뽀로로야!" (Hello, I'm Pororo!)                               |
| `Q`     | Prints the source code of the current program.                               |
| `9`     | Prints the lyrics of the "99 Friends of Pororo" song.                        |
| `+`     | Increments an internal accumulator, but there is no way to access it. (Similar to a NOP command) |

# Execution
There are two ways to run the interpreter:
1.  **Direct Source Code Input:**
```bash
$ python3 main.py [source code]
```
-   Enter the code to be executed directly in the `[source code]` part.

2.  **Using a Source File:**

```bash
$ python3 main.py -f [source file]
```
    
    -   Use the `-f` option to specify a file containing the source code.
    -   Enter the path to the source code file in the `[source file]` part.

## Example Usage
1. **Executing Direct Source Code:**
```bash
$ python3 main.py PPQ+PQ++
```

Executing the above code will produce the following output:

```
안녕 난 뽀로로야! 안녕 난 뽀로로야! PPQ+PQ++ 안녕 난 뽀로로야! PPQ+PQ++
```
2. **Executing a Source File:**

```bash
$ python main.py -f my_code
```

**Notes:**

*   The source file must use UTF-8 encoding.

## Influence

This language is inspired by HQ9+.