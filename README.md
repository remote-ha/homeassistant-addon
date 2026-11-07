# Remote Home Assistant

[English](#english) · [Polski](#polski) · [Deutsch](#deutsch) · [Nederlands](#nederlands) · [Français](#français) · [Svenska](#svenska)

## English

New accounts include **30 days of Pro free**, with 2 installations and no card. After the trial, the account switches to Free with 1 remotely accessible installation. You can then purchase Pro; the trial never triggers an automatic charge.

**Moving from the previous repository:** installed apps do not move automatically between repositories. Install the app from this repository. For an existing Remote HA installation, revoke its old device, generate a new pairing token and pair the new app. Revocation interrupts remote access; the installation address and access rules stay saved. Do not uninstall the previous app until you have backed up any app data you need.

A secure way back to your Home Assistant. Connect through an encrypted tunnel, choose who gets through, and keep control of your home.

### Register and install

[Install with AI (in Polish)](./INSTALL_WITH_AI.md)

Create your account at [remote-ha.com/register](https://remote-ha.com/en/register), verify your email, and open the [dashboard](https://remote-ha.com/en/dashboard). Under **Add a home**, choose a name and an available address, then select **Add installation**.

Requires **Home Assistant OS**, an administrator account and an **aarch64 (ARM64)** or **amd64 (x86-64)** device. Home Assistant Container does not include the app store. Before Home Assistant 2026.2, **Apps** was called **Add-ons**.

**Install with a button:** [Add the Remote HA repository to Home Assistant](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fremote-ha%2Fhomeassistant-addon). Choose your Home Assistant instance, confirm adding the repository, then find **Remote Home Assistant** under **Settings → Apps → Install app** and select **Install**.

**Add the repository manually:**

1. Open **Settings → Apps → Install app**.
2. Open the **⋮** menu at the top right and choose **Repositories**.
3. Paste `https://github.com/remote-ha/homeassistant-addon` and select **Add**.
4. Close the dialog, find **Remote Home Assistant** in **Remote Home Assistant Apps**, and select **Install**. Refresh the store or select **Check for updates** if it does not appear.

The app store downloads the app from the [public GitHub repository](https://github.com/remote-ha/homeassistant-addon); no ZIP download or manual file copying is needed.

**HACS:** HACS does not install Home Assistant apps (formerly add-ons). This repository is an app, not a HACS integration. Use the app-store methods above. See the [HACS FAQ](https://www.hacs.xyz/docs/faq/addons/) and the [full installation guide](https://remote-ha.com/en/docs).

After signing in, follow the setup steps in the dashboard. Select a home to see its overview, access firewall, activity and connection settings. Your subscription is under **Account & billing**. The language and appearance controls are in the top bar; on small screens, appearance is also in the menu.

### Pair your home

Install the app before generating a pairing token. In the dashboard, select **Pairing token** on your installation. In Home Assistant, open **Settings → Apps → Remote Home Assistant → Configuration**, paste the token into **Token** (`pairing_token` in the YAML editor) and **Save**. On **Info**, select **Start**, or **Restart** if already running. Enable **Start on boot**. Wait for **Connected** in the dashboard, open the installation address and use your usual Home Assistant login.

[remote-ha.com](https://remote-ha.com)

## Polski

Nowe konto otrzymuje **30 dni Pro za darmo**, z 2 instalacjami i bez karty. Po próbie konto przechodzi na Free ze zdalnym dostępem do 1 instalacji. Możesz wtedy wykupić Pro; próba nie powoduje automatycznego pobrania opłaty.

**Przejście ze starego repozytorium:** zainstalowana aplikacja nie przenosi się automatycznie do nowego repozytorium. Zainstaluj aplikację z tego repozytorium. Przy istniejącej instalacji Remote HA cofnij dostęp staremu urządzeniu, utwórz nowy token parowania i sparuj nową aplikację. Cofnięcie dostępu przerywa zdalne połączenie; adres instalacji i reguły dostępu pozostają zapisane. Przed odinstalowaniem poprzedniej aplikacji wykonaj kopię jej potrzebnych danych.

Bezpieczny dostęp do Twojego Home Assistanta z dowolnego miejsca. Łącz się przez szyfrowany tunel, decyduj, kogo wpuszczasz, i zachowaj kontrolę nad swoim domem.

### Rejestracja i instalacja

[Zainstaluj z pomocą AI](./INSTALL_WITH_AI.md)

Utwórz konto na [remote-ha.com/register](https://remote-ha.com/pl/register), potwierdź adres e-mail i otwórz [panel](https://remote-ha.com/pl/dashboard). W sekcji **Dodaj dom** wpisz nazwę, wybierz dostępny adres i kliknij **Dodaj instalację**.

Wymagane są **Home Assistant OS**, konto administratora i urządzenie **aarch64 (ARM64)** lub **amd64 (x86-64)**. Home Assistant Container nie zawiera sklepu aplikacji. Przed wersją Home Assistant 2026.2 menu **Aplikacje** nosiło nazwę **Dodatki**.

**Instalacja przyciskiem:** [Dodaj repozytorium Remote HA do Home Assistant](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fremote-ha%2Fhomeassistant-addon). Wybierz swoją instancję Home Assistant i potwierdź dodanie repozytorium. Następnie w **Ustawienia → Aplikacje → Zainstaluj aplikację** znajdź **Remote Home Assistant** i wybierz **Zainstaluj**.

**Ręczne dodanie repozytorium:**

1. Otwórz **Ustawienia → Aplikacje → Zainstaluj aplikację**.
2. W menu **⋮** w prawym górnym rogu wybierz **Repozytoria**.
3. Wklej `https://github.com/remote-ha/homeassistant-addon` i wybierz **Dodaj**.
4. Zamknij okno, znajdź **Remote Home Assistant** w sekcji **Remote Home Assistant Apps** i kliknij **Zainstaluj**. Jeśli aplikacji nie widać, odśwież sklep lub wybierz **Sprawdź aktualizacje**.

Sklep pobiera aplikację z [publicznego repozytorium GitHub](https://github.com/remote-ha/homeassistant-addon). Nie trzeba pobierać pliku ZIP ani ręcznie kopiować plików.

**HACS:** HACS nie instaluje aplikacji Home Assistant (dawniej dodatków). To repozytorium zawiera aplikację, a nie integrację HACS. Użyj jednej z metod instalacji przez sklep opisanych powyżej. Zobacz [wyjaśnienie HACS](https://www.hacs.xyz/docs/faq/addons/) oraz [pełną instrukcję instalacji](https://remote-ha.com/pl/docs).

Po zalogowaniu przejdź przez kroki konfiguracji w panelu. Wybierz dom, aby zobaczyć przegląd, zaporę dostępu, aktywność i ustawienia połączenia. Abonament znajdziesz w sekcji **Konto i abonament**. Język i wygląd zmienisz w górnym pasku; na małych ekranach wygląd jest też w menu.

### Parowanie z kontem

Najpierw zainstaluj aplikację, a następnie w panelu przy swojej instalacji kliknij **Token parowania**. W Home Assistant otwórz **Ustawienia → Aplikacje → Remote Home Assistant → Konfiguracja**, wklej token w pole **Token** (`pairing_token` w edytorze YAML) i zapisz. Na karcie informacji wybierz **Uruchom** lub **Uruchom ponownie**, jeśli aplikacja już działa. Włącz uruchamianie przy starcie systemu. Poczekaj na status **Połączono** w panelu, otwórz adres instalacji i zaloguj się swoim kontem Home Assistant.

[remote-ha.com](https://remote-ha.com)

## Deutsch

Neue Konten erhalten **30 Tage Pro kostenlos**, mit 2 Installationen und ohne Karte. Danach wechselt das Konto zu Free mit Fernzugriff auf 1 Installation. Anschließend kannst du Pro abonnieren; der Testzeitraum führt zu keiner automatischen Abbuchung.

**Wechsel vom bisherigen Repository:** installierte Apps wechseln nicht automatisch das Repository. Installiere die App aus diesem Repository. Entziehe bei einer vorhandenen Remote-HA-Installation dem alten Gerät den Zugriff, erstelle ein neues Kopplungstoken und kopple die neue App. Dabei wird die Fernverbindung unterbrochen; Adresse und Zugriffsregeln bleiben gespeichert. Sichere benötigte App-Daten, bevor du die bisherige App deinstallierst.

Ein sicherer Weg zurück zu deinem Home Assistant. Verbinde dich über einen verschlüsselten Tunnel, entscheide, wer Zugang erhält, und behalte die Kontrolle über dein Zuhause.

### Konto erstellen und installieren

[Mit KI installieren (auf Polnisch)](./INSTALL_WITH_AI.md)

Erstelle dein Konto auf [remote-ha.com/register](https://remote-ha.com/de/register), bestätige deine E-Mail-Adresse und öffne das [Dashboard](https://remote-ha.com/de/dashboard). Gib unter **Zuhause hinzufügen** einen Namen ein, wähle eine verfügbare Adresse und klicke auf **Installation hinzufügen**.

Du benötigst **Home Assistant OS**, ein Administratorkonto und ein Gerät mit **aarch64 (ARM64)** oder **amd64 (x86-64)**. Home Assistant Container enthält keinen App-Store. Vor Home Assistant 2026.2 hieß **Apps** noch **Add-ons**.

**Installation per Schaltfläche:** [Remote-HA-Repository zu Home Assistant hinzufügen](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fremote-ha%2Fhomeassistant-addon). Wähle deine Home-Assistant-Instanz, bestätige das Repository und suche unter **Einstellungen → Apps → App installieren** nach **Remote Home Assistant**. Wähle **Installieren**.

**Repository manuell hinzufügen:**

1. Öffne **Einstellungen → Apps → App installieren**.
2. Wähle im Menü **⋮** oben rechts **Repositories**.
3. Füge `https://github.com/remote-ha/homeassistant-addon` ein und wähle **Hinzufügen**.
4. Schließe den Dialog, suche **Remote Home Assistant** unter **Remote Home Assistant Apps** und wähle **Installieren**. Aktualisiere die Seite oder suche im Store nach Updates, falls die App fehlt.

Der App-Store lädt die App aus dem [öffentlichen GitHub-Repository](https://github.com/remote-ha/homeassistant-addon) herunter. Du musst keine ZIP-Datei herunterladen oder Dateien manuell kopieren.

**HACS:** HACS installiert keine Home-Assistant-Apps (früher Add-ons). Dieses Repository enthält eine App und keine HACS-Integration. Verwende die oben beschriebenen Methoden im App-Store. Siehe die [HACS-FAQ](https://www.hacs.xyz/docs/faq/addons/) und die [vollständige Installationsanleitung](https://remote-ha.com/de/docs).

Folge nach dem Anmelden den Einrichtungsschritten im Dashboard. Wähle ein Zuhause aus, um Übersicht, Zugriffsfirewall, Aktivitäten und Verbindungseinstellungen zu öffnen. Dein Abonnement findest du unter **Konto & Abonnement**. Sprache und Darstellung lassen sich in der oberen Leiste ändern; auf kleinen Bildschirmen ist die Darstellung auch im Menü verfügbar.

### Dein Zuhause koppeln

Installiere die App, bevor du einen Token erzeugst. Wähle im Dashboard bei deiner Installation **Kopplungstoken**. Öffne in Home Assistant **Einstellungen → Apps → Remote Home Assistant → Konfiguration**, füge den Token unter **Token** ein (`pairing_token` im YAML-Editor) und speichere. Wähle auf der Infoseite **Starten** oder **Neu starten**, falls die App bereits läuft. Aktiviere den Start beim Systemstart. Warte im Dashboard auf **Verbunden**, öffne die Adresse deiner Installation und melde dich mit deinem Home-Assistant-Konto an.

[remote-ha.com](https://remote-ha.com)

## Nederlands

Nieuwe accounts krijgen **30 dagen gratis Pro**, met 2 installaties en zonder betaalkaart. Daarna gaat het account naar Free met toegang op afstand tot 1 installatie. Je kunt dan Pro nemen; de proefperiode leidt nooit tot een automatische afschrijving.

**Overstappen van de vorige repository:** geïnstalleerde apps verhuizen niet automatisch. Installeer de app vanuit deze repository. Trek bij een bestaande Remote HA-installatie de toegang van het oude apparaat in, maak een nieuw koppeltoken en koppel de nieuwe app. Dit onderbreekt de verbinding op afstand; het installatieadres en de toegangsregels blijven bewaard. Maak een back-up van benodigde appgegevens voordat je de vorige app verwijdert.

Een veilige weg terug naar je Home Assistant. Maak verbinding via een versleutelde tunnel, bepaal wie toegang krijgt en houd de controle over je huis.

### Registreren en installeren

[Installeren met AI (in het Pools)](./INSTALL_WITH_AI.md)

Maak je account aan op [remote-ha.com/register](https://remote-ha.com/nl/register), bevestig je e-mailadres en open het [dashboard](https://remote-ha.com/nl/dashboard). Vul bij **Huis toevoegen** een naam in, kies een beschikbaar adres en klik op **Installatie toevoegen**.

Je hebt **Home Assistant OS**, een beheerdersaccount en een apparaat met **aarch64 (ARM64)** of **amd64 (x86-64)** nodig. Home Assistant Container bevat geen appwinkel. Vóór Home Assistant 2026.2 heette **Apps** nog **Add-ons**.

**Installeren met een knop:** [Voeg de Remote HA-repository toe aan Home Assistant](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fremote-ha%2Fhomeassistant-addon). Kies je Home Assistant-instantie, bevestig de repository en zoek **Remote Home Assistant** via **Instellingen → Apps → App installeren**. Kies **Installeren**.

**De repository handmatig toevoegen:**

1. Open **Instellingen → Apps → App installeren**.
2. Kies rechtsboven in het menu **⋮** voor **Repositories**.
3. Plak `https://github.com/remote-ha/homeassistant-addon` en kies **Toevoegen**.
4. Sluit het venster, zoek **Remote Home Assistant** onder **Remote Home Assistant Apps** en kies **Installeren**. Vernieuw de winkel of controleer op updates als de app ontbreekt.

De appwinkel downloadt de app uit de [openbare GitHub-repository](https://github.com/remote-ha/homeassistant-addon). Je hoeft geen ZIP-bestand te downloaden of bestanden handmatig te kopiëren.

**HACS:** HACS installeert geen Home Assistant-apps (voorheen add-ons). Deze repository bevat een app, geen HACS-integratie. Gebruik de bovenstaande methoden via de appwinkel. Zie de [HACS-FAQ](https://www.hacs.xyz/docs/faq/addons/) en de [volledige installatiehandleiding](https://remote-ha.com/nl/docs).

Volg na het aanmelden de stappen in het dashboard. Selecteer een huis om het overzicht, de toegangsfirewall, activiteit en verbindingsinstellingen te bekijken. Je abonnement staat onder **Account en abonnement**. Taal en weergave wijzig je in de bovenste balk; op kleine schermen staat weergave ook in het menu.

### Je huis koppelen

Installeer de app voordat je een token aanmaakt. Kies in het dashboard **Koppeltoken** bij je installatie. Open in Home Assistant **Instellingen → Apps → Remote Home Assistant → Configuratie**, plak het token in **Token** (`pairing_token` in de YAML-editor) en sla op. Kies op de informatiepagina **Starten** of **Herstarten** als de app al actief is. Schakel starten bij het opstarten in. Wacht op **Verbonden** in het dashboard, open het installatieadres en meld je aan met je Home Assistant-account.

[remote-ha.com](https://remote-ha.com)

## Français

Les nouveaux comptes bénéficient de **30 jours de Pro gratuits**, pour 2 installations et sans carte bancaire. Le compte passe ensuite à Free avec un accès à distance à 1 installation. Vous pouvez alors souscrire à Pro ; l’essai ne déclenche aucun prélèvement automatique.

**Migration depuis l’ancien dépôt :** les applications installées ne changent pas automatiquement de dépôt. Installez l’application depuis ce dépôt. Pour une installation Remote HA existante, révoquez l’ancien appareil, créez un nouveau jeton et associez la nouvelle application. La connexion à distance est interrompue ; l’adresse et les règles d’accès sont conservées. Sauvegardez les données nécessaires avant de désinstaller l’ancienne application.

Retrouvez votre Home Assistant en toute sécurité. Connectez-vous via un tunnel chiffré, choisissez qui peut y accéder et gardez le contrôle de votre maison.

### Créer un compte et installer

[Installer avec l’IA (en polonais)](./INSTALL_WITH_AI.md)

Créez votre compte sur [remote-ha.com/register](https://remote-ha.com/fr/register), confirmez votre adresse e-mail et ouvrez le [tableau de bord](https://remote-ha.com/fr/dashboard). Dans **Ajouter une maison**, saisissez un nom, choisissez une adresse disponible et cliquez sur **Ajouter une installation**.

Vous devez disposer de **Home Assistant OS**, d’un compte administrateur et d’un appareil **aarch64 (ARM64)** ou **amd64 (x86-64)**. Home Assistant Container ne comprend pas de boutique d’applications. Avant Home Assistant 2026.2, les **Apps** s’appelaient **Add-ons**.

**Installation avec un bouton :** [Ajouter le dépôt Remote HA à Home Assistant](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fremote-ha%2Fhomeassistant-addon). Choisissez votre instance Home Assistant, confirmez l’ajout du dépôt, puis recherchez **Remote Home Assistant** dans **Paramètres → Applications → Installer une application** et sélectionnez **Installer**.

**Ajouter le dépôt manuellement :**

1. Ouvrez **Paramètres → Applications → Installer une application**.
2. Dans le menu **⋮** en haut à droite, sélectionnez **Dépôts**.
3. Collez `https://github.com/remote-ha/homeassistant-addon` et sélectionnez **Ajouter**.
4. Fermez la fenêtre, recherchez **Remote Home Assistant** dans **Remote Home Assistant Apps** et sélectionnez **Installer**. Actualisez la boutique ou recherchez les mises à jour si l’application n’apparaît pas.

La boutique télécharge l’application depuis le [dépôt GitHub public](https://github.com/remote-ha/homeassistant-addon). Aucun téléchargement ZIP ni copie manuelle de fichiers n’est nécessaire.

**HACS :** HACS n’installe pas les applications Home Assistant (anciennement add-ons). Ce dépôt contient une application et non une intégration HACS. Utilisez les méthodes décrites ci-dessus dans la boutique. Consultez la [FAQ HACS](https://www.hacs.xyz/docs/faq/addons/) et le [guide d’installation complet](https://remote-ha.com/fr/docs).

Après la connexion, suivez les étapes de configuration dans le tableau de bord. Sélectionnez une maison pour consulter sa vue d’ensemble, son pare-feu d’accès, son activité et ses paramètres de connexion. Votre abonnement se trouve dans **Compte et abonnement**. La langue et l’apparence se changent dans la barre supérieure ; sur petit écran, l’apparence est aussi accessible dans le menu.

### Appairer votre maison

Installez l’application avant de générer un jeton. Dans le tableau de bord, sélectionnez **Jeton d’appairage** pour votre installation. Dans Home Assistant, ouvrez **Paramètres → Applications → Remote Home Assistant → Configuration**, collez le jeton dans **Jeton** (`pairing_token` dans l’éditeur YAML) et enregistrez. Sur la page d’informations, sélectionnez **Démarrer**, ou **Redémarrer** si l’application fonctionne déjà. Activez le démarrage automatique. Attendez le statut **Connecté** dans le tableau de bord, ouvrez l’adresse de l’installation et connectez-vous avec votre compte Home Assistant.

[remote-ha.com](https://remote-ha.com)

## Svenska

Nya konton får **30 dagar gratis Pro**, med 2 installationer och utan kort. Därefter går kontot över till Free med fjärråtkomst till 1 installation. Du kan då teckna Pro; provperioden leder aldrig till automatisk debitering.

**Byte från det tidigare arkivet:** installerade appar flyttas inte automatiskt. Installera appen från det här arkivet. För en befintlig Remote HA-installation återkallar du den gamla enhetens åtkomst, skapar en ny parkopplingstoken och parkopplar den nya appen. Fjärranslutningen avbryts då, men installationsadressen och åtkomstreglerna sparas. Säkerhetskopiera de appdata du behöver innan du avinstallerar den tidigare appen.

Säker åtkomst till din Home Assistant, var du än är. Anslut via en krypterad tunnel, välj vem som får åtkomst och behåll kontrollen över ditt hem.

### Skapa ett konto och installera

[Installera med AI (på polska)](./INSTALL_WITH_AI.md)

Skapa ditt konto på [remote-ha.com/register](https://remote-ha.com/sv/register), verifiera din e-postadress och öppna [kontrollpanelen](https://remote-ha.com/sv/dashboard). Under **Lägg till ett hem** anger du ett namn, väljer en ledig adress och klickar på **Lägg till installation**.

Du behöver **Home Assistant OS**, ett administratörskonto och en enhet med **aarch64 (ARM64)** eller **amd64 (x86-64)**. Home Assistant Container innehåller ingen appbutik. Före Home Assistant 2026.2 hette **Appar** i stället **Tillägg**.

**Installera med en knapp:** [Lägg till Remote HA:s arkiv i Home Assistant](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fremote-ha%2Fhomeassistant-addon). Välj din Home Assistant-instans, bekräfta att arkivet ska läggas till och leta sedan upp **Remote Home Assistant** under **Inställningar → Appar → Installera app**. Välj **Installera**.

**Lägg till arkivet manuellt:**

1. Öppna **Inställningar → Appar → Installera app**.
2. Öppna menyn **⋮** uppe till höger och välj **Arkiv**.
3. Klistra in `https://github.com/remote-ha/homeassistant-addon` och välj **Lägg till**.
4. Stäng dialogrutan, leta upp **Remote Home Assistant** under **Remote Home Assistant Apps** och välj **Installera**. Uppdatera butiken eller välj **Sök efter uppdateringar** om appen inte visas.

Appbutiken hämtar appen från det [offentliga GitHub-arkivet](https://github.com/remote-ha/homeassistant-addon). Du behöver inte hämta någon ZIP-fil eller kopiera filer manuellt.

**HACS:** HACS installerar inte Home Assistant-appar (tidigare tillägg). Det här arkivet innehåller en app, inte en HACS-integration. Använd någon av metoderna för appbutiken ovan. Läs [HACS vanliga frågor](https://www.hacs.xyz/docs/faq/addons/) och den [fullständiga installationsguiden](https://remote-ha.com/sv/docs).

Följ installationsstegen i kontrollpanelen när du har loggat in. Välj ett hem för att se översikt, åtkomstbrandvägg, aktivitet och anslutningsinställningar. Din prenumeration finns under **Konto och prenumeration**. Språk och utseende ändras i det övre fältet; på små skärmar finns utseende även i menyn.

### Parkoppla ditt hem

Installera appen innan du skapar en parkopplingstoken. Välj **Parkopplingstoken** vid din installation i kontrollpanelen. I Home Assistant öppnar du **Inställningar → Appar → Remote Home Assistant → Konfiguration**, klistrar in token i **Token** (`pairing_token` i YAML-redigeraren) och väljer **Spara**. På informationssidan väljer du **Starta**, eller **Starta om** om appen redan körs. Aktivera **Starta vid uppstart**. Vänta tills **Ansluten** visas i kontrollpanelen, öppna installationens adress och logga in med ditt vanliga Home Assistant-konto.

[remote-ha.com](https://remote-ha.com)

## Setup

See [the setup guide](remote_home_assistant/DOCS.md) in English, Polish, German, Dutch, French and Swedish.
