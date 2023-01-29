# New-library-system-design
Aplikacja systemu bibliotecznego, która to zapewnia kompleksowe usługi związane z podstawowymi czynnościami, które to może realizować zarówno użytkownik jak i również bibliotekarz. Aplikacja posiada własną bazę danych, w której to zainicjonowano pierwszych dwóch użytkowników. Dodatkowo dodano po jednej książce, wypożyczeniu oraz karze. System ten pozwala na podstawowe funkcjonowanie biblioteki, ale również posiada dużo możliwości rozwoju na przykład zaawansowane wyszukiwanie, szczegółowe dane na temat użytkownika,czy też rezerwacje książek. 

Poniżej przedstawiono któtką instrukcję waraz z niezbędnymi informacjami do uruchomienia aplikacji. 

## Wymagane biblioteki
W celu uruchomienia zainstaluj następujące bibioteki: 
- PyQt5
- datatime
- sqlite

## Sposób uruchomiena aplikacji
W konsoli należy wpisać następujący kod: 
```python
python -u ./main.py
```
## Dodatkowe informacje 

Aby zalogować się do systemu należy wpisać następujące początkowe loginy. 

Dla administratora:
- Login: admin
- Hasło: admin1

Dla użytkownika: 
- Login: user
- Hasło: user1 