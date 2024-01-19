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

```python
def cubic_complexity_algorithm(n):
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result += 1
    return result
```

<img src="/imgs/exponencial.png" alt="complexidade-exponencial" title="complexidade-exponencial" align="center" />

<h3>10 - Vamos falar sobre complexidade fatorial?</h3>

A complexidade fatorial descreve um algoritmo cujo tempo de execução aumenta fatorialmente com o tamanho da entrada. Isso significa que o tempo de execução é proporcional ao fatorial do número de elementos na entrada.

```python
def permutations(arr):
    if len(arr) == 0:
        return [[]]
    else:
        total = []
        for i in range(len(arr)):
            remaining_elements = arr[:i] + arr[i+1:]
            sub_permutations = permutations(remaining_elements)
            for permutation in sub_permutations:
                total.append([arr[i]] + permutation)
        return total
```

<img src="/imgs/fatorial.png" alt="complexidade-fatorial" title="complexidade-fatorial" align="center" />

<h3>11 - Vamos comecar a falar sobre Big-O?</h3>

Big-O é uma notação matemática que descreve o comportamento de tempo de execução de um algoritmo em relação ao tamanho da entrada. Isso permite comparar algoritmos independentemente do hardware ou linguagem de programação usada para implementá-los.

Exemplo codigo Big-O - O(n):

```python
def sum_array(arr):
    total = 0
    for i in arr:
        total += i
    return total
```

<img src="/imgs/big-o-linear.png" alt="complexidade-big-o" title="complexidade-big-o" align="center" />

Exemplo codigo Big-O - O(1):

```python
def sum_first_two(arr):
    if len(arr) >= 2:
        return arr[0] + arr[1]
    else:
        return None
```

<img src="/imgs/big-o-constante.png" alt="complexidade-big-o" title="complexidade-big-o" align="center" />

Exemplo codigo Big-O - O(log n):

```python
def binary_search(arr, target):
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

<img src="/imgs/big-o-logaritmica.png" alt="complexidade-big-o" title="complexidade-big-o" align="center" />

Exemplo codigo Big-O - O(n^2):

```python
def sum_square_matrix(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        for j in range(n):
            total += matrix[i][j]
    return total
```

<img src="/imgs/big-o-quadratica.png" alt="complexidade-big-o" title="complexidade-big-o" align="center" />

Exemplo codigo Big-O - O(n^3):

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

<img src="/imgs/big-o-cubica.png" alt="complexidade-big-o" title="complexidade-big-o" align="center" />

Exemplo codigo Big-O - O(2^n):

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

<img src="/imgs/big-o-exponencial.png" alt="complexidade-big-o" title="complexidade-big-o" align="center" />

Exemplo codigo Big-O - O(n!):

```python
def permutations(arr):
    if len(arr) == 0:
        return [[]]
    else:
        total = []
        for i in range(len(arr)):
            remaining_elements = arr[:i] + arr[i+1:]
            sub_permutations = permutations(remaining_elements)
            for permutation in sub_permutations:
                total.append([arr[i]] + permutation)
        return total
```

<img src="/imgs/big-o-fatorial.png" alt="complexidade-big-o" title="complexidade-big-o" align="center" />

<h3>12 - Vamos falar sobre P e NP?</h3>

P e NP são classes de problemas em teoria da computação. Problemas em P podem ser resolvidos em tempo polinomial, enquanto problemas em NP podem ser verificados em tempo polinomial. A questão P = NP é uma das perguntas mais importantes em ciência da computação.

Exemplo codigo O(n^2) P:

```python
def is_valid_solution(board):
    # verify that each row, column, and 3x3 square contains the numbers 1-9
    for row in range(9):
        used_nums = set()
        for col in range(9):
            num = board[row][col]
            if num in used_nums:
                return False
            if num != 0:
                used_nums.add(num)

    # verify that each column contains the numbers 1-9
    for col in range(9):
        used_nums = set()
        for row in range(9):
            num = board[row][col]
            if num in used_nums:
                return False
            if num != 0:
                used_nums.add(num)

    # verify that each 3x3 square contains the numbers 1-9
    for i in range(3):
        for j in range(3):
            used_nums = set()
            for row in range(3):
                for col in range(3):
                    num = board[3*i + row][3*j + col]
                    if num in used_nums:
                        return False
                    if num != 0:
                        used_nums.add(num)
    return True
```

<h3>13 - Vamos falar sobre complexidade assintotica?</h3>

A complexidade assintótica descreve o comportamento do algoritmo quando a entrada aumenta para um tamanho infinito. Ela é representada por Big-O e é uma forma de descrever a complexidade de um algoritmo sem se preocupar com constantes e termos de baixa ordem.

Complexidade assintotica eh descrita por Big-O

Exemplo codigo O(n):

```python
def find_min_max(arr):
  n = len(arr)
  min_val = max_val = arr[0]
  for i in range(1, n):
    if arr[i] < min_val:
      min_val = arr[i]
    if arr[i] > max_val:
      max_val = arr[i]
  return min_val, max_val
```

```python
def best_min_max(arr):
  n = len(arr)
  min_val = arr[0]
  for i in range(1, n):
    if arr[i] < min_val:
      min_val = arr[i]

  for i in range(1, n):
    if arr[i] > min_val:
      max_val = arr[i]

  return min_val, max_val
```

```python
def find_min(arr):
  n = len(arr)
  min_val = arr[0]
  for i in range(1, n):
    if arr[i] < min_val:
      min_val = arr[i]
  return min_val

def find_max(arr):
  n = len(arr)
  max_val = arr[0]
  for i in range(1, n):
    if arr[i] > max_val:
      max_val = arr[i]
  return max_val

def find_min_max_best(arr):
  return find_min(arr), find_max(arr)
```

<img src="/imgs/assintotica.png" alt="complexidade-assintotica" title="complexidade-assintotica" align="center" />

<h3>14 - Vamos falar sobre escalabilidade?</h3>

A escalabilidade descreve a capacidade de um sistema de lidar com um aumento na carga de trabalho. Isso pode ser medido em termos de desempenho, tempo de resposta ou tempo de execução. A escalabilidade é importante para garantir que um sistema possa lidar com um aumento na carga de trabalho sem degradar o desempenho.

Duas perspectivas de escalabilidade:

1. Requisicoes com "entradas maiores"

2. Mais requisicoes

<img src="/imgs/escalabilidade.png" alt="escalabilidade" title="escalabilidade" align="center" />

Eventualmente uma saida "boa o suficiente", produzida em um tempo menor eh preferivel a saida "perfeita", produzida em mais tempo.

<img src="/imgs/escalabilidade-2.png" alt="escalabilidade-2" title="escalabilidade-2" align="center" />