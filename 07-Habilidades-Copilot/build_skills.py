#!/usr/bin/env python3
"""
Build Skills — Empacotador Automatizado de Habilidades para o Copilot 365
Varre as pastas de habilidades em 07-Habilidades-Copilot/, valida o frontmatter YAML
e compila os pacotes .zip prontos para upload no Copilot Studio / M365 Copilot.
"""

import os
import sys
import zipfile
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def validate_yaml_frontmatter(skill_md_path):
    with open(skill_md_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return False, "SKILL.md não contém frontmatter YAML válido cercado por '---'."

    yaml_block = match.group(1)
    has_name = re.search(r"^name:\s*[a-zA-Z0-9_\-]+", yaml_block, re.MULTILINE)
    has_desc = re.search(r"^description:\s*.+", yaml_block, re.MULTILINE)

    if not has_name:
        return False, "Frontmatter YAML precisa conter o campo 'name:' em kebab-case."
    if not has_desc:
        return False, "Frontmatter YAML precisa conter o campo 'description:'."

    return True, "YAML válido."

def build_skill_package(skill_folder):
    skill_name = os.path.basename(skill_folder)
    skill_md = os.path.join(skill_folder, "SKILL.md")

    if not os.path.exists(skill_md):
        return False, f"Pular {skill_name}: SKILL.md não encontrado."

    valid, msg = validate_yaml_frontmatter(skill_md)
    if not valid:
        return False, f"Erro em {skill_name}: {msg}"

    zip_filename = f"{skill_name}.zip"
    zip_path = os.path.join(skill_folder, zip_filename)

    # Cria o arquivo ZIP empacotando SKILL.md e references/
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona SKILL.md na raiz do zip
        zipf.write(skill_md, arcname="SKILL.md")

        # Adiciona references se existir
        refs_dir = os.path.join(skill_folder, "references")
        if os.path.exists(refs_dir):
            for root, _, files in os.walk(refs_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, skill_folder)
                    zipf.write(file_path, arcname=rel_path)

    zip_size_kb = os.path.getsize(zip_path) / 1024
    return True, f"✅ {zip_filename} criado com sucesso ({zip_size_kb:.1f} KB)."

def main():
    print("=" * 60)
    print("📦 BUILD SKILLS — COPILOT 365 AGENT PACKAGER")
    print("=" * 60)

    found_skills = 0
    success_count = 0

    for item in sorted(os.listdir(BASE_DIR)):
        item_path = os.path.join(BASE_DIR, item)
        if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, "SKILL.md")):
            found_skills += 1
            ok, msg = build_skill_package(item_path)
            print(f"[{item}] -> {msg}")
            if ok:
                success_count += 1

    print("=" * 60)
    print(f"Processamento concluído: {success_count}/{found_skills} habilidades empacotadas.")
    print("=" * 60)

if __name__ == "__main__":
    main()
