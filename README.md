### Genetic Algorithm

Example:

```shell
$ python3 ga.py \
  --data '[(0, 1), (1, 0), (2, 0), (11, 10), (22, 23), (33, 35), (15, 13), (20, 3)]' \
  --population-size 800 \
  --num-iterations 100 \
  --seed 33
The best path: [(1, 0), (0, 1), (11, 10), (15, 13), (22, 23), (33, 35), (20, 3), (2, 0)]
The fitness value: 102.90037984699414
```

Figure:

![Result](./img/result.png)