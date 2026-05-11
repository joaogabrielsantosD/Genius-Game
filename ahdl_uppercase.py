"""
ahdl_uppercase.py
Converte palavras-chave AHDL de minúsculas para maiúsculas em um arquivo .ahdl ou .tdf.
Uso: python ahdl_uppercase.py <arquivo_entrada> [arquivo_saida]
"""

import re
import sys
import os

# Palavras-chave da linguagem AHDL
AHDL_KEYWORDS = {
    # Estruturas de controle
    "if", "else", "then", "elsif", "end",
    # Definição de máquinas de estado
    "machine", "states", "state", "with",
    # Lógica combinacional e sequencial
    "case", "is", "when", "others",
    # Declarações de componentes e sinais
    "subdesign", "variable", "begin",
    # Tipos e instâncias
    "input", "output", "bidir",
    "node", "dff", "dffe", "tff", "tffe", "jkff", "jkffe",
    "srff", "srffe", "latch", "tri",
    # Operadores lógicos (forma textual)
    "and", "or", "not", "xor", "xnor", "nand", "nor",
    # Constantes booleanas
    "vcc", "gnd",
    # Funções e tabelas
    "function", "returns", "table",
    # Outros
    "for", "generate", "assert", "report", "severity",
    "constant", "defaults", "clique", "help_id",
}

def uppercase_ahdl_keywords(source: str) -> str:
    """
    Substitui palavras-chave AHDL em minúsculas (ou misto) por MAIÚSCULAS,
    preservando strings entre aspas e comentários (-- ... até fim da linha).
    """

    result = []
    i = 0
    n = len(source)

    # Regex para identificar uma palavra (identificador)
    word_re = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')

    while i < n:
        # Comentário de linha: -- até o fim da linha
        if source[i:i+2] == '--':
            end = source.find('\n', i)
            if end == -1:
                result.append(source[i:])
                break
            result.append(source[i:end+1])
            i = end + 1
            continue

        # String entre aspas duplas
        if source[i] == '"':
            j = i + 1
            while j < n and source[j] != '"':
                if source[j] == '\\':   # escape
                    j += 1
                j += 1
            result.append(source[i:j+1])
            i = j + 1
            continue

        # String entre aspas simples (caractere literal em AHDL)
        if source[i] == "'":
            j = i + 1
            while j < n and source[j] != "'":
                j += 1
            result.append(source[i:j+1])
            i = j + 1
            continue

        # Palavra / identificador
        m = word_re.match(source, i)
        if m:
            word = m.group()
            if word.lower() in AHDL_KEYWORDS:
                result.append(word.upper())
            else:
                result.append(word)
            i = m.end()
            continue

        # Qualquer outro caractere
        result.append(source[i])
        i += 1

    return ''.join(result)


def process_file(input_path: str, output_path: str = None) -> None:
    if not os.path.isfile(input_path):
        print(f"Erro: arquivo '{input_path}' não encontrado.")
        sys.exit(1)

    with open(input_path, 'r', encoding='utf-8', errors='replace') as f:
        original = f.read()

    converted = uppercase_ahdl_keywords(original)

    if output_path is None:
        output_path = input_path

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(converted)

    # Relatório
    orig_lines = original.splitlines()
    conv_lines = converted.splitlines()
    changes = sum(1 for a, b in zip(orig_lines, conv_lines) if a != b)

    print(f"Arquivo de entrada : {input_path}")
    print(f"Arquivo de saída   : {output_path}")
    print(f"Linhas modificadas : {changes}")
    print("Concluído com sucesso!")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python ahdl_uppercase_keywords.py <arquivo_entrada> [arquivo_saida]")
        print("Exemplo: python ahdl_uppercase_keywords.py projeto.ahdl projeto_upper.ahdl")
        sys.exit(1)

    input_file  = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) >= 3 else None

    process_file(input_file, output_file)