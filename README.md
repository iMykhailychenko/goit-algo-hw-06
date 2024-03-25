# goit-algo-hw-06


## Завдання 1

Для вирішення завдання було обрано репрезентацію сполучень між основними містами Європи: Kyiv, Paris, Berlin, Rome, Madrid, London, Amsterdam, Prague, Vienna. Побудовано зважений граф, величини для кожного ребра представлені у вигляді відстані між містами.

![Graph](/docs/Graph.png)

## Завдання 2

- Пошук у глибину (DFS): методика полягає в тому, щоб почати з першого сусіднього вузла і проникнути якомога глибше в структуру графа, послідовно відвідуючи всі елементи. Такий підхід є ефективним для визначення маршруту між двома точками швидко та без зайвих зусиль. Однак, він може не завжди пропонувати оптимальне рішення.

- Пошук у ширину (BFS): цей метод включає огляд усіх безпосередніх сусідів поточного вузла перед тим, як перейти до їхніх сусідів, і так далі по ланцюжку. Він вимагає більше часу порівняно з DFS, але є ідеальним для задач, наприклад, знаходження найкоротшого шляху між точками.

**Результати тесту**

```
DFS order: ['Kyiv', 'Berlin', 'Vienna', 'Prague', 'Amsterdam', 'London', 'Paris', 'Madrid', 'Rome']
DFS distance: 4530

BFS order: ['Kyiv', 'Vienna', 'Prague', 'Berlin', 'Rome', 'Amsterdam', 'Paris', 'London', 'Madrid']
BFS distance: 2389
```

Шлях, знайдений за допомогою пошуку в глибину (DFS), може не бути найкоротшим між двома пунктами, оскільки він зосереджується на поглибленому дослідженні певних гілок перед поверненням назад. Метод пошуку в ширину (BFS) навпаки забезпечує визначення найкоротшого шляху, рівномірно оглядаючи сусідні станції на кожному рівні глибини. Підсумовуючи, хоча DFS може пропонувати коректні шляхи, які не є оптимальними за довжиною, BFS надійно виявляє найкоротший маршрут.


## Завдання 3

Ркзультати роботи алгоритму Дейкстри наведено в таблиці нижче. Як ми бачимо, найкраший результат буде в третьому варіанті (7707 км) 
|               |               |                 |                  |                  |                  |               |               |               |       |
|:--------------|:--------------|:----------------|:-----------------|:-----------------|:-----------------|:--------------|:--------------|:--------------|------:|
| Kyiv (0)      | Berlin (1292) | Prague (1389)   | Vienna (1514)    | Amsterdam (1869) | Paris (2170)     | London (2226) | Rome (2280)   | Madrid (3224) | 15964 |
| Paris (0)     | London (344)  | Amsterdam (701) | Berlin (878)     | Madrid (1054)    | Prague (1158)    | Vienna (1402) | Rome (1423)   | Kyiv (2170)   |  9130 |
| Berlin (0)    | Prague (280)  | Vienna (524)    | Amsterdam (577)  | Paris (878)      | London (934)     | Rome (1290)   | Kyiv (1292)   | Madrid (1932) |  7707 |
| Rome (0)      | Vienna (766)  | Prague (1017)   | Berlin (1290)    | Paris (1423)     | Amsterdam (1725) | London (1767) | Kyiv (2280)   | Madrid (2477) | 12745 |
| Madrid (0)    | Paris (1054)  | London (1398)   | Amsterdam (1755) | Berlin (1932)    | Prague (2212)    | Vienna (2456) | Rome (2477)   | Kyiv (3224)   | 16508 |
| London (0)    | Paris (344)   | Amsterdam (357) | Berlin (934)     | Prague (1065)    | Vienna (1316)    | Madrid (1398) | Rome (1767)   | Kyiv (2226)   |  9407 |
| Amsterdam (0) | London (357)  | Berlin (577)    | Paris (701)      | Prague (708)     | Vienna (959)     | Rome (1725)   | Madrid (1755) | Kyiv (1869)   |  8651 |
| Prague (0)    | Vienna (251)  | Berlin (280)    | Amsterdam (708)  | Rome (1017)      | London (1065)    | Paris (1158)  | Kyiv (1389)   | Madrid (2212) |  8080 |
| Vienna (0)    | Prague (251)  | Berlin (524)    | Rome (766)       | Amsterdam (959)  | London (1316)    | Paris (1402)  | Kyiv (1514)   | Madrid (2456) |  9188 |

