# Game-Zelen-Stas

# Карты
  Базовые карты:<br />
  +   5 карт цены. <br />
  +   5 карт рынка(баклажан, кукуруза, помидоры, брокколи, морковь).<br />
  +   карты овощей, на каждой изображены 3 случайных зелень.<br />
  Специальные карты:<br />
+    Солнышко - добавьте ещё одну карту овощей в дополнение к обычному ряду. В этом раунде 2 последние карты меняют цену овощей на рынке<br />
+    Тайфунчик - в этом раунде не будет обрушения. Все карты овощей, которые дошли до самого высшего деления и должны перескочить на низшее, остаются на высшем делении.<br />
# Раздача
+  2-6 игроков.<br />
+  Выкладываются карты цены.<br />
+  Карты рынка кладутся поверх карт цены случайно.<br />
#Условие победы<br />
  Набрать больше всех очков.<br />


# Комплектность
  Игра состоит из 60 карт:<br />
  
+  карты рынка - 5 шт.<br />
+  карты цены - 5 шт.<br />
+  карты овощей - 48 шт.<br />
+  особые карты - 2 шт.<br />
# Правила игры
Партия длится 6 раундов.<br />
В начале раунда берутся карты овощей в количестве +1 кол-ва игроков.<br />
Начиная с первого игрока и далее по часовой стрелке каждый игрок выбирает 1 карту из раскрытых и кладёт перед собой лицевой стороной вниз.<br />
Первым игроком станет тот, кто последним покупал в магазине зелень.<br />
Оставшаяся невыбранная карта указывает, какие овощи подорожают в этом раунде. За каждый символ какого-либо овоща на этой карте передвиньте его карту рынка на 1 деление вверх.<br /> Если вы должны передвинуть её выше самого верхнего деления, то овощ обрушивается в цене и его карта рынка перемещается на самое нижнее деление.<br />
Последнюю карту этого раунда положите в сброс рядом с колодой лицевой стороной вниз, а остальные перемешайте и выложите, как в начале этого раунда.<br /> Теперь первым игроком становится игрок слева от вас. Он начинает новый раунд и будет первым выбирать карту овоща из ряда.<br />
# Подсчет очков
По истечению всех раундов игроки считают кол-во овощей у себя на руках.<br />
Итоговое кол-во очков считается как сумма произведений овощей на их стоимость.<br />

# Пример текстового интерфейса игры<br />
Играют Player и AI.
Table






#Формат save-файла <br />
```
{
  "Price": "E - 0; C - 1; B - 2; T - 3;",
  "Table": [
    1) B - 1; C - 2
    2) T- 1; E - 2
    3) B - 1; C - 2
  ],
  "current_player_index": 1,
  "players": [
  {
      "name": "Player",
      "hand": "B - 1; C - 2; E - 0;  T - 0;"
      "is_human": true
    },
    {
      "name": "AI",
      "hand": "T - 1; E - 2; C - 0; B - 0",
      "is_human": false
    }
  ]
}
