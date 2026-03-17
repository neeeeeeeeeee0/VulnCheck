# VulnCheck

<h4> Этот проект представляет собой высокопроизводительный инструмент для сканирования сети и портов, разработанный на Python. Он предназначен для специалистов по безопасности, сетевых администраторов и разработчиков, желающих провести аудит безопасности своих систем, выявить открытые порты, обнаружить активные узлы в сети, а также получить базовую информацию о запущенных на портах сервисах.</h4>
<h4>
Проект создан с упором на эффективность, используя многопоточность для ускорения операций сканирования, что позволяет быстро обрабатывать большие диапазоны IP-адресов и портов. Это отличный пример использования низкоуровневых сетевых протоколов (TCP/IP) в Python и демонстрация навыков работы с многопоточностью для оптимизации производительности. </h4>

<b> **Сканирование портов (Port Scanning)** </b>
  - Поддержка сканирования TCP-портов
  - Возможность указания как отдельных портов, так и диапазонов (например, 1-1024).
  - Определение состояния порта: открыт (Open), закрыт (Closed), отфильтрован (Filtered).
  - Выявление популярных портов и связанных с ними сервисов (HTTP, SSH, FTP, Telnet и т.д.).

<b> **Обнаружение узлов (Host Discovery)** </b>
  - Сканирование диапазона IP-адресов для выявления активных устройств в сети.
  - Использование различных методов для обнаружения (например, ICMP Echo Request - "пинг").
    
<b> **Баннер-граббинг (Banner Grabbing)** </b>
  - Попытка получения информации о сервисе, работающем на открытом порту, путем подключения и чтения первого ответа (например, версия веб-сервера или SSH-сервиса).
    
<b> **Многопоточность (Multi-threading)** </b>
  - Использование потоков для параллельного сканирования, значительно сокращая время выполнения задач на больших диапазонах.
    
<b> **Настраиваемые параметры** </b>
  - Возможность установки таймаута для сетевых подключений.
  - Гибкое указание целевых IP-адресов/диапазонов и портов через аргументы командной строки.
  - Интуитивно понятный вывод:
  - Четкое и структурированное отображение результатов сканирования в консоли.

<b> 🛠 Технологический стек </b>
 - язык программирования: Python 3.x
  - socket: для низкоуровневой работы с сетевыми сокетами (TCP/IP соединения).
  - threading: для реализации многопоточности и параллельного выполнения задач.
  - argparse: для парсинга аргументов командной строки.


- <b>Full Stack Web App (React, NodeJS, Azure, and Machine Learning Components)</b>
  - [Image Analysis Middleware](https://github.com/joshmadakor1/4chan-Image-Analysis-Middleware-C964) <b><i>(Potentially NSFW)</b></i>
- <b>PowerShell</b>
  - [Windows EventLog: Failed RDP Logins Source IP to full GeoData Conversion](https://github.com/joshmadakor1/Sentinel-Lab)
  - [JWipe (Disk Wiping Utility)](https://github.com/joshmadakor1/Jwipe.PowerShell)
  - [Active Directory Bulk User Creation](https://github.com/joshmadakor1/AD_PS)
  - [FIM (File Integrity Monitor)](https://github.com/joshmadakor1/PowerShell-Integrity-FIM)
- <b>C# (.NET Desktop Applications)</b>
  - [Ransomware Proof of Concept (Encrypter)](https://github.com/joshmadakor1/EncrypterPOC)
  - [Ransomware Proof of Concept (Decrypter)](https://github.com/joshmadakor1/DecrypterPOC)
  - [Keylogger with Email Capability](https://github.com/joshmadakor1/Key-Logger-With-Email)
- <b>Python</b>
  - [Package Delivery Application (Datastructures and Algorithms Demo)](https://github.com/joshmadakor1/Package-Delivery-Pathfinding-Algorithm)

