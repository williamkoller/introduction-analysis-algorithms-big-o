# Introdução à análise de Algoritmo e Big-O

<img src="/imgs/big-o.png" alt="book" title="book" height="104" width="96" align="right"/>

<h3>1 - Por que eh importante saber Big-O?</h3>

Saber Big-O é importante porque permite determinar a complexidade de um algoritmo em relação ao tamanho da entrada. Isso ajuda a identificar algoritmos eficientes e escaláveis para lidar com grandes quantidades de dados e muitas requisições simultâneas. Empresas como Google, Amazon e Microsoft frequentemente fazem perguntas sobre complexidade de algoritmos durante o processo de seleção de candidatos

<h3>2 - Vamos falar sobre desempenho?</h3>

O desempenho de um algoritmo é fundamental para a eficiência e escalabilidade de uma solução. Compreender como medir e melhorar o desempenho é essencial para criar soluções eficientes e escaláveis. Além disso, muitas empresas valorizam o conhecimento desses conceitos durante o processo de seleção dos candidatos.

<img src="/imgs//pensando-codigo.png" alt="pensando-codigo" title="pensando-codigo" align="center" />

<h3>3 - Vamos falar sobre desempenho, do jeito certo?</h3>

Medir o desempenho de um algoritmo requer técnicas adequadas para obter resultados precisos. É importante evitar armadilhas comuns, como medir o tempo de execução em um ambiente não controlado ou medir apenas um caso específico em vez de uma amostra representativa de entradas.

<h3>4 - Vamos falar sobre complexidade linear?</h3>

A complexidade linear descreve um algoritmo cujo tempo de execução aumenta linearmente com o tamanho da entrada. Isso significa que o tempo de execução é proporcional ao número de elementos na entrada.

Exemplo codigo linear: 

```python
def sum_array_complexity(arr):
    total = 0
    for i in arr:
        total += i
    return total
```

```python
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
```

<img src="/imgs/linear.png" alt="complexidade-linear" title="complexidade-linear" align="center" />

<h3>5 - Vamos falar sobre complexidade constante?</h3>

A complexidade constante descreve um algoritmo cujo tempo de execução não varia com o tamanho da entrada. Isso significa que o tempo de execução é constante, independentemente do número de elementos na entrada.

Examplo codigo constante:

```python
def sum_first_two(arr):
    if len(arr) >= 2:
        return arr[0] + arr[1]
    else:
        return None
```

<img src="/imgs/constante.png" alt="complexidade-constante" title="complexidade-constante" align="center" />

<h3>6 - Vamos falar sobre complexidade logarítmica?</h3>

A complexidade logarítmica descreve um algoritmo cujo tempo de execução aumenta logaritmicamente com o tamanho da entrada. Isso significa que o tempo de execução é proporcional ao logaritmo do número de elementos na entrada.

Exemplo codigo logaritmico:

```python
def logarithm(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```


```python
def euclidean_search(a, b):
    while b:
        a, b = b, a % b
    return a
```

<img src="/imgs/logaritma.png" alt="complexidade-logaritmica" title="complexidade-logaritmica" align="center" />

<h3>7 - Vamos falar sobre complexidade quadratica?</h3>

A complexidade quadrática descreve um algoritmo cujo tempo de execução aumenta quadraticamente com o tamanho da entrada. Isso significa que o tempo de execução é proporcional ao quadrado do número de elementos na entrada.

Exemplo codigo quadratica:

```python
def sum_square_matrix(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        for j in range(n):
            total += matrix[i][j]
    return total
```

```python
def pair_sum(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs
```

<img src="/imgs/quadratica.png" alt="complexidade-quadratica" title="complexidade-quadratica" align="center" />


<h3>8 - Vamos falar sobre complexidade cubica?</h3>

A complexidade cúbica descreve um algoritmo cujo tempo de execução aumenta cúbicamente com o tamanho da entrada. Isso significa que o tempo de execução é proporcional ao cubo do número de elementos na entrada.

Exemplo codigo cubica:

```python
def multiply_matrices(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
```

<img src="/imgs/cubica.png" alt="complexidade-cubica" title="complexidade-cubica" align="center" />

<h3>9 - Vamos falar sobre complexidade exponencial?</h3>

A complexidade exponencial descreve um algoritmo cujo tempo de execução aumenta exponencialmente com o tamanho da entrada. Isso significa que o tempo de execução é proporcional a uma constante elevada à potência do número de elementos na entrada.

Exemplo codigo exponencial:

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

<img src="/imgs/exponencial.png" alt="complexidade-exponencial" title="complexidade-exponencial" align="center" />