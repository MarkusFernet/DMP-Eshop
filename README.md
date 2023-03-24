# DMP - Eshop

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="" alt="Logo" width="80" height="80">
  </a>
</div>
<br />

# Version 1.0:
- Způsoby dopravy před platbou
  - Možnost měnit a přidávat způsoby dopravy v adminu
  - Automatické vybrání dopravy při načtení stránky (Nelze nevybrat žádnou dopravu)
  - Uložení výběru dopravy do sessions (Není třeba vybírat znovu způsob dopravy, když se rozhodnete přidat další produkt. Předešlý výber se uloží a zvolí sám)
- Vybrání adresy před platbou
  - Lze přidat novou adresu jen když žádnou nemáte
  - Můžete změnit adresu
  - Možnost si vybrat z více adres, kterou chcete použít
  - Po úpravě/přidání/vybrání adresy přesměrováno na předešlou stránku (Pokladna/účet)
  - Zobrazení chyby při nevybrání adresy
- Placení za pomocí PayPal
  - Semi-working
- Přidání orders, neboli historie provedených plateb zákazníka

# Version 0.3:
- Přidání wishlistu

# Version 0.2:
- Aktivace zasílání emailů
- Aktualizace košíku po odstranění všech produktů
- Správné počítání celkové ceny
- Vylepšení databáze produktů
- Přidání sledování plateb
- Možnost přidat více obrázků k produktům
- Vylepšení vzhledu stránek
- Přeložení poloviny stránek
- Zlepšení přehlednosti kódu
- Vzhled potvrzovacího emailu
- Možnost přidávání více adres
- Změna vzhledu účtu
- Odstranění username

# Version 0.1:
- Schopnost vytvářet produkty a kategorie v admin sekci
- Základní responsivita
- Přidávání, odtraňování a updatování produktů do košíku pomocí sessions
- Registrace, přihlašování, ohlašování, úprava a smazání účtů 
- Reset hesla účtů a neaktivované fungující zasíláni emailů
- Fungující nahrání na hosting <a href="https://web-production-c8c7.up.railway.app/">Railway.app</a>

### To do:
- Placení
- Slevy?
- Rozklikávat obrázky u produktu
- Graficky přidat čáru nad TOTAL PAY pro lepší přehlednost
- Změnit POČET pole na vypisovací z vybíracího
- Změnit způsob přidávání do košíku
- Přeložení košíku, účtů a errorů
- Přeložit reset status, reset confirm, register email confirm a activation invalid a zkontrolovat (zajisit pravidelnost oproti login, register)
- Predelat reset confirm cely vzhled
- Zvětšit možnost změnění účtu
- Vzhled reset hesla emailu -> predelani views na reset hesla
- Prázdný košík -> doporučení?
- Mezi krok u mazani uctu
- MEZERA MEZI BTN A FORM
- status info pridat do dashboard kdyz neni zadna historie objednavek
- Pocitani s regular_price/discounted pri pridani do kosiku
- sjednotit sirku a styly vsech forms
- spravit možnost změn informací uctu
- Po odstraneni produktu z nabidky, stale viditelny skoro vsude
