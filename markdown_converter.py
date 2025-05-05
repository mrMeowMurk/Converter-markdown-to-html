#!/usr/bin/env python3
import click
import markdown
from pathlib import Path
from typing import List, Optional
from concurrent.futures import ThreadPoolExecutor
import sys


THEMES = {
    'light': """
        body {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #fff;
        }
    """,
    'dark': """
        body {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #e0e0e0;
            background-color: #1a1a1a;
        }
        a { color: #58a6ff; }
        code { color: #f0f0f0; }
    """,
    'sepia': """
        body {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            font-family: Georgia, serif;
            line-height: 1.6;
            color: #704214;
            background-color: #f4ecd8;
        }
        a { color: #8b4513; }
    """
}

COMMON_STYLES = """
    pre {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 5px;
        overflow-x: auto;
    }
    code {
        background-color: #f5f5f5;
        padding: 2px 5px;
        border-radius: 3px;
    }
    img {
        max-width: 100%;
        height: auto;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 15px 0;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #f5f5f5;
    }
    blockquote {
        border-left: 4px solid #ddd;
        margin: 0;
        padding-left: 15px;
        color: #666;
    }
"""


def convert_markdown_to_html(input_text: str, extensions: List[str]) -> str:
    """
    Конвертирует markdown текст в HTML.
    
    Args:
        input_text: Входной текст в формате Markdown
        extensions: Список расширений Markdown для использования
        
    Returns:
        str: Сконвертированный HTML текст
    """
    md = markdown.Markdown(extensions=extensions)
    return md.convert(input_text)


def process_single_file(
    input_file: Path,
    output_file: Path,
    theme: str,
    extensions: List[str],
    quiet: bool = False
) -> bool:
    """
    Обрабатывает один файл Markdown.
    
    Args:
        input_file: Путь к входному файлу
        output_file: Путь к выходному файлу
        theme: Название темы оформления
        extensions: Список расширений Markdown
        quiet: Подавлять вывод сообщений
        
    Returns:
        bool: True если конвертация прошла успешно, False в противном случае
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        
        html_content = convert_markdown_to_html(markdown_text, extensions)
        
        theme_style = THEMES.get(theme, THEMES['light'])
        full_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{input_file.stem}</title>
    <style>
        {theme_style}
        {COMMON_STYLES}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
        
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
            
        if not quiet:
            click.echo(f"✅ Конвертация успешно завершена: {output_file}")
        return True
        
    except Exception as e:
        if not quiet:
            click.echo(f"❌ Ошибка при конвертации {input_file}: {str(e)}", err=True)
        return False


@click.command()
@click.argument('input_files', type=click.Path(exists=True, path_type=Path), nargs=-1, required=True)
@click.option(
    '--output-dir',
    '-o',
    type=click.Path(path_type=Path),
    help='Директория для сохранения HTML файлов. По умолчанию - та же директория, что и входной файл.'
)
@click.option(
    '--theme',
    '-t',
    type=click.Choice(['light', 'dark', 'sepia'], case_sensitive=False),
    default='light',
    help='Тема оформления HTML'
)
@click.option(
    '--quiet',
    '-q',
    is_flag=True,
    help='Подавить вывод сообщений о процессе конвертации'
)
def main(
    input_files: tuple[Path, ...],
    output_dir: Optional[Path],
    theme: str,
    quiet: bool
):
    """
    Конвертирует Markdown файлы в HTML файлы.
    
    Поддерживает конвертацию одного или нескольких файлов.
    Можно указать директорию для выходных файлов и тему оформления.
    """
    extensions = [
        'tables',           # Таблицы
        'fenced_code',      # Блоки кода
        'codehilite',      # Подсветка синтаксиса
        'attr_list',       # Атрибуты элементов
        'def_list',        # Списки определений
        'footnotes',       # Сноски
        'md_in_html',      # Markdown внутри HTML
        'toc',             # Оглавление
        'smarty',          # Умные кавычки
        'sane_lists',      # Улучшенные списки
    ]

    success_count = 0
    error_count = 0
    
    with click.progressbar(
        input_files,
        label='Конвертация файлов',
        show_pos=True
    ) as files:
        for input_file in files:
            if output_dir:
                output_file = output_dir / f"{input_file.stem}.html"
            else:
                output_file = input_file.with_suffix('.html')
            
            if process_single_file(input_file, output_file, theme, extensions, quiet):
                success_count += 1
            else:
                error_count += 1
    
    if not quiet:
        total = len(input_files)
        click.echo(f"\nОбработано файлов: {total}")
        click.echo(f"Успешно: {success_count}")
        if error_count > 0:
            click.echo(f"С ошибками: {error_count}", err=True)

    if error_count > 0:
        sys.exit(1)


if __name__ == '__main__':
    main() 