# SecureCICD

## CICD docs
Proces CICD jest zaprojektowany w ten sposób, aby przeprowadzić testy jednostkowe oraz bezpieczeństwa i, w zależności od ich powodzenia, zbudować obraz dockerowy aplikacji. Gwoli dbania o jakość kodu, został dodany również job dot. zgodności ze standardem PEP8. Wszystkie testy są wykonywane na obrazie _ubuntu-latest_ dla Pythona w wersji 3.10.

Podatności jakie zostały wprowadzone w aplikacji to:
- hardcoded secret - plik _app.py_, linia 3
- eval injection - plik _app.py_, linia 11 (https://owasp.org/www-community/attacks/Direct_Dynamic_Code_Evaluation_Eval%20Injection)



### Wyzwalanie
Zadania CICD są uruchamiane za każdym razem, kiedy:

- zmiany wypychane są do gałęzi main
- tworzony jest Pull Request do gałęzi main

### Build
Budowana jest aplikacja webowa bazująca na FastAPI oraz silniku uvicorn. Instalowane są zależności oraz uruchamiane są testy jednostkowe.

### Safety-SCA
Uruchamiane jest oprogramowanie _safety_, będące wrapperem OWASP Dependency Check dla języka Python. Instalowane są wszystkie zależności, a następnie skanowane jest wirtualne środowiska interpretera python, nie natomiast sam plik _requirements.txt_. Ma to tę zaletę, że skanujemy wszystkie faktycznie instalowane zależności, również zależności naszych zależności.

Dodaliśmy tu instrukcję warunkową:
```bash
- if: steps.scan-1.outcome != 'failure'
  run: echo 'Safety failed to run, but the next step in the pipeline continued.' && exit 1
```

Powodem jest znaczna ilość podatności znajdowana przez oprogramowanie, której nie mogliśmy zniwelować tak, aby zachowane były podstawowe funkcje podatnej aplikacji. Efektem jest stosowny monit na liście zadań o znalezionych podatnościach, natomiast cały proces może kontynuować (aby spełnić wymogi zadania 2).

### Bandit-SAST
Bandit inicjuje testy, których wyniki mówią o:
- Severity - istotność znalezionej podatności,
- Confidentiality - pewność jaką ma narzędzie, że wskazany fragment kodu jest podatny.

Nasze ustawienia łapią każdą podatność (nawet LOW) z poziomem Confidentiality LOW. Jest to spowodowane faktem, że podatność hardcoded secret jest zgłaszana z poziomem LOW, ponieważ na ogół generuje ona sporo wyników fałszywie pozytywnych (np. przy sprawdzaniu czy zmienna password == "admin"). Z tego względu musieliśmy obniżyć próg zgłaszania podatności.

Te podatności są powodem, dla którego PR z zadania 2 się blokuje, a obraz dockerowy nie jest budowany.

### ZAP-DAST
Wykorzystane zostało narzędzie ZAP od OWASP, które dla wskazanego endpointa aplikacji webowej wykonuje dynamiczną analizę. Aplikacja nie oferuje w zasadzie żadnych funkcji, toteż podatności tutaj nie występują. Rezultaty tego skanu są zamieszczane w Issues projektu.

### Code-PEP-Format
Krótkie sprawdzenie polegające na zweryfikowaniu wszystkich plików z rozszerzeniem .py czy kod zawarty w nich spełnia zasady definiowane przez format PEP.

### final-build
Zadanie budujące dockerowy obraz aplikacji z tagiem beta.