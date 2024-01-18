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