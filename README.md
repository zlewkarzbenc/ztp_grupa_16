# Wizualizacja poziomu zanieczyszczeń (PM2.5)

Projekt ma na celu  wizualizację danych dotyczących poziomu zanieczyszczenia powietrza PM2.5, 
aby ułatwić analizę danych oraz przedstawić zmiany stężenia pyłu w czasie w polskich miastach. 

----------

#### Repozytorium zawiera:
* Pliki z kodem źródłowym:
  * `load_data.py` - moduł odpowiedzialny za wczytywanie i czyszczenie danych
  * `compute_averages.py` - moduł, który oblicza średnie miesięczne dla miast zawartych w danych wejściowych
  * `visualizations.py` - moduł generujący wykresy i wizualizacje danych
  * `main.ipynb` - notebook, który pokazuje użycie wszystkich modułów
* Pliki danych:
  * `all_data.csv` - surowe dane wejściowe używane w późniejszych obliczeniach i ogólnej analizie
  * `monthly_average.csv` - miesięczne średnie stężenia PM2.5 w miastach, które są zawarte w pliku all_data.csv

---------

#### Jak zainstalować i uruchomić projekt?

1. Sklonuj repozytorium
> git clone https://github.com/zlewkarzbenc/ztp_grupa_16

2. Utwórz wirtualne środowisko (zalecane)
> python -m venv venv
> <br> source ./venv/bin/activate

3. Zainstaluj potrzebne biblioteki
> pip install -r requirements.txt

4. Uruchom główny notebook
> jupyter notebook

---------

#### Źródła danych

[Główny Inspektorat Ochrony Środowiska – powietrze.gios.gov.pl](https://powietrze.gios.gov.pl/pjp/archives)

---------

### Autorzy: Aleksander Janowiak, Dominika Aniszewska