# Порівняння алгоритмів для видачі решти: жадібний алгоритм та алгоритм динамічного програмування

### Огляд

Цей проєкт містить реалізацію двох алгоритмів для задачі видачі решти із заданими номіналами монет: жадібного алгоритму та 
алгоритму динамічного програмування (АДП). Жадібний алгоритм використовує підхід, де пріоритет надається найбільшому доступному номіналу монет, 
тоді як АДП знаходить оптимальне рішення для мінімізації загальної кількості монет.
Метою є оцінка ефективності кожного алгоритму за кількістю монет та часом виконання, особливо для великих значень суми.

### Методика

- **Жадібний алгоритм**: вибирає найбільший можливий номінал для кожної операції видачі решти.
- **Алгоритм динамічного програмування**: обчислює мінімальну кількість монет, щоб точно досягти необхідної суми.

### Результати експериментів

Наведені нижче результати показують загальну кількість монет і час виконання кожного алгоритму для різних значень суми.
У підсумок не включені дані зі стандартним набором монет `[50, 25, 10, 5, 2, 1]`, бо в усіх випадках обидва алгоритми видавали однакову кількість монет
і різнилися лише за часом виконання на користь жадібного алгоритму, у випадках з великими сумами - навіть у більше ста тисяч разів!
Обидва алгоритми зазвичай забезпечують однакову точну суму, але виявлені випадки, де жадібний алгоритм не досяг точної суми, що призвело до відхилень у його точності.

#### Приклад 1: сума 8573, номінали [25, 10, 4, 2]

- **Жадібний алгоритм**: `{25: 342, 10: 2, 2: 1}`, Загальна кількість монет: 345, Час виконання: 0.000028 сек
  - Розрахована сума: $\(25 \times 342 + 10 \times 2 + 2 \times 1 = 8572\)$ - не досягнуто потрібної суми.
- **Алгоритм динамічного програмування**: `{4: 2, 10: 4, 25: 341}`, Загальна кількість монет: 347, Час виконання: 0.007691 сек
  - Розрахована сума: точно 8573

#### Приклад 2: сума 94857, номінали [25, 10, 4, 2]

- **Жадібний алгоритм**: `{25: 3794, 4: 1, 2: 1}`, Загальна кількість монет: 3796, Час виконання: 0.000024 сек
  - Розрахована сума: $\(25 \times 3794 + 4 \times 1 + 2 \times 1 = 94856\)$ - не досягнуто потрібної суми.
- **Алгоритм динамічного програмування**: `{2: 1, 10: 3, 25: 3793}`, Загальна кількість монет: 3797, Час виконання: 0.058377 сек
  - Розрахована сума: точно 94857

### Висновки

- **Точність**: АДП гарантує точне досягнення цільової суми за рахунок оптимальної комбінації монет, тоді як жадібний алгоритм інколи не забезпечує необхідної точності, як у прикладах вище.
- **Продуктивність**: Жадібний алгоритм працює швидше, особливо для великих значень, оскільки він не проводить повного пошуку. Водночас АДП вимагає більше часу на обчислення, але забезпечує
мінімальну кількість монет і точне значення суми. 
- **Отже**: Жадібний алгоритм підходить для простих випадків із стандартними номіналами монет, але для ситуацій, де необхідна точність або де доступні номінали не гарантують оптимального результату, варто застосовувати АДП.
