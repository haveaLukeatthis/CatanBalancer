<h1 align="center">CatanBalancer</h1>

<p align="center">A small Python program that generates a <i>balanced</i> Catan board </p>

A Catan board should follow the following rules to be balanced:
1. No two brick🧱 or stone🪨 tiles next to one another
2. No three sheep🐑, wheat🌾 or wood🪵 tiles connected to each pther
3. No resource tiles close to their matching port
4. No two of the same number next to each other
5. No sixes or eights next to each other
6. No two of same number on the same resource
7. No sixes or eights on the same resource

This program generates the board tiles randomly, checks if it follows the rules and continues if the board breaks any of the rules.
If it found a board that follows the rules it generates the numbers on the tiles until they follow the rules too.

It takes an average of 128 attempts to generate balanced tiles and an average of 453 attempts, but it usually takes less than a second to generate a balanced board.


See the Video:
https://youtu.be/N11TCOPFLfo
