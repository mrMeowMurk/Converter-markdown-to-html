# 📝 Markdown to HTML Converter

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Мощный и удобный конвертер Markdown в HTML с поддержкой тем оформления и расширенными возможностями форматирования.

[Возможности](#-возможности) •
[Установка](#-установка) •
[Использование](#-использование) •
[Примеры](#-примеры) •
[Документация](#-документация)

</div>

## ✨ Возможности

### 🎯 Основные функции
- 📄 Конвертация одного или нескольких Markdown файлов в HTML
- 🎨 Три встроенные темы оформления:
  - ☀️ Светлая (по умолчанию)
  - 🌙 Тёмная
  - 📜 Сепия
- 📊 Прогресс-бар при конвертации нескольких файлов
- 📁 Гибкая настройка выходной директории

### 🚀 Поддержка расширенного Markdown
- 📑 Таблицы с автоматическим форматированием
- 💻 Блоки кода с подсветкой синтаксиса
- 📝 Списки определений
- 📌 Сноски
- 📚 Оглавление
- 🔄 Markdown внутри HTML
- ✨ Умные кавычки
- ✅ И многое другое

## 🚀 Установка

### Предварительные требования
- Python 3.6 или выше
- pip (менеджер пакетов Python)

### Шаги установки

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/your-username/markdown-to-html-converter.git
   cd markdown-to-html-converter
   ```

2. **Создайте виртуальное окружение**
   ```bash
   python -m venv .venv
   ```

3. **Активируйте виртуальное окружение**
   
   Windows:
   ```bash
   .venv\Scripts\activate
   ```
   
   Linux/Mac:
   ```bash
   source .venv/bin/activate
   ```

4. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Использование

### Базовая конвертация
```bash
python markdown_converter.py input.md
```

### Расширенные опции

#### 📁 Пакетная обработка
```bash
python markdown_converter.py file1.md file2.md file3.md
```

#### 🎨 Выбор темы
```bash
python markdown_converter.py input.md -t dark
```

#### 📂 Указание выходной директории
```bash
python markdown_converter.py input.md -o output_directory
```

#### 🤫 Тихий режим
```bash
python markdown_converter.py input.md -q
```

## 📋 Параметры командной строки

| Параметр | Сокращение | Описание | Значение по умолчанию |
|----------|------------|----------|----------------------|
| `--theme` | `-t` | Тема оформления (light/dark/sepia) | light |
| `--output-dir` | `-o` | Директория для выходных файлов | Директория входного файла |
| `--quiet` | `-q` | Подавить вывод сообщений | False |

## 💡 Примеры

### 1️⃣ Простая конвертация
```bash
python markdown_converter.py README.md
```
Результат: `README.html` в той же директории

### 2️⃣ Пакетная обработка с тёмной темой
```bash
python markdown_converter.py docs/*.md -t dark -o build/html
```
Результат: Все .md файлы из директории docs будут сконвертированы в HTML с тёмной темой и сохранены в build/html

### 3️⃣ Тихая конвертация в стиле сепия
```bash
python markdown_converter.py document.md -t sepia -q
```
Результат: Тихая конвертация с применением темы сепия

## 📚 Поддерживаемые элементы Markdown

### 📝 Базовые элементы
- Заголовки (# H1, ## H2, etc.)
- Форматирование текста (**жирный**, *курсив*)
- Списки (маркированные и нумерованные)
- Ссылки и изображения
- Цитаты

### 📊 Расширенные элементы
- Таблицы с выравниванием
- Блоки кода с подсветкой синтаксиса
- Списки определений
- Сноски
- Оглавление

## 🤝 Вклад в проект

Мы приветствуем ваш вклад в развитие проекта! Вот как вы можете помочь:

1. 🍴 Форкните репозиторий
2. 🔧 Создайте ветку для ваших изменений
3. ✨ Внесите изменения
4. 📝 Создайте pull request

## 📝 Лицензия

Этот проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).

## 👥 Авторы

- MeowMurk - [GitHub](https://github.com/your-username)

---

<div align="center">
Сделано с ❤️ для сообщества Python
</div> 